import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.express as px
import pandas as pd
from datetime import datetime
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


def load_and_process_data():
    df = pd.read_csv('./data/people.csv', sep=',')
    df['Date of birth'] = pd.to_datetime(df['Date of birth'], format='%Y-%m-%d')
    df['age'] = df['Date of birth'].apply(calculate_age)

    age_bins = [0, 18, 35, 50, 65, float('inf')]
    age_labels = ['0-17', '18-35', '36-50', '51-65', '65+']
    df['Age Group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels)

    df['Age Group'] = pd.Categorical(df['Age Group'], categories=age_labels, ordered=True)

    return df


def calculate_age(row):
    current_date = datetime.now()
    age = current_date.year - row.year
    if (current_date.month, current_date.day) < (row.month, row.day):
        age -= 1
    return age


def create_figures(df):
    sex_counts = df['Sex'].value_counts().reset_index()
    sex_counts.columns = ['Sex', 'count']
    sex_fig = px.bar(sex_counts, x='Sex', y='count',
                     labels={'Sex': 'Sex', 'count': 'Count'},
                     title='Sex Distribution',
                     color='Sex',
                     color_discrete_map={'Male': 'blue', 'Female': 'pink'})

    age_group_counts = df['Age Group'].value_counts().reset_index()
    age_group_counts.columns = ['Age Group', 'count']

    age_group_counts['Age Group'] = pd.Categorical(age_group_counts['Age Group'],
                                                   categories=df['Age Group'].cat.categories, ordered=True)
    age_group_counts = age_group_counts.sort_values('Age Group')

    age_group_fig = px.bar(age_group_counts, x='Age Group', y='count',
                           labels={'Age Group': 'Age Group', 'count': 'Count'},
                           title='Age Group Distribution',
                           color='Age Group',
                           color_discrete_map={'0-17': 'green', '18-35': 'orange', '36-50': 'blue', '51-65': 'purple',
                                               '65+': 'red'})

    avg_age_by_job_fig = px.bar(df.groupby('Job Title')['age'].mean().reset_index(),
                                x='Job Title', y='age',
                                labels={'Job Title': 'Job Title', 'age': 'Average Age'},
                                title='Average Age by Job Title',
                                color='age',
                                color_continuous_scale='Viridis')

    return sex_fig, age_group_fig, avg_age_by_job_fig


app.layout = dbc.Container([
    html.H1("People Analysis Dashboard", style={'textAlign': 'center', 'marginTop': '20px'}),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='sex-graph')
        ], width=6),

        dbc.Col([
            dcc.Graph(id='age-group-graph')
        ], width=6),
    ], style={'marginTop': '30px'}),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='avg-age-job-graph')
        ], width=12),
    ], style={'marginTop': '30px'}),

    dcc.Interval(
        id='interval-update',
        interval=60000,
        n_intervals=0
    )

], fluid=True)


@app.callback(
    [Output('sex-graph', 'figure'),
     Output('age-group-graph', 'figure'),
     Output('avg-age-job-graph', 'figure')],
    Input('interval-update', 'n_intervals')
)
def update_graphs(n):
    df = load_and_process_data()
    sex_fig, age_group_fig, avg_age_by_job_fig = create_figures(df)
    return sex_fig, age_group_fig, avg_age_by_job_fig


if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)

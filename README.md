# Dashboard de Análise de Pessoas

Este projeto é uma aplicação web baseada em **Dash** e **Plotly** para visualização interativa de dados. O objetivo é analisar e visualizar dados demográficos de pessoas, incluindo a distribuição por sexo, grupos etários e média de idade por cargo. Os dados são visualizados por meio de gráficos de barras, que são atualizados dinamicamente a cada minuto.

## Funcionalidades

- **Gráfico de Distribuição por Sexo**: Exibe a distribuição de indivíduos do sexo masculino e feminino.
- **Gráfico de Distribuição por Grupos Etários**: Mostra a quantidade de pessoas em diferentes faixas etárias (0-17, 18-35, 36-50, 51-65, 65+).
- **Gráfico de Idade Média por Cargo**: Exibe a média de idade para diferentes cargos.

Os dados são atualizados dinamicamente a cada 60 segundos para refletir as informações mais recentes.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/dashboard-analise-pessoas.git
    cd dashboard-analise-pessoas
    ```

2. Instale as dependências necessárias:
    ```bash
    pip install -r requirements.txt
    ```

    O arquivo `requirements.txt` deve conter:
    ```
    dash==2.7.0
    dash-bootstrap-components==1.3.0
    plotly==5.0.0
    pandas==1.4.2
    ```

3. Certifique-se de que o arquivo `people.csv` está presente no diretório `data`. Se o arquivo não estiver disponível, adicione o conjunto de dados correto.

## Uso

Para iniciar o dashboard, execute o seguinte comando:

```bash
python app.py

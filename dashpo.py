import mysql.connector
import dash
from dash import dcc
from dash import html
import pandas as pd


banco = mysql.connector.connect(host="database-2.cgnraaiqytel.us-west-2.rds.amazonaws.com", user="admin", password="usuariopi6", database="infos") #conectando ao banco

df = pd.read_sql('SELECT * FROM informacoes', banco) #lendo informacao do banco

#iniciando dash
app = dash.Dash (__name__)
server = app.server



colors = {
        'background': '',
        'text': '#368cda'
    }

app.layout = html.Div(style={'backgroundColor': colors['background']},children=[

    html.H1(
        children='SX Plug V2',
        style={
        'textAlign': 'center',
        'color': colors['text']
        }

    ),

    html.Div(
        children='''Dashboard de consumo energetico''',
        style={
            'textAlign':'center',
            'color': colors['text'],
        }
    ),


#criando primeiro grafico
    dcc.Graph(
        id='Grafico do SXPlug1',
        figure={
            'data': [{'x': df['hora'], 'y': df['potencia'], 'type': 'line', 'name': '2020'},], #inserindo dados
            'layout': {'title': 'Consumo de energia por dia',
            'xaxis' : dict(
                title='Horario',
                titlefont=dict(
                family='Arial, monospace',
                size= 25,
                color='black'    
                )
            ),

            'yaxis': dict(
                title='Consumo [kWh]',
                titlefont=dict(
                family='Arial, monospace',
                size=25,
                color='black'
                )  
            )} 

        }),


#criando segundo dash
    dcc.Graph(
        id='Grafico do SXPlug2',
        figure={
            'data': [{'x': df['data'], 'y': df['potencia'], 'type': 'bar', 'name': '2020'},],
            'layout': {'title': 'Consumo de energia por mês',
            'xaxis' : dict(
                title='Dias',
                titlefont=dict(
                family='Arial, monospace',
                size= 25,
                color='black'    
                )
            ),

            'yaxis': dict(
                title='Consumo [kWh]',
                titlefont=dict(
                family='Arial, monospace',
                size=25,
                color='black'
                )  
            )}               
        })
    
])



if __name__ == '__main__':
    app.run_server(debug=False)


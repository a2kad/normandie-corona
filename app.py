# -*- coding: utf-8 -*-
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

# Open CSV
data_csv = pd.read_csv('covid.csv')

# Get last row
last_day = data_csv.tail(1)
confirme = last_day['Confirme']
death = last_day['Death']
hospitalized = last_day['Hospitalized']
age = last_day['Age']
all_date = data_csv['Date']
all_confirme = data_csv['Confirme']
date = last_day['Date']
man = int(last_day['Hommes'])
woman = int(last_day['Femmes'])


# Bar-Graphic
fig = go.Figure(data=[go.Bar(x=all_date, y=all_confirme, text = 'Cas confirmés')], layout = {'title': 'Résultat positif au COVID-19 (depuis le 24 février)'})
# Pie-Graphic
labels = ['Hommes','Femmes']
values = [man, woman]
fig2 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.2)], layout = {'title': 'Hommes/Femmes décès à l\'hôpital'})

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title = 'Normandie.COVID-19'

app.layout = html.Div([
    html.Div([
        html.H2('Normandie.COVID-19')
    ], className='header'),
    html.Div([
        html.P([
            dcc.Markdown('''
            Source: [L’Agence régionale de santé de Normandie] (https://www.normandie.ars.sante.fr/)
            ''')
        ]),
        html.P('Date de dernière mise à jour : '+ date +' 2020'

        )
    ], className='marckdown'),

    html.Div([
        html.Div([
            html.Div([
                html.H2(confirme),
                html.P('positives au COVID-19')
            ], className='block'),
            html.Div([
                html.H2(death),
                html.P('décès à l\'hôpital')
            ], className='block'),
            html.Div([
                html.H2(hospitalized),
                html.P('sont hospitalisées')
            ], className='block'),
            html.Div([
                html.H2(age),
                html.P('âge médian')
            ], className='block')
        ], className='cards'),
        html.Div([
            html.Div([
                dcc.Graph(
                    id = 'example-graph',
                    figure=fig

                )
            ], className='graph-one'),

            html.Div([
                dcc.Graph(
                    id = 'example-graph-2',
                    figure=fig2
                )

                                
            ], className='graph-two')
        ], className='graph')
    ]),
    html.Footer([
        html.Div(["Copyright © 2020 Reshetnikov Ruslan"
        ], className='footer')

    ])
], className='container')

if __name__=="__main__":
    app.run_server(debug=True)
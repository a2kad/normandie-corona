# -*- coding: utf-8 -*-
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

data_csv = pd.read_csv('covid.csv')
#print(data_csv.head())
last_day = data_csv.tail(1)
confirme = last_day['Confirme']
death = last_day['Death']
hospitalized = last_day['Hospitalized']
recovered = last_day['Recovered']
all_date = data_csv['Date']
all_confirme = data_csv['Confirme']

fig = go.Figure(data=[go.Bar(x=all_date, y=all_confirme, text = 'Cas confirmés')], layout = {'title': 'Résultat positif sur COVID-19 (depuis le 24 février)'})

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app=dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Div([
        #html.Img(src='/assets/logo.png'),
        html.H2('Normandie.COVID-19')
    ], className='header'),
    html.Aside([
        html.Ul([
            html.Li(['City 1'
            ], className='sidenav__list-item'),
            html.Li(['City 2'
            ], className='sidenav__list-item'),
            html.Li(['City 3'
            ], className='sidenav__list-item')
            

        ], className='sidenav__list')

    ],className='sidenav'),
    html.Div([
        html.Div([
            html.Div([
                html.H2(confirme),
                html.P('positives au COVID-19')
            ], className='overviewcard'),
            html.Div([
                html.H2(death),
                html.P('décès à l\'hôpital')
            ], className='overviewcard'),
            html.Div([
                html.H2(hospitalized),
                html.P('sont hospitalisées')
            ], className='overviewcard'),
            html.Div([
                html.H2(recovered),
                html.P('sont sorties de l\'hôpital')
            ], className='overviewcard')
        ], className='main-overview'),
        html.Div([
            html.Div([
                dcc.Graph(
                    id = 'example-graph',
                    figure=fig

                )
            ], className='card'),
            html.Div(['Card 1',

            ], className='card'),
            html.Div(['Card 2'
                                
            ], className='card')
        ], className='main-cards')
    ],className='main'),
    html.Footer([
        html.Div(["Copyright 2020 Reshetnikov Ruslan"
        ], className='footer-copyright')

    ], className='footer')
], className='grid-container')

if __name__=="__main__":
    app.run_server(debug=True)
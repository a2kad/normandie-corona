# -*- coding: utf-8 -*-
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html

data = pd.read_csv('covid.csv')
print(data.head())

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
                html.H2('586'),
                html.P('Confirmed')
            ], className='overviewcard'),
            html.Div([
                html.H2('586'),
                html.P('Confirmed')
            ], className='overviewcard'),
            html.Div([
                html.H2('586'),
                html.P('Confirmed')
            ], className='overviewcard')
        ], className='main-overview'),
        html.Div([
            html.Div(['Map'

            ], className='card'),
            html.Div(['Card 1'

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
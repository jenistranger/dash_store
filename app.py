from dash import Dash, html
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container

from flask import Flask

from components import test_graphs, navbar, test_filters, test_stats, test_waterfall

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], update_title='Загрузка...')


app.layout = dbc.Container([
    navbar,
    test_stats(),
    # html.Hr(),
    dbc.Row([
        html.Hr(),
        dbc.Col(test_filters(), md=1),
        dbc.Col([
            dbc.Row([
                    dbc.Col(test_graphs("1"), md=6, className="graph-border"),
                    dbc.Col(test_graphs("2"), md=6, className="graph-border"),
                ]),
                dbc.Row([
                    dbc.Col(test_waterfall("График: 3"), md=6, className="graph-border"),
                    dbc.Col(test_graphs("4"), md=6, className="graph-border"),
                ]),
    ])
    ])
], className="app-container ")

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=55544, debug=True)

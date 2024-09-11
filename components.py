import dash_bootstrap_components as dbc
from dash import html, dcc


#навигация

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Главное меню", href="/")),
        dbc.NavItem(dbc.NavLink("Настройки", href="/settings")),
        dbc.NavItem(dbc.NavLink("Помощь", href="/help"))
    ],
    brand="ПРОИЗВОДСТВО",
)

#тестовый график

def test_graphs(id):
    return html.Div(children=[
                html.H3(children=f"График: {id}"),
                dcc.Graph(
                    id=f'ig-{id}',
                    # id='interactive-graph',
                    figure={
                        'data': [
                            {'x': [1, 2, 3, 4, 5], 'y': [1, 4, 9, 16, 25], 'type': 'line', 'name': 'Линия'},
                            {'x': [1, 2, 3, 4, 5], 'y': [2, 6, 12, 20, 30], 'type': 'scatter', 'mode': 'markers', 'name': 'Точки'}
                        ],
                        'layout': {
                            'title': 'Тестовый график',
                            'xaxis': {'title': 'Ось X'},
                            'yaxis': {'title': 'Ось Y'}
                        }
                    }
                )
            ])

def test_filters():
    return html.Div(children=[
                html.H3(children="Фильтры"),
                dcc.Dropdown(
                    id='dropdown-filter',
                    options=[
                        {'label': 'Фильтр 1', 'value': 'filter1'},
                        {'label': 'Фильтр 2', 'value': 'filter2'},
                        {'label': 'Фильтр 3', 'value': 'filter3'}
                    ],
                    placeholder="Выберите фильтр"
                ),
                dcc.RadioItems(
                    id='radio-filter',
                    options=[
                        {'label': 'Вариант 1', 'value': 'option1'},
                        {'label': 'Вариант 2', 'value': 'option2'},
                        {'label': 'Вариант 3', 'value': 'option3'}
                    ],
                    labelStyle={'display': 'inline-block'}
                )
                ]
            )

def test_waterfall(name):
    return html.Div(children=[
                html.H3(children=f"{name}"),
                dcc.Graph(
                    id='waterfall-chart',
                    figure={
                        'data': [
                            {
                                'type': 'bar',
                                'name': 'Значения',
                                'x': ['План', 'A', 'B', 'C', 'D', 'E', 'Факт'],
                                'y': [1917, 130, 19, 81, -3, 86, 2201],
                                'marker': {'color': 'blue'}
                            }
                        ],
                        'layout': {
                            'title': 'Водопадная диаграмма',
                            'xaxis': {'title': 'Этапы'},
                            'yaxis': {'title': 'Значения'}
                        }
                    }
                )
])

def test_stats():
    return html.Div([
        dbc.Row([
            dbc.Col(html.H5("300 тыс.т")),
            dbc.Col(html.H5("133 млн.м3")),
            dbc.Col(html.H5("455 тыс.т")),
            dbc.Col(html.H5("413 тыс.т")),
        ])
    ])


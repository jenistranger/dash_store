import dash_bootstrap_components as dbc
from dash import html, dcc
import dash_mantine_components as dmc
#навигация
navbar = dbc.NavbarSimple(
    color="white",
    children=[
        dbc.NavItem(dbc.NavLink("Главное меню", href="/")),
        dbc.NavItem(dbc.NavLink("Экспорт", href="/export")),
        dbc.NavItem(dbc.NavLink("Поделиться", href="/share")),
        dbc.NavItem(dbc.NavLink("Комментарии", href="/comments")),
        dbc.NavItem(dbc.NavLink("Настройки", href="/settings")),
        dbc.NavItem(dbc.NavLink("Помощь", href="/help")),
        dbc.NavItem(dbc.NavLink("Чат в TrueConf", href="/trueconf")),
    ],
    brand="ПРОИЗВОДСТВО",
    className = "div-navbar"
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
def test_filters(name):
    return html.Div(children=[
                html.H3(children=f"{name}"),
                dcc.Dropdown(
                    id=f'dropdown-filter-{name}',
                    options=[
                        {'label': 'Фильтр 1', 'value': 'filter1'},
                        {'label': 'Фильтр 2', 'value': 'filter2'},
                        {'label': 'Фильтр 3', 'value': 'filter3'}
                    ],
                    placeholder="Выберите фильтр"
                ),
                dcc.RadioItems(
                    id=f'radio-filter-{name}',
                    options=[
                        {'label': 'Вариант 1', 'value': 'option1'},
                        {'label': 'Вариант 2', 'value': 'option2'},
                        {'label': 'Вариант 3', 'value': 'option3'}
                    ],
                    labelStyle={'display': 'inline-block'}
                )
                ]
            )
# def dropdown_example(*args):
    
#     dcc.Dropdown(
#         id='dropdown-example',
#         options=[
#             {'label': 'Вариант 1', 'value': 'value1'},
#             {'label': 'Вариант 2', 'value': 'value2'},
#             {'label': 'Вариант 3', 'value': 'value3'}
#         ],
#         placeholder="Выберите вариант"
#     ),
def dropdown_example(*args, placeholder, id):
    options = [
        {'label': arg, 'value': str(i + 1)}  
        for i, arg in enumerate(args)
    ]
    return dcc.Dropdown(
        id=id,
        options=options,
        multi=True,
        placeholder=placeholder
    )
def foo_checklist_example(title, id, *args):
    options = [
        {'label': arg, 'value': str(i + 1)}  
        for i, arg in enumerate(args)
    ]
    return html.Div([
                html.H5(f"{title}"),
                dcc.Checklist(
                    id=f"{id}",
                    options=options,
                    # labelStyle={'display': 'block'}  # Отображаем лейблы по одному
                ),
                html.Div(id=f'output-container-{id}', children=''),
            ], className='filters-border')
def checklist_example(title):
    return html.Div([
                html.H5(f"{title}"),
                dcc.Checklist(
                    id='checklist-example',
                    options=[
                        {'label': 'Вариант 1', 'value': 'value1'},
                        {'label': 'Вариант 2', 'value': 'value2'},
                        {'label': 'Вариант 3', 'value': 'value3'}
                    ],
                    # labelStyle={'display': 'block'}  # Отображаем лейблы по одному
                ),
                html.Div(id='output-container', children=''),
            ], className='filters-border')
def button_example(title, id):
    return html.Button(id=f"{id}", n_clicks=0, children=f'{title}'),
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
            
            dbc.Col([
                html.Div([
                    html.H6("Газ (млн. м3)"),
                    html.H5("300"),
                    dmc.Badge("Месяц: +15%", color="green")
                ], className="info-card")
    
            ], className="stats-center"),
            dbc.Col([
                html.Div([
                    html.H6("Конденсат (тыс. т)"),
                    html.H5("300"),
                    dmc.Badge("Месяц: +23%", color="green")
                ], className="info-card")
            ], className="stats-center"),
            dbc.Col([
                html.Div([
                    html.H6("Нефть (тыс.т)"),
                    html.H5("1300.1"),
                    dmc.Badge("Месяц: -5%", color="red")
                ], className="info-card")
            ], className="stats-center"),
            dbc.Col([
                html.Div([
                    html.H6("Коэффициент эксплуатации"),
                    html.H5("99.1%"),
                    dmc.Badge("Месяц: +4%", color="green")
                ], className="info-card")
            ], className="stats-center"),
            # dbc.Col(html.H5("133 млн.м3", className="info-card"), className="stats-center"),
            # dbc.Col(html.H5("455 тыс.т", className="info-card"), className="stats-center"),
            # dbc.Col(html.H5("413 тыс.т", className="info-card"), className="stats-center"),
        ])
    ], className="stats-block")
             

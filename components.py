import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input, callback, State
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
        dbc.NavItem(dbc.NavLink("Загрузка данных", href="/upload")),
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
# def upload_data():
#     return dbc.Form(
#         dbc.Row([
#             dbc.Label("Тип новой записи", width="auto"),
#             dbc.Col(
#                 dbc.Input(placeholder="Enter email"),
#                 className="me-3",
#             ),
#             dbc.Label("Название", width="auto"),
#             dbc.Col(
#                 dbc.Input(type="email", placeholder="Enter email"),
#                 className="me-3",
#             ),
#             dbc.Col(dbc.Button("Подтвердить"), width="auto")
#         ])
#     )
def upload_data():
    return dbc.Form(
        dbc.Row(
            [
                # dbc.Label("Тип новой записи", width="auto"),
                dcc.Dropdown(
                    id="operation-type",
                    placeholder="Выберите",
                    options=[
                        {'label': 'Новая запись', 'value' : 'new'},
                        {'label': 'Регулярное обновление', 'value' : 'update'}
                    ],
                    value='update'
                ),       
                html.Div(id='additional-fields'),
                # dbc.Button('Подтвердить', id='submit-button', n_clicks=0),
            ]
        )
    )
@callback(
    Output('additional-fields', 'children'),
    Input('operation-type', 'value')
)
def update_fields(operation_type):
    if operation_type == 'new':
        return html.Div([
            dcc.Dropdown(
                id='data-type',
                options=[
                    {'label': 'Страна', 'value': 'country'},
                    {'label': 'Флюид', 'value': 'fluid'}
                ],
                value='country'
            ),
            html.Div(id='input-field'),
        ])
    else:
        return html.Div()  # For regular updates, we assume no additional fields for now
@callback(
    Output('input-field', 'children'),
    Input('data-type', 'value')
)
def display_input_field(data_type):
    # if data_type == 'country':
    #     return dcc.Input(id='country-name', type='text', placeholder='Введите название страны')
    # elif data_type == 'fluid':
    #     return dcc.Input(id='fluid-name', type='text', placeholder='Введите название флюида')
    # return html.Div()
    layout = html.Div([
        dcc.Input(id=f'{data_type}-name', type='text', placeholder=f'Введите название'),
        dbc.Row([
            dbc.Button('Подтвердить', id='submit-button', n_clicks=0),
        ]),
        html.Div(id='output-message')
    ])
    return layout
@callback(
    Output('output-message', 'children'),
    Input('submit-button', 'n_clicks'),
    State('operation-type', 'value'),
    State('data-type', 'value'),
    State('country-name', 'value'),
    State('fluid-name', 'value')
)
def handle_submission(n_clicks, operation_type, data_type, country_name, fluid_name):
    if n_clicks > 0:
        if operation_type == 'new':
            if data_type == 'country':
                return f'Новая запись: страна - {country_name}'
            elif data_type == 'fluid':
                return f'Новая запись: флюид - {fluid_name}'
    return ''

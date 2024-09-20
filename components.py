import dash_bootstrap_components as dbc
from dash import html, dcc, Output, Input, callback, State, callback_context
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



def radio_period(title):
    return html.Div([
                html.H5(f"{title}"),
                dcc.RadioItems(
                    id='radio_period',
                    options=[
                        {'label': 'День', 'value': 'day'},
                        {'label': 'Месяц', 'value': 'month'},
                        {'label': 'Квартал', 'value': 'quarter'},
                        {'label': 'Год', 'value': 'year'},
                    ],
                    value='month'
                    # labelStyle={'display': 'block'}  # Отображаем лейблы по одному
                ),
                # html.Div(id='output-container', children=''),
            ], className="filters-border")



from datetime import datetime, date



#загружать в датастор ласт дату
@callback(
        Output("date_picker", "children"),
        Input("radio_period", "value")
)
def date_pick(value):
    current_year = datetime.now().year
    if value == "year":
        return html.Div([
                    dcc.Dropdown(
                        id='year-dropdown',
                        options=[{'label': str(year), 'value': year} for year in range(2020, current_year+1)],
                        placeholder="Выберите год"
                    )
                ])
    elif value == "month":
        return html.Div([

                        dcc.Dropdown(
                            id='year-dropdown-m',
                            options=[{'label': str(year), 'value': year} for year in range(2020, current_year + 1)],
                            placeholder="Выберите год",
                            value=current_year
                        ),
                        dcc.Dropdown(
                            id='month-dropdown',
                            options=[
                                {'label': 'Январь', 'value': 1},
                                {'label': 'Февраль', 'value': 2},
                                {'label': 'Март', 'value': 3},
                                {'label': 'Апрель', 'value': 4},
                                {'label': 'Май', 'value': 5},
                                {'label': 'Июнь', 'value': 6},
                                {'label': 'Июль', 'value': 7},
                                {'label': 'Август', 'value': 8},
                                {'label': 'Сентябрь', 'value': 9},
                                {'label': 'Октябрь', 'value': 10},
                                {'label': 'Ноябрь', 'value': 11},
                                {'label': 'Декабрь', 'value': 12}
                            ],
                            placeholder="Выберите месяц",
                            value=datetime.now().month  # По умолчанию текущий месяц
                        )
                    ])
    elif value=='day':
        return html.Div(
            [
                dcc.DatePickerSingle(
                        id='date-picker-single',
                        min_date_allowed=date(2020, 1, 1),
                        max_date_allowed=datetime.now(),
                        initial_visible_month=datetime.now(),
                        month_format='D, MMMM, YYYY',
                        display_format='D.M.YYYY/Q',
                        date=datetime.now(),
                        clearable=True,
                        with_portal=True,
                        placeholder="День"
                    ),
            ],
            className="current-date-picker"
        )
    elif value=='quarter':
        return html.Div(
            [

                dcc.Dropdown(
                            id='year-dropdown-q',
                            options=[{'label': str(year), 'value': year} for year in range(2020, current_year + 1)],
                            placeholder="Выберите год",
                            value=current_year
                        ),
                        dcc.Dropdown(
                            id='quarter-dropdown',
                            options=[
                                {'label': 'Первый', 'value': 'qua-1'},
                                {'label': 'Второй', 'value': 'qua-2'},
                                {'label': 'Третий', 'value': 'qua-3'},
                                {'label': 'Четвертый', 'value': 'qua-4'},
                            ],
                            placeholder="Выберите квартал",
                            # value=datetime.now().month  # По умолчанию текущий месяц
                        )

            ]
        )






def hc_checklist(title):
    return html.Div([
                html.H5(f"{title}"),
                dcc.Checklist(
                    id="hc-checklist",
                    options=[
                        {'label': 'Природный газ', "value" : 'nat_gas'},
                        {'label': 'Газовый конденсат', "value" : 'condensate_gas'},
                        {'label': 'Нефть', "value" : 'oil'},
                        {'label': 'Газопродукты', "value" : 'product_gas'},
                    ],
                    value=['oil'],
                ),
                # html.Div(id=f'output-container-{id}', children=''),
            ], className='filters-border')



options_assets= ['Ипати Акио', 'Блоки 05-2/05-3', 'Шахпахты', 'ВИНЗ']
#тут надо подгружать данные из БД
def assets_checklist(title):
    return html.Div([
                html.H5(f"{title}"),
                dcc.Checklist(["Все"], [], id="all-checklist"),
                dcc.Checklist(
                    options_assets,
                    [],
                    id="assets-checklist",
                    # options= options_assets
                    
                    # [
                    #     # {'label': 'ВСЕ', "value" : 'all'},
                    #     {'label': 'Ипати Акио', "value" : 'asset_1'},
                    #     {'label': 'Блоки 05-2/05-3', "value" : 'asset_2'},
                    #     {'label': 'Шахпахты', "value" : 'asset_3'},
                    #     {'label': 'ВИНЗ', "value" : 'asset_4'},
                    # ]
                ),
                # html.Div(id=f'output-container-{id}', children=''),
            ], className='filters-border')


@callback(
    Output("assets-checklist", "value"),
    Output("all-checklist", "value"),
    Input("assets-checklist", "value"),
    Input("all-checklist", "value"),
)
def sync_checklists(assets_checklist, all_selected):
    ctx = callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "assets-checklist":
        all_selected = ["Все"] if set(assets_checklist) == set(options_assets) else []
    else:
        assets_checklist = options_assets if all_selected else []
    return assets_checklist, all_selected

def radio_units(title):
    return html.Div([
                html.H5(f"{title}"),
                dcc.RadioItems(
                    id='radio_units',
                    options=[
                        {'label': 'млн.м3', 'value': 'mil_m3'},
                        {'label': 'млн.фут', 'value': 'mil_pounds'},
                        {'label': 'тыс.т', 'value': 'tho_tons'},
                        {'label': 'тыс.барр.', 'value': 'tho_bars'},
                        {'label': 'млн.тут', 'value': 'mil_tut'},
                    ],
                    # labelStyle={'display': 'block'}  # Отображаем лейблы по одному
                ),
                # html.Div(id='output-container', children=''),
            ], className="filters-border")



#просто тест
@callback(
        Output('props_test', 'children'),
        Input('hc-checklist', 'value'),
        Input('assets-checklist', 'value'),
        Input('radio_units', 'value'),
        Input('radio_period', 'value'),

)
def print_filters(hc, assets, units, period):
    return html.P(f"{hc} - {assets} - {units} - {period}")



#Получение данных о дате







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

            # dbc.Col([

            #     html.Div([

            #         html.H6("Фонд скважин"),
            #         html.H5("73%"),
            #         dbc.Row(
            #             [
            #                 dbc.Col(
            #                     [
            #                         html.P("Общий"),
            #                         html.P('16')
            #                     ]
            #                 ),
            #                 dbc.Col(
            #                     [
            #                         html.P("Действующий"),
            #                         html.P('15')
            #                     ]
            #                 ),  
            #                 dbc.Col(
            #                     [
            #                         html.P("В работе"),
            #                         html.P('10')
            #                     ]
            #                 ),
            #             ])
            #         ], className="info-card"),
                    
            # dbc.Col([
            #     html.Div([
            #         html.H6("Ключевые события"),
            #         html.H5("7"),
            #         dbc.Row(
            #             [
            #                 dbc.Col(
            #                     [
            #                         html.P("Плановое"),
            #                         html.P('16')
            #                     ]
            #                 ),
            #                 dbc.Col(
            #                     [
            #                         html.P("Внеплановое"),
            #                         html.P('15')
            #                     ]
            #                 ), 
            #             ]
            #         ),
            #     ], className="info-card")
            # ], className="stats-center"),
            # ])
        ], className="stats-block" ) 
        ])# className="stats-block")

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

# def upload_data():
#     return dbc.Form(
#         dbc.Row(
#             [
#                 # dbc.Label("Тип новой записи", width="auto"),
#                 dcc.Dropdown(
#                     id="operation-type",
#                     placeholder="Выберите",
#                     options=[
#                         {'label': 'Новая запись', 'value' : 'new'},
#                         {'label': 'Регулярное обновление', 'value' : 'update'}
#                     ],
#                     value='update'
#                 ),       
#                 html.Div(id='additional-fields'),
#                 # dbc.Button('Подтвердить', id='submit-button', n_clicks=0),
#             ]
#         )
#     )

# @callback(
#     Output('additional-fields', 'children'),
#     Input('operation-type', 'value')
# )
# def update_fields(operation_type):
#     if operation_type == 'new':
#         return html.Div([
#             dcc.Dropdown(
#                 id='data-type',
#                 options=[
#                     {'label': 'Страна', 'value': 'country'},
#                     {'label': 'Флюид', 'value': 'fluid'}
#                 ],
#                 value='country'
#             ),
#             html.Div(id='input-field'),
#         ])
#     else:
#         return html.Div()  # For regular updates, we assume no additional fields for now

# @callback(
#     Output('input-field', 'children'),
#     Input('data-type', 'value')
# )
# def display_input_field(data_type):
#     # if data_type == 'country':
#     #     return dcc.Input(id='country-name', type='text', placeholder='Введите название страны')
#     # elif data_type == 'fluid':
#     #     return dcc.Input(id='fluid-name', type='text', placeholder='Введите название флюида')
#     # return html.Div()
#     layout = html.Div([
#         dcc.Input(id=f'{data_type}-name', type='text', placeholder=f'Введите название'),
#         dbc.Row([
#             dbc.Button('Подтвердить', id='submit-button', n_clicks=0),
#         ]),
#         html.Div(id='output-message')
#     ])
#     return layout

# @callback(
#     Output('output-message', 'children'),
#     Input('submit-button', 'n_clicks'),
#     State('operation-type', 'value'),
#     State('data-type', 'value'),
#     State('country-name', 'value'),
#     State('fluid-name', 'value')
# )
# def handle_submission(n_clicks, operation_type, data_type, country_name, fluid_name):
#     if n_clicks > 0:
#         if operation_type == 'new':
#             if data_type == 'country':
#                 return f'Новая запись: страна - {country_name}'
#             elif data_type == 'fluid':
#                 return f'Новая запись: флюид - {fluid_name}'
#     return ''

def upload_data():
    
    select = dbc.Select(
        id="select_type",
        options=[
            {"label": "Регулярное обнволение", "value": "upd"},
            {"label": "Новая запись", "value": "new"},
        ],
        placeholder="..."
    )

    layout = html.Div(
            [
                dbc.Label("Тип записи"),
                select,
                html.Div(id="additional")

            ], className="centeredUplod")
    
    return layout 


# def testing_inputGroup():
#     dropdown_menu_items = [
#     dbc.DropdownMenuItem("Страна", id="dropdown-menu-country"),
#     dbc.DropdownMenuItem("Флюид", id="dropdown-menu-fluid"),
#     # dbc.DropdownMenuItem(divider=True),
#     # dbc.DropdownMenuItem("Clear", id="dropdown-menu-item-clear"),
#     ]

#     input_group = dbc.InputGroup(
#         [
#             dbc.DropdownMenu(dropdown_menu_items, label="Generate"),
#             dbc.Input(id="input-group-dropdown-input", placeholder="name"),
#         ]
#     )
#     return


@callback(
    Output('additional', 'children'),
    Input('select_type', 'value')
    
)
def config_selector(select_type):
    if select_type == "new":
        select = dbc.Select(
            id="select_new",
            options=[
                {"label": "Страна", "value": "s_country"},
                {"label": "Флюид", "value": "s_fluid"},
            ],
        )
        layout = html.Div(
            [
                dbc.Label("Объект"),
                select,
                html.Div(id="new_name")
            ]
        )
        return layout
    elif select_type == "upd":
        return html.Div([
                    dbc.Row([
                        dbc.Col(
                            [
                                dbc.Label("Период"),
                                dbc.Select(
                                        id="select_period",
                                        options=[
                                            {"label": "День", "value": "day"},
                                            {"label": "Месяц", "value": "month"},
                                            {"label": "Квартал", "value": "quarter"},
                                            {"label": "Год", "value": "year"},
                                        ],
                                    )
                            ]
                        ),
                        dbc.Col(
                            [
                                dbc.Label("Дата"),
                                dbc.Input(id="name_input", placeholder="...", type="text"),
                            ]
                        ),
                        dbc.Col(
                            [
                                 dbc.Label("Актив"),
                                 dbc.Input(id="name_input", placeholder="...", type="text"),
                            ]
                        ),
                        dbc.Col(
                            [
                                 dbc.Label("Скважина"),
                                 dbc.Input(id="name_input", placeholder="...", type="text"),
                            ]
                        ),
                        dbc.Col(
                            [
                                 dbc.Label("Месторождение"),
                                 dbc.Input(id="name_input", placeholder="...", type="text"),
                            ]
                        ),
                        dbc.Col(
                            [
                                 dbc.Label("Флюид"),
                                dbc.Select(
                                            id="hc-select",
                                            options=[
                                                {'label': 'Природный газ', "value" : 'nat_gas'},
                                                {'label': 'Газовый конденсат', "value" : 'condensate_gas'},
                                                {'label': 'Нефть', "value" : 'oil'},
                                                {'label': 'Газопродукты', "value" : 'product_gas'},
                                            ],
                                        ),
                            ]
                        ),
                        dbc.Col(
                            [
                                 dbc.Label("Объем"),
                                 dbc.Input(id="name_input", placeholder="...", type="text"),
                            ]
                        ),
                        dbc.Col(
                            [
                                dbc.Label("ЕИ"),
                                dbc.Select(
                                        id='Select_units',
                                        options=[
                                            {'label': 'млн.м3', 'value': 'mil_m3'},
                                            {'label': 'млн.фут', 'value': 'mil_pounds'},
                                            {'label': 'тыс.т', 'value': 'tho_tons'},
                                            {'label': 'тыс.барр.', 'value': 'tho_bars'},
                                            {'label': 'млн.тут', 'value': 'mil_tut'},
                                        ])
                            ]
                        ),
                        dbc.Col(
                            [
                                 dbc.Label("Лицензия"),
                                 dbc.Input(id="name_input", placeholder="...", type="text"),
                            ]
                        ),
                        dbc.Col(
                            [
                                 dbc.Label("План/Факт"),
                                 dbc.Select(
                                        id='Select_units',
                                        options=[
                                            {'label': 'Планированная', 'value': 'plan'},
                                            {'label': 'Фактическая', 'value': 'fact'},

                                        ])
                            ]
                        ),
                    ])
                ], className="moreSpaceUpload")
    

from db_main import load_countries

#Добавить проверку на повторение
@callback(
    Output('new_name', 'children'),
    Input('select_new', 'value')
)
def set_new_name(select_new):
    if select_new == "s_fluid" or select_new == "s_country":
        layout = html.Div(
            [
                dbc.Label("Название нового объекта"),
                dbc.Input(id="name_input", placeholder="...", type="text"),
                dbc.Button(
                        "Подтвердить", id="new_sub_button", className="me-2", n_clicks=0
                    ),
                html.Div(id="final_new"),
                
            ]
        )
        return layout
    else:
        return ''

@callback(
    Output('final_new', 'children'),
    Input('new_sub_button', 'n_clicks'),
    State('name_input', 'value'),
)
def add_new_country(n_clicks, value):
    if n_clicks:
        temp_data = load_countries()
        for item in temp_data:
            if item[0].lower() == value.lower():
                return dbc.Alert("Данная запись уже есть в базе.", color="danger"),
    
        return dbc.Alert("Данные успешно добавлены", color="success"),



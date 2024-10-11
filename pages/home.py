import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, callback_context

from datetime import date
from datetime import datetime

import calendar



from xlsx_parser import fig_with_wells, fig_plus, fig_waterfall
# from components import test_waterfall

dash.register_page(__name__, path="/", name='Главная страница')


period_radioitems = html.Div(
    [
        dbc.Label("Выберите один"),
        dbc.RadioItems(
            options=[
                {"label": "Месяц", "value": "month"},
                {"label": "Период", "value": "period"},
            ],
            value="month",
            id="period-radioitems",
        ),
    ]
)


#сделать проверку на минимальную и максимальную дату
@callback(
    Output("date-picker-container", "children"),
    Input("period-radioitems", "value")
)
def display_date_picker(value):
    if value == "period":
        return dcc.DatePickerRange(
            id="date-picker-range",
            start_date_placeholder_text="От",
            end_date_placeholder_text="До",
            display_format="YYYY-MM-DD",
            max_date_allowed=date(datetime.now().year, datetime.now().month-1, calendar.monthrange(datetime.now().year, datetime.now().month-1)[1])
        )
    return None





@callback(
    Output("output-date-picker", "children"),
    Input("date-picker-range", "start_date"),
    Input("date-picker-range", "end_date")
)
def update_output(start_date, end_date):
    if start_date and end_date:
        return f"Выбранный период: с {start_date} по {end_date} || {type(start_date)}"
    return None


@callback(
    Output('output-dateinfo-picker', 'children'),
    Input('date-picker-range', 'start_date'),
    Input('date-picker-range', 'end_date')
)
def update_output(start_date, end_date):
    if start_date and end_date:

        from_period(start_date, end_date)

        start = datetime.strptime(start_date, "%Y-%m-%d").date()
        end = datetime.strptime(end_date, "%Y-%m-%d").date()
        delta = (end - start).days
        
        

        if delta <= 31:
            return f"По дням - {delta}"
        elif delta <= 365:
            return f"По месяцам - {delta}"
        else:
            return f"По годам - {delta}"
    return ""





#тут обновление графиков
#кроме водопада!
#пока без оптимизации

from xlsx_parser import get_actual_data, create_fig_with_wells, create_fig_plus, get_gas_stats_monthly, from_period

@callback(
    [
        Output("first_chart", "figure"),
        Output("second_chart", "figure"),
        Output("output-month-picker", "children"),
        Output("total_gas_value", "children"),  # для обновления общего значения газа
        Output("month_change", "children"),  # для обновления изменения за месяц
        Output("month_change", "style"),     # для изменения цвета текста
        Output("year_change", "children"),   # для обновления изменения за год
        Output("year_change", "style")       # для изменения цвета текста
    ],
    Input("period-radioitems", "value"),
)
def update_output(value):
    if value == 'month':
        props = get_actual_data()
        stats = get_gas_stats_monthly(props[0], props[1])

        # Создаем графики
        fig1 = create_fig_with_wells(props[0], props[1], "(актуальный месяц)")
        fig2 = create_fig_plus(props[1], "(актуальный месяц)")

        # Формируем текст и стиль для изменения за месяц
        month_change_text = f"Месяц: {(stats['difference_by_month']/1000000):.2f} | {stats['percentage_by_month']:.2f}%"
        month_change_style = {"color": "#0ea64d"} if stats['percentage_by_month'] >= 0 else {"color": "#e24931"}

        # Формируем текст и стиль для изменения за год
        year_change_text = f"Год: {(stats['difference_by_year']/1000000):.2f} | {stats['percentage_by_year']:.2f}%"
        year_change_style = {"color": "#0ea64d"} if stats['percentage_by_year'] >= 0 else {"color": "#e24931"}

        # Обновляем общую сумму газа
        total_gas_value = f"{(stats['current_month_sum']/1000000):.1f}"

        return (
            fig1, 
            fig2, 
            f"Актуальный месяц сейчас - {datetime.now().month-1}\nПо данным - {props[0]}", 
            total_gas_value,
            month_change_text,
            month_change_style,
            year_change_text,
            year_change_style
        )

    # Если не выбран месяц, возвращаем пустые данные
    return {}, {}, None, "", "", {}, "", {}






hydrocarbons_checklist = html.Div(
    [
        dbc.Label("Можно выбрать несколько"),
        dbc.Checklist(
            options=[
                {"label": "Природный газ", "value": "natural_gas"},
                {"label": "Газовый конденсат", "value": "condensat"},
                {"label": "Нефть", "value": "oil", "disabled":True},
                {"label": "Газопродукты", "value": "products", "disabled":True},
            ],
            value="natural_gas",
            id="hydrocarbons-checklist",
            switch=True,
        ),
    ]
)

options_assets = ['Ипати Акио', 'Блоки 05-2/05-3', 'Шахпахты', 'ВИНЗ']
projects_checklist = html.Div([
    dbc.Label("Можно выбрать несколько"),
    dbc.Checklist(
        options=[{"label": "Все", "value" : "Все"}], 
        value=["Все"], 
        id="all-checklist",
        switch=True
        ),
    dbc.Checklist(
        options=[{"label" : asset , "value" : asset} for asset in options_assets],
        value=[],
        id="projects-checklist",
        switch=True
    ),
])

@callback(
    Output("projects-checklist", "value"),
    Output("all-checklist", "value"),
    Input("projects-checklist", "value"),
    Input("all-checklist", "value"),
)
def sync_checklists(projects_checklist, all_selected):
    ctx = callback_context
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]

    if input_id == "projects-checklist":
        if set(projects_checklist) == set(options_assets):
            all_selected = ["Все"]
        else:
            all_selected = []
    else:
        projects_checklist = options_assets if all_selected else []

    return projects_checklist, all_selected

units_radioitems = html.Div(
    [
        dbc.Label("Выберите один"),
        dbc.RadioItems(
            options=[
                {"label": "млн.м3", "value": "milm3"},
                {"label": "млн.фут", "value": "milpound", "disabled" : True},
                {"label": "тыс.т", "value": "thouton", "disabled" : True},
                {"label": "тыс.барр.", "value": "thoubars", "disabled" : True},
                {"label": "млн.тут", "value": "miltut", "disabled" : True}
            ],
            value="milm3",
            id="units-radioitems",
        ),
    ]
)

gas_stats_period = dbc.Toast(
    [
        html.H5(id="total_gas_value", children="Загрузкa...", className="m-0"),
        html.Div([
            html.P(children="Загрузкa...", id="month_change", className="mb-0", style={"color": "#0ea64d"}),
            html.P(children="Загрузкa...", id="year_change", className="mb-0", style={"color": "#e24931"}),
        ], className="pb-1 mt-1", style={"background-color": "rgba(142, 216, 248, 0.2)", "border-radius": "7px"})
    ],
    header="Газ (млн.м3)",
    className="p-0  mr-0",
    style={"width": "16rem"}
)

condensat_stats_period = dbc.Toast(
    [
        html.H5("1317.1", className="m-0"),
        html.Div([
            html.P("Месяц: +12.392 | +3.5%", className="mb-0", style={"color" : "#0ea64d"}),
            html.P("Год: +123.892 | -0.5%", className="mb-0", style={"color":"#e24931"}),
        ], className="pb-1 mt-1", style={"background-color" : "rgba(142, 216, 248, 0.2)", "border-radius": "7px"}),
        
    ],
    header="Конденсат (тыс.т)",
    className="p-0 mr-0",
    style={"width":"16rem"}


)


oil_stats_period = dbc.Toast(
    [
        html.H5("1317.1", className="m-0"),
        html.Div([
            html.P("Месяц: +12.392 | +3.5%", className="mb-0", style={"color" : "#0ea64d"}),
            html.P("Год: +123.892 | -0.5%", className="mb-0", style={"color":"#e24931"}),
        ], className="pb-1 mt-1", style={"background-color" : "rgba(142, 216, 248, 0.2)", "border-radius": "7px"}),
    ],
    header="Нефть (тыс.т)",
    className="p-0 mr-0",
    style={"width":"16rem"}



)


work_stats_period = dbc.Toast(
    [
        html.H5("99.2%", className="m-0"),
        html.Div([
            html.P("Месяц: +4%", className="mb-0", style={"color" : "#0ea64d"}),
            html.P("Год: -0.7%", className="mb-0", style={"color":"#e24931"}),
        ], className="pb-1 mt-1", style={"background-color" : "rgba(142, 216, 248, 0.2)", "border-radius": "7px"})
        
    ],
    header="Коэффициент эксплуатации",
    className="p-0 mr-0",
    style={"width":"16rem"}
)

wells_stats_period = dbc.Toast(
    [
        html.H5("75%", className="mb-0"),
        html.Div([
            dbc.Row(
            [
                dbc.Col([
                    html.P("Общий", className="mb-0"),
                    html.P("15", className="mb-0")
                ],style={"white-space" : "nowrap"}, className="m-0", width="auto", align="center"), #
                dbc.Col([
                    html.P("Действующий", className="mb-0"),
                    html.P("13", className="mb-0")
                ],style={"white-space" : "nowrap"}, className="m-0", width="auto", align="center"),
                dbc.Col([
                    html.P("В работе", className="mb-0"),
                    html.P("9", className="mb-0") #style={"padding-bottom" : "0"})
                ], style={"white-space" : "nowrap"}, className="m-0 pr-0", width="auto", align="center"),
            ],
                justify="center",
            ),
        ], className="pb-1 mt-1", style={"background-color" : "rgba(142, 216, 248, 0.2)", "border-radius": "7px"})
        
    ],
    className="p-0 m-0",
    header="Фонд скважин",
    # className="toast_me"
    style={"width":"18rem"}
)



key_events_stats_period = dbc.Toast(
    [
        html.H5("7", className="mb-0"),
        html.Div([
            dbc.Row(
            [
                dbc.Col([
                    html.P("Плановое", className="mb-0"),
                    html.P("15", className="mb-0")
                ],style={"white-space" : "nowrap", "color" : "#0ea64d"}, className="m-0", align="center"), #
                dbc.Col([
                    html.P("Внеплановое", className="mb-0"),
                    html.P("13", className="mb-0")
                ],style={"white-space" : "nowrap", "color" : "#e24931"}, className="m-0", align="center"),

            ],
            align="center"
            ),

        ], className="pb-1 mt-1", style={"background-color" : "rgba(142, 216, 248, 0.2)", "border-radius": "7px"})
                
    ],
    className="p-0 m-0",
    header="Ключевые события",
    # className="toast_me"
    style={"width":"16rem"}
    
)

#помещение фильтра в колапс
def to_collapse(item, unit_id, title):
    return html.Div(
        [
            dbc.Button(
                f"{title}",         
                id=f"collapse-button-{unit_id}",
                className="collapse-button",
                n_clicks=0,
            ),
            dbc.Collapse(
                dbc.Card(
                    item,
                    className="p-2"
                    ),
                id=f"collapse-{unit_id}",
                is_open=False,
            ),
        ]
    )

#работа с колапсами
@callback(
    Output("collapse-period", "is_open"),
    [Input("collapse-button-period", "n_clicks")],
    [State("collapse-period", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@callback(
    Output("collapse-hydrocarbons", "is_open"),
    [Input("collapse-button-hydrocarbons", "n_clicks")],
    [State("collapse-hydrocarbons", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output("collapse-projects", "is_open"),
    [Input("collapse-button-projects", "n_clicks")],
    [State("collapse-projects", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output("collapse-units", "is_open"),
    [Input("collapse-button-units", "n_clicks")],
    [State("collapse-units", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@callback(
    Output("radioitems-checklist-output", "children"),
    [Input("period-radioitems", "value"),
     Input("hydrocarbons-checklist", "value"),
     Input("projects-checklist", "value"),
     Input("units-radioitems", "value"),
     ]
)
def on_form_change(radio_items_value, hc_velues, projects, units):
    template = f"Период: {radio_items_value}, УВ: {hc_velues}, Проект: - {projects}, ЕИ: {units} selected."
    return template


layout = html.Div(
    [
        html.Div(
            [
                dbc.Row([
                    dbc.Col([gas_stats_period]),
                    dbc.Col([condensat_stats_period]),
                    dbc.Col([oil_stats_period]),
                    dbc.Col([work_stats_period]),
                    dbc.Col([wells_stats_period]),
                    dbc.Col([key_events_stats_period]),
                ], justify="center", style={"margin-bottom" : "2rem"})
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                                dbc.Row([
                                    dbc.Col([
                                        to_collapse(period_radioitems, "period", "По состоянию на"),
                                    ], width=12), 
                                ], className="mb-2"),
                                dbc.Row([
                                    dbc.Col([
                                        to_collapse(hydrocarbons_checklist, "hydrocarbons", "Тип УВ"),
                                    ], width=12),
                                ], className="mb-2"),
                                dbc.Row([
                                    dbc.Col([
                                        to_collapse(projects_checklist, "projects", "Активы"),
                                    ], width=12),
                                ], className="mb-2"),
                                dbc.Row([
                                    dbc.Col([
                                        to_collapse(units_radioitems, "units", "Един. измерения"),
                                    ], width=12),
                                ]),
                                dbc.Row([
                                    dbc.Col(
                                        html.Div([
                                        ], id='date-picker-container')
                                    , width=12)
                                ])
                            ],
                            style={"margin-top" : "3rem"},
                            className="filters",

                        ),
                    ],
                    width=2, 
                ),

                

                dbc.Col(
                    [

                        dbc.Row(
                            [
                                dbc.Col([
                                    fig_with_wells
                                ], md=6),
                                dbc.Col([
                                    fig_plus
                                ], md=6)
                            ]
                        ),
                        dbc.Row(
                            [
                                dbc.Col([
                                    fig_waterfall
                                ], md=6)
                            ]
                        )
                    ]
                )
            ],
        ),
        html.P(id="radioitems-checklist-output"),
        html.Div(id="output-date-picker"),
        html.Div(id="output-month-picker"),
        html.Div(id="output-dateinfo-picker") 
    ]
)







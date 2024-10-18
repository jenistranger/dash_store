import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, callback_context

from datetime import date
from datetime import datetime

import calendar

import devcallbacks


from devparser import fig_plus, fig_waterfall, test_with_wells #, fig_with_wells


from devparser import get_actual_data, create_fig_plus, get_gas_stats_monthly, from_period, figure_with_wells_condensat, figure_with_wells_gas, common_figure_wells



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

from db_main import select_hydrocarbons
hydrocarbons_list = select_hydrocarbons()
hydrocarbons_checklist = html.Div(
    [
        dbc.Label("Можно выбрать несколько"),
        dbc.Checklist(
            options=[{"label" : _hc, "value" : _hc} for _hc in hydrocarbons_list],
            # options=[
                
            #     {"label": "Природный газ", "value": "газ"},
            #     {"label": "Газовый конденсат", "value": "конденсат"},
            #     {"label": "Нефть", "value": "нефть", "disabled":True},
            #     {"label": "Газопродукты", "value": "products", "disabled":True},
            # ],
            value=[],
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


units_radioitems = html.Div(
    [
        dbc.Label("Выберите один"),
        dbc.RadioItems(
            options=[
                {"label": "м3", "value": "m3"},
                {"label": "фут", "value": "pound", "disabled" : True},
                {"label": "т", "value": "ton", "disabled" : True},
                {"label": "барр.", "value": "bars", "disabled" : True},
                {"label": "тут", "value": "tut", "disabled" : True}
            ],
            value="м3",
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

from genx import generate_wells_month

wells_genx = generate_wells_month(),

wells_stats_period = dbc.Toast(
    [
        html.H5(f"{wells_genx[0]['percent_found']}%", className="mb-0"),
        html.Div([
            dbc.Row(
            [
                dbc.Col([
                    html.P("Общий", className="mb-0"),
                    html.P(f"{wells_genx[0]['total']}", className="mb-0")
                ],style={"white-space" : "nowrap"}, className="m-0", width="auto", align="center"), #
                dbc.Col([
                    html.P("Действующий", className="mb-0"),
                    html.P(f"{wells_genx[0]['current']}", className="mb-0")
                ],style={"white-space" : "nowrap"}, className="m-0", width="auto", align="center"),
                dbc.Col([
                    html.P("В работе", className="mb-0"),
                    html.P(f"{wells_genx[0]['active']}", className="mb-0")
                ], style={"white-space" : "nowrap"}, className="m-0 pr-0", width="auto", align="center"),
            ],
                justify="center",
            ),
        ], className="pb-1 mt-1", style={"background-color" : "rgba(142, 216, 248, 0.2)", "border-radius": "7px"})
        
    ],
    className="p-0 m-0",
    header="Фонд скважин",
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
                                ], className="mb-2"),
                                
                                dbc.Row([
                                    dbc.Col([
                                        html.Div(
                                            [
                                                dbc.Button("Оперативная сводка"),
                                            ],
                                            className="d-grid gap-2",
                                        )
                                    ], width=12),
                                ], className="mb-2"),
                                dbc.Row([
                                    dbc.Col([
                                        html.Div(
                                            [
                                                dbc.Button("Отчёты оператора"),
                                            ],
                                            className="d-grid gap-2",
                                        )
                                    ], width=12),
                                ], className="mb-2"),
                                dbc.Row([
                                    dbc.Col([
                                        html.Div(
                                            [
                                                dbc.Button("Обзорная схема"),
                                            ],
                                            className="d-grid gap-2",
                                        )
                                    ], width=12),
                                ], className="mb-2"),
                                dbc.Row([
                                    dbc.Col([
                                        html.Div(
                                            [
                                                dbc.Button("Планирование"),
                                            ],
                                            className="d-grid gap-2",
                                        )
                                    ], width=12),
                                ], className="mb-2"),
                                dbc.Row([
                                    dbc.Col([
                                        html.Div(
                                            [
                                                dbc.Button("Ключевые события"),
                                            ],
                                            className="d-grid gap-2",
                                        )
                                    ], width=12),
                                ], className="mb-2"),


                                dbc.Row([
                                    dbc.Col(
                                        html.Div([
                                            dcc.DatePickerRange(
                                                id="date-picker-range",
                                                start_date_placeholder_text="От",
                                                end_date_placeholder_text="До",
                                                display_format="YYYY-MM-DD",
                                                max_date_allowed=date(datetime.now().year, datetime.now().month-1, calendar.monthrange(datetime.now().year, datetime.now().month-1)[1]),
                                                style={'display': 'none'}
                                            )
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
                                    # fig_with_wells
                                    test_with_wells
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


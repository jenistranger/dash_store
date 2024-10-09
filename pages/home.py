import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback, callback_context

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
            display_format="YYYY-MM-DD"
        )
    return None


from datetime import datetime



@callback(
    Output("output-date-picker", "children"),
    Input("date-picker-range", "start_date"),
    Input("date-picker-range", "end_date")
)
def update_output(start_date, end_date):
    if start_date and end_date:
        return f"Выбранный период: с {start_date} по {end_date}"
    return None


@callback(
    Output("output-month-picker", "children"),
    Input("period-radioitems", "value")
)
def update_output(value):
    if value == 'month':
        return f"Актуальный месяц - {datetime.now().month-1}"
    return None







hydrocarbons_checklist = html.Div(
    [
        dbc.Label("Можно выбрать несколько"),
        dbc.Checklist(
            options=[
                {"label": "Природный газ", "value": 1},
                {"label": "Газовый конденсат", "value": 2},
                {"label": "Нефть", "value": 3},
                {"label": "Газопродукты", "value": 4},
            ],
            value=[1],
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
                {"label": "млн.фут", "value": "milpound"},
                {"label": "тыс.т", "value": "thouton"},
                {"label": "тыс.барр.", "value": "thoubars"},
                {"label": "млн.тут", "value": "miltut"}
            ],
            value="milm3",
            id="units-radioitems",
        ),
    ]
)

gas_stats_period = dbc.Toast(
    [html.H5("Месяц: +12,392 | +3.5%", className="mb-0")],
    header="Газ (млн.м3)",
    className="toast_me"

)

condensat_stats_period = dbc.Toast(
    [html.P("Месяц: +12,392 | +3.5%", className="mb-0")],
    header="Конденсат (тыс.т)",
    className="toast_me"
)


oil_stats_period = dbc.Toast(
    [html.P("Месяц: +12,392 | +3.5%", className="mb-0")],
    header="Нефть (тыс.т)",
    className="toast_me"
)


work_stats_period = dbc.Toast(
    [html.P("Месяц: +12,392 | +3.5%", className="mb-0")],
    header="Коэффициент эксплуатации",
    className="toast_me"
)

wells_stats_period = dbc.Toast(
    [html.P("Месяц: +12,392 | +3.5%", className="mb-0")],
    header="Фонд скважин",
    className="toast_me"
)
key_events_stats_period = dbc.Toast(
    [html.P("Месяц: +12,392 | +3.5%", className="mb-0")],
    header="Ключевые события",
    className="toast_me"
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
    template = f"Radio button {radio_items_value}, hc - {hc_velues}, projects - {projects}, units - {units} selected."
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
                ])
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
                                    ], width=12),  # Установите ширину колонки
                                ], className="mb-2 mt-3"),  # Добавьте отступ между строками
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
                            className="filters",

                        ),
                    ],
                    width=2, 
                ),
                dbc.Col(
                    [
                        html.Div(
                            "graphs",
                            style={'border': '1px solid black'}
                        )
                    ]
                )
            ],
        ),
        html.P(id="radioitems-checklist-output"),
        html.Div(id="output-date-picker"),
        html.Div(id="output-month-picker") 
    ]
)







import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import Input, Output, State, callback

dash.register_page(__name__, path="/", name='Главная страница')



period_radioitems = html.Div(
    [
        dbc.Label("Выберите один"),
        dbc.RadioItems(
            options=[
                {"label": "Месяц", "value": "month"},
                {"label": "Год", "value": "year"},
                {"label": "Период", "value": "period"},
            ],
            value="month",
            id="period-radioitems",
        ),
    ]
)

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


projects_checklist = html.Div(
    [
        dbc.Label("Можно выбрать несколько"),
        dbc.Checklist(
            options=[
                {"label": "Все", "value": 1},
                {"label": "Проект 1", "value": 2},
                {"label": "Проект 2", "value": 3},
                {"label": "Проект 3", "value": 4},
                {"label": "Проект 4", "value": 5},
            ],
            value=[],
            id="projects-checklist",
            switch=True,
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
                className="mb-3",
                color="primary",
                n_clicks=0,
            ),
            dbc.Collapse(
                dbc.Card(
                    item
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




#нужно будет переписать
@callback(
    Output("projects-checklist", "value"),
    Input("projects-checklist", "value"),
    State("projects-checklist", "options")
)
def update_checklist(selected_projects, options):
    all_values = [option["value"] for option in options]
    if 1 in selected_projects:
        return all_values
    if len(all_values) != len(selected_projects):
        if 1 not in selected_projects:
            return selected_projects
        elif 1 in selected_projects:
            selected_projects.remove(1)
            return selected_projects




@callback(
    Output("radioitems-checklist-output", "children"),
    [Input("period-radioitems", "value"),
     Input("hydrocarbons-checklist", "value"),
     Input("projects-checklist", "value"),
     ]
)
def on_form_change(radio_items_value, hc_velues, projects):
    template = f"Radio button {radio_items_value}, hc - {hc_velues}, projects - {projects} selected."
    return template





layout = html.Div(
    [
        html.Div(
            [
                dbc.Row([
                    dbc.Col([
                        gas_stats_period
                    ]),
                    dbc.Col([
                        condensat_stats_period
                    ]),
                    dbc.Col([
                        oil_stats_period
                    ]),
                    dbc.Col([
                        work_stats_period
                    ]),
                    dbc.Col([
                        wells_stats_period
                    ]),
                    dbc.Col([
                        key_events_stats_period
                    ]),
                ])
            ]
        ),
        html.Div(
            [
                dbc.Row([
                    dbc.Col([
                        to_collapse(period_radioitems, "period", "По состоянию на"),
                    ], width=3),
                ]),
                dbc.Row([
                    dbc.Col([
                        to_collapse(hydrocarbons_checklist, "hydrocarbons", "Тип УВ"),
                    ], width=3),
                ]),
                dbc.Row([
                    dbc.Col([
                        to_collapse(projects_checklist, "projects", "Активы"),
                    ], width=3),
                ]),
            ]
        ),
        
        html.P(id="radioitems-checklist-output"),
    ]
)




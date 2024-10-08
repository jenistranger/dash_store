from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import dash_mantine_components as dmc

from flask import Flask

from components import test_graphs, navbar, test_stats, test_waterfall, radio_period, button_example, hc_checklist, radio_units, assets_checklist

app = Dash(server=Flask(__name__), external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.title = "Производство"


def main_page():
    return dbc.Container([
                # navbar,
                test_stats(),
                dbc.Row([
                    dbc.Col([
                                # html.Div(
                                #     dbc.Accordion(
                                #         [
                                #             dbc.AccordionItem(
                                #                 checklist_example(title="По состоянию на"),
                                #                 title="Item 1",
                                #             ),
                                #             dbc.AccordionItem(
                                #                 "This is the content of the second section",
                                #                 title="Item 2",
                                #             ),
                                #             dbc.AccordionItem(
                                #                 "This is the content of the third section",
                                #                 title="Item 3",
                                #             ),
                                #         ],
                                #         always_open=True,
                                #     )
                                # ),
                                # dropdown_example("Первый", "Второй", "Третий", id='dropdown_period', placeholder="Период"),
                                radio_period(title="По состоянию на"),
                                hc_checklist("Тип УВ"),
                                assets_checklist("Актив"),
                                radio_units("Един. измереня"),
                                html.Button('Оперативная сводка', id='submit-val', className="button-28"),
                                html.Button('Отчеты оператора', id='submit-val-1', className="button-28"),
                                html.Button('Обзорная схема', id='submit-val-2', className="button-28"),
                                html.Button('Планирование', id='submit-val-3', className="button-28"),
                                html.Button('Ключевые события', id='submit-val-4', className="button-28"),
                                html.Div(id='date_picker')
                            ], 
                            md=2),
                    #фильтры
                    dbc.Col([
                        #cтата
                        
                        dbc.Row([
                                dbc.Col(test_graphs("1"), md=6, className="graph-border"),
                                dbc.Col(test_graphs("2"), md=6, className="graph-border"),
                            ]),
                            dbc.Row([
                                dbc.Col(test_waterfall("График: 3"), md=6, className="graph-border"),
                                dbc.Col([
                                    dmc.Stack(
                                            # gap=0,
                                            children=[
                                                dmc.Skeleton(h=450),
                                            ],
                                        )
                                ])
                                # dbc.Col(test_graphs("4"), md=6, className="graph-border"),
                            ])
                    ])
                ])
            ], className="app-container ")


def help_page():
    return html.Div([
        html.H1("Помощь"),
    ])


from components import upload_data
def upload_page():
    return html.Div([
        upload_data()
    ])

routes = {
    "/": main_page,
    "/help": help_page,
    "/upload": upload_page
}

def render_page_content(pathname):
    if pathname in routes:
        return routes[pathname]()
    else:
        return html.Div([
            html.H1("Страница не найдена"),
        ])

app.layout = html.Div([
    
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(
                id="page-content",
                children=[]  # Здесь будет ваш контент страницы
            ),

    html.Footer([
        html.Div(id="props_test"),
        html.Div(id="props_test_2"),
    ])
])

@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    return render_page_content(pathname)



if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=53999, debug=True) 

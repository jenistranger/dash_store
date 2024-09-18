from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.Container import Container
import dash_mantine_components as dmc
from flask import Flask
from components import test_graphs, navbar, test_filters, test_stats, test_waterfall, dropdown_example, checklist_example, button_example, foo_checklist_example
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
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
                                checklist_example(title="По состоянию на"),
                                foo_checklist_example("Тип УВ", "hc-type", "Природный газ", "Газовый конденсат", "Нефть", "Газопродукт"),
                                html.Button('Оперативная сводка', id='submit-val', className="button-28"),
                                html.Button('Отчеты оператора', id='submit-val-1', className="button-28"),
                                html.Button('Обзорная схема', id='submit-val-2', className="button-28"),
                                html.Button('Планирование', id='submit-val-3', className="button-28"),
                                html.Button('Ключевые события', id='submit-val-4', className="button-28"),
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
                                dbc.Col(test_graphs("4"), md=6, className="graph-border"),
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
            )    # Навбар
    # dcc.Loading(
    #     id="loading-container",
    #     children=[
    #         html.Div(
    #             id="page-content",
    #             children=[]  # Здесь будет ваш контент страницы
    #         )
    #     ],
    #     type="circle",  # или "default", "cube", "dot", "graph", "circle"
    #     color="#476f95",  # цвет загрузки
    #     fullscreen=True  # показывать только на контенте страницы  лучше поставить False
    # )
    #удалить загрузку и оставить это
    # html.Div(id='page-content')
])
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    return render_page_content(pathname)
if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=55189, debug=True)

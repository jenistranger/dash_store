import dash
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import secrets
from flask import Flask

server = Flask(__name__)
server.secret_key = secrets.token_hex(16)
server.config["SESSION_PERMANENT"] = False
server.config["SESSION_TYPE"] = "filesystem"

app = Dash(server=server,
           url_base_pathname='/',
           suppress_callback_exceptions=True,
           assets_folder='assets',
           title='Производство',
           use_pages=True,
           pages_folder='devpages'
           )



navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Главное меню", href="/")),
        dbc.NavItem(dbc.NavLink("Экспорт", href="/#")),
        dbc.NavItem(dbc.NavLink("Поделиться", href="/#")),
        dbc.NavItem(dbc.NavLink("Комментарии", href="/#")),
        dbc.NavItem(dbc.NavLink("Настройки", href="/settings")),
        dbc.NavItem(dbc.NavLink("Помощь", href="/about")),
        dbc.NavItem(dbc.NavLink("Чат в TrueConf", href="/#")),
    ],
    brand="Производство",
    brand_href="/",
)
upper_sidebar = html.Div([html.H4(''), navbar],
                         className="upper_sidebar")

bottom_sidebar = html.Div(children=[html.H4("Версия 0.1")
], className='bottom_sidebar')

main_content = html.Div(dash.page_container,className="main_content")

app.layout = html.Div([
    upper_sidebar,
    main_content,
    bottom_sidebar
])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=53996, debug=True)

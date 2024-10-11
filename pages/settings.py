import dash
from dash import html

dash.register_page(__name__, path="/settings", name="Настройки")

layout = html.Div(
    [
        html.H1("Настройки"),
        html.P("Тут можно поменять цвета, расположение и т.д.")
    ]
)

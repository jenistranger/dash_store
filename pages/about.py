import dash
from dash import html

dash.register_page(__name__, path="/about", name="О приложении")

layout = html.Div(
    [
        html.H1("О приложении"),
        html.P("Здесь информация")
    ]
)

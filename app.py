
import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Rice Field Digital Twin"),
    html.P("3D interactive rice field with weather, IoT, ML model and satellite terrain.")
])

if __name__ == '__main__':
    app.run_server(debug=True)

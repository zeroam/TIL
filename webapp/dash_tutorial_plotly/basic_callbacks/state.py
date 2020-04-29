import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id="input-1-state", type="text", value="Montreal"),
        dcc.Input(id="input-2-state", type="text", value="Canada"),
        html.Button(id="submit-button-state", n_clicks=0, children="Submit"),
        html.Div(id="number-output"),
    ]
)


@app.callback(
    Output("number-output", "children"),
    [Input("submit-button-state", "n_clicks")],
    [State("input-1-state", "value"),
     State("input-2-state", "value")])
def update_output(n_clicks, input1, input2):
    return f"""
    The Button has been passed {n_clicks} times,
    Input 1 is "{input1}",
    and Input 2 is "{input2}"
    """


if __name__ == "__main__":
    app.run_server(debug=True)
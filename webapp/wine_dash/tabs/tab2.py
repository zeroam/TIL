import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

from app import app
from database import transforms

df = transforms.df

layout = html.Div(
    id='table-paging-with-graph-container',
    className='five columns'
)

@app.callback(Output('table-paging-with-graph-container', 'children'),
    [Input('rating-95', 'value'),
     Input('price-slider', 'value')])
def update_graph(ratingcheck, prices):
    dff = df

    low = prices[0]
    high = prices[1]

    dff = dff.loc[(dff['price'] >= low) & (dff['price'] <= high)]

    if ratingcheck == ['Y']:
        dff = dff.loc[dff['points'] >= 95]

    trace1 = go.Scattergl(
        x=dff['points'],
        y=dff['price'],
        mode='markers',
        opacity=0.7,
        marker={
            'size': 8,
            'line': {'width': 0.5, 'color': 'white'}
        },
        name='Price v Points'
    )

    return html.Div([
        dcc.Graph(
            id='rating-price',
            figure={
                'data': [trace1],
                'layout': dict(
                    xaxis={'type': 'log', 'title': 'Rating'},
                    yaxis={'title': 'Price'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])
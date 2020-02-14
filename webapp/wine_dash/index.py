import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table

import pandas as pd
import sqlite3
import plotly.graph_objs as go

from app import app
from database import transforms
from tabs import sidepanel, tab1, tab2


# get wine data as global variable
df = transforms.df

# set the app.layout
app.layout = sidepanel.layout

# callback to control the tab content
@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-1':
        return tab1.layout
    elif tab == 'tab-2':
        return tab2.layout

operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    print(filter_part)  # for debugging
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1:-1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # world operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3


@app.callback(
    Output('table-sorting-filtering', 'data'),
    [Input('table-sorting-filtering', 'page_current'),
     Input('table-sorting-filtering', 'page_size'),
     Input('table-sorting-filtering', 'sort_by'),
     Input('table-sorting-filtering', 'filter_query'),
     Input('rating-95', 'value'),
     Input('price-slider', 'value'),
    ])
def update_table(page_current, page_size, sort_by, filter, ratingcheck, prices):
    filtering_expressions = filter.split(' && ')
    dff = df
    print(ratingcheck)

    low = prices[0]
    high = prices[1]

    dff = dff.loc[(dff['price'] >= low) & (dff['price'] <= high)]

    if ratingcheck == ['Y']:
        dff = dff.loc[dff['points'] >= 95]

    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

    if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
        # these operators match pandas series operator method names
        dff = dff.loc[getattr(dff[col_name], operator)(filter_value)]
    elif operator == 'contains':
        dff = dff.loc[dff[col_name].str.contains(filter_value)]
    elif operator == 'datestartswith':
        # this is a simplification of the front-end filtering logic
        # only works with complete fields in standart format
        dff = dff.loc[dff[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff = dff.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )

    page = page_current
    size = page_size
    return dff.iloc[page * size: (page + 1) * size].to_dict('records')


if __name__ == '__main__':
    app.run_server()
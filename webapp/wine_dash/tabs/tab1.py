import dash_html_components as html
import dash_table

from database import transforms

df = transforms.df

PAGE_SIZE = 50
layout = html.Div(dash_table.DataTable(
    id='table-sorting-filtering',
    columns=[
        {'name': i, 'id': i, 'deletable': True} for i in df
    ],
    style_table={
        'height': '750px', 'overflowX': 'scroll'
    },
    style_data_conditional=[
        {
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgb(248, 248, 248)'
        }
    ],
    style_cell={
        'height': '90',
        # all three widths are needed
        'minwidth': '140px', 'width': '140px', 'maxWidth': '140px',
        'textAlign': 'left', 'whiteSpace': 'normal'
    },
    style_cell_conditional=[
        {'if': {'column_id': 'description'},
        'width': '48%'},
        {'if': {'column_id': 'title'},
        'width': '18%'},
    ],
    page_current=0,
    page_size=PAGE_SIZE,
    page_action='custom',
    filter_action='custom',
    filter_query='',
    sort_action='custom',
    sort_mode='multi',
    sort_by=[]
))
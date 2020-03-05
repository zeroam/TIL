import praw
import pandas as pd
import pprint

import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_table
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from config import cid, csec, ua


# create a reddit connection
reddit = praw.Reddit(client_id = cid,
                     client_secret=csec,
                     user_agent=ua)


def get_posts_from_reddit(subreddit):
    # list for df conversion
    posts = []

    # return 100 new posts from wallstreetbets
    new_bets = reddit.subreddit('wallstreetbets').new(limit=100)

    # return the important attribute
    for post in new_bets:
        posts.append([post.title, post.score, post.num_comments, 
                    post.selftext, post.created, post.pinned,
                    post.total_awards_received])

    # create a dataframe
    posts_df = pd.DataFrame(posts, columns=['title', 'score', 'comments',
                        'post', 'created', 'pinned', 'total awards'])

    # copy the dataframe
    df = posts_df.copy()
    # count words in post
    df['words'] = df['post'].apply(lambda x : len(x.split()))
    # count characters in post
    df['chars'] = df['post'].apply(lambda x : len(x.replace(' ', '')))
    # calculate word density
    df['word density'] = (df['words'] / (df['chars'] + 1)).round(3)
    # count unique words
    df['unique words'] = df['post'].apply(lambda x: len(set(w for w in x.split())))
    # percent of unique words
    df['unique density'] = (df['unique words'] / df['words']).round(3)

    return df


app = dash.Dash(__name__)
df = get_posts_from_reddit('wallstreetbets')

app.layout = html.Div([
    html.P(html.Button('Refresh', id='refresh')),
    html.P(html.Div(html.H3('Enter Subreddit'))),
    dcc.Input(id='input-1-state', type='text', value='wallstreetbets'),
    dash_table.DataTable(
        id='table',
        style_cell_conditional=[
            {'if': {'column_id': 'title'},
             'width': '200px'},
            {'if': {'column_id': 'post'},
             'width': '670px',
             'height': 'auto'},
        ],
        style_cell={
            'overflow': 'hidden',
            'textOverflow': 'ellipsis',
            'maxWidth': '50px'
        },
        style_table={
            'maxHeight': '700px',
            'overflowY': 'scroll'
        },
        style_data_conditional=[
            {
                'if': {
                    'column_id': 'score',
                    'filter_query': '{score} gt 50'
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'score',
                    'filter_query': '{score} lt 10'
                },
                'backgroundColor': '#B20000',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'comments',
                    'filter_query': '{comments} gt 45'
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'comments',
                    'filter_query': '{comments} lt 20'
                },
                'backgroundColor': '#B20000',
                'color': 'white',
            },
            {
                'if': {
                    'column_id': 'unique density',
                    'filter_query': '{unique density} lt 0.7'
                },
                'backgroundColor': '#3D9970',
                'color': 'white',
            }
        ],
        columns=[{'name': i, 'id': i} for i in df.columns],
        data=df.to_dict('records')
    )
])


@app.callback(Output('table', 'data'),
              [Input('refresh', 'n_clicks')],
              [State('input-1-state', 'value')])
def update_data(n_clicks, subreddits):
    if subreddits is None:
        subreddits = 'wallstreetbets'
    else:
        subreddits

    print(n_clicks)

    if n_clicks is None:
        raise PreventUpdate
    else:
        df = get_posts_from_reddit(subreddits)

        return df.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
import dash
import dash_auth
import dash_html_components as html


VALID_USERNAME_PASSWORD_PAIRS = [
    ['hello', 'world']
]

app = dash.Dash('auth')
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.H1(
    children='Hello World'
)


if __name__ == '__main__':
    app.run_server()
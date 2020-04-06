from flask import Flask
app = Flask(__name__,
            instance_relative_config=False,
            template_folder='templates',
            static_folder='static')


@app.route('/')
def hello():
    return 'Hello World'

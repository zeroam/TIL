import pandas as pd
from pydataset import data
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.debug = True
Bootstrap(app)


@app.route('/show', methods=['GET'])
def dataViewer_2():
    dataset_name = request.args.get('dataset')
    if dataset_name == None:
        dataset_name = 'Aids2'

    if type(data(dataset_name)) != pd.core.frame.DataFrame:
        return (f'Bad dataset name:{dataset_name}')

    df = data(dataset_name)

    return render_template('df.html', name=dataset_name, 
        data=df.to_html())


if __name__ == '__main__':
    app.run()

import pandas as pd
from pydataset import data

from flask import Flask, request

app = Flask(__name__)
app.debug = True


@app.route('/show', methods=['GET'])
def dataViewer_1():
    dataset_name = request.args.get('dataset')
    if dataset_name == None:
        dataset_name = 'Aids2'  # default if no arg passed

    if type(data(dataset_name)) != pd.core.frame.DataFrame:
        return(f'Bad dataset name:{dataset_name}')

    return data(dataset_name).to_html(header='true',
        table_id='table')


if __name__ == '__main__':
    app.run()

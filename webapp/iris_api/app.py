import os
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from model.Train import train_model
from sklearn.externals import joblib

app = Flask(__name__)
api = Api(app)

if not os.path.isfile('iris-model.model'):
    train_model()

model = joblib.load('iris-model.model')


class MakePrediction(Resource):
    @staticmethod
    def post():
        posted_data = request.get_json()
        sepal_length = posted_data['sepal_length']
        sepal_width = posted_data['sepal_width']
        petal_length = posted_data['petal_length']
        petal_width = posted_data['petal_width']

        prediction = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
        class_name = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
        predicted_class = class_name[prediction]

        return jsonify({
            'Prediction': predicted_class
        })

api.add_resource(MakePrediction, '/predict')


if __name__ == '__main__':
    app.run(debug=True)
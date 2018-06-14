from flask import Flask, request
from flask import render_template, make_response
from flask_restful import Resource, Api
from flask_jsonpify import jsonify
from Tweetext import Tweetext

app = Flask(__name__)
api = Api(app)


@app.route('/', methods = ['GET', 'POST'])
def classify():
    if request.method == 'GET':
        return jsonify({"data": 'nothing'})

    elif request.method == 'POST':
        req_data = request.get_json()
        input = req_data['input']

        # empty input
        if len(input) <= 1:
            return jsonify({"result" : "Invalid: empty string"})

        # invalid input
        if not isinstance(input, str):
            return jsonify({"result": "Invalid: not string"})

        classifier = Tweetext()
        label = classifier.classify(input)

        return jsonify({"result": label})


# class Classifier(Resource):
#     def __init__(self):
#         # Create classifier
#         self.classifier = Tweetext()
#
#     def get(self):
#         return make_response(render_template('classifier.html'), 200,)
#         # return jsonify({"data": 'nothing'})
#
#     def post(self):
#
#         #Posted Input as json
#         req = request.form
#         #get input value
#         input = req['input']
#         label = "label"
#
#         # empty input
#         if len(input) <= 1:
#             return make_response(render_template('classifier.html'), 200,)
#
#         # invalid input
#         if not isinstance(input, str):
#             result = "Invalid input."
#
#         else:
#             # classify input, and get it's label(category)
#             result = self.classifier.classify(input)
#
#         self.classifier.__del__()
#         # Send result
#         return make_response(render_template('classifier.html', label = result ))
#         # return jsonify({"label" : result})
#
# api.add_resource(Classifier,'/')  # Route_1

if __name__ == '__main__':
    app.run(port=5002, debug = True)

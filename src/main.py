from flask import Flask, jsonify, abort

months = [
    {"id": 1, "name": "January"},
    {"id": 2, "name": "Febuary"},
    {"id": 3, "name": "March"},
    {"id": 4, "name": "April"},
    {"id": 5, "name": "May"},
    {"id": 6, "name": "June"},
    {"id": 7, "name": "July"},
    {"id": 8, "name": "Agust"},
    {"id": 9, "name": "September"},
    {"id": 10, "name": "Oktober"},
    {"id": 11, "name": "November"},
    {"id": 12, "name": "December"},
]

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_months():
    return jsonify(months)

@app.route("/", methods=["POST"])
def post_months():
    return jsonify({"success": True}), 201

@app.route("/", methods=["PUT"])
#TODO: make function for update api

@app.route("/", methods=["DELETE"])
#TODO: make function for delete api


#TODO: make function that returns the errors 

#TODO: make function for format on the return of each requests


if __name__ == "__main__":
    app.run(debug=True)


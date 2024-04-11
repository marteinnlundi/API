from flask import Flask, jsonify, request, abort

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
    # Assuming data comes in as JSON for a new month like: {"id": 13, "name": "NewMonth"}
    data = request.get_json()
    if 'id' not in data or 'name' not in data:
        abort(400, description="Missing 'id' or 'name' in request body")
    months.append(data)
    return jsonify({"success": True}), 201

@app.route("/<int:month_id>", methods=["PUT"])
def put_months(month_id):
    data = request.get_json()
    month = next((m for m in months if m['id'] == month_id), None)
    if not month:
        abort(404, description="Month not found")
    month.update(data)
    return jsonify(month)

@app.route("/<int:month_id>", methods=["DELETE"])
def delete_month(month_id):
    global months
    months = [m for m in months if m['id'] != month_id]
    return jsonify({"success": True}), 204

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found', 'message': error.description}), 404

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad request', 'message': error.description}), 400

if __name__ == "__main__":
    app.run(debug=True)

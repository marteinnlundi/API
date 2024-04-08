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

@app.route("/", methods=["GET"])
def get_months():
    return jsonify(months)

@app.route("/", methods=["POST"])
def post_months():
    return jsonify({"success": True}), 201

if __name__ == "__main__":
    app.run(debug=True)

    
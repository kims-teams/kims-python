from flask import Flask, request, jsonify
from input.service.data_cleaner import get_json_result

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process_data():
    try:
        input_data = request.get_json()
        result_json = get_json_result(input_data)
        return result_json, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)

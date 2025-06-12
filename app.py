from flask import Flask, request, jsonify
from input.service.data_cleaner import get_json_result
from flask_cors import CORS
import pandas as pd


app = Flask(__name__)
CORS(app)

@app.route("/process", methods=["POST"])
def process_data():
    try:
        input_data = request.get_json()
        result_json = get_json_result(input_data)
        return result_json, 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/upload/<entity>", methods=['POST'])
def upload_file(entity):
    print(entity)
    if 'file' not in request.files:
        return jsonify({'error': '파일이 없습니다.'}), 400

    file = request.files['file']
    filename = file.filename

    #  확장자 검사: .csv 또는 .xlsx만 허용
    if not filename.lower().endswith(('.csv', '.xlsx')):
        return jsonify({'error': 'CSV 또는 Excel(xlsx) 파일만 업로드할 수 있습니다.'}), 400

    try:
        if filename.lower().endswith('.csv'):
            # 한글 깨짐 방지를 위해 utf-8-sig → cp949 순서로 시도
            try:
                df = pd.read_csv(file, encoding='utf-8-sig')
            except UnicodeDecodeError:
                file.seek(0)  # 파일 포인터를 처음으로 되돌림
                df = pd.read_csv(file, encoding='cp949')
        else:
            df = pd.read_excel(file)
            # 엑셀 파일인 경우

        from input.service.data_cleaner import clean_uploaded_dataframe

        result = clean_uploaded_dataframe(entity, df)

        return jsonify(result)

    except Exception as e:
        # 예외 처리
        return jsonify({'error': str(e)}), 500



def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


if __name__ == "__main__":
    app.run(debug=True, port=5000)



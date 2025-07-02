import traceback
from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import input.service.data_cleaner as cleaner
from input.service.arima_service import arima_function
from input.service.prophet_service import prophet_function

app = Flask(__name__)
CORS(app)


@app.route("/api/input-file/<entity>", methods=['POST'])
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

        result = cleaner.clean_uploaded_dataframe(entity, df)

        return jsonify(result)

    except Exception as e:
        # 예외 처리
        print("💥 Flask 서버 예외 발생:")
        traceback.print_exc()  # ← 전체 에러 스택 찍힘
        return jsonify({'error': str(e)}), 500


@app.route("/api/forecast/arima", methods=['POST'])
def api_arima():
    file = request.files['file']
    data = pd.read_excel(file, dtype={"시점": "str"})
    result = arima_function(data)
    return jsonify(result)


@app.route("/api/forecast/prophet", methods=['POST'])
def api_prophet():
    file = request.files['file']
    data = pd.read_excel(file, dtype={"시점": "str"})
    result = prophet_function(data)
    return jsonify(result)



if __name__ == "__main__":
    app.run(debug=True, port=5000)

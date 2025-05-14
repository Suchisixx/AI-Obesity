from flask import Flask, request, render_template
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

# Tải mô hình và các thành phần cần thiết
xgb = joblib.load('xgb_model.pkl')
grid = joblib.load('grid_model.pkl')
label_encoder = joblib.load('label_encoder.pkl')
columns = joblib.load('columns.pkl')  # danh sách cột đúng lúc training

# Các cột đầu vào
num_cols = ['Age', 'Height']
binary_cat_cols = ['Sex', 'Overweight_Obese_Family', 'Consumption_of_Fast_Food', 'Smoking', 'Calculation_of_Calorie_Intake']
multi_cat_cols = [
    'Frequency_of_Consuming_Vegetables', 'Number_of_Main_Meals_Daily',
    'Food_Intake_Between_Meals', 'Liquid_Intake_Daily', 'Physical_Excercise',
    'Schedule_Dedicated_to_Technology', 'Type_of_Transportation_Used'
]
all_cat_cols = binary_cat_cols + multi_cat_cols

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = {}
        for col in num_cols + all_cat_cols:
            value_str = request.form.get(col)
            if value_str is None or value_str.strip() == "":
                return render_template('index.html', prediction_text=f'Vui lòng nhập đầy đủ thông tin cho trường: {col}')
            try:
                value = float(value_str)
            except ValueError:
                return render_template('index.html', prediction_text=f'Dữ liệu không hợp lệ cho {col}. Hãy nhập số.')

            # Kiểm tra hợp lệ
            allowed_values = {
                'Sex': [1, 2], 'Overweight_Obese_Family': [1, 2], 'Consumption_of_Fast_Food': [1, 2],
                'Smoking': [1, 2], 'Calculation_of_Calorie_Intake': [1, 2],
                'Frequency_of_Consuming_Vegetables': [1, 2, 3], 'Number_of_Main_Meals_Daily': [1, 2, 3],
                'Food_Intake_Between_Meals': [1, 2, 3, 4], 'Liquid_Intake_Daily': [1, 2, 3],
                'Physical_Excercise': [1, 2, 3, 4, 5], 'Schedule_Dedicated_to_Technology': [1, 2, 3],
                'Type_of_Transportation_Used': [1, 2, 3, 4, 5]
            }
            if col in allowed_values and int(value) not in allowed_values[col]:
                return render_template('index.html', prediction_text=f'Giá trị không hợp lệ cho {col}. Cho phép: {allowed_values[col]}')

            data[col] = value

        # Tạo DataFrame
        input_df = pd.DataFrame([data])

        # KHÔNG mã hóa one-hot, vì dữ liệu huấn luyện không mã hóa
        # Chỉ cần reindex để đảm bảo các cột khớp với columns.pkl
        input_encoded = input_df.reindex(columns=columns, fill_value=0)

        # Dự đoán
        pred_xgb = xgb.predict(input_encoded)[0]
        pred_grid = grid.predict(input_encoded)[0]

        # Giải mã nhãn
        class_names = {1: 'Thiếu cân', 2: 'Bình thường', 3: 'Thừa cân', 4: 'Béo phì'}
        result_xgb = class_names[label_encoder.inverse_transform([pred_xgb])[0]]
        result_grid = class_names[label_encoder.inverse_transform([pred_grid])[0]]

        return render_template('index.html', prediction_text=f'<strong>XGBoost:</strong> {result_xgb}<br><strong>GridSearch:</strong> {result_grid}')
    except Exception as e:
        return render_template('index.html', prediction_text=f'Đã xảy ra lỗi: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
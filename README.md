## Hướng Dẫn Dự Án AI-Obesity

### 1. Giới Thiệu Dự Án

**AI-Obesity** là một dự án sử dụng trí tuệ nhân tạo sử dụng mô hình XGBoost để **dự đoán tình trạng béo phì** dựa trên dữ liệu thực tế. Nhằm hỗ trợ các nghiên cứu y tế và chăm sóc sức khỏe.
- Nguồn dữ liệu : https://www.kaggle.com/datasets/suleymansulak/obesity-dataset

### Mục tiêu:
- Phân loại các mức độ béo phì dựa trên đặc trưng người dùng.
- Xử lý mất cân bằng dữ liệu bằng kỹ thuật **SMOTE**.
- Dùng GridSearchCV tìm lưới tham số để tối ưu hóa mô hình dự đoán
- Cung cấp mã nguồn, mô hình, và hướng dẫn tái sử dụng.

### Tính năng chính:
- Tiền xử lý dữ liệu bằng Python (Jupyter Notebook).
- Huấn luyện mô hình phân loại (XGBoost).
- Lưu mô hình bằng `joblib` để tái sử dụng.
- Triển khai giao diện web dự đoán với Flask.

---

### 2. Yêu Cầu Hệ Thống

### Phần mềm:
- Python 3.8+
- Jupyter Notebook
- Git (để clone repo)
- Trình duyệt (nếu chạy web app)

### 📦 Thư viện Python:
Bạn cần các thư viện sau:

```text
from flask import Flask, request, render_template
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler 
from sklearn.dummy import DummyClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBClassifier
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

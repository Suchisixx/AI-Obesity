# Hướng Dẫn Dự Án AI-Obesity

## 1. Giới Thiệu Dự Án

**AI-Obesity** là một dự án sử dụng trí tuệ nhân tạo để phân tích và **dự đoán mức độ béo phì** dựa trên dữ liệu thực tế. Dự án này áp dụng các kỹ thuật **machine learning (học máy)**, đặc biệt là **XGBoost**, nhằm hỗ trợ các nghiên cứu y tế và chăm sóc sức khỏe.

### Mục tiêu:
- Phân loại các mức độ béo phì dựa trên đặc trưng người dùng.
- Xử lý mất cân bằng dữ liệu bằng kỹ thuật **SMOTE**.
- Cung cấp mã nguồn, mô hình, và hướng dẫn tái sử dụng.

### ⚙️ Tính năng chính:
- Tiền xử lý dữ liệu bằng Python (Jupyter Notebook).
- Huấn luyện mô hình phân loại (XGBoost).
- Lưu mô hình bằng `joblib` để tái sử dụng.
- (Tùy chọn) Triển khai giao diện web đơn giản với Flask.

---

## 2. 💻 Yêu Cầu Hệ Thống

### 🧩 Phần mềm:
- Python 3.8+
- Jupyter Notebook
- Git (để clone repo)
- Trình duyệt (nếu chạy web app)

### 📦 Thư viện Python:
Bạn cần các thư viện sau:

```text
pandas
numpy
scikit-learn
xgboost
imbalanced-learn
jupyter

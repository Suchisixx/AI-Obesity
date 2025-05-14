Dự án AI-Obesity

Tổng quan
Dự án AI-Obesity là một sáng kiến nhằm phân tích và dự đoán mức độ béo phì bằng các kỹ thuật học máy (machine learning). Kho lưu trữ này chứa mã nguồn, dữ liệu và các mô hình đã được huấn luyện để khám phá và xây dựng mô hình dự đoán phân loại béo phì dựa trên nhiều đặc trưng khác nhau.

Tính năng
Tiền xử lý và phân tích dữ liệu bằng Python và Jupyter Notebook.
Áp dụng các mô hình học máy (ví dụ: XGBoost) để dự đoán béo phì.
Xử lý tập dữ liệu bằng file Excel và các đối tượng đã được lưu dưới dạng pickle để tối ưu hóa.
Khám phá kỹ thuật cân bằng dữ liệu như SMOTE để xử lý các lớp không cân bằng.

Các file trong dự án
Obesity-Code.ipynb: File Jupyter Notebook chính chứa mã nguồn để xử lý dữ liệu, huấn luyện và đánh giá mô hình.
Obesity_Dataset.xlsx: Tập dữ liệu được sử dụng để huấn luyện và kiểm tra mô hình.
app.py: Tệp Python, có thể dùng để tạo ứng dụng web hoặc API để tương tác với mô hình.
columns.pkl, grid_model.pkl, label_encoder.pkl, scaler.pkl, xgb_model.pkl: Các file pickle lưu trữ dữ liệu đã xử lý, mô hình và cấu hình.
templates/: Thư mục chứa các template HTML (nếu có, dùng cho giao diện web).
README.md: File này, cung cấp tổng quan về dự án.

Cài đặt
Tải kho lưu trữ về máy:

git clone https://github.com/Suchisix/AI-Obesity.git

Di chuyển vào thư mục dự án:

cd AI-Obesity
Cài đặt các thư viện cần thiết:

pip install -r requirements.txt

(Lưu ý: Hãy tạo file requirements.txt với các thư viện cần thiết như pandas, numpy, scikit-learn, xgboost, imbalanced-learn, nếu chưa có.)

Đảm bảo bạn đã cài đặt Jupyter Notebook để chạy các file .ipynb.

Cách sử dụng
Mở file Obesity-Code.ipynb trong Jupyter Notebook để xem và chạy mã nguồn.
Tải tập dữ liệu từ Obesity_Dataset.xlsx và tiền xử lý theo hướng dẫn trong notebook.
Huấn luyện và đánh giá mô hình bằng các đoạn mã đã cung cấp.
(Tùy chọn) Chạy file app.py nếu có triển khai giao diện web hoặc API.

Tập dữ liệu
Tập dữ liệu (Obesity_Dataset.xlsx) chứa các đặc trưng liên quan đến béo phì, với nhãn cho các lớp khác nhau. Dự án áp dụng kỹ thuật SMOTE để giải quyết vấn đề mất cân bằng lớp, giúp cải thiện hiệu suất trên các lớp thiểu số.

Đóng góp
Bạn có thể fork kho lưu trữ này, thực hiện cải tiến và gửi pull request. Đối với các thay đổi lớn, vui lòng mở một issue trước để thảo luận về ý tưởng của bạn.

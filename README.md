Hướng Dẫn Dự Án AI-Obesity

1. Giới Thiệu Dự Án

Dự án AI-Obesity tập trung vào việc sử dụng trí tuệ nhân tạo (AI) để phân tích và dự đoán mức độ béo phì dựa trên dữ liệu. Dự án này triển khai các kỹ thuật học máy (machine learning) để xây dựng mô hình phân loại béo phì, giúp hỗ trợ nghiên cứu và ứng dụng trong lĩnh vực y tế.

Mục Tiêu





Phân loại các mức độ béo phì dựa trên các đặc trưng trong tập dữ liệu.



Xử lý dữ liệu không cân bằng bằng kỹ thuật SMOTE để cải thiện hiệu suất mô hình.



Cung cấp mã nguồn và tài liệu để người dùng khác có thể tái sử dụng và phát triển.

Các Tính Năng Chính





Tiền xử lý dữ liệu với Python và Jupyter Notebook.



Huấn luyện mô hình học máy (XGBoost) để dự đoán béo phì.



Lưu trữ và tái sử dụng mô hình qua các file pickle.



(Tùy chọn) Triển khai giao diện web hoặc API thông qua file app.py.



2. Yêu Cầu Hệ Thống

Để chạy dự án này, bạn cần chuẩn bị các phần mềm và công cụ sau:

Phần Mềm Cần Thiết





Python 3.8+: Ngôn ngữ lập trình chính.



Jupyter Notebook: Để chạy file Obesity-Code.ipynb.



Git: Để tải mã nguồn từ GitHub.



Trình duyệt web: Nếu bạn chạy app.py để sử dụng giao diện web.

Thư Viện Python

Dưới đây là danh sách các thư viện cần thiết:





pandas: Xử lý dữ liệu.



numpy: Tính toán số học.



scikit-learn: Xây dựng và đánh giá mô hình học máy.



xgboost: Mô hình chính để dự đoán.



imbalanced-learn: Xử lý dữ liệu không cân bằng (SMOTE).



jupyter: Chạy file notebook.

Bạn có thể cài đặt tất cả bằng cách tạo file requirements.txt với nội dung sau và chạy lệnh cài đặt.



3. Hướng Dẫn Cài Đặt

Bước 1: Tải Mã Nguồn

Tải kho lưu trữ từ GitHub bằng lệnh sau:

git clone https://github.com/Suchisix/AI-Obesity.git

Bước 2: Di Chuyển Vào Thư Mục Dự Án

cd AI-Obesity

Bước 3: Cài Đặt Thư Viện

Tạo file requirements.txt với nội dung sau:

pandas
numpy
scikit-learn
xgboost
imbalanced-learn
jupyter

Sau đó, chạy lệnh:

pip install -r requirements.txt

Bước 4: Kiểm Tra Jupyter Notebook

Đảm bảo bạn có thể chạy Jupyter Notebook:

jupyter notebook



4. Cấu Trúc Dự Án

Dự án bao gồm các file và thư mục sau:





Obesity-Code.ipynb: File chính chứa mã nguồn để tiền xử lý, huấn luyện và đánh giá mô hình.



Obesity_Dataset.xlsx: Tập dữ liệu về béo phì, chứa các đặc trưng và nhãn.



app.py: File Python để triển khai ứng dụng (nếu có).



columns.pkl, grid_model.pkl, label_encoder.pkl, scaler.pkl, xgb_model.pkl: Các file lưu trữ mô hình và dữ liệu đã xử lý.



templates/: Thư mục chứa các file HTML (nếu có giao diện web).



README.md: Tài liệu hướng dẫn này.



5. Hướng Dẫn Sử Dụng

5.1. Khám Phá Dữ Liệu





Mở file Obesity-Code.ipynb bằng Jupyter Notebook:

jupyter notebook Obesity-Code.ipynb



Xem phần tiền xử lý dữ liệu để hiểu cách dữ liệu được đọc từ Obesity_Dataset.xlsx và chuẩn hóa.

5.2. Huấn Luyện Mô Hình





Trong Obesity-Code.ipynb, chạy các ô mã nguồn liên quan đến huấn luyện mô hình XGBoost.



Kiểm tra việc sử dụng SMOTE để cân bằng dữ liệu (nếu có).



Lưu ý: Các file pickle (xgb_model.pkl, v.v.) đã chứa mô hình được huấn luyện sẵn, bạn có thể tải trực tiếp nếu không muốn huấn luyện lại.

5.3. Đánh Giá Mô Hình





Xem phần đánh giá trong notebook, bao gồm các chỉ số như accuracy, f1-score, và ma trận nhầm lẫn.



So sánh hiệu suất mô hình với và không dùng SMOTE.

5.4. Triển Khai Ứng Dụng (Tùy Chọn)

Nếu dự án có giao diện web:





Chạy file app.py:

python app.py



Mở trình duyệt và truy cập địa chỉ được cung cấp (thường là http://localhost:5000).



6. Thông Tin Tập Dữ Liệu

Tập dữ liệu Obesity_Dataset.xlsx chứa các đặc trưng liên quan đến béo phì, ví dụ:





Cân nặng, chiều cao, BMI.



Thói quen ăn uống, hoạt động thể chất.



Nhãn phân loại (ví dụ: thiếu cân, bình thường, thừa cân, béo phì).

Dữ liệu có hiện tượng mất cân bằng lớp (imbalanced classes), và dự án đã áp dụng kỹ thuật SMOTE để xử lý vấn đề này.



7. Đóng Góp

Chúng tôi hoan nghênh mọi đóng góp từ cộng đồng:





Fork kho lưu trữ này.



Tạo nhánh mới cho thay đổi của bạn:

git checkout -b ten-nhanh-moi



Commit và push thay đổi:

git commit -m "Mô tả thay đổi"
git push origin ten-nhanh-moi



Mở pull request trên GitHub.

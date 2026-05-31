# 📷 Smart RollCall System

Welcome to the **RollCall** repository! Manual attendance tracking is time-consuming and prone to errors. This project solves that by transforming standard cameras into smart, biometric attendance loggers.

Using cutting-edge Computer Vision and Facial Recognition, **RollCall** detects, identifies, and logs individuals in real-time, instantly updating an attendance database or spreadsheet. 

## ✨ Key Features
* **Real-Time Face Recognition:** Accurately detects and identifies registered faces from a live video feed with high confidence.
* **Automated Data Logging:** Automatically marks the timestamp and attendance status, exporting the daily logs to a database or CSV file.
* **Dynamic Registration:** Easy pipeline to enroll new individuals by capturing their facial encodings and saving them to the system.
* **Dashboard / Reporting (Optional):** Generates clean, formatted attendance sheets for easy administrative review.

## 🛠️ Technical Stack
* **Language:** Python
* **Vision & AI:** OpenCV (`cv2`), `face_recognition` (dlib)
* **Data Management:** Pandas, SQLite / CSV
* **UI/Web (If applicable):** Streamlit / Tkinter / Flask



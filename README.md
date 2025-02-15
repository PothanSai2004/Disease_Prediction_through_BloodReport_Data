# Disease Prediction through Blood Report Data

## 🏥 Project Overview
This project leverages **Machine Learning** to predict diseases based on blood report data. It utilizes an **ensemble learning approach** combining **Random Forest, SVM, and Gradient Boost** to classify six different diseases with high accuracy.

## 🚀 Features
- **Multi-Disease Prediction:** Supports prediction of multiple diseases using blood test parameters.
- **Ensemble Learning:** Uses Random Forest, Support Vector Machine (SVM), and Gradient Boost.
- **Web-Based Interface:** Flask-based web application for easy access.
- **Data Preprocessing:** Implements scaling, encoding, and feature engineering.
- **Model Persistence:** Trained models are stored as `.pkl` files for quick inference.

## 📂 Project Structure
```
├── static/                   # CSS, JS, and image files
├── templates/                # HTML templates for the web interface
├── app.py                    # Main Flask application
├── commitment_model.pkl       # Trained machine learning model
├── label_encoder.pkl          # Label encoder for categorical features
├── scaler.pkl                 # Scaler for data normalization
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation
```

## 🖼 Project Outcomes
![image](https://github.com/user-attachments/assets/d40a32f7-9a3e-467a-b0f9-a493adaa6c79)
![image](https://github.com/user-attachments/assets/5f5e47ab-8983-4ce2-9f63-a59ffd25f731)

### Web Interface
![image](https://github.com/user-attachments/assets/e3ad68cc-47ae-41c9-a3c2-2fa00ddc566b)
![image](https://github.com/user-attachments/assets/e83f66cf-9e39-4288-a015-f5216e544606)


## ⚙️ Setup Instructions
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### **2️⃣ Create and Activate Virtual Environment (Optional but Recommended)**
```bash
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```bash
python app.py
```
The Flask app should now be running on **http://127.0.0.1:5000/**

## 📌 Technologies Used
- **Programming Language:** Python
- **Machine Learning:** Random Forest, SVM, Gradient Boost
- **Frameworks:** Flask
- **Libraries:** Pandas, NumPy, Scikit-Learn, Matplotlib
- **Storage:** Pickle (`.pkl` models for persistence)

## ✨ Contributing
Feel free to fork this repository and contribute to improvements. Pull requests are welcome!

## 📜 License
This project is licensed under the **MIT License**.

---

🔗 **Author:** [Your Name](https://github.com/your-username)  
📩 **Contact:** your-email@example.com  
🚀 **GitHub Repo:** [Disease Prediction](https://github.com/your-username/your-repository-name)

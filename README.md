# 🎓 Campus Placement Prediction

A machine learning web application that predicts whether a student will get placed on campus based on academic and personal profile data.

---

## 📌 Overview

This project uses historical campus recruitment data to train a classification model that predicts placement outcomes. The web interface is built with Flask, allowing students to input their details and instantly get a placement prediction.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Web Framework | Flask |
| ML Library | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Language | Python 3.x |

---

## 📁 Project Structure

```
campus-placement-prediction/
│
├── app.py                  # Flask application entry point
├── model.py                # ML model training and saving
├── requirements.txt        # Project dependencies
│
├── data/
│   └── placement_data.csv  # Dataset
│
├── model/
│   └── placement_model.pkl # Saved trained model
│
├── templates/
│   ├── index.html          # Input form page
│   └── result.html         # Prediction result page
│
├── static/
│   └── style.css           # Styling
│
└── notebooks/
    └── EDA.ipynb           # Exploratory Data Analysis
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/campus-placement-prediction.git
cd campus-placement-prediction
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Train the Model
```bash
python model.py
```

### 5. Run the Flask App
```bash
python app.py
```

### 6. Open in Browser
```
http://127.0.0.1:5000
```

---

## 📊 Input Features

The model uses the following student attributes for prediction:

| Feature | Description |
|---|---|
| Gender | Male / Female |
| SSC Percentage | 10th grade marks (%) |
| SSC Board | Central / Others |
| HSC Percentage | 12th grade marks (%) |
| HSC Board | Central / Others |
| HSC Stream | Science / Commerce / Arts |
| Degree Percentage | Graduation marks (%) |
| Degree Type | Field of graduation |
| Work Experience | Yes / No |
| Employability Test Score | Aptitude test percentage |
| MBA Percentage | MBA marks (%) |
| Specialisation | Mkt&HR / Mkt&Fin |

---

## 🎯 Output

- **Placed** ✅ — Student is likely to get placed
- **Not Placed** ❌ — Student may not get placed

---

## 🤖 ML Models Used

The following models were trained and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier *(best performer)*
- Support Vector Machine (SVM)

### Model Evaluation Metrics
- Accuracy
- Precision & Recall
- F1 Score
- Confusion Matrix

---

## 📈 Sample Results

```
Model               Accuracy
---------------------------
Logistic Regression   82%
Decision Tree         79%
Random Forest         87%  ✅ Best
SVM                   84%
```

---

## 📦 requirements.txt

```
Flask
Scikit-Learn
Pandas
Numpy
matplotlib
Seaborn
```

---

## 🚀 Future Improvements

- Add more features like certifications, internships, backlogs
- Deploy on Render / Railway / Vercel
- Add student dashboard with history
- Improve UI with Bootstrap or Tailwind CSS
- Use deep learning for better accuracy

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@aravind-18y](https://github.com/aravind-18y)
- LinkedIn: [aravind pasupuleti](https://linkedin.com/in/aravind-pasupuleti)

---

## 📄 License

This project is licensed under the MIT License.

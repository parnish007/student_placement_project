

# 🎓 Student Placement Prediction System

### *An End-to-End Machine Learning Problem-Solving Project*

![Banner](https://github.com/parnish007/student_placement_project/blob/main/frontend/assests/banner.jpg)

---

## 🚨 Problem Statement

Campus placements are one of the most critical and stressful phases of a student’s academic journey.
Despite having grades, skills, and experience, students **lack a clear, data-driven indicator** of their placement readiness.

### ❌ The Problem

* Students don’t know *where they stand*
* Colleges lack early prediction tools
* Placement decisions are often reactive, not proactive

---

## 💡 Solution

This project builds a **Machine Learning–powered placement prediction system** that predicts whether a student is likely to be:

> ✅ **Placed** or ❌ **Not Placed**

based on **academic performance, skills, and experience**.

It is a **complete end-to-end ML project**, covering:

* Data analysis
* Model training
* Evaluation
* Deployment via Streamlit

---

## 🧠 Model Input Features

The prediction is based on the following **real-world student attributes**:

| Feature                    | Description                       |
| -------------------------- | --------------------------------- |
| **IQ**                     | Cognitive ability score           |
| **Prev_Sem_Result**        | Previous semester academic result |
| **CGPA**                   | Overall cumulative GPA            |
| **Academic_Performance**   | Academic consistency indicator    |
| **Internship_Experience**  | Internship experience (Yes/No)    |
| **Extra_Curricular_Score** | Activities & participation score  |
| **Communication_Skills**   | Soft skills rating                |
| **Projects_Completed**     | Number of completed projects      |

🎯 **Target Variable:**
`Placed` / `Not Placed`

---

## 🛠 Tech Stack

| Category      | Tools               |
| ------------- | ------------------- |
| Language      | Python              |
| ML            | Scikit-learn        |
| Data          | Pandas, NumPy       |
| Visualization | Matplotlib, Seaborn |
| Frontend      | Streamlit           |
| Notebook      | Jupyter             |

---

## 📂 Project Structure

```
student_placement_project/
│
├── dataset/                 # Training dataset
├── notebook/                # EDA & model building (.ipynb)
├── model/                   # Trained ML model
├── frontend/
│   ├── app.py               # Streamlit app
│   └── assets/
│       ├── banner.png
│       ├── output1.png
│       └── output2.png
├── requirements.txt
└── README.md
```

---

## 📊 Jupyter Notebook (ML Workflow)

The `.ipynb` notebook documents **everything**:

✔ Data loading & preprocessing
✔ Feature selection
✔ Model training
✔ Accuracy score calculation
✔ Evaluation metrics
✔ Model saving for deployment

📌 Located inside: `notebook/`

This makes the project **transparent, explainable, and interview-ready**.

---

## 📈 Model Performance

The model is evaluated using standard ML metrics such as:

* Accuracy Score
* Prediction consistency
* Classification results

📌 Exact performance metrics are shown in the notebook.

---

## 🖥 Application Screenshots

### 🔹 Student Input Interface

![App Input UI](frontend/assets/output1.png)

---

### 🔹 Placement Prediction Result

![Prediction Output](https://github.com/parnish007/student_placement_project/blob/main/frontend/assests/output1.png)
![Prediction Output]((https://github.com/parnish007/student_placement_project/blob/main/frontend/assests/output2.png))


These screenshots show the **real working application**, not mockups.

---

## 🚀 How to Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/parnish007/student_placement_project.git
cd student_placement_project
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run Streamlit App

```bash
streamlit run frontend/app.py
```

➡ Open in browser: `http://localhost:8501`

---

## 🔄 Machine Learning Pipeline

1. Data ingestion
2. Feature preprocessing
3. Model training
4. Model evaluation
5. Model serialization
6. Real-time prediction via Streamlit

This project demonstrates **production-style ML workflow**, not just experimentation.

---

## 🌱 Future Enhancements

* Use advanced models (Random Forest, XGBoost)
* Add probability confidence scores
* Deploy on cloud (Streamlit Cloud / Render)
* Enable CSV batch predictions

---

## 💼 Why This Project Stands Out

✅ Solves a real-world problem
✅ End-to-end ML pipeline
✅ Clean code & structure
✅ Deployed application
✅ Explainable notebooks

Perfect for:

* ML / Data Science internships
* Placement interviews
* GitHub portfolio

---

## ⭐ Support

If you found this project useful:

* ⭐ Star the repository
* 🍴 Fork it
* 📢 Share it



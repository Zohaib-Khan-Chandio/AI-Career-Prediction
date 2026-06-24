# AI Career Prediction System

An intelligent web-based career guidance system that predicts the most suitable career path for students based on their academic background, aptitude scores, and personal preferences.

The system uses a Decision Tree Machine Learning Model trained on student-related data to analyze user inputs and recommend career tracks with confidence scores. The trained model is stored and loaded at runtime, enabling fast and efficient predictions without retraining.

---

## Project Overview

Choosing the right career path can be difficult for students due to the variety of available options. This project helps students make informed decisions by using Artificial Intelligence and Machine Learning techniques.

The application collects information about:

* Academic background
* Subject interests
* Aptitude levels
* Personal preferences
* Work environment choices

Based on these inputs, the Decision Tree model predicts the most suitable career track and displays confidence percentages for the top recommendations.

---

## Features

### Academic Information Collection

Students provide:

* Matriculation background
* Intermediate program
* Academic performance level

### Aptitude Assessment

Interactive rating system (1–5) for:

* Mathematics Skills
* Verbal Skills
* Creative Skills
* Technical Skills

### Preference Analysis

Students select:

* Preferred study duration
* Desired work environment

### AI-Powered Prediction

* Uses a pre-trained Decision Tree model
* Generates real-time predictions
* No model retraining required during execution

### Prediction Dashboard

Displays:

* Best Career Recommendation
* Confidence Percentage
* Runner-Up Career Options
* Probability Visualization

### Reset Functionality

Allows users to start the assessment again without reloading the entire application.

---

## Why Decision Tree?

The core machine learning algorithm used in this project is the Decision Tree Classifier.

A Decision Tree works similarly to human decision-making by asking a series of questions and splitting data into branches until a final prediction is reached.

### Example

If a student has:

* High Mathematics Skill
* High Technical Aptitude
* Science Background

The Decision Tree may follow a path such as:

```text
Math Skill > 4
    ├── Technical Skill > 4
    │       └── Software Engineering
    └── Technical Skill ≤ 4
            └── Data Analysis
```

### Advantages of Decision Trees

* Easy to understand and interpret
* Fast prediction speed
* Handles both numerical and categorical data
* Visual representation of decision-making process
* Requires minimal data preprocessing

### Model Performance

* Algorithm: Decision Tree Classifier
* Accuracy: Approximately 92%
* Model Storage: `trained_model.pkl`
* Inference Type: Real-Time Prediction

---

## Technology Stack

### Backend

* Python
* Flask

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* Decision Tree Classifier

### Frontend

* HTML5
* CSS3
* JavaScript (ES6)

### Model Deployment

* Pickle (`.pkl`)

---

## Project Structure

```text
AI-Career-Prediction/
│
├── app.py
├── trained_model.pkl
├── requirements.txt
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Zohaib-Khan-Chandio/AI-Career-Prediction.git

cd AI-Career-Prediction
```

### 2. Create Virtual Environment

#### Windows

```powershell
python -m venv venv

.\venv\Scripts\Activate.ps1
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

```text
http://127.0.0.1:5000
```

or

```text
http://localhost:5000
```

---

## Workflow

1. Student enters academic information.
2. Student rates aptitude skills.
3. Student selects preferences.
4. Data is sent to the Flask backend.
5. The Decision Tree model processes the input.
6. Career prediction is generated.
7. Results and confidence scores are displayed.

---

## Future Improvements

* Random Forest Comparison
* Career Recommendation Reports (PDF)
* User Authentication System
* Career Trend Analytics
* Model Retraining Interface
* Career Roadmap Suggestions
* Database Integration

---

## Author

**Zohaib Khan Chandio**

BBA Student | Machine Learning Enthusiast

GitHub: https://github.com/Zohaib-Khan-Chandio

---

## License

This project is developed for educational and academic purposes.

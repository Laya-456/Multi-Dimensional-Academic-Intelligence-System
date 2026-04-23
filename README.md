# Multi-Dimensional Academic Intelligence System

## Overview

This project analyzes student performance using multiple parameters such as **marks, attendance, and assignment scores**.
It uses Python along with libraries like **Pandas, NumPy, and Matplotlib** to perform structured data analysis, classification, and generate meaningful insights.

---

##  Features

* Random student data generation
* Data storage using **Lists, Tuples, Dictionary, Set**
* Statistical analysis using **NumPy**
* Structured representation using **Pandas DataFrame**
* Feature Engineering (**Performance Index**)
* Student classification (At Risk, Average, Good, Top Performer)
* Pattern detection (Consistency, Attendance Risk, Top Performers)
* Visualization using **Matplotlib**
* Final system insight generation

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Math module
* Random module

---

## Data Structure

Each student record contains:

```
(StudentID, Marks, Attendance, Assignments, PerformanceIndex)
```

---

## Working Process

### 1️. Data Generation

* Generates student data using `random`
* Number of students based on **last digit of roll number**

---

### 2️. Feature Engineering

Performance Index is calculated as:

```
Performance Index = (Marks * 0.6 + Assignments * 0.4) * log(Attendance + 1)
```

---

### 3️. Classification Logic

* **At Risk** → Marks < 40 OR Attendance < 50
* **Top Performer** → Marks > 90 AND Attendance > 80
* **Good** → Marks between 71–90
* **Average** → Remaining students

---

### 4️. Statistical Analysis

* Mean (manual calculation)
* Median
* Standard Deviation
* Correlation (Marks vs Attendance)
* Normalization of marks

---

### 5️. Pattern Detection

* **Consistency** → Std Dev < 15
* **Attendance Risk** → More than 3 students with attendance < 50
* **Top Performers** → At least 2 students

---

### 6️. Final Insight

* Stable Academic System
* Moderate Performance
* Critical Attention Required

---

## Learning Outcomes

* Applied real-world data analysis using Python
* Understood integration of multiple libraries
* Learned feature engineering and normalization
* Improved logical thinking using classification and pattern detection

---

## How to Run

```bash
pip install pandas numpy matplotlib
python your_file_name.py
```

import random
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

roll_last_digit = 6
num_students = roll_last_digit if roll_last_digit != 0 else 10

def generate_data(n):
    data=[]
    for i in range(1,n+1):
        marks=random.randint(0,100)
        attendance=random.randint(0,100)
        assignments=random.randint(0,50)
        perf_index=(marks*0.6 + assignments*0.4)*math.log(attendance+1)
        data.append((i, marks, attendance, assignments, perf_index))
    return data

def classify_students(df):
    categories={}
    for _,row in df.iterrows():
        sid=row['StudentID']
        marks=row['Marks']
        attendance=row['Attendance']
        if marks<40 or attendance<50:
            categories[sid]="At Risk"
        elif marks>90 and attendance>80:
            categories[sid]="Top Performer"
        elif 71 <= marks <= 90:
            categories[sid]="Good"
        else:
            categories[sid]="Average"
    return categories

def analyze_data(df):
    marks = df['Marks'].values
    mean_marks = sum(marks) / len(marks)
    median_marks = np.median(marks)
    std_dev = np.std(marks)
    max_marks = np.max(marks)
    correlation = np.corrcoef(df['Marks'], df['Attendance'])[0][1]
    min_m=np.min(marks)
    max_m=np.max(marks)
    df['Normalized_Marks'] = [(x - min_m) / (max_m - min_m) if max_m != min_m else 0 for x in marks]
    consistency = "Consistent" if std_dev < 15 else "Inconsistent"
    attendance_risk = sum(df['Attendance'] < 50) > 3
    top_performers = sum(
        (df['Marks'] > 90) & (df['Attendance'] > 80)        
    ) >= 2
    if consistency == "Consistent" and not attendance_risk:
        insight="Stable Academic System"
    elif attendance_risk:
        insight="Critical Attention required"
    else:
        insight="Moderate Performance"
    summary_tuple=(mean_marks, std_dev, max_marks)
    return summary_tuple, correlation, consistency, attendance_risk, top_performers, insight

data=generate_data(num_students)
unique_ids = {student[0] for student in data}
print("\n==== UNIQUE STUDENT IDS ====")
print(unique_ids)
df=pd.DataFrame(data, columns=['StudentID', 'Marks', 'Attendance', 'Assignments', 'PerformanceIndex'])
categories=classify_students(df)
summary, corr, consistency, att_risk, top_perf, insight=analyze_data(df)
print("\n==== STUDENT DATA ====")
print(df)
print("\n==== CATEGORY DICTIONARY ====")
print(categories)
print("\n==== STATISTICAL SUMMARY ====")
print("Mean Marks:", summary[0])
print("Standard Deviation:", summary[1])
print("Maximum Marks:", summary[2])
print("Median Marks:", np.median(df['Marks']))
print("\nCorrelation between Marks and Attendance:", corr)
print("\n==== PATTERN DETECTION ====")
print("Consistency:", consistency)
print("Attendance Risk(>3 students <50%):", att_risk)
print("Top Performers >= 2:", top_perf)
print("\n==== FINAL SYSTEM INSIGHT ====")
print("Insight:", insight)

plt.hist(df['Marks'], bins=5)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Distribution of Student Marks")
plt.show()
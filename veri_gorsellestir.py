import pandas as pd
import matplotlib.pyplot as plt

# Load data
student_data = pd.read_csv('ogrenci_veri.csv')

# Create histograms for exam scores and daily study hours
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.hist(student_data['exam_score'], bins=20, color='blue', alpha=0.7)
plt.title('Distribution of Exam Scores')
plt.xlabel('Exam Scores')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(student_data['daily_study_hours'], bins=20, color='green', alpha=0.7)
plt.title('Distribution of Daily Study Hours')
plt.xlabel('Daily Study Hours')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Scatter plot between exam scores and daily study hours
plt.figure(figsize=(8, 6))
plt.scatter(student_data['daily_study_hours'], student_data['exam_score'], color='red', alpha=0.5)
plt.title('Scatter Plot of Exam Scores vs. Daily Study Hours')
plt.xlabel('Daily Study Hours')
plt.ylabel('Exam Scores')
plt.grid()
plt.show()
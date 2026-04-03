
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

students = data["StudentID"]
math_scores = data["MathScore"]

plt.figure()
plt.bar(students, math_scores)

plt.xlabel("Student ID")
plt.ylabel("Math Score")
plt.title("Math Scores of Students")

plt.xticks(rotation=90)

plt.show()
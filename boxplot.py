import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df[['MathScore', 'PhysicsScore', 'ChemistryScore', 'ProgrammingScore']].boxplot()

plt.title('Box Plot of Student Scores')
plt.xlabel('Subjects')
plt.ylabel('Scores')

plt.show()
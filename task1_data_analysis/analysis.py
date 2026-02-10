import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("employee_data.csv")

print(data.head())
print("Average Salary:", data["Salary"].mean())

plt.bar(data["Name"], data["Salary"])
plt.title("Salary Distribution")
plt.show()

plt.scatter(data["Experience"], data["Salary"])
plt.title("Experience vs Salary")
plt.show()

sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

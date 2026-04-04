import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x=["A","B"], y=[10,20])

plt.title("Simple Bar Chart")
plt.xlabel("Category")
plt.ylabel("Values")
plt.show()

labels = ["A", "B", "C"]
sizes = [5, 75, 20]


plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Pie Chart Example")
plt.show()
# import pandas as pd
# import numpy as np

# np.random.seed(42)

# n = 400

# location = np.array(["Urban"]*200 + ["Rural"]*200)

# digital_payment = []

# for loc in location:
#     if loc == "Urban":
#         digital_payment.append(np.random.choice(["Yes","No"], p=[0.7,0.3]))
#     else:
#         digital_payment.append(np.random.choice(["Yes","No"], p=[0.435,0.565]))

# income = np.random.randint(15000,100000,n)

# monthly_expenditure = income * np.random.uniform(0.5,0.9,n)

# discretionary_spending = monthly_expenditure * np.random.uniform(0.2,0.4,n)

# data = pd.DataFrame({
#     "Location":location,
#     "Digital_Payment":digital_payment,
#     "Income":income,
#     "Monthly_Expenditure":monthly_expenditure.astype(int),
#     "Discretionary_Spending":discretionary_spending.astype(int)
# })

# data.to_csv("../dataset/digital_payment_dataset.csv",index=False)

# print("Dataset created successfully")
# print(data.head())


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

np.random.seed(42)

n = 400

location = np.array(["Urban"]*200 + ["Rural"]*200)

digital_payment = []

for loc in location:
    if loc == "Urban":
        digital_payment.append(np.random.choice(["Yes","No"], p=[0.7,0.3]))
    else:
        digital_payment.append(np.random.choice(["Yes","No"], p=[0.435,0.565]))

income = np.random.randint(15000,100000,n)

monthly_expenditure = income * np.random.uniform(0.5,0.9,n)

discretionary_spending = monthly_expenditure * np.random.uniform(0.2,0.4,n)

data = pd.DataFrame({
    "Location":location,
    "Digital_Payment":digital_payment,
    "Income":income,
    "Monthly_Expenditure":monthly_expenditure.astype(int),
    "Discretionary_Spending":discretionary_spending.astype(int)
})

# save dataset
data.to_csv("../dataset/digital_payment_dataset.csv",index=False)

print("Dataset created successfully")

# create visualization folder
os.makedirs("../report/plots",exist_ok=True)

sns.set(style="whitegrid")

# 1 Adoption distribution
plt.figure()
sns.countplot(data=data,x="Digital_Payment")
plt.title("Digital Payment Adoption Distribution")
plt.savefig("../report/plots/adoption_distribution.png")

# 2 Urban vs Rural adoption
plt.figure()
sns.countplot(data=data,x="Location",hue="Digital_Payment")
plt.title("Urban vs Rural Digital Payment Adoption")
plt.savefig("../report/plots/location_adoption.png")

# 3 Income distribution
plt.figure()
sns.histplot(data["Income"],kde=True)
plt.title("Income Distribution")
plt.savefig("../report/plots/income_distribution.png")

# 4 Expenditure vs Digital payment
plt.figure()
sns.boxplot(data=data,x="Digital_Payment",y="Monthly_Expenditure")
plt.title("Expenditure Comparison")
plt.savefig("../report/plots/expenditure_vs_payment.png")

# 5 Discretionary spending
plt.figure()
sns.barplot(data=data,x="Digital_Payment",y="Discretionary_Spending")
plt.title("Discretionary Spending Comparison")
plt.savefig("../report/plots/discretionary_spending.png")

# 6 Income vs expenditure scatter
plt.figure()
sns.scatterplot(data=data,x="Income",y="Monthly_Expenditure",hue="Digital_Payment")
plt.title("Income vs Monthly Expenditure")
plt.savefig("../report/plots/income_vs_expenditure.png")

# 7 Correlation heatmap
plt.figure()
corr = data[["Income","Monthly_Expenditure","Discretionary_Spending"]].corr()
sns.heatmap(corr,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.savefig("../report/plots/correlation_heatmap.png")

print("All visualizations saved in report/plots folder")
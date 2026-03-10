import pandas as pd
from scipy.stats import chi2_contingency, ttest_ind

data = pd.read_csv("../dataset/digital_payment_dataset.csv")

# Chi-square test
contingency = pd.crosstab(data["Location"],data["Digital_Payment"])
chi2,p,_,_ = chi2_contingency(contingency)

print("Chi-square test")
print("p-value:",p)

# t-test
adopters = data[data["Digital_Payment"]=="Yes"]["Discretionary_Spending"]
non_adopters = data[data["Digital_Payment"]=="No"]["Discretionary_Spending"]

t,p = ttest_ind(adopters,non_adopters)

print("\nT-test discretionary spending")
print("p-value:",p)
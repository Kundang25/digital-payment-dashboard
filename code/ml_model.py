import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

data = pd.read_csv("../dataset/digital_payment_dataset.csv")

# encode values
data["Location"] = data["Location"].map({"Urban":1,"Rural":0})
data["Digital_Payment"] = data["Digital_Payment"].map({"Yes":1,"No":0})

X = data[["Location","Income","Monthly_Expenditure","Discretionary_Spending"]]
y = data["Digital_Payment"]

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = RandomForestClassifier()

model.fit(X_train,y_train)

pred = model.predict(X_test)

print(classification_report(y_test,pred))
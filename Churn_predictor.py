
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

data = pd.DataFrame({
    "monthly_bill": [500,800,600,1200,400,900,700,1100,450,850],
    "tenure_months": [24,3,18,2,36,1,12,4,30,2],
    "support_calls": [1,5,2,8,0,6,1,7,0,5],
    "will_leave": [0,1,0,1,0,1,0,1,0,1]
})
print(data)

X = data[["monthly_bill","tenure_months","support_calls"]]
Y = data["will_leave"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, Y_train)

accuracy = model.score(X_test, Y_test)
print(f"Accuracy: {accuracy*100:.1f}%")

monthly_bill = int(input("Monthly bill: "))
tenure_months = int(input("Tenure (months): "))
support_call = int(input("Support calls: "))

prediction = model.predict([[monthly_bill, tenure_months, support_call]])

if prediction[0] == 1:
    print("Will Churn")
else:
    print("Will Stay")

print("System End")

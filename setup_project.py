import os

# main folder
base = "Digital_Payment_Project"

# subfolders
folders = [
    "dataset",
    "code",
    "powerbi",
    "report"
]

# create main folder
os.makedirs(base, exist_ok=True)

# create subfolders
for folder in folders:
    os.makedirs(os.path.join(base, folder), exist_ok=True)

# create files
open(os.path.join(base,"dataset","digital_payment_dataset.csv"),"w").close()
open(os.path.join(base,"code","analysis.py"),"w").close()
open(os.path.join(base,"powerbi","dashboard.pbix"),"w").close()

print("Project structure created successfully!")
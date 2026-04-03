import pandas as pd

data = {
    "name": ["Jay", "Rahul", "Aman", "Riya"],
    "marks": [90, 85, 88, 92]
}

df = pd.DataFrame(data)

# 1. print only marks column
print(df["marks"])
# 2. print students with marks > 88
print(df[df["marks"] > 88])
# 3. print average marks
print(df["marks"].mean())
# 4. print second row
print(df.iloc[1])
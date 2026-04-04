import pandas as pd

data = {
    "name": ["Jay", "Rahul", "Aman", "Riya"],
    "marks": [90, 85, 88, 92]
}

df = pd.DataFrame(data)

print(df.set_index("name"))

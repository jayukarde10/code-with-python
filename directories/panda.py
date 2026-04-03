import pandas as pd

data={
    "name":["jay","adi","rit"],
    "marks":[90,91,67]
}
df = pd.DataFrame(data)
print(df,
      df.shape,      # (rows, columns)
    df.columns ,   # column names
    df.head() ,    # first 5 rows
    df.tail()  )   # last 5 rows


print("___________________")
print(df["name"])
print(df[["name","marks"]])

print(df.iloc[0] )   # first row

#add a new column
df["grade"]=["a","b","c"]
print(df)

print(df[df["marks"] > 85])

df["marks"].mean()
df["marks"].max()
df["marks"].min()


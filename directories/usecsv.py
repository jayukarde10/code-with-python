import pandas as pd

df = pd.read_csv("data.csv")
print(df)

print(df.head())              # first rows
print(df["marks"].mean())     # average marks
print(df["marks"].max())      # max marks

# average marks per city
print(df.groupby("city")["marks"].mean())
import numpy as np

df["status"] = np.where(df["marks"] > 88, "Pass", "Average")

print(df)

df.to_csv("new_data.csv", index=False)#crete new and save in new file

## ================== CSV (PANDAS) SUMMARY ==================

import pandas as pd

## -----------------------------------------------------------
## 1. WHAT IS CSV
## -----------------------------------------------------------
## CSV = Comma Separated Values
## Data stored like Excel table (rows & columns)

## Example:
## name,marks,city
## Jay,90,Mumbai
## Rahul,85,Pune

## -----------------------------------------------------------
## 2. READ CSV (LOAD DATA)
## -----------------------------------------------------------
df = pd.read_csv("data.csv")

## -----------------------------------------------------------
## 3. VIEW DATA
## -----------------------------------------------------------
df.head()        ## first 5 rows
df.tail()        ## last 5 rows
df.shape         ## (rows, columns)
df.columns       ## column names

## -----------------------------------------------------------
## 4. ACCESS DATA
## -----------------------------------------------------------
df["marks"]              ## column
df.iloc[0]               ## row
df[df["marks"] > 80]     ## filter

## -----------------------------------------------------------
## 5. HANDLE MISSING VALUES
## -----------------------------------------------------------
df.isnull()        ## check missing
df.fillna(0)       ## replace missing
df.dropna()        ## remove missing

## -----------------------------------------------------------
## 6. MODIFY DATA
## -----------------------------------------------------------
df["new_col"] = df["marks"] * 2

## -----------------------------------------------------------
## 7. ANALYSIS
## -----------------------------------------------------------
df["marks"].mean()
df["marks"].max()
df.groupby("city")["marks"].mean()

## -----------------------------------------------------------
## 8. SAVE CSV
## -----------------------------------------------------------
df.to_csv("new_data.csv", index=False)

## -----------------------------------------------------------
## 9. IMPORTANT RULE
## -----------------------------------------------------------
## File must be in correct path (same folder or full path)

## ================== END ==================
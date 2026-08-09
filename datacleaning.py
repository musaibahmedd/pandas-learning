import pandas as pd

###DATA CLEANING = THE PROCESS OF FIXING/REMOVING:
#incomplete, incorrect, or irrelevant data.
# 75% of work done with pandas is data cleaning.

df = pd.read_csv("pandas.csv")

# 1. Drop irrelevant columns
#df = df.drop(columns=["Legendary", "No"])


####HANDLE MISSING DATA ####

#df = df.dropna(subset=["Type2"])

#df = df.fillna({"Type2": "None"})



#3. FIX INCONSISTENT VALUES

df["Type1"] = df["Type1"].replace("Fire", "Flame")
print(df.to_string())
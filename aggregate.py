import pandas as pd 

###AGGREGATE FUNCTIONS = REDUCES A SET OF VALUE INTO A SINGLE SUMMARY VALUE
#                        USED TO SUMMARIZE AND ANALYZE DATA
#                        OFTEN USED WITH "groupby()" FUNCTION

df = pd.read_csv("pandas.csv")


###THESE AGGREGATE FUNCTIONS APPLY TO WHOLE DATFRAME
#print(df.mean(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.count())


###SINGLE COLUMN AGGREGATE FUNCTIONS###
#print(df["Height"].mean())
#print(df["Height"].sum())
#print(df["Height"].min())
#print(df["Height"].max())
#print(df["Height"].count())


group = df.groupby("Type1")

#print(group["Height"].mean())
#print(group["Height"].sum())
#print(group["Height"].min())
#print(group["Height"].max())
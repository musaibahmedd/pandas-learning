#################  HOW WE CAN IMPORT CSV(COMMA-SEPARATED VALUES)
##################                   JSON(JavaScript object notation)###########

#import pandas as pd

#df = pd.read_csv("pandas.csv")
#print(df)


#########DIFFERENT "SELECTION" TECHNIQUES USING PANDAS####################

import pandas as pd

#df = pd.read_csv("pandas.csv")

###SELECTION BY COLUMN###
#print(df["Name"])

#IF YOU WANT TO PRINT THE ENTIRE THING#
#print(df["Name"].to_string())

###TO SELECT MULTIPLE COLUMNS###
#print(df[["Name", "Height"]])


###SELECTION BY ROWS###

##NOW TO SET A COLUMN TO SERVE AS INDEX SOWE CAN ACCESS 
###NAMES BY LABEL

df = pd.read_csv("pandas.csv", index_col="Name")
#print(df.loc["Pikachu"]) #ACCESSING ROWS BY LABEL

pokemon = input("Enter a pokemon name: ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found")
   
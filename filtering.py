import pandas as pd 

df = pd.read_csv("pandas.csv")

###FILTERING = KEEPINF THE ROWS THAT MATCH A CONDITION

#tall_pokemon = df[df["Height"] >= 2]
#heavy_pokemon = df[df["Weight"] >= 100]

#legendary_pokemon = df[df["Legendary"] == 1]

#water_pokemon = df[(df["Type1"] == "Water") |
 #                  (df["Type2"] == "Water")]
#print(water_pokemon)
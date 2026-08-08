import pandas as pd

#Series = A Pandas 1-Dimensional labeled array that can hold any data type
#    Think of it like a single column in a spreadsheet

#data = [230, 234, 255]

#series = pd.Series(data)
#print(series)
#####################################################################

#IF AT ANY TIME YOU NEED TO ACCESS A A VALUE DIRECTLY WITHIN A SERIES, ACCESS THE LOC PROPERTY MEANING LOCATION.

#data = [230, 234, 255, 150, 175]
#series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])

#series.loc['a'] = 100
#print(series)

#USE iloc FOR INTEGER LOCATION.

#data = [230, 234, 255, 150, 175]
#series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
#print(series[series > 200])

########################################################################

#calories = {'day1': 420, 'day2': 380, 'day3': 390}

#series = pd.Series(calories)

#series.loc["day1"] += 200
#print(series)

######################################################################


##"DATAFRAME" = A  tabular data structure with rows and colums. (2 dimensional)

#data = {
  #  "Name": ["Bhaskar", "Santhosh", "Naveen"],
 #   "Age": [32, 25, 55]
#}

#df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

#################ADD A NEW COLUMN############################
#df["Job"] = ["Manager", "Bandly", "Engineer"]

##################ADD A NEW ROW###############
#new_row = pd.DataFrame([{"Name" : "Ramesh", "Age": 45, "Job" : "Accountant"}], index=["Employee 4"])
#df = pd.concat([df, new_row])

#print(df)      






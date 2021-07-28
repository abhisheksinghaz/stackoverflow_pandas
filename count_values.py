# question: https://stackoverflow.com/questions/68557136/count-frequency-of-values/68559335#68559335

import pandas as pd

A=[['10','20','20'],['20','10','10'],['15','10','15'],'12']
B=[['30','20','30'],'10',['5','30','30'],'40']
C=[['0','0'],'30','5','8']

df=pd.DataFrame({
                "A":A,
                "B":B,
                "C":C}) 

# Add the following lines to your file

# fetching the column headings 
col_names = [col for col in df.columns]

# using the following for loops to iterate through each cell of the dataframe
for item in col_names:
  for index in range(len(df)):
    
    # following prints the current cell address
    print( "For cell (" + item + "," + str(index) + ") :" )

    # for fetching each unique element of the cell of dataframe
    for set_item in set(df[item][index]):

      print("Count of " + str(set_item)+ " -> " + str( df[item][index].count(set_item)), end='    ' )
    print()

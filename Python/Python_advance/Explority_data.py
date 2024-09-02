# sorting data . plot in graph
# In here consider data like CSV file data ( Database like data )

# import pandas library
import pandas as pd

# read csv file
df = pd.read_csv("C:/Users/Anushanga/Downloads/Farming_Data.csv")
print(df.head())

df[['Farmer', 'Latitude', 'Longitude']]
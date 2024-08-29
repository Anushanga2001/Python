# Histrogram for data 
import matplotlib.pyplot as plt
import numpy as np

# when consider cumilative values

# consider according to the counties get the vote percentage for obama
# Ex - From 20% counties 36% have voted for obama 

# draw the a hstrogram
# bins means that no of range that consider for drawing the graph
# percenage get for the x axist

bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]	# x axis

plt.hist(df_swing['dem_share'], bins=bin_edges)
plt.show()

# seaborn library
import seaborn as sns
# mainly use for time series data ( continous data )
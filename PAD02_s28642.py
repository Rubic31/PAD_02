import numpy as np
import pandas as pd

#Zadanie 1

data = pd.read_csv('president_heights.csv')
heights = np.array(data['height(cm)'])
#print(heights)


print("Mean height:       ", np.mean(heights))
print("Standard deviation:", np.std(heights))
print("Minimum height:    ", heights.min())
print("Maximum height:    ", heights.max())

print("25th percentile:   ", np.percentile(heights, 25))
print("Median:            ", np.median(heights))
print("75th percentile:   ", np.percentile(heights, 75))
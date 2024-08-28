# There are many library in python
# Ex - Numpy, Matplotlib, Tensorflow, Pandas, beautiful soup 

# Example of Numpy installation
# pip install numpy
# display - import numpy as np

# numpy use
import numpy as np

weight = np.array([50, 60, 70, 80])
height = np.array([1.5, 1.6, 1.7, 1.8])

# devide weight by height
bmi = weight / height
print(bmi)

# I want to multiply the weight array by 2
weight = np.array([50, 60, 70, 80])
weight = weight * 2
print(weight)

# 2D numpy array
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array)

# get the shape of array
print(array.shape)

# print the [1,1] element
print(array[1, 1])
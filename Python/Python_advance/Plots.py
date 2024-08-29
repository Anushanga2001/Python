# import matplot lib library
import matplotlib.pyplot as plt

weight = [50, 60, 70, 80] + [90, 100, 110, 120]
height = [1.5, 1.6, 1.7, 1.8] + [1.5, 1.7, 2.9, 2.2]

plt.plot(weight, height)

plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Weight vs Height")

plt.show()
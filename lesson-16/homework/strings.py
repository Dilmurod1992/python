import numpy as np

lst = [12.23, 13.32, 100, 36.32]
print("Original List:", lst)


arr = np.array(lst)
print("One-dimensional NumPy array:", arr)

import numpy as np

matrix = np.arange(2, 11).reshape(3, 3)

print(matrix)

import numpy as np

vector = np.zeros(10)
print("Original vector:\n", vector)


vector[6] = 11
print("Updated vector:\n", vector)

import numpy as np

arr = np.arange(12, 38)

print(arr)

import numpy as np

arr = np.array([1, 2, 3, 4])
print("Original array:", arr)

float_arr = arr.astype(float)
print("Array converted to float:", float_arr)

import numpy as np

fahrenheit = np.array([0, 12, 45.21, 34, 99.91, 32])
print("Values in Fahrenheit degrees:", fahrenheit)

celsius = (fahrenheit - 32) * 5/9
print("Values in Centigrade degrees:", np.round(celsius, 2))

fahrenheit_converted = (celsius * 9/5) + 32
print("Values in Fahrenheit degrees:", np.round(fahrenheit_converted, 2))
import numpy as np

arr = np.array([10, 20, 30])
print("Original array:", arr)

new_arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("After append values to the end of the array:", new_arr)

import numpy as np

print("Random Array:", arr)

mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

print("Mean of the array:", mean_val)
print("Median of the array:", median_val)
print("Standard Deviation of the array:", std_val)

import numpy as np

arr = np.random.rand(10, 10)
print("Random 10x10 Array:\n", arr)

min_val = np.min(arr)
max_val = np.max(arr)

print("\nMinimum value:", min_val)
print("Maximum value:", max_val)

import numpy as np

arr = np.random.rand(3, 3, 3)
print("3x3x3 Random Array:\n", arr)

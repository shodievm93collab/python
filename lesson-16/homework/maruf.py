import numpy as np

# 1. Convert List to 1D Array
original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("1. Original List:", original_list)
print("One-dimensional NumPy array:", array_1d)
print()

# 2. Create 3x3 Matrix (2 to 10)
matrix_3x3 = np.arange(2, 11).reshape(3, 3)
print("2. 3x3 Matrix with values from 2 to 10:")
print(matrix_3x3)
print()

# 3. Null Vector (10) & Update Sixth Value
null_vector = np.zeros(10)
print("3. Null vector of size 10:")
print(null_vector)

# Note: Sixth value index is 5 (0-based)
null_vector[5] = 11
print("Update sixth value to 11:")
print(null_vector)
print()

# 4. Array from 12 to 38
arr_12_38 = np.arange(12, 38)
print("4. Array with values from 12 to 38:")
print(arr_12_38)
print()

# 5. Convert Array to Float Type
arr_int = np.array([1, 2, 3, 4])
arr_float = arr_int.astype(float)
print("5. Original array:", arr_int)
print("Converted to float type:", arr_float)
print()

# 6. Celsius to Fahrenheit Conversion
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32
print("6. Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)
print()

# 7. Append Values to Array
original_arr = np.array([10, 20, 30])
values_to_append = [40, 50, 60, 70, 80, 90]
new_arr = np.append(original_arr, values_to_append)
print("7. Original array:", original_arr)
print("After append values to the end of the array:", new_arr)
print()

# 8. Array Statistical Functions
rand_arr = np.random.rand(10)  # random floats in [0,1)
mean_val = np.mean(rand_arr)
median_val = np.median(rand_arr)
std_dev = np.std(rand_arr)
print("8. Random array:", rand_arr)
print(f"Mean: {mean_val:.4f}, Median: {median_val:.4f}, Std Dev: {std_dev:.4f}")
print()

# 9. Find min and max in 10x10 array
rand_10x10 = np.random.rand(10, 10)
min_val = np.min(rand_10x10)
max_val = np.max(rand_10x10)
print("9. 10x10 random array:")
print(rand_10x10)
print(f"Minimum value: {min_val:.4f}, Maximum value: {max_val:.4f}")
print()

# 10. Create a 3x3x3 array with random values
rand_3d = np.random.rand(3, 3, 3)
print("10. 3x3x3 array with random values:")
print(rand_3d)

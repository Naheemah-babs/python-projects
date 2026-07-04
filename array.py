import numpy as np
# matrix in python
matrix = np.random.randint(1, 101, size=(4,4))
print(matrix)

row_sum = np.sum(matrix, axis = 1)
print(row_sum)


# Create a 3D random array and compute statistics along specific axes
# Create a 3D random array (3 x 4 x 5)
arr = np.random.randint(1, 101, size=(3, 4, 5))

print("3D Array:")
print(arr)

# Mean along axis 0
print("\nMean along axis 0:")
print(np.mean(arr, axis=0))

# Mean along axis 1
print("\nMean along axis 1:")
print(np.mean(arr, axis=1))

# Mean along axis 2
print("\nMean along axis 2:")
print(np.mean(arr, axis=2))

# Maximum values along axis 0
print("\nMaximum along axis 0:")
print(np.max(arr, axis=0))

# Minimum values along axis 1
print("\nMinimum along axis 1:")
print(np.min(arr, axis=1))

# Standard deviation along axis 2
print("\nStandard deviation along axis 2:")
print(np.std(arr, axis=2))

# Generate a dataset of random floats and normalize between 0 and 1
import numpy as np

# Generate 20 random floats between 10 and 100
data = np.random.uniform(10, 100, 20)

print("Original Data:")
print(data)

# Min-Max Normalization
normalized = (data - np.min(data)) / (np.max(data) - np.min(data))

print("\nNormalized Data:")
print(normalized)

print("\nMinimum:", np.min(normalized))
print("Maximum:", np.max(normalized))


#conditional replacement to create a binary mask for values above a threshold

# Generate a random array
data = np.random.randint(0, 100, 20)

print("Original Data:")
print(data)

# Set threshold
threshold = 50

# Create binary mask
binary_mask = np.where(data > threshold, 1, 0)

print("\nThreshold:", threshold)
print("Binary Mask:")
print(binary_mask)
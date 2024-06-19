import numpy as np
import csv

# Generate random data points
num_points = 100  # Number of data points

X = np.random.rand(num_points)  # Random x values between 0 and 1
y = 2 * X + 3 + np.random.randn(num_points)  # Linear relationship with noise

# Prepare data for CSV
data = [["x", "y"]]
for i in range(num_points):
  data.append([X[i], y[i]])

# Write data to CSV file
with open("data1.csv", "w", newline="") as csvfile:
  writer = csv.writer(csvfile)
  writer.writerows(data)

print("CSV file generated successfully: data1.csv")
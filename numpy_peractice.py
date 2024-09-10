import numpy as np
import matplotlib.pyplot as plt

# Setting the parameters of the normal distribution
mean = 0
std_dev = 1
num_samples = 1000

# Generate data from normal distribution
data = np.random.normal(mean, std_dev, num_samples)

# Calculation of statistical features
mean_data = np.mean(data)
std_dev_data = np.std(data)
median_data = np.median(data)

print(f"Mean: {mean_data}")
print(f"Standard Deviation: {std_dev_data}")
print(f"Median: {median_data}")

# histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='blue', alpha=0.7, edgecolor='black')
plt.title('Histogram of Random Data from Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
# Create a data density curve
count, bins, ignored = plt.hist(data, bins=30, density=True, alpha=0.5, color='g', edgecolor='black')

# Standard normal distribution function
density = (1/(std_dev * np.sqrt(2 * np.pi))) * np.exp( - (bins - mean)**2 / (2 * std_dev**2))

plt.plot(bins, density, '--', color='red')
plt.title('Density Plot with Normal Distribution Fit')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
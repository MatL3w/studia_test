import dask.array as da
import dask.distributed
import numpy as np

x = da.random.random((10000, 10000), chunks=(1000, 1000))

# Calculate the mean and standard deviation of the Dask array
mean_x = x.mean()
std_dev_x = x.std()

# Compute the results in parallel
mean_result = mean_x.compute()
std_dev_result = std_dev_x.compute()

print(f"Mean of the Dask array: {mean_result}")
print(f"Standard Deviation of the Dask array: {std_dev_result}")
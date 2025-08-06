import numpy as np 


def total_rainfall(rainfall_array):
    return np.sum(rainfall_array)

def average_rainfall(rainfall_array):
    return np.mean(rainfall_array)

def zero_rainfall(rainfall_array):
    return np.sum(rainfall_array==0)

def high_rainfall(rainfall_array):
    return np.where(rainfall_array>5)[0]

def percentile75_rainfall(rainfall_array):
    return np.percentile(rainfall_array,75)

if __name__ == "__main__":
    sample_rainfall = [0.0, 5.2, 3.1, 0.0, 12.4, 0.0, 7.5]
    rainfall_array = np.array(sample_rainfall)
    print("Rainfalls (mm): ",rainfall_array)
    print("Total Rainfall (mm): ",round(total_rainfall(rainfall_array),1))
    print("Zero rainy days: ", zero_rainfall(rainfall_array))
    print("High rainfall days: ", high_rainfall(rainfall_array))
    print("75th percentile of rainfall: ",percentile75_rainfall(rainfall_array))





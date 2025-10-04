import numpy as np


def average_temperature(celsius_temp):
    return round(np.mean(celsius_temp),2)

def max_temperature(celsius_temp):
    return np.max(celsius_temp)

def min_temperature(celsius_temp):
    return np.min(celsius_temp)

def fahrenheit_temperature(celsius_temp):
    return celsius_temp *9/5 + 32  

def high_temperature(celsius_temp):
    return np.where(celsius_temp>20)[0]
    

if __name__ == "__main__":
    celsius_temp = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])

    print("Average temperatur in °C: ",average_temperature(celsius_temp))
    print("Minimum temperature in °C: ",max_temperature(celsius_temp))
    print("Minimum temperature in °C: ",min_temperature(celsius_temp))
    print("Temperatures in °F: ",*fahrenheit_temperature(celsius_temp))
    print("High temperature day(s): ",*high_temperature(celsius_temp))




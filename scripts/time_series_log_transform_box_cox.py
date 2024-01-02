import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 


from sklearn.metrics import mean_squared_error
from math import sqrt
from statistics import mean 

train_data = pd.read_csv("/Users/paramanandbhat/Downloads/6.4_Stationarity_for_time_series (3)/data/train_data.csv")
valid_data = pd.read_csv("/Users/paramanandbhat/Downloads/6.4_Stationarity_for_time_series (3)/data/valid_data.csv")


print(train_data.shape)
train_data.head()

print(valid_data.shape)
valid_data.head()

# Required Preprocessing 


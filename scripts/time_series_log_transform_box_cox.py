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
train_data.timestamp = pd.to_datetime(train_data['Date'],format='%Y-%m-%d')
train_data.index = train_data.timestamp

valid_data.timestamp = pd.to_datetime(valid_data['Date'],format='%Y-%m-%d')
valid_data.index = valid_data.timestamp


def adf_test(timeseries):
    
    #Perform Dickey-Fuller test:
    print ('Results of Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput=pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])

    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print (dfoutput)



plt.figure(figsize=(12,8))

plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(valid_data.index, valid_data['count'], label='valid')
plt.legend(loc='best')
plt.title("Train and Validation Data")
plt.show()

# dickey fuller, kpss
from statsmodels.tsa.stattools import adfuller, kpss

train_data['count_diff'] = train_data['count'] - train_data['count'].shift(1)
train_data['count_log'] = np.log(train_data['count'])
train_data['count_log_diff'] = train_data['count_log'] - train_data['count_log'].shift(1)

plt.figure(figsize=(12,8))

plt.plot(train_data.index,train_data['count_log_diff'], label='stationary series')
plt.legend(loc='best')
plt.title("Stationary Series")
plt.show()

adf_test(train_data['count_log_diff'].dropna())

def kpss_test(timeseries):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c')
    kpss_output = pd.Series(kpsstest[0:3], index=['Test Statistic','p-value','Lags Used'])
    for key,value in kpsstest[3].items():
        kpss_output['Critical Value (%s)'%key] = value
    print (kpss_output)

kpss_test(train_data['count'])

train_data['count_diff'] = train_data['count'] - train_data['count'].shift(1)

plt.figure(figsize=(12,8))

plt.plot(train_data.index, train_data['count'], label='train_data')
plt.plot(train_data.index,train_data['count_diff'], label='stationary series')
plt.legend(loc='best')
plt.title("Stationary Series")
plt.show()

adf_test(train_data['count_log_diff'].dropna())

kpss_test(train_data['count_log_diff'].dropna())

from scipy import stats 

transformed_data, lambda_value = stats.boxcox(train_data['count'], lmbda=None) 

train_data['count_boxcox'] = transformed_data
train_data['count_boxcox_diff'] = train_data['count_boxcox'] - train_data['count_boxcox'].shift(1)

plt.figure(figsize=(12,8))

plt.plot(train_data.index,train_data['count_boxcox_diff'], label='box cox transformation')
plt.legend(loc='best')
plt.title("Stationary Series")
plt.show()








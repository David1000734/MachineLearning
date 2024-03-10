import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# ******************** REMOVE ********************
# https://mkang.faculty.unlv.edu/teaching/CS489_689/code3/Linear_Regression.html
# https://www.youtube.com/watch?v=VmbA0pi2cRQ
# https://www.youtube.com/watch?v=P8hT5nDai6A
# https://www.youtube.com/watch?v=ltXSoduiVwY
# https://www.youtube.com/watch?v=sRh6w-tdtp0
# Multiple linear Regression
# x1, x2, x3, xn
# m1, m2, m3, mn
# Y = m1x1 + m2x2 + m3x3 + mnxn + c
# c -> y-intercept
# ******************** REMOVE ********************
data = pd.read_csv("auto-mpg.data.csv")

# Function will be utilizeing the Min-Max Scaling
def normalize_Data(data_Column):
    """
    normalize_Data will utilize Min-Max Scaling to set
    values between 0 - 1.
    
    :param data_Column: Recieve the column to be normalized
    :return: Output the normalized column in dataType List
    """
    new_Data_List = []

    # Bottom value will remain constent throughout loop
    bottom = max(data_Column) - min(data_Column)        # x_Max - x_Min

    # Traverse each value within data_Column to perform calculation
    for i in range(len(data_Column)):
        # X_norm = (x - x_Min) / (X_Max - X_Min)
        top = data_Column[i] - min(data_Column)         # x - x_Min
        result = top / bottom                   # Top / Bot
        new_Data_List.append(result)
    # For, END
    return new_Data_List
# Normalize_Data funct, END

def un_normalize_Data(data_Column, max, min):
    """
    Given that we know what the specific data's min and max is, 
    we can get it's original value by the following formula:
    X: is norm-val
    Un-normalized val = X * (max - min) + min

    :param data_Column: Normalized data
    :param max: Original Max value of data
    :param min: Original Min value of data
    :return: un-normalized data row
    """
    unNorm_Data_List = []

    for i in range(len(data_Column)):
        print(data_Column[i])

    return unNorm_Data_List

# *************** CHANGE THE CODE DOWN HERE ***************
def linear_Model(x_val, y_target, learning_rate, iteration, arr):
    m = y_target.size
    # Create column of 0's of the same size as x's features
    theta = np.zeros((x_val.shape[1], 1))

    for i in range(iteration):
        y_pred = np.dot(x_val, theta)

        # Cost Function
        # 1/2m Sum(y_pred - Y)^2, where Y is the actual value
        cost = ((1 / (2 * m)) * np.sum((y_pred - y_target) ** 2, axis = 0))
        # cost = (1/(2*m))*np.sum(np.square(y_pred - y_target))

        # Gradient Descent
        # d_theta = 1/m(matrix_mul(X^T, y_pred - Y))
        d_theta = ((1 / m) * np.dot(x_val.transpose(), y_pred - y_target))
        # d_theta = (1/m)*np.dot(x_val.T, y_pred - y_target)

        # theta = theta - alpha * d_theta
        theta = theta - learning_rate * d_theta
        # print(theta)

        arr.append(cost)

    return theta

# To be removed...
def mean_Error(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].mpg
        y = points.iloc[i].horsepower
        total_Error += (y - (m * x + b)) ** 2
    total_Error / float(len(points))
# To be removed...

# ******************** Main ********************

lr_lambda = 1               # Learning Rage
max_Iteration = 10000       # Iterations

# Drop the last row (Car Name)
data = data.iloc[:, :-1]

build_DF = pd.DataFrame()

# Normalize data and rebuild back into dataFrame
for i in range(len(data.columns)):
    # To change to DataFrame...
    temp_DF = pd.DataFrame(normalize_Data(data.iloc[:, i]))
    # Get name of each column
    columnName = "STD_" + data.columns[i]

    # Rebuild the data back into a DataFrame
    build_DF.insert(i, columnName, temp_DF, True)
# For, END

# Normalize all data and then un-normalize later
# X is all values besides MPG
x = build_DF.iloc[ : , 1 : 7]

# Y is the MPG, the predicting value
y = build_DF.iloc[ : , 0 : 1]

# Adding a column of 1's
# x["theta_0"] = 1
cost_arr = []

theta = linear_Model(x, y, lr_lambda, max_Iteration, cost_arr)
un_normalize_Data(cost_arr, 32, 18)
#print(cost_arr)

rng = np.arange(0, max_Iteration)
plt.plot(rng, cost_arr)
plt.show()


# print(np.corrcoef(build_DF))
# print(build_DF)
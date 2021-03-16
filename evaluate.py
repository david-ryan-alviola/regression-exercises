import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels.formula.api import ols
from sklearn.metrics import mean_squared_error
from math import sqrt

def plot_residuals(y, yhat):
    sns.scatterplot(x=y, y=yhat - y)
    plt.title("Residuals")
    plt.ylabel("yhat - y")
    plt.show()
    
def plot_residuals_against_x(x, y, yhat, df):
    sns.scatterplot(x=x, y=(yhat - y), data=df)
    plt.title("Residuals")
    plt.ylabel("yhat - y")
    plt.show()
    
def regression_errors(y, yhat):
    sse2 = mean_squared_error(y, yhat) * len(y)
    ess = sum((yhat - y.mean()) ** 2)
    tss = ess + sse2
    mse = mean_squared_error(y, yhat)
    rmse = sqrt(mse)
    
    return sse2, ess, tss, mse, rmse

def baseline_mean_errors(y):
    index = []
    
    for i in range(1, len(y) + 1):
        index.append(i)
        
    y_mean = pd.Series(y.mean(), index=index)

    sse2_baseline = mean_squared_error(y, y_mean) * len(y)
    mse_baseline = mean_squared_error(y, y_mean)
    rmse_baseline = sqrt(mse_baseline)
    
    return sse2_baseline, mse_baseline, rmse_baseline

def better_than_baseline(y, yhat):
    sse2, ess, tss, mse, rmse = regression_errors(y, yhat)
    sse2_baseline, mse_baseline, rmse_baseline = baseline_mean_errors(y)
    
    return compare_sum_squared_errors(sse2, sse2_baseline)

def model_signficance(ols_model):
    r2 = ols_model.rsquared
    p_value = ols_model.f_pvalue
    alpha = .05

    print(f"variance:  {r2}, p:  {p_value}, a: {alpha},  signficant:  {p_value < alpha}")
    return r2, p_value, p_value < alpha
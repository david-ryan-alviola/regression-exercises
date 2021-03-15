import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_variable_pairs(df, target):
    for column in df.columns:
        if column != target:
            sns.lmplot(x=column, y=target, data=df)
            
def months_to_years(df):
    df_copy = df.copy()
    df_copy['tenure_years'] = round(df_copy.tenure / 12)
    
    return df_copy

def plot_categorical_and_continuous_vars(df, cont_vars, cat_vars, target, target_type):
    
    if target_type == "categorical":
        for categorical in cat_vars:
            sns.heatmap(df[[target, categorical]])
        
        for continous in cont_vars:
            sns.swarmplot(x=continous, y=target, data=df)
    
    else:
        for continous in cont_vars:
            sns.relplot(x=continous, y=target, data=df)
            
        for categorical in cat_vars:
            sns.swarmplot(x=categorical, y=target, data=df)
import numpy as np
import tensorflow as tf
import pandas as pd 

df = pd.read_csv('data.csv')

df.drop('customerID' , axis = 'columns' , inplace= True)


df1 = df[df.TotalCharges!= ' ']

df1 = df1.copy()
df1['TotalCharges'] = pd.to_numeric(df1.TotalCharges)
df1.replace('No internet service' , 'No' , inplace= True)
df1.replace('No phone service' , 'No' , inplace = True)

print(df1.iloc[[0]])


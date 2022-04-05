# README.md
We have the data of top 1000 youtubers with most number of subscribers which we are showing on barplot using Matplotlib funtion. 
First we import the Libraries which are :- 
import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Then we pass the read function so that python reads our CSV file 

df_youtube= pd.read_csv("top_1000_youtubers.csv",sep=",", encoding='ISO-8859-1')
print("done")

Then we use the Matplotlib inline function and the matplotlib regular function to display the barplot of distribution of channels. 


Finally, uploaded the same in the Github.

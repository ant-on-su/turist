#%% [markdown]
# ## Turistic Data from Maczek
# First massage the data, then try phi-K

#%%
import pandas as pd
import xlrd
import numpy as np

#%%
df = pd.read_excel("./data/Copy of wyniki baza danych 5 dec 2018.xls", 
header=0, convert_float=True)
df.head()

#%%
df = df[df.komfort != 'komfort']
df = df.applymap(lambda x: x.strip() if type(x) is str else x)
df=df.apply(pd.to_numeric, errors='ignore')
df.dropna(axis='columns', how="all", inplace=True)
df.dropna(axis='rows', how="all", inplace=True)
df.shape

#%%
df['M3']=df['M3'].map({'ukraina' : 1, 'polska' :0})
df.head()

#%%
df.dtypes
#%% [markdown]
# ## Turistic Data from Maczek
# First massage the data, then try phi-K

#%%
import pandas as pd
import xlrd

#%%
df = pd.read_excel("./data/Copy of wyniki baza danych 5 dec 2018.xls")
df.head()

#%%
df = df[df.komfort != 'komfort']
df.dropna(axis=0, how="all", inplace=True)
df.dropna(axis=1, how="all", inplace=True)
df.shape

#%%
df = df.apply(pd.to_numeric, errors='ignore', downcast='integer')
df.dtypes
#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


pd.read_csv('fuel_ferc1.csv')


# In[46]:


data_f = pd.read_csv('fuel_ferc1.csv')


# In[47]:


data_f.describe(include='all')


# In[48]:


data_f.isnull()


# In[49]:


data_f.dropna()


# In[50]:


data_f.isnull().sum()


# In[51]:


data_f.duplicated().any()


# In[52]:


data_f.dropna()


# In[53]:


data_f.groupby('fuel_unit')['fuel_unit'].count()


# In[54]:


data_f[['fuel_unit']]=data_f[['fuel_unit']].fillna(value=('mcf'))


# In[55]:


data_f.describe(include='all')


# In[56]:


data_f


# Grouping The Data

# In[57]:


data_f[['fuel_unit']]=data_f[['fuel_unit']].fillna(value=('mcf'))


# In[58]:


data_f


# In[59]:


data_f.groupby('report_year')['report_year'].count()


# In[60]:


#Group Fuel Code
data_f.groupby('fuel_type_code_pudl').first()


# In[61]:


# Merging Data
df_data1 = data_f.iloc[0:19000].reset_index(drop=True)
df_data2 = data_f.iloc[19000:].reset_index(drop=True)


# In[62]:


#Checking the length of the dataframes
assert len(data_f) == (len(df_data1) + len(df_data2))


# In[37]:


pd.merge(df_data1, df_data2, how="inner")
pd.merge(df_data1, df_data2, how="outer")
pd.merge(df_data1, df_data2, how="left")


# In[66]:


#Commencement of graph plotting
plt.figure(figsize=(7,4))
plt.xticks(rotation=90)
fuel_unit = pd.DataFrame({'unit':['BBL', 'GAL', 'GRAMSU', 'KGU', 'MCF', 'MMBTU', 'MWDTH', 'MWHTH', 'TON'],
            'count':[7998, 84, 464, 110, 11354, 180, 95, 100, 8958]})
sns.barplot(data=fuel_unit, x='unit', y='count')
plt.xlabel('Fuel Unit')


#Take Log of Fuel unit to reduce the extreme values
g = sns.barplot(data=fuel_unit, x='unit', y='count')
g.set_yscale("log")
g.set_ylim(1, 12000)
plt.xlabel('Fuel Unit')


# In[68]:


#boxplot
sns.boxplot(x="fuel_type_code_pudl", y="utility_id_ferc1",
            palette=["m", "g"], data=data_f)


# In[81]:


#KDE Plot
sample_df = data_f.sample(n=50, random_state=4)
sns.regplot(x=sample_df["utility_id_ferc1"], y=sample_df["fuel_cost_per_mmbtu"], fit_reg=False)


# In[82]:


sns.kdeplot(sample_df['fuel_cost_per_unit_burned'], shade=True, color="red")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import resample
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("./bc.csv") 


# In[18]:


data.dtypes


# In[19]:


del data['Id']


# In[20]:


data.dtypes


# In[21]:


cols = data.columns.drop('Class')


# cols = data.columns.drop('Class')

# In[22]:


data[cols] = data[cols].apply(pd.to_numeric, errors='coerce')


# In[23]:


data["Class"].value_counts()


# In[24]:


trainData, testData = train_test_split(data, test_size = 0.3, random_state=1)


# In[25]:


trainData["Class"].value_counts()


# In[26]:


data_majority = trainData[trainData.Class=="benign"]
data_minority = trainData[trainData.Class=="malignant"]


# In[27]:


data_majority_downsampled = resample(data_majority, 
                                 replace=False,    
                                 n_samples=167,     
                                 random_state=123)


# In[28]:


data_majority_downsampled["Class"].value_counts()


# In[29]:


data_downsampled = pd.concat([data_majority_downsampled, data_minority])


# In[30]:


data_downsampled["Class"].value_counts()


# In[31]:


data_minority_upsampled = resample(data_minority, 
                                 replace=True,     
                                 n_samples=311,   
                                 random_state=123)


# In[32]:


data_upsampled = pd.concat([data_majority, data_minority_upsampled])


# In[33]:


data_upsampled["Class"].value_counts()


# In[34]:


y = data_upsampled.Class
X = data_upsampled.drop('Class', axis=1)
 
clf_1 = LogisticRegression().fit(X, y)
 
pred_y_1 = clf_1.predict(X)
 
print( np.unique( pred_y_1 ) )

print( accuracy_score(y, pred_y_1) )


# In[35]:


y = data_downsampled.Class
X = data_downsampled.drop('Class', axis=1)
 
clf_1 = LogisticRegression().fit(X, y)
 
pred_y_1 = clf_1.predict(X)
 
print( np.unique( pred_y_1 ) )

print( accuracy_score(y, pred_y_1) )


# In[ ]:





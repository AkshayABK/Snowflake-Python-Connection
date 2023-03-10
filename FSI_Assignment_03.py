#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install snowflake-connector-python


# In[2]:


import getpass


# In[3]:


import snowflake.connector


# In[7]:


conn = snowflake.connector.connect(
    user='AkshayABK',
    password=getpass.getpass(),
    account='KTOKQKS-IW06925',
    database='carinsurancedb',)


# In[12]:


cursor= conn.cursor()
cursor.execute("Call AvgCarValueProcedure()")
cursor.fetchall()


# In[11]:


cursor.execute("call AvgOccupationIncome()")
cursor.fetchall()


# In[14]:


AVG_INCOME_occ=cursor.execute("select * FROM AVGOCCUPINCOME;")
AVG_INCOME_occ.fetchall()


# In[15]:


AVG_INCOME_car=cursor.execute("select * FROM AVGOCCUPINCOME;")
AVG_INCOME_car.fetchall()


# In[18]:


db = cursor.execute("show tables")
db.fetchall()


# In[ ]:





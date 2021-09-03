#!/usr/bin/env python
# coding: utf-8

# # IR System

# ### Import Libraries

# In[28]:


import pandas as pd
from elasticsearch import Elasticsearch


# ### Establish Connection

# In[29]:


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])



# ### Import Csv File

# In[30]:


df = pd.read_csv(r'wiki_movie_plots_deduped.csv')


# ### List 10 Documents

# In[31]:


df.head()


# ### Fill NaN as Unknown

# In[32]:


df['Cast'] = df['Cast'].fillna("Unknown")


# ## Output to Elastic

# In[33]:


out_df = df.to_json(orient="records")
import json
out_data = json.loads(out_df)


# In[34]:


record_list = []
for record in out_data:
    record["_index"] =  "movies_data-all"
    record_list.append(record)


# In[38]:


from elasticsearch import helpers
helpers.bulk(es, record_list)


# ### Ingestion Complete

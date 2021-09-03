#!/usr/bin/env python
# coding: utf-8

# # IR System

# ### Import Libraries

# In[8]:


import pandas as pd
from elasticsearch import Elasticsearch


# ### Establish Connection

# In[9]:


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])



# ### Variables

# In[10]:


director = "Michael Curtiz"
genre = "comedy"


# ### Query

# In[11]:


query  = {"size":10,"query":{"bool":{"should":[{"term":{"Director.keyword":{"value":director,"boost":1}}},{"term":{"Genre.keyword":{"value":genre,"boost":3}}}],"minimum_should_match":1}}}


# In[12]:


res = es.search(index="movies_data-all", body=query)


# ### Hits

# In[13]:


total_hits = res["hits"]["total"]["value"]
print("Total Hits ==> ",total_hits)


# In[15]:


hits  = res["hits"]["hits"]
hit_list = []
for hit in hits:
    hit_list.append(hit["_source"])


# ### Raw Records (Hits)

# In[16]:


print(hits)


# In[17]:


dfItem = pd.DataFrame.from_records(hit_list)
print(dfItem)


# In[ ]:





# In[ ]:

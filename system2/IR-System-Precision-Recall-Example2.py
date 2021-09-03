#!/usr/bin/env python
# coding: utf-8

# # IR System

# ### Import Libraries

# In[2]:


import pandas as pd
from elasticsearch import Elasticsearch


# ### Establish Connection

# In[38]:


es = Elasticsearch(
    cloud_id=",
    http_auth=("elastic", ""),
)


# ### Query

# In[40]:


query  = {"_source":"Director","version":"true","size":5,"sort":[{"_score":{"order":"desc"}}],"fields":[],"script_fields":{},"stored_fields":["*"],"query":{"bool":{"must":[],"should":[{"multi_match":{"type":"best_fields","query":"playing","lenient":"true"}},{"multi_match":{"type":"best_fields","query":"Hanna-Barbera","lenient":"true"}},{"multi_match":{"type":"best_fields","query":"animation","lenient":"true"}},{"multi_match":{"type":"best_fields","query":"Tom and Jerry","lenient":"true"}}],"must_not":[]}},"highlight":{"pre_tags":["@kibana-highlighted-field@"],"post_tags":["@/kibana-highlighted-field@"],"fields":{"*":{}},"fragment_size":2147483647}}


# In[41]:


res = es.search(index="movies_data-all", body=query)


# ### Hits

# In[42]:


hits  = res["hits"]["hits"]
hit_list = []
for hit in hits:
    hit_list.append(hit["_source"])


# ### Raw Records (Hits)

# In[43]:


print(hits)


# In[ ]:





# ## Precision: How Many Selected Items are Relavent
# #### Precision () is defined as the number of true positives () over the number of true positives plus the number of false positives ().
# ##### Link: https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html

# In[44]:


def calculate_precision(true_positives, false_positives):
    precision = (true_positives)/(false_positives+true_positives)
    return (precision)


# ## Recall: How Many Relavent Items are Selected
# #### The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives.
# ##### Link: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html

# In[45]:


def calculate_recall(true_positives, false_negatives):
#     R = tp / (tp + fn) Formula
    recall = (true_positives)/(false_negatives+true_positives)
    return (recall)


# ## Query Result from the search above
# ___
# ### Search based on top 5 hits
# ___
# #### Search strings are 
# 1. playing
# 2. Hanna-Barbera
# 3. animation
# 4. Tom and Jerry
# ___
# *** 

# ## Results
# ___
# ### True Positives from the query above : 5
# ___
# ### False Positives from the query above : 0
# ___
# ### False Negatives from the query above : 0
# ___
# ___

# In[46]:


recall = calculate_recall(true_positives=5,false_negatives=0)
print("Recall : %5.2f" % (recall))


# In[48]:


precision = calculate_precision(true_positives=5, false_positives=0)
print("Precision : %5.2f" % (precision))


# In[ ]:





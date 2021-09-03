#!/usr/bin/env python
# coding: utf-8

# # IR System

# ### Import Libraries

# In[2]:


import pandas as pd
from elasticsearch import Elasticsearch


# ### Establish Connection

# In[3]:


es = 


# ### Query

# In[5]:


query  = {"_source":"Genre","version":"true","size":5,"sort":[{"_score":{"order":"desc"}}],"fields":[],"script_fields":{},"stored_fields":["*"],"query":{"bool":{"must":[],"should":[{"term":{"Genre.keyword":{"value":"film noir","boost":2}}},{"multi_match":{"type":"best_fields","query":"American","lenient":"true","boost":1.5}},{"multi_match":{"type":"best_fields","query":"husband","lenient":"true"}},{"multi_match":{"type":"best_fields","query":"evidence","lenient":"true","boost":1}}],"must_not":[]}},"highlight":{"pre_tags":["@highlighted@"],"post_tags":["@highlighted@"],"fields":{"*":{}},"fragment_size":2147483647}}


# In[6]:


res = es.search(index="movies_data-all", body=query)


# ### Hits

# In[7]:


hits  = res["hits"]["hits"]
hit_list = []
for hit in hits:
    hit_list.append(hit["_source"])


# ### Raw Records (Hits)

# In[8]:


import json
print(json.dumps(hits))


# In[ ]:





# ## Precision: How Many Selected Items are Relavent
# #### Precision () is defined as the number of true positives () over the number of true positives plus the number of false positives ().
# ##### Link: https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html

# In[9]:


def calculate_precision(true_positives, false_positives):
    precision = (true_positives)/(false_positives+true_positives)
    return (precision)


# ## Recall: How Many Relavent Items are Selected
# #### The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives.
# ##### Link: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html

# In[10]:


def calculate_recall(true_positives, false_negatives):
#     R = tp / (tp + fn) Formula
    recall = (true_positives)/(false_negatives+true_positives)
    return (recall)


# ## Query Result from the search above
# ___
# ### Search based on top 5 hits
# ___
# #### Search strings are 
# 1. film noir (score boosted for this with 2)
# 2. American (score boosted for this with 1.5)
# 3. husband
# 4. evidence
# ___
# *** 

# ## Results for K=5
# ___
# ### True Positives from the query above : 5
# ___
# ### False Positives from the query above : 0
# ___
# ### False Negatives from the query above : 0
# ___
# ___

# In[11]:


recall = calculate_recall(true_positives=5,false_negatives=0)
print("Recall : %5.2f" % (recall))


# In[12]:


precision = calculate_precision(true_positives=5, false_positives=0)
print("Precision : %5.2f" % (precision))


# In[ ]:





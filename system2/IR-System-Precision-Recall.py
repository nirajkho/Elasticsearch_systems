#!/usr/bin/env python
# coding: utf-8

# # IR System

# ### Import Libraries

# In[2]:


import pandas as pd
from elasticsearch import Elasticsearch


# ### Establish Connection

# In[3]:


es = Elasticsearch([{'host': 'localhost', 'port': 9200}])



# ### Query

# In[8]:


query  = {"_source":"Director","size":5,"sort":[{"_score":{"order":"desc"}}],"fields":[],"script_fields":{},"stored_fields":["*"],"query":{"bool":{"must":[],"should":[{"multi_match":{"type":"best_fields","query":"profession","lenient":"true"}},{"multi_match":{"type":"best_fields","query":"Edward Buzzell","lenient":"true"}}],"must_not":[]}},"highlight":{"pre_tags":["@kibana-highlighted-field@"],"post_tags":["@/kibana-highlighted-field@"],"fields":{"*":{}},"fragment_size":2147483647}}


# In[9]:


res = es.search(index="movies_data-all", body=query)


# ### Hits

# In[11]:


hits  = res["hits"]["hits"]
hit_list = []
for hit in hits:
    hit_list.append(hit["_source"])


# ### Raw Records (Hits)

# In[21]:


print(hits)


# In[ ]:





# ## Precision: How Many Selected Items are Relavent
# #### Precision () is defined as the number of true positives () over the number of true positives plus the number of false positives ().
# ##### Link: https://scikit-learn.org/stable/auto_examples/model_selection/plot_precision_recall.html

# In[28]:


def calculate_precision(true_positives, false_positives):
    precision = (true_positives)/(false_positives+true_positives)
    return (precision)


# ## Recall: How Many Relavent Items are Selected
# #### The recall is the ratio tp / (tp + fn) where tp is the number of true positives and fn the number of false negatives.
# ##### Link: https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html

# In[29]:


def calculate_recall(true_positives, false_negatives):
#     R = tp / (tp + fn) Formula
    recall = (true_positives)/(false_negatives+true_positives)
    return (recall)


# ## Query Result from the search above
# ___
# ### Search based on top 5 hits
# ___
# #### Search strings are profession & Edward Buzzell
# ___
# ***

# ## Results
# ___
# ### True Positives from the query above : 2
# ___
# ### False Positives from the query above : 3
# ___
# ### False Negatives from the query above : 0
# ___
# ___

# In[36]:


recall = calculate_recall(true_positives=2,false_negatives=0)
print("Recall : %5.2f" % (recall))


# In[37]:


precision = calculate_precision(true_positives=2, false_positives=3)
print("Precision : %5.2f" % (precision))


# In[ ]:

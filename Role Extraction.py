#!/usr/bin/env python
# coding: utf-8

# In[13]:


import spacy
from spacy.pipeline import EntityRuler
from spacy.lang.en import English


# In[14]:


nlp= English()
ruler= EntityRuler(nlp)
nlp.add_pipe(ruler)


# In[18]:


### load patterns from disk
ruler.from_disk('Entity Patterns')


# In[19]:


len(ruler.patterns)


# In[20]:


print(ruler.patterns[:5])


# In[30]:


doc= nlp(u"Request you to please add 'CS - Supervisor Refund Appr' role for userid VILAKKA")
for ent in doc.ents:
    print(ent.text +'-->'+ ent.label_+'-->'+ ent.ent_id_)


# In[ ]:





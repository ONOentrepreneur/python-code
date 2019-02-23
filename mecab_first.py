
# coding: utf-8

# In[2]:

import MeCab


# In[3]:

mecab = MeCab.Tagger ("-Ochasen")


# In[6]:

print(mecab.parse("僕はピクニックに行った"))


# In[ ]:




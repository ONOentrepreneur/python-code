
# coding: utf-8

# In[6]:

get_ipython().run_cell_magic('bash', '', 'python format.py')


# In[11]:

result = get_ipython().getoutput('python format.py')


# In[12]:

result


# In[13]:

type(result)


# In[15]:

get_ipython().run_cell_magic('bash', '', "python\nprint('ご飯')")


# In[16]:

get_ipython().run_cell_magic('bash', '', 'pwd')


# In[17]:

get_ipython().system('ls')


# In[20]:

x = get_ipython().getoutput('ls')


# In[23]:

type(x[1])


# In[24]:

type(x)


# In[25]:

get_ipython().run_cell_magic('bash', '', 'pwd\ncd ..\npwd')


# In[27]:

get_ipython().run_cell_magic('bash', '', 'pwd')


# In[ ]:




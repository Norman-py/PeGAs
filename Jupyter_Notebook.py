#!/usr/bin/env python
# coding: utf-8

# <center>
#     <img src="https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/Logos/organization_logo/organization_logo.png" width="300" alt="cognitiveclass.ai logo"  />
# </center>
# 

# #### Add your code below following the instructions given in the course
# 

# # My Jupyter Notebook on IBM Watson Studio

# Norman Lützner
# Supply Chain

# *I am interested in data science because quantity of data increases more and more and Excel raised the white flag already. Working and predicting data opens new horizons for me to improve quality and speed.*

# ### Calculates x1 and x2 from an quadratic function equation in normalform. The result will be plotted.

# In[32]:


def Quad_form(x):
    return a*x**2+b*x+c

a=2
b=-8
c=6
x=0

x=x/a
b=b/a
c=c/a

if pow(b,2)/4-c<0: 
    print("c or b variable wrong")

import math

def x1(x,b,c):
    return -b/2 + math.sqrt(pow(b,2)/4-c)
def x2(x,b,c):
    return -b/2 - math.sqrt(pow(b,2)/4-c)

print("x1:",x1(x,b,c),"x2:",x2(x,b,c),"y:",Quad_form(x))


# In[30]:


import matplotlib.pyplot as plt
plt.plot([-4,-3,-2,-1,0,1, 2, 3, 4],[Quad_form(-4),Quad_form(-3),Quad_form(-2),Quad_form(-1),Quad_form(0),Quad_form(1),Quad_form(2),Quad_form(3),Quad_form(4)])
plt.show()


# |Action|command|example|
# |--------------|-------------|-------------|
# |import library|import|import matplotlib.pyplot as plt|
# |calculate with exponents|pow(base,exponent)|pow(1,2)|
# 

# <dl>
#   <dt>Definition list</dt>
#   <dd>Is something people use sometimes.</dd>
# 
#   <dt>Markdown in HTML</dt>
#   <dd>Does *not* work **very** well. Use HTML <em>tags</em>.</dd>
# </dl>

# ![alt text](https://www.python.org/static/img/python-logo.png)

# In[ ]:





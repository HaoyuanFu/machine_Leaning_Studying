
# coding: utf-8

# In[55]:


from numpy import *
##import numpy as np


# In[56]:


x=array([0,1,2,3,4,5,6,7,8])
y=array([0,0.8,0.9,0.1,-0.8,-1, -1.2,-1.1,-1.3])


# In[57]:


from scipy.interpolate import *


# In[58]:


p1=polyfit(x,y,1)


# In[59]:


print (p1)


# In[60]:


from matplotlib.pyplot import *
get_ipython().run_line_magic('matplotlib', 'inline')


# In[61]:


p2=polyfit(x,y,2)
p3=polyfit(x,y,3)


# In[62]:


plot (x,y,'o')
xp=linspace(-2,6,100)
plot(xp,polyval(p1,xp),'r-')
plot(xp,polyval(p2,xp),'b--')
plot(xp,polyval(p3,xp),'m:')
               


# In[63]:


yfit=p1[0]*x+p1[1]
print(yfit)
print(y)


# In[64]:


yresid=y-yfit
SSresid=sum(pow(yresid,2))
SStotal=len(y)*var(y)
rsq = 1-SSresid/SStotal
print(rsq)


# In[65]:


from scipy.stats import *
slope,intercept,r_value,p_value,std_err = linregress(x,y)
print(pow(r_value,2))
print(p_value)


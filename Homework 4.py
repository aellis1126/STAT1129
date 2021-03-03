#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Question 1: Creating an Array
import numpy as np
Answer1=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
Answer1


# In[12]:


#Question 2: Creating Integer Arrays
x=np.arange(1,7)
y=np.arange(5,11)

print(x)
print(y)


# In[14]:


#Question 3: Plotting a Line with Integer Arrays
import matplotlib
import matplotlib.pyplot as plt
plt.plot(x,y)

plt.show()


# In[29]:


#Question 4: Recreating Plot from Assignment with Three Lines
y1 = np.arange(10,13)
y2 = np.arange(5,9)
y3 = np.arange(1,5)

plt.plot(y1)
plt.plot(y2)
plt.plot(y3)

plt.title("3 Line Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()


# In[56]:


#Question 5: Subplots

#Plot 1
x=np.array([0,1,2,3,4,5])
y=np.array([0,1,2,3,4,5])

plt.subplot=(1,2,1)
plt.plot(x,y)

#Plot 2
x=np.array([0,1,2,3,4,5])
y=np.array([0,.5,1,1.5,2,2.5])

plt.subplot=(1,2,2)
plt.plot(x,y)

#Plot 3
x=np.array([0,1,2,3,4,5])
y=np.array([0,2,4,6,8,10])

plt.subplot=(1,3,3)
plt.plot(x,y)

plt.title("Differentiation in Slope")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()


# In[ ]:





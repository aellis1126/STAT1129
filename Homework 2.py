#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 1
FavColors=["Blue","Yellow","Gray","Maroon"]
print(FavColors[0])
print(FavColors[1])
print(FavColors[2])
print(FavColors[3])
print(FavColors)


# In[22]:


#Question 2
n=0
for n in range(0,10):
    print(n)


# In[23]:


#Question 3
n=0
while n<10:
    print(n)
    n=n+1


# In[25]:


#Question 4
n=0
while n<=10:
    print(n)
    n=n+1
else:
    print('Greater than 10')


# In[39]:


#Question 5
n=30
sum=0
i=1

while i<=n:
    sum=sum+i
    i=i+1
print(sum)
print("The sum of integers from 1-30 is",sum)


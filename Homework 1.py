#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Question 1
FavColors=["Blue","Yellow","Gray","Maroon"]


# In[3]:


print(FavColors)


# In[5]:


#Question 2
Numbers=list(range(30,61,3))
print(Numbers)


# In[15]:


#Question 3
Dictionary = {
      "Sunny": "play",
      "Rainy": "watching tv",
      "Cloudy": "walk"
}
print(Dictionary)


# In[16]:


Dictionary.update({"Snowy":"ski"})
print(Dictionary)


# In[50]:


#Question 4
score= float(input("Score of Assignment"))
if score >=90:
    print("A")
elif score >=80 and score<90:
    print("B")
elif score >=70 and score<80:
    print("C")
else:
    print("F")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Question 0
marks= {"Andy":88, "Amy": 66, "James":90, "Jules":55, "Arthur":77}


# In[97]:


#Question 1
for k,v in marks.items():
    print("Student Name=",k,", Grade=",v)


# In[96]:


#Question 2
import statistics
for k,v in marks.items():
    v= grades
statistics.mean(grades)
max(grades)
min(grades)
print("The mean grade is", statistics.mean(grades),".",
     "The maximum grade is", max(grades),".",
     "The minimum grade is", min(grades),".")


# In[64]:


#Question 3
for k,v in marks.items():
    if "J" in k:
        break
    print(k)
    


# In[65]:


#Question 4
for k,v in marks.items():
    if "J" in k:
        continue
    print(k)


# In[98]:


#Question 5
def gradefinder(student_name ="" ):
    for student in marks:
        if student == student_name:
            print(marks[student])
            break
    else:
        print("This student does not exist.")
        
gradefinder("Andy")    


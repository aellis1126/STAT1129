#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question 1
#a. I think this code will print 5:30


# In[6]:


class Clock():
    def __init__ (self,time):
        self.time=time
    def print_time(self):
        time='6:30'
        print(self.time)
        
clock = Clock('5:30')
clock.print_time()


# In[ ]:


#b. This prints 5:30, and not 6:30, 
#because 5:30 is associate with the clock variable that is printing self. Adding the 5:30 nullifies the 6:30.


# In[ ]:


#Question 2
#a. I think this code will print 10:30


# In[10]:


class Clock():
    def __init__ (self,time):
        self.time=time
    def print_time(self, time):
        print(time)
        
clock = Clock('5:30')
clock.print_time('10:30')


# In[ ]:


#b It will take the parameters as the new variable value


# In[ ]:


#Question 3
#a. I think this code will print 5:30 and 10:30, for the two places


# In[11]:


class Clock():
    def __init__ (self,time):
        self.time=time
    def print_time (self):
        print(self.time)
        
class Clock1(Clock):
    pass

boston_clock = Clock('5:30')
paris_clock = Clock1('10:30')

boston_clock.print_time()
paris_clock.print_time()


# In[ ]:


#b. This prints two times because while the the two clocks are the same object, 
#we place an argument to pass through to the second input.


# In[17]:


#Question 4
class Queue():
    def __init__ (self):
        self.items = []
        
    def isEmpty(self):
        if self.items == []:
            print("Queue is empty")
    
    def enqueue(self, item):
        self.items.append(item)
        
    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    
    def print_queue(self):
        print(self.items)

Q=Queue()

Q.print_queue()
Q.isEmpty()

Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)
Q.enqueue(4)

Q.print_queue()
Q.isEmpty()

Q.dequeue()
Q.dequeue()
Q.dequeue()
Q.dequeue()

Q.print_queue()
Q.isEmpty()


#!/usr/bin/env python
# coding: utf-8

# In[60]:


#Question 1
import json
import numpy as np
import matplotlib.pyplot as plt
list = [2,4,6,8,4,5,2,1,9,0,4,6,7,4,3,2,1,9,10,3,7,9,6,0,1,3,5,6,7,8,9,10,2,3,6,8,9,10,6,7,4,3]
freq = {}
for items in list:
    freq[items] = list.count(items)
      
for key, value in freq.items():
    print ("% d : % d"%(key, value))

#Plotting the Frequencies 
plt.hist(list,21)    
plt.title("Frequency of Integers in a Random List")
plt.xlabel("Integer")
plt.ylabel("Frequency")
plt.show()

#Saving as a JSON file
with open('results.json', 'w') as fp:
    json.dump(freq, fp, sort_keys=True, indent=2)


# In[81]:


#Question 2 Analyzing My Facebook Data
import pandas as pd
import json
df= pd.read_json('your_posts_1.json')

#Cleaning up the Data
df.rename(columns={'timestamp':'date'},inplace=True)
df= df.drop(['attachments','title','tags'], axis=1)
pd.to_datetime(df['date'])
df.head(3)
print(df.shape)
df.tail(3)

df = df.set_index('date')
post_counts = df['data'].resample('MS').size()
post_counts

#Plotting Data
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.barplot(x_labels, post_counts, color="purple")
#Formatting the Plot
sns.set(rc={'figure.figsize':(40,20)})
sns.set(font_scale=3)
x_labels = post_counts.index
plt.xlabel('Date')
plt.ylabel('Posts in Month')
plt.title('Analysis of Facebook Posts Per Month for Andrew Ellis from 2011-2021')
#reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))


plt.show()


# In[83]:


#Displaying the first 5 months of data and last 5 months of data
post_counts


# In[ ]:





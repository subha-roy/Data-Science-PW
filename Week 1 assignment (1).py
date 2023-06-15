#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
v1 = 'Jay'
v2 = ['DS', 'Ml', 'Python']
v3 = 3.123
v4 = ("Apple", "Mango", "Banana")


# In[1]:


#Q1
v1 = 'Jay'
v2 = ['DS', 'Ml', 'Python']
v3 = 3.123
v4 = ("Apple", "Mango", "Banana")


# In[2]:


#Q2
var1=""
var2='[DS, ML, Python]'
var3=['DS', 'Ml', 'Python']
var4=1


# In[3]:


type(var1)


# In[4]:


type(var2)


# In[5]:


type(var3)


# In[6]:


type(var4)


# In[7]:


#Q3
#i--> /=> to divise
#ii--> %=> to get the reminder
#iii--> //=> for floor division or interger division
#iv--> **=> square power


# In[8]:


#Q4
a = [1,2,23.43, 'pyhton', 'DS', True, 'ML', False, 'NN', 3+4j]
for i in a:
    print(i)


# In[9]:


#Q5
A=88
B=2
counter = 0
while (A % B) == 0:
    A //= B
    counter += 1
print(counter)    


# In[10]:


#Q6
l = list(range(26))
for i in l:
    if i%3==0:
        print(i)


# In[11]:


#Q7
'''mutability means when u can change a particular data at a particular index 
but when u try to change a data or specifically string, eg. 'Subho' instead of 'Subha' u can't change it-- imutability
String is imutable object, where as list is mutable object'''
#e.g. of mutable data
l = [1,2,3,4,"Subha", "Python", 3+4j]
l[3] = "Jay"
l


# In[ ]:





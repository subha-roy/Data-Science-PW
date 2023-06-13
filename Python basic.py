#!/usr/bin/env python
# coding: utf-8

# In[20]:


# U know what is variable, go through it by python udemy file


# In[2]:


#Complex number--> use 'j' instead of 'i'
a = 3+4j


# In[3]:


type(a)


# In[5]:


#we can separate 'real' and 'imaginary' part from the complex number
a.real


# In[6]:


a.imag


# In[7]:


a = 10
s = "Joy"
#type casting
str(a) + s


# MUTABILITY AND IMUTABILITY

# In[9]:


b = "Subha"
b[1]


# In[10]:


#List
l = [1,2,3,4,"Subha", "Python", 3+4j]
type(l)


# In[13]:


#forward indexing and backward indexing
l[4]


# In[14]:


l[-2]


# In[16]:


l[1:-1]


# In[17]:


l[3] = "Raj"


# In[18]:


l


# In[21]:


#mutability means when u can change a particular data at a particular index 
#but when u try to change a data or specifically string, eg. 'Subho' instead of 'Subha' u can't change it-- imutability
#String is imutable object, where as list is mutable object


# In[3]:


name = input("Your name: ")
age = input("Your age: ")

print("My name is {} and age is {}.".format(name, age))


# In[5]:


age = int(input("What is your age?: "))
if age>18:
    print("You are eligible to vote.")
else:
    print("You can't vote.")


# In[6]:


age = int(input("What is your age?: "))
if age>=18 and age<=45:
    print("You are young blood.")


# In[10]:


price = int(input("What is the price of your product that you want to purchase?\n"))

if price>1000:
    print(f"You'll get a 25% off on the product.and the price will be {.75*price}.")
else:
    print(f"You'll get a 20% off on the product and the price will be {.8*price}.")


# In[16]:


#nested if statement
price = int(input("What is the price of your product that you want to purchase?\n"))

if price>=3000:
    print(f"You'll get a 40% off on the product.and the price will be {.6*price}.")
elif price>=2000 and price<3000:
    print(f"You'll get a 30% off on the product.and the price will be {.7*price}.")
    if price==2999:
        gift = input("Which one do you want to get. Type the option\n 1) Suitcase, 2) Dinning Set\n".lower())
        print(f"You'll get a {gift}.")
elif price>=1000 and price<2000:
    print(f"You'll get a 20% off on the product.and the price will be {.8*price}.")
    if price==1999:
        gift = input("Which one do you want to get. Type the option\n 1) Game for children, 2) Cup set\n".lower())
        print(f"You'll get a {gift}.")
else:
    print(f"You'll get a 10% off on the product and the price will be {.9*price}.")


# In[19]:


#single statement
val = int(input("Enter the value: "))
if (val<=900):print("Congratulation you availed an offer of 15%.")
else:
    print("Go home.")


# In[ ]:





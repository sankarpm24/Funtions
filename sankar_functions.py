#!/usr/bin/env python
# coding: utf-8

# In[8]:


i=1
while(i<5):
    print(i)
    i+=1


# In[9]:


i=1
while(i<=5):
    print(i)
    if i==3:
     break
    i+=1


# In[10]:


i=1
while(i<=5):
   i+=1
   if i==3:
    continue
   print(i)


# In[11]:


def funcexample():
    print("This is a sample function")
funcexample()


# In[1]:


def func():
    print("This is a sample function")
print("testing")
func()


# In[2]:


#one argument func
lastname="Ponnusamy"
def func(firstname):
    print(firstname+" "+lastname)
func("Sankar")
    


# In[3]:


lastname="Ponnusamy"
def func(firstname):
   print(firstname+" "+lastname)
func("Sankar")
func("Baskar")
func("Ravi")


# In[6]:


#Multiple argument func
lastname="Ponnusamy"
def func(firstname,city,phonenum):
    print(firstname+" "+lastname,city,phonenum)
func("Sankar","Pondicherry",12345)
func("Baskar","chennai",56789)
func("Ravi","Bangalore",78547)


# In[7]:


#Func with formatted string
lastname="Ponnusamy "
def funcexample(firstname,city,phonenum):
    print(f"Hello ,{firstname.title()}"+" "+lastname,f"your city is {city.upper()}",f" and contact number is {phonenum}")
funcexample("sankar","Pondicherry",12345)
funcexample("baskar","chennai",56789)
funcexample("ravi","Bangalore",78547)
    


# In[ ]:





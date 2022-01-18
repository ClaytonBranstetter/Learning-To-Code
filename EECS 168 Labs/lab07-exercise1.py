'''
Author: Clayton Branstetter
KUID: 3089206
Date: 11/03/2021
Lab: lab#07
Last modified: 11/03/2021
Purpose: File Handling
'''

# In[ ]:


import re
file_name = str(input("Write the name of the file"))


# In[1]:


# Using readlines()
file1 = open(file_name, 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))


# In[ ]:


# In[ ]:


# In[9]:


x = Lines[0].split(" ")


# In[10]:


x


# In[11]:


cleanString = re.sub('\n', '', Lines[0])


# In[12]:


cleanString


# In[15]:


x = cleanString.split(" ")


# In[16]:


x


# In[103]:


file_name = str(input("Write the name of the file"))
file1 = open(file_name, 'r')
Lines = file1.readlines()


# In[104]:


total = 0
average_list = []
for i in range(len(Lines)):
    sub_total = 0
    cleanString = re.sub('\n', '', Lines[i])
    x = cleanString.split(" ")
    for element in x:
        total += float(element)
        sub_total += float(element)
    average_list.append(sub_total/len(x))
total = float(total)
average_total = total / (len(Lines) * len(x))
average_total = float(average_total)
averages = open("averages.txt", "w")
averages.write("Total average: "+str(average_total)+"\n")
for i in range(len(average_list)):
    n = float(average_list[i])

    averages.write("Row "+str(i+1)+" average: "+str(n)+"\n")
averages.close()


# In[105]:


def Reverse(lst):
    return [ele for ele in reversed(lst)]


reverse = open("reverse.txt", "w")
for i in range(len(Lines)):
    sub_total = 0
    cleanString = re.sub('\n', '', Lines[i])
    x = cleanString.split(" ")
    x = Reverse(x)

    for e in x:

        reverse.write(str(e)+" ")
    reverse.write("\n")
reverse.close()


# In[106]:


flipped = Reverse(Lines)


# In[107]:


textfile = open("flipped.txt", "w")
for element in flipped:
    textfile.write(element + "\n")
textfile.close()

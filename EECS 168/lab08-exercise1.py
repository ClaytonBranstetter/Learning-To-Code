'''
Author: Clayton Branstetter
KUID: 3089206
Date: 11/03/2021
Lab: lab#08
Last modified: 11/03/2021
Purpose: Dictionary
'''

# In[28]:


import re


def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        word = clean_word(word)
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


# In[29]:


def clean_word(word):

    word = re.sub('\W+', '', word)
    return word


# In[36]:


def unique_words(words_counts):
    L = []
    for key in words_counts:
        if words_counts[key] == 1:
            L.append(key)
    return L


# In[90]:


def list_to_text(L):
    ch = ""
    for e in L:
        ch = ch+" "+e
    return ch


def main():

    w = "Welcome"
    print(w.center(20, '='))
    file_name = str(input("Please Enter the name of the file"))
    with open(file_name, 'r') as f:
        listl = []
        for line in f:
            strip_lines = line.strip()
            listli = strip_lines.split()

            m = listl.append(listli)
    text = ""
    for i in range(len(listl)):
        text += list_to_text(listl[i])+" "
    word_data = word_count(text)
    word_data_file = open("word_data.txt", "w")
    for element in word_data:
        word_data_file.write(str(element)+":"+str(word_data[element])+" \n")
    word_data_file.close()

    unique_words_file = open("unique_words.txt", "w")
    List = unique_words(word_data)
    for element in List:
        unique_words_file.write(str(element)+"\n")
    unique_words_file.close()


# In[91]:
main()

#!/usr/bin/env python
# coding: utf-8

# In[17]:


import cv2
import re
import pytesseract
from prettytable import PrettyTable
import spacy
nlp = spacy.load(r"/Users/sanjaydilii/Desktop/ner/output/model-best")


# In[13]:


path = (r'/Users/sanjaydilii/Downloads/83b6e8c5-dcaa-4c5e-80c6-357ce719263e.JPG')
img_cv = cv2.imread(path)
img_rgb = cv2.cvtColor(img_cv,cv2.COLOR_BGR2RGB)
txt = pytesseract.image_to_string(img_rgb)
my_string = txt
string = re.sub(r'\s+', ' ', my_string)


# In[ ]:


print(string)


# In[22]:


att = []
key = []
doc = nlp(" ".join(string.split('\n')))
for ent in doc.ents:
    att.append(ent.text)
    key.append(ent.label_.upper())
    table = PrettyTable()
    table.field_names = key
    table.add_row(att)


# In[24]:


print(table)


# In[ ]:





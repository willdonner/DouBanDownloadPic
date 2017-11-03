import nltk
import os
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
from numpy import *
import re

# str2=[]
listkey = []
listval = []

with open('/Users/willdonner/DevsTest/stop_words.txt','r',encoding='utf-8') as file1:
    str1 = file1.read()
    str2 = re.sub("[^A-Za-z\ ]", "", str1)
    tokenstr = nltk.word_tokenize(str2)
    fdist = nltk.FreqDist(tokenstr)

    print(u".........统计出现最多的前30个词..............")
for key, val in sorted(fdist.items(), key=lambda x: (x[1], x[0]), reverse=True)[:20]:
    listkey.append(key)
    listval.append(val)
    print(key, val, u' ')

df = pd.DataFrame(listval,columns=[u'count'])
df.index = listkey
# plt.figure()
df.plot(kind='kde')
plt.show()

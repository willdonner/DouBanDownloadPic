import pandas as pd
from numpy import *
import matplotlib.pyplot as plt
import nltk
import re
word_box =[]
box = []
with open('/Users/willdonner/DevsTest/result1.txt','r',encoding='utf-8') as file1:
  inputfile = file1.read()
  str2 = re.sub("[^A-Za-z\ ]", "", inputfile)
  tokens = nltk.tokenize.word_tokenize(str2)
  fd = nltk.FreqDist(tokens)
  fd.plot(20,cumulative=False)
  plt.show()
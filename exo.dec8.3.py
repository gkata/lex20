import sys
import re
import math
import nltk
from nltk.collocations import *
from nltk.tokenize import word_tokenize
import numpy as np

#nltk.download('punkt')

# Ecrivez la fonction 'main' qui lit le fichier donné en argument, le tokenise 
# avec word_tokenize de nltk et prépare les dictionnaires de mots et de bigrams 
# (clé: mot/bigram, valeur: fréquence) : 
# 1) le dictionnaire des mots : wordfreq 
# 2) le dictionnaire des bigrams : bifreq
# 3) la fréquence totale des mots : N
# 4) la fréquence totale des bigrams : B


def normalize(word):
 return re.sub(r"[\.\,\?\:\;\"\'\-]",r"",word.lower())

stop = {}
f = open("stopwords.lst", "r")
for line in f:
  stop[normalize(line.rstrip())] = 1
f.close


def main():
  wordfreq = {}
  bifreq = {}
  N = 0
  B = 0

  f = open(sys.argv[1], "r")
  for line in f:
    words1 = word_tokenize(line)
    words = []
    for w in words1:
      words.append(normalize(w))

    for word in words:
      if stop.get(word) == 1 or word == '':
        continue
      else:
        N += 1
        if wordfreq.get(word) == None:
          wordfreq[word] = 1
        else:
          wordfreq[word] += 1

    for k in range(1,len(words)):
      if stop.get(words[k-1]) == 1 or stop.get(words[k]) == 1 or words[k-1] == '' or words[k] == '':
        continue
      if words[k-1] == '' or words[k] == '':
        continue        
      bigram = words[k-1] + ' ' + words[k]
      B += 1
      if bifreq.get(bigram) == None:
        bifreq[bigram] = 1
      else:
        bifreq[bigram] += 1


  print ('N=' + str(N))
  print ('B=' + str(B))

  vocab = sorted(wordfreq, key=wordfreq.get, reverse=True)[0:1000]
  M = np.zeros([1000,1000])
  
  for w1 in vocab:
    for w2 in vocab:      
      if bifreq.get(w1 + ' ' + w2) != None:
        M[vocab.index(w1),vocab.index(w2)] += bifreq[w1 + ' ' + w2]
      if bifreq.get(w2 + ' ' + w1) != None:
        M[vocab.index(w1),vocab.index(w2)] += bifreq[w2 + ' ' + w1] 
 
  print (bifreq['united states'])
  print (M[vocab.index('united'),vocab.index('states')])
  print (M[vocab.index('states'),vocab.index('united')])
  
  
  onehot = np.zeros([1000])
  user = input("Enter a word:")
  onehot[vocab.index(user.rstrip())] = 1
  print (onehot)
  
  #for word in sorted(wordfreq, key=wordfreq.get, reverse=True):
  #  print (word + "\t" +  str(wordfreq[word]))


  #for word in sorted(bifreq, key=bifreq.get, reverse=True):
  #  print (word + "\t" +  str(bifreq[word]))



if __name__ == '__main__':
  main()

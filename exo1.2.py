import sys
import re
import math
import nltk
from nltk.collocations import *
from nltk.tokenize import word_tokenize

#nltk.download('punkt')

# Ecrivez la fonction 'main' qui lit le fichier donné en argument, le tokenise 
# avec word_tokenize de nltk et prépare les dictionnaires de mots et de bigrams 
# (clé: mot/bigram, valeur: fréquence) : 
# 1) le dictionnaire des mots : wordfreq 
# 2) le dictionnaire des bigrams : bifreq
# 3) la fréquence totale des mots : N
# 4) la fréquence totale des bigrams : B

def main():
  wordfreq = {}
  bifreq = {}
  N = 0
  B = 0
  
 ### your code here ###


  f = open(sys.argv[1], "r")
  for line in f:
    words = word_tokenize(line)

    for word in words:
      N += 1
      if wordfreq.get(word) == None:
        wordfreq[word] = 1
      else:
        wordfreq[word] += 1

    for k in range(1,len(words)):
      bigram = words[k-1] + ' ' + words[k]
      B += 1   
      if bifreq.get(bigram) == None:
        bifreq[bigram] = 1
      else:
        bifreq[bigram] += 1

  print ('N=' + str(N))
  print ('B=' + str(B))

  for word in sorted(wordfreq, key=wordfreq.get, reverse=True):
    print (word + "\t" +  str(wordfreq[word]))

  for word in sorted(bifreq, key=bifreq.get, reverse=True):
    print (word + "\t" +  str(bifreq[word]))


if __name__ == '__main__':
  main()


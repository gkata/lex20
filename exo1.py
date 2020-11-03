import sys
import re
import math
import nltk
from nltk.collocations import *
from nltk.tokenize import word_tokenize

nltk.download('punkt')

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



if __name__ == '__main__':
  main()


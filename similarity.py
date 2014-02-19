#!/usr/bin/python
# coding:utf-8

import re, math
from collections import Counter
from itertools import izip, islice, tee

a = "Rua Nossa Senhora das Graças"
b = "Rua Nsa. Sra. das Graças"
c = "R. N. Sa. das Graças"

N = 3
a3 = izip(*(islice(seq, index, None) for index, seq in enumerate(tee(a, N))))
b3 = izip(*(islice(seq, index, None) for index, seq in enumerate(tee(b, N))))
c3 = izip(*(islice(seq, index, None) for index, seq in enumerate(tee(c, N))))

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

def simhash(tokens, hashbits=32):
   if hashbits > 64: hashbits = 64
   v = [0]*hashbits
   for t in [x.__hash__() for x in tokens]:
       bitmask = 0
       for i in xrange(hashbits):
           bitmask = 1 << i
           if t & bitmask:
               v[i] += 1
           else:
               v[i] -= 1
   fingerprint = 0
   for i in xrange(hashbits):
       if v[i] >= 0:
           fingerprint += 1 << i
   return fingerprint

def similarity(a, b, hashbits=32):
   # Use Hamming Distance to return % of similar bits
   x = (a ^ b) & ((1 << hashbits) - 1)
   tot = 0
   while x:
       tot += 1
       x &= x-1
   return float(hashbits-tot)/hashbits

print "SIMHASH Simliarity between \""+a+"\" and \""+b+"\" is",similarity(simhash(a3),simhash(b3))
print "COSINE Simliarity between \""+a+"\" and \""+b+"\" is",get_cosine(text_to_vector(a),text_to_vector(b))

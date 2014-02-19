#!/usr/bin/python
# coding:utf-8

a = "Rua Nossa Senhora das Graças"
b = "Rua Nsa. Sra. das Graças"

from itertools import izip, islice, tee
N = 3
a3 = izip(*(islice(seq, index, None) for index, seq in enumerate(tee(a, N))))
b3 = izip(*(islice(seq, index, None) for index, seq in enumerate(tee(b, N))))

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

print "Simliarity between \""+a+"\" and \""+b+"\" is",similarity(simhash(a3),simhash(b3))

#!/usr/bin/env python3

import sys
import re


lines = sys.stdin.read().strip().split('\n')
a = int(lines[0])
b = list([int(x) for x in lines[1].split(',') if x != 'x'])
best_id = -1
best_time = 100000000
for c in b:
  z = c * (a // c)
  if z < a:
    z += c
  if best_time > z:
    best_id = c
    best_time = z

print(best_id, best_time)
print(best_id * (best_time - a))

def gcd(a, p, q, b, r, s):
  while a != 0 and b != 0:
    if a >= b:
      x = a // b
      p -= x * r
      q -= x * s
      a -= x * b
    else:
      x = b // a
      r -= x * p
      s -= x * q
      b -= x * a
  if a == 0:
    return b, r, s
  else:
    return a, p, q

def inverse(a, p):
  d, x, y = gcd(a, 1, 0, p, 0, 1)
  if d != 1:
    print(a, p, d)
    raise ValueError()
  return x


def chinesse(x, p, y, q):
  a = x * q * inverse(q, p) + y * p * inverse(p, q)
  a = a % (p * q)
  if a % p != x or a % q != y:
    raise ValueError()
  return a, p * q


b = lines[1].split(',')

x = 0
p = 1
for i in range(len(b)):
  if b[i] == 'x':
    continue
  q = int(b[i])
  x, p = chinesse(x, p, (q - i) % q, q)
  print(x, p, (q - i) % q, q)
print(x)

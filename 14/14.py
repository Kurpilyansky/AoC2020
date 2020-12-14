#!/usr/bin/env python3

import sys
import re

def get_val(b, mask):
  for i in range(len(mask)):
    if mask[i] == '0':
      if b & (1 << i):
        b -= (1 << i)
    elif mask[i] == '1':
      if (b & (1 << i)) == 0:
        b += (1 << i)
  return b

def get_indices(b, mask):
  bits = []
  for i in range(len(mask)):
    if mask[i] == 'X':
      bits.append(i)
      if b & (1 << i):
        b -= (1 << i)
    elif mask[i] == '1':
      if (b & (1 << i)) == 0:
        b += (1 << i)

  for a in range(1 << len(bits)):
    c = b
    for i in range(len(bits)):
      if a & (1 << i):
        c += (1 << bits[i])
    yield c

lines = sys.stdin.read().strip().split('\n')
mask = 'X' * 36
mem = dict()
for line in lines:
  if line[:4] == 'mask':
    mask = str(line.split()[2][::-1])
    continue
    
  print(line)
  index, b = map(int, line.strip('mem[').split('] = '))
  print(index, b)
  mem[index] = get_val(b, mask)
print(mem)
print(sum(mem.values()))


mask = 'X' * 36
mem = dict()
for line in lines:
  if line[:4] == 'mask':
    mask = str(line.split()[2][::-1])
    continue
    
  print(line)
  index, val = map(int, line.strip('mem[').split('] = '))
  print(index, val)
  for index in get_indices(index, mask):
    mem[index] = val

print(mem)
print(sum(mem.values()))


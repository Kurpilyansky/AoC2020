#!/usr/bin/env python3

import sys
import re

def check(ranges, x):
  for name, r in ranges.items():
    for q in r:
      if q[0] <= x <= q[1]:
        return True
  return False

def main():
  a, b, c = sys.stdin.read().strip().split("\n\n")
  #print(a)
  ranges = dict()
  for line in a.split('\n'):
    tokens = line.split(': ')
    d = tokens[1].split(' or ')
    ranges[tokens[0]] = tuple([tuple(map(int, x.split('-'))) for x in d])
  print(ranges)

  valid = []
  ans = 0
  for line in c.split('\n')[1:]:
    v = list(map(int, line.split(',')))
    ok = True
    for x in v:
      if not check(ranges, x):
        ans += x
        ok = False
    if ok:
      valid.append(v)
  print(ans)

  keys = list(ranges.keys())
  good = [set(range(len(keys))) for x in ranges]
  for i, key in enumerate(keys):
    for v in valid:
      for j, x in enumerate(v):
        if not check({key: ranges[key]}, x):
          good[i].discard(j)
  #print('\n'.join(map(lambda x: ' '.join(map(str, x)), valid)))
  #print(good)
  #print([len(x) for x in good])
  perm = [-1] * len(ranges)
  while True:
    ok = True
    for i, good_i in enumerate(good):
      if len(good_i) == 1:
        perm[i] = list(good_i)[0]
        for good_j in good:
          good_j.discard(perm[i])
        ok = False
        break
    if ok:
      break
  print(perm)

  my_ticket = list(map(int, b.split('\n')[1].split(',')))
  ans2 = 1
  for i, key in enumerate(keys):
    if key.startswith('departure'):
      ans2 *= my_ticket[perm[i]]
  print(ans2)

if __name__ == "__main__":
  main()

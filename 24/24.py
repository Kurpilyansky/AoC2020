#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy


def norm(x, y, z):
  k = x + y + z
  x -= k
  y += k
  z -= k
  return x, y, z

def find_point(s):
  x = 0
  y = 0
  z = 0
  i = 0
  while i < len(s):
    if s[i] == 'e':
      x += 1
    elif s[i] == 'w':
      x -= 1
    elif s[i] == 'n':
      i += 1
      if s[i] == 'e':
        y += 1
      elif s[i] == 'w':
        z += 1
    elif s[i] == 's':
      i += 1
      if s[i] == 'e':
        z -= 1
      elif s[i] == 'w':
        y -= 1
    i += 1

  return norm(x, y, z)

def get_neighs(pt):
  for i in range(3):
    for dx in [-1, 1]:
      pt2 = list(pt)
      pt2[i] += dx
      yield norm(*pt2)
      
def get_next(cur):
  neighs_cnt = dict()
  for pt in cur:
    for npt in get_neighs(pt):
      neighs_cnt[npt] = neighs_cnt.get(npt, 0) + 1
  return {pt for pt, cnt in neighs_cnt.items() if cnt == 2 or (cnt == 1 and pt in cur)}

def main():
  lines = sys.stdin.read().strip().split('\n')
  alive = set()
  for line in lines:
    pt = find_point(line)
    if pt in alive:
      alive.remove(pt)
    else:
      alive.add(pt)
  print(len(alive))

  for i in range(int(sys.argv[1])):
    alive = get_next(alive)
  print(len(alive))

if __name__ == "__main__":
  main()

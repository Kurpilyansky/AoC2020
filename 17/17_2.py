#!/usr/bin/env python3

import sys
import re

def get_key(x, y, z, w):
  return ','.join(map(str, [x, y, z, w]))

def gen_next(cur):
  neigh = dict()
  for x, y, z, w in cur:
    for dx in range(-1, 2):
      for dy in range(-1, 2):
        for dz in range(-1, 2):
          for dw in range(-1, 2):
            x1 = x + dx
            y1 = y + dy
            z1 = z + dz
            w1 = w + dw
            key = get_key(x1, y1, z1, w1)
            if key not in neigh:
              neigh[key] = 0
            neigh[key] += 1 if dx or dy or dz or dw else 0
  new = set()
  for key in neigh:
    x, y, z, w = map(int, key.split(','))
    cnt = neigh[get_key(x, y, z, w)]
    if (x, y, z, w) in cur and (cnt == 2 or cnt == 3):
      new.add((x, y, z, w))
    if (x, y, z, w) not in cur and cnt == 3:
      new.add((x, y, z, w))
  return new
    
      

def main():
  a = sys.stdin.read().strip().split("\n")
  cur = set()
  for x in range(len(a)):
    for y in range(len(a[0])):
      if a[x][y] == '#':
        cur.add((x, y, 0, 0))

  for i in range(6):
    cur = gen_next(cur)
    print(len(cur))

if __name__ == "__main__":
  main()

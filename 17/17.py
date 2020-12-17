#!/usr/bin/env python3

import sys
import re
import itertools

def gen_next(cur):
  neigh = dict()
  for pt  in cur:
    for dpt in itertools.product(range(-1, 2), repeat=len(pt)):
      npt = tuple(map(sum, zip(pt, dpt)))
      neigh[npt] = neigh.get(npt, 0) + 1
  new = set()
  for pt in neigh:
    cnt = neigh[pt]
    if cnt == 3 or (cnt == 4 and pt in cur):
      new.add(pt)
  return new
      

def main():
  dim = int(sys.argv[1])
  a = sys.stdin.read().strip().split("\n")
  cur = set()
  for x in range(len(a)):
    for y in range(len(a[0])):
      if a[x][y] == '#':
        cur.add(tuple([x, y] + [0] * (dim - 2)))

  for i in range(6):
    cur = gen_next(cur)
    print(len(cur))

if __name__ == "__main__":
  main()

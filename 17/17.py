#!/usr/bin/env python3

import sys
import re
import itertools

def gen_next_inlined(cur, dim):
  neigh = {npt: len(list(gr)) for npt, gr in itertools.groupby(sorted(map(lambda x: tuple(map(sum, zip(*x))), itertools.product(cur, itertools.product(range(-1, 2), repeat=dim)))))}
  return {pt for pt, cnt in neigh.items() if cnt == 3 or (cnt == 4 and pt in cur)}


def gen_next(cur):
  neigh = dict()
  for pt in cur:
    for dpt in itertools.product(range(-1, 2), repeat=len(pt)):
      npt = tuple(map(sum, zip(pt, dpt)))
      neigh[npt] = neigh.get(npt, 0) + 1
  return {pt for pt, cnt in neigh.items() if cnt == 3 or (cnt == 4 and pt in cur)}


def main():
  dim = int(sys.argv[1])
  a = sys.stdin.read().strip().split("\n")
  cur = set()
  for x in range(len(a)):
    for y in range(len(a[0])):
      if a[x][y] == '#':
        cur.add((x, y) + (0,) * (dim - 2))

  for i in range(6):
    cur = gen_next(cur)
    print(len(cur))

if __name__ == "__main__":
  main()

#!/usr/bin/env python3

import sys
import re


def genNext(n, m, w, neigh):
  w2 = list([[chr(ord(s[y])) for y in range(len(s))] for s in w])
  any_changed = False
  for x in range(n):
    for y in range(m):
      cnt = 0
      for x1, y1 in neigh[x][y]:
        if w[x1][y1] == '#':
          cnt += 1
      if cnt == 0 and w[x][y] == 'L':
        w2[x][y] = '#'
        any_changed = True

      if cnt >= 5 and w[x][y] == '#':
        w2[x][y] = 'L'
        any_changed = True
#print(w[x][y], w2[x][y], x, y, cnt)
  return [''.join(s) for s in w2], any_changed


def find_neighbours(n, m, w):
  neigh = [[[] for y in range(m)] for x in range(n)]
  for x in range(n):
    for y in range(m):
      for dx in range(-1, 2):
        for dy in range(-1, 2):
          if dx == 0 and dy == 0:
            continue
          x1 = x + dx
          y1 = y + dy
          while (0 <= x1 < n) and (0 <= y1 < m):
            if w[x1][y1] == '#' or w[x1][y1] == 'L':
              neigh[x][y].append((x1, y1))
              break
            x1 += dx
            y1 += dy
  return neigh

w = sys.stdin.read().strip().split('\n')
n = len(w)
m = len(w[0])
neigh = find_neighbours(n, m, w)

while True:
#  print('\n'.join(w))
#  print()
  w, any_changed = genNext(n, m, w, neigh)
  if not any_changed:
    break
print('\n'.join(w))
print(sum([s.count('#') for s in w]))


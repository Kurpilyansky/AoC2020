#!/usr/bin/env python3

import sys
import re


lines = sys.stdin.read().strip().split('\n')

dx = [(1, 0), (0, -1), (-1, 0), (0, 1)]

x = 0
y = 0
dir_ = 0
for line in lines:
  ch = line[0]
  num = int(line[1:])
  if ch == 'N':
    y += num
  elif ch == 'E':
    x += num
  elif ch == 'W':
    x -= num
  elif ch == 'S':
    y -= num
  elif ch == 'L':
    dir_ = (dir_ + 4 - num // 90) % 4
  elif ch == 'R':
    dir_ = (dir_ + num // 90) % 4
  elif ch == 'F':
    x += dx[dir_][0] * num
    y += dx[dir_][1] * num
  print(ch, num, x, y)

print(x, y)
print(abs(x) + abs(y))



x = 0
y = 0
dx1 = 10
dy1 = 1
for line in lines:
  ch = line[0]
  num = int(line[1:])
  if ch == 'N':
    dy1 += num
  elif ch == 'E':
    dx1 += num
  elif ch == 'W':
    dx1 -= num
  elif ch == 'S':
    dy1 -= num
  elif ch == 'L':
    for i in range(num // 90):
      dx1, dy1 = -dy1, dx1
  elif ch == 'R':
    for i in range(num // 90):
      dx1, dy1 = dy1, -dx1
  elif ch == 'F':
    x += dx1 * num
    y += dy1 * num
  print(ch, num, x, y)
print(x, y)
print(abs(x) + abs(y))


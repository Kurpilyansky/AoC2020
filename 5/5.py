import sys
import re


def parse():
  lines = sys.stdin.read().strip().split('\n')
  return lines


def decode(s, zero, one):
  res = 0
  pow2 = 1
  for ch in s[::-1]:
    if ch == one:
      res += pow2
    pow2 *= 2
  return res

lines = parse()
res = -1
ids = []
for line in lines:
  x = decode(line[:7], 'F', 'B')
  y = decode(line[7:], 'L', 'R')
  cur = x * 8 + y
  ids.append(cur)
  res = max(res, cur)
print(res)

ids = list(sorted(ids))
for i in range(1, len(ids)):
  if ids[i - 1] + 2 == ids[i]:
    print(ids[i] - 1)

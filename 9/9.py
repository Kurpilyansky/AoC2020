import sys
import re


def is_good(v, x):
  for i in range(len(v)):
    for j in range(i):
      if v[i] + v[j] == x:
        return True
  return False


a = list(map(int, sys.stdin.read().strip().split('\n')))
k = int(sys.argv[1])

for i in range(k, len(a)):
  if not is_good(a[:i][-k:], a[i]):
    res = a[i]
    break

print(res)
for i in range(len(a)):
  s = a[i]
  for j in range(i + 1, len(a)):
    s += a[j]
    if s == res:
      print(min(a[i:j+1]) + max(a[i:j + 1]))

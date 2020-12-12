import sys
import re


def parse():
  groups = sys.stdin.read().strip().split('\n\n')
  res = 0
  for group in groups:
    cnt = 0
    for i in range(26):
      if group.count(chr(ord('a') + i)):
        cnt += 1
    res += cnt
  print(res)

  res = 0
  for group in groups:
    yes = [True] * 26
    for line in group.split('\n'):
      for i in range(26):
        if not line.count(chr(ord('a') + i)):
          yes[i] = False
    res += sum(yes)
  print(res)


lines = parse()


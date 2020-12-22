#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy


def parse_food(s):
  a, b = s.strip(')').split(' (contains ')
  return set(a.split()), set(b.split(', '))


def main():
  lines = sys.stdin.read().strip().split("\n")
  food = list(map(parse_food, lines))
  
  alergens = functools.reduce(lambda x, y: x|y, map(lambda x: x[1], food))
  ingrs = functools.reduce(lambda x, y: x|y, map(lambda x: x[0], food))
  print(len(alergens))
  print(len(ingrs))
  bad_ingrs = {aler: functools.reduce(lambda x, y: x&y, [a for a, b in food if aler in b]) for aler in alergens}
  bad = functools.reduce(lambda x, y: x|y, bad_ingrs.values())
  good = ingrs.difference(bad)
  print(bad)
  print(good)
  print([x for a, b in food for x in a if x in good])
  print(len([x for a, b in food for x in a if x in good]))
  while True:
    exact = functools.reduce(lambda x, y: x|y, [b for a, b in bad_ingrs.items() if len(b) == 1])
    print(bad_ingrs)
    print(exact)
    ok = True
    for a, b in bad_ingrs.items():
      if len(b) != 1:
        bad_ingrs[a] = b.difference(exact)
        ok = False
    if ok:
      break
  print(','.join(map(lambda x: list(x[1])[0], sorted(bad_ingrs.items()))))


if __name__ == "__main__":
  main()

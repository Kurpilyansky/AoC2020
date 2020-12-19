#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy


def match(s, rules):
  dp = dict()

  @functools.lru_cache(None)
  def findDP(rule_id, left, right):
    rule = rules[rule_id]
    length = right - left

    if rule[0] == 0:
      return (length == 1 and s[left] == rule[1])

    def check(v):
      if len(v) == 1:
        return findDP(v[0], left, right)
      elif len(v) == 2:
        return any([findDP(v[0], left, middle) and findDP(v[1], middle, right) for middle in range(left + 1, right)])
      else:
        raise ValueError('v %s' % str(v))

    return any(map(check, rule[1]))

  return findDP(0, 0, len(s))


def normalize_rules(rules):
  rules = copy.deepcopy(rules)
  new_rules = []
  new_rule_id = max(rules.keys()) + 1
  for rule_id, rule in rules.items():
    if rule[0] == 0:
      continue
    for i in range(len(rule[1])):
      q = rule[1][i]
      if len(q) <= 2:
        continue
      x = q[0]
      y = q[1]
      for j in range(2, len(q)):
        new_rules.append((new_rule_id, [y, q[j]]))
        y = new_rule_id
        new_rule_id += 1
      rule[1][i] = [x, y]
  for rule_id, rule in new_rules:
    rules[rule_id] = (1, [rule])
  return rules


def count_matched(rules, words):
  rules = normalize_rules(rules)
  return sum(map(lambda x: match(x, rules), words))


def parse_rule(s):
  if s[0] == '"':
    return 0, s[1]
  else:
   return 1, list(map(lambda q: list(map(int, q.split())), s.split(' | ')))


def main():
  a, b = sys.stdin.read().strip().split("\n\n")
  rules = {int(x): parse_rule(y) for x, y in map(lambda s: s.split(': '), a.split('\n'))}
  words = b.split('\n')

  print(count_matched(rules, words))

  rules[8] = parse_rule('42 | 42 8')
  rules[11] = parse_rule('42 31 | 42 11 31')
  print(count_matched(rules, words))



if __name__ == "__main__":
  main()

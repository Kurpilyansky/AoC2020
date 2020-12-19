#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy


def parse_rule_outputs(s):
  def parse_rule_output(s):
    if s[0] == '"':
      return s.strip('"')
    else:
      return list(map(int, s.split()))

  return list(map(parse_rule_output, s.split(' | ')))


def match(rules, word):

  @functools.lru_cache(None)
  def findDP(rule_id, left, right):

    def try_output(output):
      if isinstance(output, str):
        return word[left:right] == output
      elif len(output) == 1:
        return findDP(output[0], left, right)
      elif len(output) == 2:
        return any([findDP(output[0], left, middle) and findDP(output[1], middle, right) for middle in range(left + 1, right)])
      else:
        raise ValueError('Invalid output %s' % str(output))

    return any(map(try_output, rules[rule_id]))

  return findDP(0, 0, len(word))

def normalize_rules(rules):
  rules = copy.deepcopy(rules)
  new_rules = []
  new_rule_id = max(rules.keys()) + 1
  for rule_id, rule_outputs in rules.items():
    for i in range(len(rule_outputs)):
      output = rule_outputs[i]
      if isinstance(output, str):
        continue
      if len(output) <= 2:
        continue
      x = output[0]
      y = output[1]
      for z in output[2:]:
        new_rules.append((new_rule_id, [y, z]))
        y = new_rule_id
        new_rule_id += 1
      rule_outputs[i] = [x, y]
  print(new_rules)
  for rule_id, rule_output in new_rules:
    rules[rule_id] = [rule_output]
  print(sorted(rules.items()))
  return rules


def count_matched(rules, words):
  rules = normalize_rules(rules)
  return sum(map(lambda word: match(rules, word), words))


def count_matched2(rules, words):
  @functools.lru_cache(None)
  def can_output(rule_id, word):
    def try_output(rule_output):
      if isinstance(rule_output, str):
        return word == rule_output
      elif len(rule_output) == 1:
        return can_output(rule_output[0], word)
      elif len(rule_output) == 2:
        return any([can_output(rule_output[0], word[:middle]) and can_output(rule_output[1], word[middle:]) for middle in range(1, len(word))])
      else:
        raise ValueError('Invalid output %s' % str(rule_output))

    return any(map(try_output, rules[rule_id]))

  rules = normalize_rules(rules)
  return sum(map(lambda word: can_output(0, word), words))



def main():
  a, b = sys.stdin.read().strip().split("\n\n")
  rules = {int(x): parse_rule_outputs(y) for x, y in map(lambda s: s.split(': '), a.split('\n'))}
  words = b.split('\n')

  print(count_matched(rules, words))

  rules[8] = parse_rule_outputs('42 | 42 8')
  rules[11] = parse_rule_outputs('42 31 | 42 11 31')
  print(count_matched(rules, words))



if __name__ == "__main__":
  main()

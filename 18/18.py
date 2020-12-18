#!/usr/bin/env python3

import sys
import re
import itertools


class Parser:
  def __init__(self, ops):
    self._ops = ops
    self._s = None
    self._i = None
  
  def _skip_spaces(self):
    while self._i < len(self._s) and self._s[self._i] == ' ':
      self._i += 1

  def _cur_lexem(self):
    self._skip_spaces()
    if self._i < len(self._s):
      return self._s[self._i]
    else:
      return None

  def _skip_lexem(self, exp_lex):
    lex = self._cur_lexem()
    if lex != exp_lex:
      raise ValueError()
    self._i += 1

  def _apply(self, op, val1, val2):
    if op == '+':
      return val1 + val2
    elif op == '*':
      return val1 * val2
    else:
      raise ValueError()

  def _calc_one(self):
    lex = self._cur_lexem()
    if lex == '(':
      self._i += 1
      val = self._calc_many()
      self._skip_lexem(')')
      return val
    elif '0' <= lex <= '9':
      self._i += 1
      val = int(lex)
      return val
    else:
      raise ValueError()

  def _calc_many(self, cur_priority = 0):
    if cur_priority >= len(self._ops):
      return self._calc_one()
    val = self._calc_many(cur_priority + 1)
    while True:
      lex = self._cur_lexem()
      if lex not in self._ops[cur_priority]:
        return val
      op = lex
      self._i += 1

      cur_val = self._calc_many(cur_priority + 1)
      val = self._apply(op, val, cur_val)

  def calc_expr(self, s):
    self._s = s
    self._i = 0
    return self._calc_many()

def calc1(s):
  return Parser([['+', '*']]).calc_expr(s)

def calc2(s):
  return Parser([['*'], ['+']]).calc_expr(s)

def solve(exprs, calc):
  vals = list(map(calc, exprs))
  print(vals)
  print(sum(vals))

def main():
  exprs = sys.stdin.read().strip().split("\n")
  solve(exprs, calc1)
  solve(exprs, calc2)

if __name__ == "__main__":
  main()

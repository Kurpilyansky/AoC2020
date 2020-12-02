import sys

def parse_line(line):
  a, b, c = line.strip().split()
  L, R = map(int, a.split('-'))
  return L, R, b[0], c


def is_good1(L, R, ch, psw):
  return L <= psw.count(ch) <= R


def is_good2(L, R, ch, psw):
  return (psw[L - 1] == ch) != (psw[R - 1] == ch)


queries = list(map(parse_line, sys.stdin))
print(sum([is_good1(*q) for q in queries]))
print(sum([is_good2(*q) for q in queries]))


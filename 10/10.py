import sys
import re


def is_good(v, x):
  for i in range(len(v)):
    for j in range(i):
      if v[i] + v[j] == x:
        return True
  return False


a = list(map(int, sys.stdin.read().strip().split('\n')))
a.sort()
a = [0] + a + [a[-1] + 3]

diff1 = 0
diff3 = 0
for i in range(1, len(a)):
  if a[i] - a[i - 1] == 1:
    diff1 += 1
  elif a[i] - a[i - 1] == 3:
    diff3 += 1
  else:
    raise ValueError()
print(diff1, diff3)
print(diff1 * diff3)

dp = [1]
for i in range(1, len(a)):
  cur = 0
  for j in range(1, i + 1):
    if a[i - j] >= a[i] - 3:
      cur += dp[i - j]
  dp.append(cur)
print(a)
print(dp)
print(dp[-1])

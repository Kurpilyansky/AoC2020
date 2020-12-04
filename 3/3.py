import sys

def find(a, dx, dy):
  n = len(a)
  m = len(a[0])
  x, y = 0, 0
  res = 0
  while x < n:
    if a[x][y % m] == '#':
      res += 1
    x += dx
    y += dy
  return res

a = list(map(lambda x: x.strip(), sys.stdin))

print(find(a, 1, 3))

res = 1
for dx, dy in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
  res *= find(a, dx, dy)
print(res)


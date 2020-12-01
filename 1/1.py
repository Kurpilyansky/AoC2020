import sys

a = list(map(int, sys.stdin))

for i in range(len(a)):
  for j in range(i):
    if a[i] + a[j] == 2020:
      print(a[i] * a[j])

for i in range(len(a)):
  for j in range(i):
    for k in range(j):
      if a[i] + a[j] + a[k] == 2020:
        print(a[i] * a[j] * a[k])

#!/usr/bin/env python3

import sys
import re

lines = sys.stdin.read().strip().split('\n')
nums = list(map(int, lines[0].split(',')))

last = dict()
for i in range(len(nums)):
  if nums[i] not in last:
    last[nums[i]] = []
  last[nums[i]].append(i)

z = int(sys.argv[1])
while len(nums) < z:
  x = nums[-1]
  if len(last[x]) == 1:
    y = 0
  else:
    y = last[x][-1] - last[x][-2]
  if y not in last:
    last[y] = []
  last[y].append(len(nums))
  nums.append(y)

print(nums[-1])


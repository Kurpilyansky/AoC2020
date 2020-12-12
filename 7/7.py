import sys
import re


def parse():
  lines = sys.stdin.read().strip().split('\n')

  res = dict()
  for line in lines:
    x, y = line.strip('.').split(' contain ')
    z = y.split(', ')
    tt = []
    for v in z:
      if v == 'no other bags':
        continue
      m = re.match(r'^(\d+) (.+ bag)s?$', v)
      tt.append((int(m.group(1)), m.group(2)))
    res[x[:-1]] = tt
  return res


bags = parse()

out = dict()
for x, y in bags.items():
  for z in y:
    if z[1] not in out:
      out[z[1]] = list()
    out[z[1]].append(x)

q = list()
used = set()
q.append('shiny gold bag')
while q:
  v = q.pop()
  for u in out.get(v, list()):
    if u not in used:
      used.add(u)
      q.append(u)

print(len(used))

def dfs(v, ed, cnt):
#  if v in cnt:
#    return cnt[v]
  cnt[v] = 0
  for x, u in ed[v]:
    cnt[v] += x * (dfs(u, ed, cnt) + 1)
  return cnt[v]

print(dfs('shiny gold bag', bags, dict()))

import sys

n = int(sys.argv[1])
deg = int(sys.argv[2])
names = []
names.append('shiny gold')
for i in range(n - 1):
  name = chr(ord('a') + i % 26) + chr(ord('a') + i // 26)
  names.append('%s %s' % (name, name))

for i in range(n):
  ins = []
  for j in range(deg):
    if i + j + 1 < n:
      ins.append('1 %s bag' % names[i + j + 1])

  if not ins:
    ins = ['no other bags']
  print('%s bags contain %s.' % (names[i], ', '.join(ins)))
    


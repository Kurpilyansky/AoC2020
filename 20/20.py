#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy

def parse_tile(s):
  lines = s.split('\n')
  return int(lines[0].strip(':').split()[1]), lines[1:]

def get_borders_raw(tile):
  yield tile[0]
  yield ''.join(map(lambda x: x[0], tile))
  yield tile[-1]
  yield ''.join(map(lambda x: x[-1], tile))

def get_borders(tile):
  for i, border in enumerate(get_borders_raw(tile)):
    if border > border[::-1]:
      yield -(i + 1), border[::-1]
    else:
      yield (i + 1), border

def main():
  blocks = sys.stdin.read().strip().split("\n\n")
  tiles = {num: a for num, a in map(parse_tile, blocks)}

  borders = dict()
  for num, tile in tiles.items():
    for i, border in get_borders(tile):
      if border > border[::-1]:
        borders.setdefault(border[::-1], []).append((num, i))
      else:
        borders.setdefault(border, []).append((num, i))
#      borders.setdefault(border[::-1], []).append((num, -(i + 1)))
  print(borders)
  print(max(map(len, borders.values())))

  """
  print(3079, list(get_borders(tiles[3079])))
  print(2311, list(get_borders(tiles[2311])))
  for border in get_borders(tiles[3079]):
    print(borders[border])
  """

  cnt = dict()
  for border, x in borders.items():
    if len(x) == 1:
#    if len(set(map(lambda y: y[0], x))) == 1:
      cnt[x[0][0]] = cnt.get(x[0][0], 0) + 1
  corners = [x for x, y in cnt.items() if y == 2]
  print(corners)
  print(functools.reduce(lambda x, y: x * y, corners))

  n = int(len(tiles) ** 0.5)
  k = len(tiles[corners[0]][0]) - 2
  kk = len(tiles[corners[0]][0])
  a = [[None] * n for i in range(n)]
  b = [[' '] * (n * k) for i in range(n * k)]

  def rotate90(num):
    kk = len(tiles[num])
    tmp = [[' '] * kk for i in range(kk)]
    for x in range(kk):
      for y in range(kk):
        tmp[x][y] = tiles[num][y][kk - 1 - x]
    tiles[num] = [''.join(s) for s in tmp]

  def flip_vert(num):
    kk = len(tiles[num])
    tmp = [[' '] * kk for i in range(kk)]
    for x in range(kk):
      for y in range(kk):
        tmp[x][y] = tiles[num][x][kk - 1 - y]
    tiles[num] = [''.join(s) for s in tmp]

  def flip_sym(num):
    kk = len(tiles[num])
    tmp = [[' '] * kk for i in range(kk)]
    for x in range(kk):
      for y in range(kk):
        tmp[x][y] = tiles[num][y][x]
    tiles[num] = [''.join(s) for s in tmp]

  def put(x, y, num):
    print('put', x, y, num)
    a[x][y] = num
    for i in range(k):
      for j in range(k):
        b[x * k + i][y * k + j] = tiles[num][i + (kk - k) // 2][j + (kk - k) // 2]


  def try_all(num, func):
    for _1 in range(1):
      flip_sym(num)
      for _2 in range(2):
        flip_vert(num)
        for _3 in range(4):
          rotate90(num)
          if func():
            return

  def find(x, y, num, zn, bb, sign):
    def func():
      bs = list(get_borders(tiles[num]))
      print(bs)
      if bs[zn][1] == bb and bs[zn][0] * sign > 0:
        print('\n'.join(tiles[num]))
        put(x, y, num)
        return True
    try_all(num, func)

             

  rot = 0
  while True:
    bs = list(get_borders(tiles[corners[0]]))
    if len(borders[bs[0][1]]) == 1 and len(borders[bs[1][1]]) == 1:
      break

    rotate90(corners[0])
  put(0, 0, corners[0])

  for x in range(n):
    for y in range(n):
      print('\n'.join(map(lambda x: ''.join(x), b)))
      cnum = a[x][y]
      bs = list(get_borders(tiles[cnum]))
      print(cnum, bs)
      for _, bb in bs:
        print(borders[bb])
      if y + 1 < n:
        bnum = list([num for num, _ in borders[bs[3][1]] if num != cnum])[0]
        find(x, y + 1, bnum, 1, bs[3][1], bs[3][0])
      if x + 1 < n:
        bnum = list([num for num, _ in borders[bs[2][1]] if num != cnum])[0]
        find(x + 1, y, bnum, 0, bs[2][1], bs[2][0])


  def find_monsters(ans):
    mask = ['                  # ',
            '#    ##    ##    ###',
            ' #  #  #  #  #  #   ']
    ZZZ = 999999

    def func():
      for x in range(n * k - len(mask)):
        for y in range(n * k - len(mask[0])):
          ok = True
          for dx in range(len(mask)):
            for dy in range(len(mask[0])):
              if mask[dx][dy] == '#' and tiles[ZZZ][x + dx][y + dy] == '.':
                ok = False
          if ok:
            for dx in range(len(mask)):
              for dy in range(len(mask[0])):
                if mask[dx][dy] == '#':
                  s = [ch for ch in tiles[ZZZ][x + dx]]
                  s[y + dy] = 'O'
                  tiles[ZZZ][x + dx] = ''.join(s)
            print(x, y)
            ans[0] += 1

    tiles[ZZZ] = b
    try_all(ZZZ, func)

  ans = [0]
  find_monsters(ans)
  print(ans)
  print('\n'.join(map(lambda x: ''.join(x), b)))
  print(sum(map(lambda s: ''.join(s).count('#'), b)))

if __name__ == "__main__":
  main()

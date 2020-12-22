#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy


def parse_player(s):
  lines = s.strip().split('\n')
  return list(map(int, lines[1:]))


def score(player):
  res = 0
  for i in range(1, len(player) + 1):
    res += i * player[-i]
  return res

game_ids = 0

def recursive_score(players):
  global game_ids
  game_ids += 1
  game_id = game_ids
  used = set()

  round_id = 1
  while players[0] and players[1]:
#    print("Game #%d Round %d: %s vs %s" % (game_id, round_id, str(players[0]), str(players[1])))

    key = tuple(map(tuple, players))
    if key in used:
      return 0, score(players[0])
    used.add(key)

    if players[0][0] <= len(players[0]) - 1 and players[1][0] <= len(players[1]) - 1:
      winner = recursive_score(list([list(players[0][1:][:players[0][0]]), list(players[1][1:][:players[1][0]])]))[0]
    else:
      winner = 0 if players[0][0] > players[1][0] else 1

    if winner == 0:
      players[0].append(players[0][0])
      players[0].append(players[1][0])
    else:
      players[1].append(players[1][0])
      players[1].append(players[0][0])
    players[0] = players[0][1:]
    players[1] = players[1][1:]

    round_id += 1
  if players[0]:
    return 0, score(players[0])
  else:
    return 1, score(players[1])


def main():
  blocks = sys.stdin.read().strip().split("\n\n")
  players = list(map(parse_player, blocks))

  while players[0] and players[1]:
    if players[0][0] > players[1][0]:
      players[0].append(players[0][0])
      players[0].append(players[1][0])
    else:
      players[1].append(players[1][0])
      players[1].append(players[0][0])
    players[0] = players[0][1:]
    players[1] = players[1][1:]

  print(score(players[0]) + score(players[1]))
  


  players = list(map(parse_player, blocks))
  print(recursive_score(players)[1])

if __name__ == "__main__":
  main()

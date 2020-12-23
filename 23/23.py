#!/usr/bin/env python3

import sys
import re
import functools
import itertools
import copy


def next1(s):
  cur = int(s[0]) - 1
  t = s[1:4]
  s = s[:1] + s[4:]
  while str(cur) not in s:
    cur = (cur - 1) % 10
  index = 0
  while s[index] != str(cur):
    index += 1
  s = s[:index+1] + t + s[index+1:]
  s = s[1:] + s[:1]
  return s

def part1(s, iters):
  for i in range(iters):
    s = next1(s)
  while s[0] != '1':
    s = s[1:] + s[:1]
  print(''.join(s[1:]))

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class List:
  def __init__(self, nodes):
    self.head = nodes[0]
    self.head.next = self.head
    self.head.prev = self.head
    for node in nodes[1:]:
      self.add_after(self.head.prev, node)

  def add_after(self, after_node, new_node):
    new_node.prev = after_node
    new_node.next = after_node.next
    new_node.prev.next = new_node
    new_node.next.prev = new_node

  def remove_second(self):
    node = self.head.next
    self.head.next = node.next
    self.head.next.prev = self.head
    node.prev = None
    node.next = None
    return node

  def rotate(self):
    self.head = self.head.next

  def dump(self):
    v = [self.head.data]
    node = self.head.next
    while node.data != v[0]:
      v.append(node.data)
      node = node.next
    print(v)
    

def part2(s, iters, COUNT):
  vals = list(list(map(int, list(s))) + list(range(len(s) + 1, COUNT + 1)))
  nodes = [Node(x) for x in vals]
  arr = List(nodes)
  nodes = {node.data: node for node in nodes}
  for i in range(iters):
    if i % 100000 == 0:
      print(i)
    dest = (arr.head.data - 2) % COUNT + 1
    arr2 = []
    for j in range(3):
      arr2.append(arr.remove_second())
    removed = set(map(lambda x: x.data, arr2))
    while dest in removed:
      dest = (dest - 2) % COUNT + 1
    for node in arr2[::-1]:
      arr.add_after(nodes[dest], node)
    arr.rotate()

    #arr.dump()
  while arr.head.data != 1:
    arr.rotate()
  x = 1
  for i in range(2):
    y = arr.remove_second().data
    print(y)
    x *= y
  print(x)


def main():
  s = list(sys.stdin.read().strip())
  iters = int(sys.argv[1])
#part1(s, iters)
  part2(s, iters, int(sys.argv[2]))

if __name__ == "__main__":
  main()

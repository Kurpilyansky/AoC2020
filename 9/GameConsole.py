#!/usr/bin/env python3

import sys

class HaltException(Exception):
  pass


class NoInputException(Exception):
  pass


class CycleFoundException(Exception):
  def __init__(self, acc):
    self.acc = acc


class CodeError(Exception):
  pass


class Argument:
  def __init__(self, prog, addr, mode):
    self._prog = prog
    self._addr = addr
    self._mode = mode

  def pos(self):
    if self._mode == 0:
      return self._prog.data(self._addr)
    elif self._mode == 2:
      return self._prog.data(self._addr) + self._prog.rel_base()
    else:
      raise CodeError("Unexpected mode %d" % self._mode)

  def val(self):
    if self._mode == 0:
      return self._prog.data(self._prog.data(self._addr))
    elif self._mode == 1:
      return self._prog.data(self._addr)
    elif self._mode == 2:
      return self._prog.data(self._prog.data(self._addr) + self._prog.rel_base())
    else:
      raise CodeError("Unexpected mode %d" % self._mode)

  def __repr__(self):
    return '(addr %d mode %d)' % (self._addr, self._mode)
    #return '(addr %d mode %d pos %d val %d)' % (self._addr, self._mode, self.pos(), self.val())

class Program:
  def __init__(self, code, inputs=None, verbose=False, cycle_diagnostic=False):
    #self._data = dict({i: data[i] for i in range(len(data))})
    self._code = code
    self._ip = 0
    self._acc = 0
    self._inputs = inputs
    self._outputs = []
    self._verbose = verbose
    self._is_halted = False
    self._visit = set() if cycle_diagnostic else None

  def is_halted(self):
    return self._is_halted

  def put_input(self, val):
    self._inputs.append(val)

  def run(self):
    try:
      while True:
        self._do()
    except HaltException as e:
      res = self._outputs
      self._outputs = []
      self._is_halted = True
      return self._acc
    except NoInputException as e:
      res = self._outputs
      self._outputs = []
      return self._acc

  def command(self, addr):
    if addr < 0:
      raise CodeError('addr %d' % addr)
    line = self._code[addr]
    op = line[0]
    args = list(map(int, line[1:]))
    return op, args

  def data(self, addr):
    if addr < 0:
      raise CodeError('addr %d' % addr)
    return self._data.get(addr, 0)

  def write_data(self, addr, value):
    if addr < 0:
      raise CodeError('addr %d' % addr)
    self._data[addr] = value

  def _do(self):
    if self._ip == len(self._code):
      raise HaltException()
    if self._ip < 0 or self._ip > len(self._code):
      raise CodeError('Bad ip %d' % self._ip)
    if self._visit is not None:
      if self._ip in self._visit:
        raise CycleFoundException(self._acc)
      self._visit.add(self._ip)

    op, args = self.command(self._ip)
    if op == "acc":
      self._apply(op, args, lambda args: self._acc_plus(*args))
    elif op == "jmp":
      self._apply(op, args, lambda args: self._jmp(*args))
    elif op == "nop":
      self._apply(op, args, lambda args: self._nop(*args))
    else:
      raise CodeError("Unknown op %d" % op)

  def _apply(self, op, args, func):
    if self._verbose:
      print(self._ip, op, args)
    if func(args) is None:
      self._ip += 1

  def _acc_plus(self, arg):
    self._acc += arg

  def _jmp(self, arg):
    self._ip += arg
    return True

  def _nop(self, arg):
    pass

  def _input(self, index):
    if self._inputs is None:
      self.write_data(index.pos(), int(input()))
    else:
      if self._inputs:
        self.write_data(index.pos(), self._inputs[0])
        self._inputs = self._inputs[1:]
      else:
        raise NoInputException()
  
  def _output(self, val):
    self._outputs.append(val.val())
    if self._verbose:
      print('output %d' % self._outputs[-1])


def parse_prog_code(filename):
  with open(sys.argv[1]) as f:
    lines = f.read().strip().split('\n')
    code = []
    for line in lines:
      tokens = line.split()
      code.append(tokens)
    return code


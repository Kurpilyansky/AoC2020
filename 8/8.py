import sys
import re
from GameConsole import * 


code = parse_prog_code(sys.argv[1])

try:
  prog = Program(code, cycle_diagnostic=True)
  prog.run()
except CycleFoundException as e:
  print(e.acc)


def run(code):
  try:
    prog = Program(code, cycle_diagnostic=True)
    return prog.run()
  except:
    return


for i in range(len(code)):
  if code[i][0] == "jmp":
    code[i][0] = "nop"
    res = run(code)
    if res is not None:
      print(res)
    code[i][0] = "jmp"

  if code[i][0] == "nop":
    code[i][0] = "jmp"
    res = run(code)
    if res is not None:
      print(res)
    code[i][0] = "nop"



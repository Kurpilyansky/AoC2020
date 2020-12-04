import sys
import re

def split_by_empty_line(lines):
  SEPARATOR = '@_@'
  text = ' '.join([SEPARATOR if not line else line for line in lines])
  return [s for s in text.strip().split(SEPARATOR)]

def parse_passport(s):
  fields = [x.split(':') for x in s.strip().split()]
  return dict({name: val for name, val in fields})

def parse():
  lines = list(map(lambda x: x.strip(), sys.stdin))
  blocks = split_by_empty_line(lines)
  return list(map(parse_passport, blocks))


def valid_field1(name, val):
  return val is not None


def valid_field2(name, val):
  if not valid_field1(name, val):
    return False
  if name == "byr":
    return 1920 <= int(val) and int(val) <= 2002
  if name == "iyr":
    return 2010 <= int(val) and int(val) <= 2020
  if name == "eyr":
    return 2020 <= int(val) and int(val) <= 2030
  if name == "hgt":
    if val[-2:] == 'cm':
      return 150 <= int(val[:-2]) and int(val[:-2]) <= 193
    elif val[-2:] == 'in':
      return 59 <= int(val[:-2]) and int(val[:-2]) <= 76
    else:
      return False
  if name == "hcl":
    return re.match(r'^#[0-9a-f]{6}$', val)
  if name == "ecl":
    return val in 'amb blu brn gry grn hzl oth'.split()
  if name == 'pid':
    return re.match(r'^[0-9]{9}$', val)
  if name == 'cid':
    return True
  print(name, val)
  raise ValueError(name + ' ' + val)


required_names = ['byr', 'iyr', 'eyr', 'hgt', 'ecl', 'hcl', 'pid']
def find_valid_passport_count(passports, valid_field):
  def valid_passport(passport):
    return sum(map(lambda name: not valid_field(name, passport.get(name, None)), required_names)) == 0
  return sum(map(valid_passport, passports))

passports = parse()
print(find_valid_passport_count(passports, valid_field1))
print(find_valid_passport_count(passports, valid_field2))


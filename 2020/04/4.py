#!/usr/bin/env python3
import re

from math import prod

def read_input(filepath):
    def passport_fields(passport):
        passport_obj = {}
        for field in passport:
            k, v = field.split(':')
            passport_obj.update({k: v})
        return passport_obj

    with open(filepath) as f:
        content = f.read()

    passports = content.rstrip().split('\n\n')
    for i, passport in enumerate(passports):
        passports[i] =  passport_fields(
            passport.replace(' ', '\n').split('\n')
        )

    return passports


def validate_byr(yr):
    return 1920 <= int(yr) <= 2002


def validate_iyr(yr):
    return 2010 <= int(yr) <= 2020


def validate_eyr(yr):
    return 2020 <= int(yr) <= 2030


def validate_hgt(hgt):
    _hgt = re.search(r'^(\d+)(cm|in)$', hgt)
    if not _hgt:
        return False
    if _hgt[2] == 'cm' and not 150 <= int(_hgt[1]) <= 193:
        return False
    if _hgt[2] == 'in' and not 59 <= int(_hgt[1]) <= 76:
        return False
    return True


def validate_hcl(hcl):
    return re.search(r'^#([a-f]|[0-9]){6}$', hcl)


def validate_ecl(ecl):
    return re.search(r'^(amb|blu|brn|gry|grn|hzl|oth)$', ecl)


def validate_pid(pid):
    return re.search(r'^\d{9}$', pid)


def part1(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid'
    try:
        for key in required_fields:
            passport[key]
    except KeyError:
        return False
    return True


def part2(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid'
    try:
        if not all([
                    validate_byr(passport['byr']),
                    validate_iyr(passport['iyr']),
                    validate_eyr(passport['eyr']),
                    validate_hgt(passport['hgt']),
                    validate_hcl(passport['hcl']),
                    validate_ecl(passport['ecl']),
                    validate_pid(passport['pid'])
                ]):
            return False
    except KeyError:
        return False
    return True


assert(validate_byr(2002))
assert(not validate_byr(2003))
assert(validate_hgt('60in'))
assert(validate_hgt('190cm'))
assert(not validate_hgt('190'))
assert(not validate_hgt('190in'))
assert(validate_hcl('#123abc'))
assert(not validate_hcl('#123abz'))
assert(not validate_hcl('123abc'))
assert(validate_ecl('brn'))
assert(not validate_ecl('wat'))
assert(validate_pid('000000001'))
assert(not validate_pid('0123456789'))

passports = read_input('input.txt')
# passports = read_input('example.txt')

part1 = len(list(filter(part1, passports)))
part2 = len(list(filter(part2, passports)))

print(f"PART 1: {part1}")
print(f"PART 2: {part2}")

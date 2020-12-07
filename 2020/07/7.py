#!/usr/bin/env python3

def parse_input(filepath):
    with open(filepath) as f:
        c = f.read().rstrip()

    rules = {}
    for rule in c.splitlines():
        bag_name, bag_rules = rule.split(" contain ")
        bag_rules = bag_rules.rstrip('.').split(', ')

        try:
            bag_rules.remove('no other bags')
        except ValueError:
            pass

        rules[bag_name.rstrip(' ')] = bag_rules

    return rules


# TODO: this takes 10 seconds and can be optimized
def find_parents(bag_name, rules):
    bag_name = bag_name.rstrip('s')
    parents = []
    for k, v in rules.items():
        for i in v:
            if bag_name in i:
                parents.append(k)
    if parents:
        for parent in parents:
            parents.extend(find_parents(parent, rules))
    return parents


def count_bags(bag_name, rules):
    if not bag_name.endswith('s'):
        bag_name += 's'

    count = 0
    for i in rules[bag_name]:
        _split = i.split(' ')
        qt, bag = int(_split[0]), " ".join(_split[1:])
        count += (qt * count_bags(bag, rules))
    count += 1

    return count


rules = parse_input('input.txt')
# rules = parse_input('example.txt')

print("PART 1: " + str(len(set(find_parents('shiny gold bag', rules)))))
print("PART 2: " + str(count_bags('shiny gold bag', rules) - 1))

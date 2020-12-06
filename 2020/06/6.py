#!/usr/bin/env python3

ANSWER_PART1 = 6587
ANSWER_PART2 = 3235

def read_input(filepath):
    """Returns nested lists with the following levels
       - group
       - person
       - answers
    """
    def parse_group(group):
        return list(map(list, group.split('\n')))

    with open(filepath) as f:
        content = f.read().rstrip()

    groups = content.split('\n\n')
    return [parse_group(g) for g in groups]
     

def flatten_list(l):
    flat_list=[]
    for i in l:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
            continue
        flat_list.append(i)
    return flat_list


def part1(filepath):
    with open(filepath) as f:
        content = f.read().rstrip()

    return sum(
        len(
            set(list(p.replace('\n', '')))
        ) for p in content.split('\n\n')
    )


def part2(filepath):
    groups = read_input(filepath)

    count = 0
    for group in groups:
        size = len(group)
        answers = flatten_list(group)
        for a in set(answers):
            if size == answers.count(a):
                count += 1
    return count


print(f"PART 1: {part1('input.txt')}")
print(f"PART 2: {part2('input.txt')}")

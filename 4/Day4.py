
import sys


def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    parsed_input = []
    for line in text:
        range_a, range_b = line.split(',')
        lower_a, upper_a = range_a.split('-')
        lower_b, upper_b = range_b.split('-')

        parsed_input.append( ( (int(lower_a), int(upper_a)),
                               (int(lower_b), int(upper_b))
                             ) )

    print(f"Input parsed")
    return parsed_input

def part1_criteria(tuple_list):
    set_l = set(range(tuple_list[0][0], tuple_list[0][1]+1))
    set_r = set(range(tuple_list[1][0], tuple_list[1][1]+1))

    if set_l.issuperset(set_r) or set_r.issuperset(set_l):
        return 1
    else:
        return 0

def part1(parsed_input):
    
    return sum(map(part1_criteria, parsed_input))

def part2_criteria(tuple_list):
    set_l = set(range(tuple_list[0][0], tuple_list[0][1]+1))
    set_r = set(range(tuple_list[1][0], tuple_list[1][1]+1))

    if len(set_l.intersection(set_r)) != 0:
        return 1
    else:
        return 0

def part2(parsed_input):

    return sum(map(part2_criteria, parsed_input))

def main(args):

    #parsed_input = parse_input("test_input.txt")
    parsed_input = parse_input()
    part1_solution = part1(parsed_input)
    print(f"Part 1 Solution:\t{part1_solution}")

    part2_solution = part2(parsed_input)
    print(f"Part 2 Solution:\t{part2_solution}")

    print(f"Done!")

if __name__ == "__main__":
    main(sys.argv)
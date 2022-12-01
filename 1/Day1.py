
import sys

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    parsed_input = []

    cur = []
    for line in text:
        if line == '':
            parsed_input.append(cur)
            cur = []
            continue
        cur.append(int(line))

    print(f"Input parsed")
    return parsed_input

def part1(parsed_input):

    # Find the element that has the highest sum, and report that sum
    cur_max_sum = 0
    for elf in parsed_input:
        cur_sum = sum(elf)
        if cur_sum > cur_max_sum:
            cur_max_sum = cur_sum

    return cur_max_sum

def part2(parsed_input):

    # Find the three elves with the highest sum, return the sum of their sums

    # Dumb solution, just redo part 1 keeping track of three sums instead
    cur_max_sum = 0
    cur_sub_max_sum = 0
    cur_sub_sub_max_sum = 0
    for elf in parsed_input:
        cur_sum = sum(elf)
        if cur_sum > cur_max_sum:
            cur_sub_sub_max_sum = cur_sub_max_sum
            cur_sub_max_sum = cur_max_sum
            cur_max_sum = cur_sum
        elif cur_max_sum > cur_sum > cur_sub_max_sum:
            cur_sub_sub_max_sum = cur_sub_max_sum
            cur_sub_max_sum = cur_sum
        elif cur_sub_max_sum > cur_sum > cur_sub_sub_max_sum:
            cur_sub_sub_max_sum = cur_sum

    return cur_max_sum + cur_sub_max_sum + cur_sub_sub_max_sum


def main(args):

    parsed_input = parse_input()
    part1_solution = part1(parsed_input)
    print(f"Part 1 Solution:\t{part1_solution}")

    part2_solution = part2(parsed_input)
    print(f"Part 2 Solution:\t{part2_solution}")

    print(f"Done!")

if __name__ == "__main__":
    main(sys.argv)
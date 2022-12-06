
import sys

def item_to_priority(item):

    priority = None
    if 'a' <= item <= 'z':
        priority = ord(item) - ord('a') + 1
    elif 'A' <= item <= 'Z':
        priority = ord(item) - ord('A') + 27 
    else:
        priority = None

    return priority

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    parsed_input = []
    for line in text:
        split_line = (line[:int(len(line)/2)], line[int(len(line)/2):])
        parsed_input.append(split_line)

    print(f"Input parsed")
    return parsed_input

def part1(parsed_input):

    priority_accum = 0
    for line in parsed_input: 
        compart_a, compart_b = line

        # Find intersection
        intersection = [item for item in set(compart_a) if item in set(compart_b)]
        if len(intersection) == 1:
            priority_accum += item_to_priority(intersection[0])
        else:
            print(f"Found malformed intersection! {intersection}")

    return priority_accum


def part2(parsed_input):
    priority_accum = 0
    for idx in range(int(len(parsed_input)/3)): 
        elf_a = parsed_input[3*idx  ][0] + parsed_input[3*idx  ][1]
        elf_b = parsed_input[3*idx+1][0] + parsed_input[3*idx+1][1]
        elf_c = parsed_input[3*idx+2][0] + parsed_input[3*idx+2][1]

        # Find intersection
        intersection = [item for item in set(elf_a) if item in set(elf_b) and item in set(elf_c)]
        if len(intersection) == 1:
            priority_accum += item_to_priority(intersection[0])
        else:
            print(f"Found malformed intersection! {intersection}")

    return priority_accum

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
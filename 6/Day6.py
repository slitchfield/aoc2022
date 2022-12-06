
import sys

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    parsed_input = text[0] # Input is single string, so just grab first line

    print(f"Input parsed")

    return parsed_input

def part1(parsed_input):

    for idx in range(len(parsed_input) - 4):
        # Create a set out of the 4 chars, and check that size == 4
        test_list = parsed_input[idx:idx+4]
        test_set  = set(test_list)
        if len(test_set) == 4:
            break

    return idx + 4 # idx is start of marker, report how many chars are processed before marker recognized

def part2(parsed_input):
    for idx in range(len(parsed_input) - 14):
        # Create a set out of the 4 chars, and check that size == 4
        test_list = parsed_input[idx:idx+14]
        test_set  = set(test_list)
        if len(test_set) == 14:
            break

    return idx + 14 # idx is start of marker, report how many chars are processed before marker recognized

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
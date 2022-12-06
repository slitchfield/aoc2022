
import sys
from collections import deque
import re

class crate_stack:

    def __init__(self, stack_defn):

        # Get the number of stacks present
        last_line = stack_defn[-1]
        _, num_stacks = last_line.rsplit(' ', 1)
        self.num_stacks = int(num_stacks)

        # Get the current depth
        cur_depth = len(stack_defn) - 1

        # Build the list of empty stacks
        self.stack_list = []
        for i in range(self.num_stacks):
            self.stack_list.append(deque())

        # Populate the individual stacks, then reverse
        for line in stack_defn:

            # Find the populated elements
            indices = [i.start() for i in re.finditer("\[", line)]
            for idx in indices:
                stack_num = idx // 4 # Stacks are "[X] "
                item = line[idx+1]
                self.stack_list[stack_num].append(item)
        
        for stack in self.stack_list:
            stack.reverse()

def parse_moves(move_list):
    out_list = []
    for line in move_list:
        tokens = line.split()
        move = {
            'num': int(tokens[1]),
            'src': int(tokens[3]),
            'dst': int(tokens[5])
        }
        out_list.append(move)

    return out_list

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    stack_definition, move_list = (text[:text.index('')], text[text.index('')+1:])

    parsed_input = {}
    parsed_input['part1'] = crate_stack(stack_definition)
    parsed_input['part2'] = crate_stack(stack_definition)
    parsed_input['move_list'] = parse_moves(move_list)

    print(f"Input parsed")

    return parsed_input

def part1(parsed_input):
    # Implement all the moves, then read out string spelled by top letters of each stack
    stack = parsed_input['part1']
    moves = parsed_input['move_list']

    for move in moves:
        num = move['num']
        src = move['src'] - 1 # Account for 0-indexing of list of stacks
        dst = move['dst'] - 1

        for i in range(num):
            item = stack.stack_list[src].pop()
            stack.stack_list[dst].append(item)

    retstr = ""
    for i in range(stack.num_stacks):
        retstr += stack.stack_list[i].pop()

    return retstr

def part2(parsed_input):
    # Implement all the moves, then read out string spelled by top letters of each stack
    stack = parsed_input['part2']
    moves = parsed_input['move_list']

    for move in moves:
        num = move['num']
        src = move['src'] - 1 # Account for 0-indexing of list of stacks
        dst = move['dst'] - 1

        append_list = []
        for i in range(num):
            append_list.append(stack.stack_list[src].pop())

        append_list.reverse() 
        stack.stack_list[dst].extend(append_list)

    retstr = ""
    for i in range(stack.num_stacks):
        retstr += stack.stack_list[i].pop()

    return retstr

def main(args):

    parsed_input = parse_input("test_input.txt")
    #parsed_input = parse_input()
    part1_solution = part1(parsed_input)
    print(f"Part 1 Solution:\t{part1_solution}")

    part2_solution = part2(parsed_input)
    print(f"Part 2 Solution:\t{part2_solution}")

    print(f"Done!")

if __name__ == "__main__":
    main(sys.argv)
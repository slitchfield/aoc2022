
import sys

class round:

    def __init__(self):
        self.opp_move = "A"
        self.my_move = "X"

    def __init__(self, opp_move, unknown):
        self.opp_move = opp_move
        self.unknown = unknown
    
    def part1_score(self):
        self.my_move = self.unknown
        move_points = self.my_move_points[self.my_move]
        round_points = self.round_score[(self.opp_move, self.my_move)]
        return move_points + round_points
    
    def part2_score(self):
        self.my_move = self.derived_outcome[(self.opp_move, self.unknown)]
        move_points = self.my_move_points[self.my_move]
        round_points = self.round_score[(self.opp_move, self.my_move)]
        return move_points + round_points
    
    my_move_points = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    round_score = {
        ("A", "X"): 3,
        ("A", "Y"): 6,
        ("A", "Z"): 0,

        ("B", "X"): 0,
        ("B", "Y"): 3,
        ("B", "Z"): 6,
        
        ("C", "X"): 6,
        ("C", "Y"): 0,
        ("C", "Z"): 3,
    }

    derived_outcome = {
        ("A", "X"): "Z",
        ("A", "Y"): "X",
        ("A", "Z"): "Y",

        ("B", "X"): "X",
        ("B", "Y"): "Y",
        ("B", "Z"): "Z",
        
        ("C", "X"): "Y",
        ("C", "Y"): "Z",
        ("C", "Z"): "X",
    }

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    parsed_input = []
    for line in text:
        opp_move, my_move = line.split(" ")
        parsed_input.append(round(opp_move, my_move))

    print(f"Input parsed")
    return parsed_input

def part1(parsed_input):
    accumulated_score = 0
    for round in parsed_input:
        score = round.part1_score()
        accumulated_score += score

    return accumulated_score

def part2(parsed_input):
    accumulated_score = 0
    for round in parsed_input:
        score = round.part2_score()
        accumulated_score += score

    return accumulated_score

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
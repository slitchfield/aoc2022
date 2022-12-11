
import sys

class state:

    def __init__(self, instrs):
        self.cur_cycle = 1
        self.X = 1
        self.V = 0
        self.instr_ptr = 0
        self.program = instrs
        self.state = "NewInst"
        
        self.cur_pos = 0
        self.cur_line = ""
        self.crt = []

    def tick(self):

        if abs(self.X - self.cur_pos) < 2:
            self.cur_line += "#"
        else:
            self.cur_line += "."
        self.cur_pos += 1
        

        if self.state == "NewInst":
            cur_instr = self.program[self.instr_ptr]

            if cur_instr[0] == "noop":
                self.state = "NewInst"
                self.instr_ptr += 1
                self.cur_cycle += 1
                if self.instr_ptr >= len(self.program):
                    self.state = "Done"

            elif cur_instr[0] == "addx":
                self.state = "AddxWB"
                self.V = cur_instr[1]
                self.cur_cycle += 1

            else:
                print(f"Unimplemented instr: {cur_instr}")
                sys.exit(0)
            
        elif self.state == "AddxWB":
            self.state = "NewInst"
            self.instr_ptr += 1
            if self.instr_ptr >= len(self.program):
                self.state = "Done"

            self.X += self.V
            self.cur_cycle += 1

        elif self.state == "Done":
            pass

        else:
            print(f"Unimplemented state: {self.state}")
            sys.exit(0)

    def print_state(self):
        pass

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    parsed_input = []
    for line in text:
        tokens = line.split()
        if len(tokens) > 1:
            tokens[1] = int(tokens[1]) # Transofrm addx imm into an int

        parsed_input.append(tokens)

    part1_state = state(parsed_input)
    part2_state = state(parsed_input)

    parsed_input = (part1_state, part2_state)

    print(f"Input parsed")

    return parsed_input

def part1(parsed_input):

    sig_strength = 0
    while parsed_input.state != "Done":
        if (parsed_input.cur_cycle) == 20:
            print(f"20th cycle!")
            print(f"\t20 * {parsed_input.X} = {20 * parsed_input.X}")
            sig_strength += (parsed_input.X * 20)

        if (parsed_input.cur_cycle) == 60:
            print(f"60th cycle!")
            print(f"\t60 * {parsed_input.X} = {60 * parsed_input.X}")
            sig_strength += (parsed_input.X * 60)
        
        if (parsed_input.cur_cycle) == 100:
            print(f"100th cycle!")
            print(f"\t100 * {parsed_input.X} = {100 * parsed_input.X}")
            sig_strength += (parsed_input.X * 100)

        if (parsed_input.cur_cycle) == 140:
            print(f"140th cycle!")
            print(f"\t140 * {parsed_input.X} = {140 * parsed_input.X}")
            sig_strength += (parsed_input.X * 140)
        
        if (parsed_input.cur_cycle) == 180:
            print(f"180th cycle!")
            print(f"\t180 * {parsed_input.X} = {180 * parsed_input.X}")
            sig_strength += (parsed_input.X * 180)
        
        if (parsed_input.cur_cycle) == 220:
            print(f"220th cycle!")
            print(f"\t220 * {parsed_input.X} = {220 * parsed_input.X}")
            sig_strength += (parsed_input.X * 220)
        
        parsed_input.tick() 

    return sig_strength 
    
def part2(parsed_input):
    
    sig_strength = 0
    while parsed_input.state != "Done":
        if len(parsed_input.cur_line) == 40:
            parsed_input.crt.append(parsed_input.cur_line)
            parsed_input.cur_line = ""
            parsed_input.cur_pos = 0
        parsed_input.tick() 

    parsed_input.crt.append(parsed_input.cur_line)
    print("Final Soln:")
    for line in parsed_input.crt:
        print(f"\t{line}")
    return None

def main(args):

    #parsed_input = parse_input("test_input.txt")
    #parsed_input = parse_input("test_input_2.txt")
    parsed_input = parse_input()
    part1_solution = part1(parsed_input[0])
    print(f"Part 1 Solution:\t{part1_solution}")

    part2_solution = part2(parsed_input[1])
    print(f"Part 2 Solution:\t{part2_solution}")

    print(f"Done!")

if __name__ == "__main__":
    main(sys.argv)
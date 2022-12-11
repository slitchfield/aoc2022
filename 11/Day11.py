
import sys

class Monkey:

    def __init__(self, inputblock):
        id_line        = inputblock[0]
        item_line      = inputblock[1]
        op_line        = inputblock[2]
        predicate_line = inputblock[3]
        predtrue_line  = inputblock[4]
        predfalse_line = inputblock[5]

        id_token = id_line.split()[-1][:-1]
        self.id = int(id_token)

        item_tokens = item_line.split(':')[-1].split(", ")
        self.items = [int(item.lstrip().rstrip()) for item in item_tokens]

        self.operation = Monkey.parse_operation(op_line)
        self.nexttarget = Monkey.generate_predicate(predicate_line, predtrue_line, predfalse_line)
        self.test = int(predicate_line.split()[-1])
        self.num_inspected = 0

    def parse_operation(op_line):
        # Parse the operation line, and return a function to implement it

        op = op_line.split(": ")[-1]
        lh, rh = op.split(" = ")
        
        arg1, operation, arg2 = rh.split()
        if arg2 != "old":
            arg2 = int(arg2)

        def operation(old, operation=operation, arg2=arg2):
            arg1 = old
            if arg2 == "old":
                arg2 = old

            if operation == '+':
                return arg1 + arg2
            elif operation == '*':
                return arg1 * arg2

        return operation

    def generate_predicate(pred_str, true_str, false_str):
        divisor_check = int(pred_str.split()[-1])
        true_target = int(true_str.split()[-1])
        false_target = int(false_str.split()[-1])

        def pred(inval, div=divisor_check, iftrue=true_target, iffalse=false_target):
            if inval % div == 0:
                return iftrue
            else:
                return iffalse 
            
        return pred

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        raw_blocks = [block.rstrip() for block in inputfile.read().split("\n\n")]
        monkey_blocks = []
        for block in raw_blocks:
            new_block = [b.rstrip().lstrip() for b in block.splitlines()]
            monkey_blocks.append(new_block)

    part1_list = []
    part2_list = []
    for monkey_block in monkey_blocks:
        part1_list.append(Monkey(monkey_block))
        part2_list.append(Monkey(monkey_block))

    parsed_input = (part1_list, part2_list)

    print(f"Input parsed")

    return parsed_input

def part1(parsed_input):

    for round in range(20):
        print(f"Round {round}:")
        for monkey in parsed_input:
            print(f"\tMonkey {monkey.id}:")
            cur_item_list = monkey.items
            monkey.items = [] # Clear out the monkey's item list. We'll throw them all elsewhere
            for item in cur_item_list:
                print(f"\t\tMonkey inspects an item with worry level {item}")
                new_level = monkey.operation(item)
                print(f"\t\t\t{item}\t->\t{new_level}")
                div_level = new_level // 3
                print(f"\t\t\t{new_level}\t->\t{div_level}")
                new_target = monkey.nexttarget(div_level)
                print(f"\t\t\tNew target is Monkey {new_target}")
                print(f"\t\t\tThrowing item with worry level {div_level} to Monkey {new_target}")
                parsed_input[new_target].items.append(div_level)

                monkey.num_inspected += 1

        print(f"\tAfter round {round}:")
        for monkey in parsed_input:
            print(f"\t\tMonkey {monkey.id}: {monkey.items}")

    max1 = 0
    max2 = 0
    for monkey in parsed_input:
        num_inspected = monkey.num_inspected
        if num_inspected > max1:
            max2 = max1
            max1 = num_inspected
        elif num_inspected > max2:
            max2 = num_inspected

        print(f"Monkey {monkey.id} inspected items {monkey.num_inspected} times.")

    return max1*max2

# https://pastebin.com/ywSE4dZE
# https://theprogrammingexpert.com/python-least-common-multiple/
def lcm(lst):
    lcm_temp = max(lst)
    while True:
        if all(lcm_temp % x == 0 for x in lst):
            break
        lcm_temp = lcm_temp + 1
    return lcm_temp

def part2(parsed_input):

    tests = []
    for monkey in parsed_input:
        tests.append(monkey.test)

    modulo = lcm(tests)

    for round in range(10000):
        for monkey in parsed_input:
            #print(f"\tMonkey {monkey.id}:")
            cur_item_list = monkey.items
            monkey.items = [] # Clear out the monkey's item list. We'll throw them all elsewhere
            for item in cur_item_list:
                #print(f"\t\tMonkey inspects an item with worry level {item}")
                new_level = monkey.operation(item)
                #print(f"\t\t\t{item}\t->\t{new_level}")
                # To keep ints managable, modulo lcm 
                div_level = new_level % modulo 
                #print(f"\t\t\t{new_level}\t->\t{div_level}")
                new_target = monkey.nexttarget(div_level)
                #print(f"\t\t\tNew target is Monkey {new_target}")
                #print(f"\t\t\tThrowing item with worry level {div_level} to Monkey {new_target}")
                parsed_input[new_target].items.append(div_level)

                monkey.num_inspected += 1

        if round == 0:
            print(f"\tAfter round {round}:")
            for monkey in parsed_input:
                print(f"\t\tMonkey {monkey.id} has inspected {monkey.num_inspected} items") 
        if round == 19:
            print(f"\tAfter round {round}:")
            for monkey in parsed_input:
                print(f"\t\tMonkey {monkey.id} has inspected {monkey.num_inspected} items") 
        if ((round+1) % 1000) == 0:
            print(f"\tAfter round {round}:")
            for monkey in parsed_input:
                print(f"\t\tMonkey {monkey.id} has inspected {monkey.num_inspected} items")

    max1 = 0
    max2 = 0
    for monkey in parsed_input:
        num_inspected = monkey.num_inspected
        if num_inspected > max1:
            max2 = max1
            max1 = num_inspected
        elif num_inspected > max2:
            max2 = num_inspected

        print(f"Monkey {monkey.id} inspected items {monkey.num_inspected} times.")

    return max1*max2

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
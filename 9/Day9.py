
import sys

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    parsed_input = []
    for line in text:
        tokens = line.split()
        parsed_input.append((tokens[0], int(tokens[1]) ) )

    print(f"Input parsed")

    return parsed_input

def move_head(direction, headpos):

    if direction == 'R':
        headpos = (headpos[0] + 1, headpos[1]    )
    if direction == 'L':
        headpos = (headpos[0] - 1, headpos[1]    )
    if direction == 'U':
        headpos = (headpos[0]    , headpos[1] + 1)
    if direction == 'D':
        headpos = (headpos[0]    , headpos[1] - 1)

    return headpos

def move_tail(headpos, tailpos):

    dx = headpos[0] - tailpos[0]
    dy = headpos[1] - tailpos[1]

    moved = False
    newtailpos = tailpos

    # Head is right on top of tail
    if dx == 0 and dy == 0:
        newtailpos = tailpos
        moved = False

    # Only need to move L or R
    elif dy == 0:
        if dx > 1:
            newtailpos = (tailpos[0] + 1, tailpos[1])
            moved = True
        elif dx < -1:
            newtailpos = (tailpos[0] - 1, tailpos[1])
            moved = True

    # Only need to move U or D
    elif dx == 0:
        if dy > 1:
            newtailpos = (tailpos[0], tailpos[1] + 1)
            moved = True
        elif dy < -1:
            newtailpos = (tailpos[0], tailpos[1] - 1)
            moved = True

    # Case where head moved and we don't need to move
    elif abs(dx) == 1 and abs(dy) == 1:
        newtailpos = tailpos
        moved = False

    # Case where head is diagonal, and we need to follow    
    else:
        movex = 0
        if dx > 0:
            movex = 1
        elif dx < 0:
            movex = -1
        else:
            print(f"diag case but 0 dx??")
            sys.exit(0)
    
        movey = 0
        if dy > 0:
            movey = 1
        elif dy < 0:
            movey = -1
        else:
            print(f"diag case but 0 dy??")
            sys.exit(0)

        newtailpos = (tailpos[0] + movex, tailpos[1] + movey)
        moved = True

    return (newtailpos, moved)

def part1(parsed_input):
    
    headpos = (0, 0)
    tailpos = (0, 0)

    visited = {}
    visited[tailpos] = 1

    for move in parsed_input:

        direction = move[0]
        units = move[1]
        print(move)
        for i in range(units):

            headpos = move_head(direction, headpos)

            tailpos, moved = move_tail(headpos, tailpos)

            print(f"\t{i+1}")
            print(f"\t\tH: {headpos}")
            print(f"\t\tT: {tailpos}")

            if moved:
                if tailpos not in visited.keys():
                    visited[tailpos] = 0
                visited[tailpos] += 1

    return len(visited)

def dump_positions(knot_positions, radius = 20):

    row = "."*(2*radius+1)
    field = [row]*(2*radius + 1)

    s = (0, 0)
    sidx = (s[0]+radius, s[1]+radius)

    line = field[sidx[1]]
    field[sidx[1]] = line[:sidx[0]] + 's' + line[sidx[0]+1:]

    for pos_idx in range(len(knot_positions) - 1, -1, -1):
        pos = knot_positions[pos_idx]
        kidx = (radius + pos[0], radius - pos[1] )

        line = field[kidx[1]]
        if pos_idx != 0:
            field[kidx[1]] = line[:kidx[0]] + repr(pos_idx) + line[kidx[0]+1:]
        else:
            field[kidx[1]] = line[:kidx[0]] + "H" + line[kidx[0]+1:]

    return ''.join([line + '\n' for line in field])

def part2(parsed_input):

    knot_positions = [
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
        (0, 0),
    ]    

    visited = {}
    visited[(0, 0)] = 1

    #print(dump_positions(knot_positions))

    for move in parsed_input:

        direction = move[0]
        units = move[1]
        print(move)
        for i in range(units):

            knot_positions[0] = move_head(direction, knot_positions[0])

            for idx in range(1, len(knot_positions)):
                knot_positions[idx], moved = move_tail(knot_positions[idx-1], knot_positions[idx])

            print(f"\t{i+1}")
            print(f"\tNew H: {knot_positions[0]}")

            if moved:
                tailpos = knot_positions[-1]
                if tailpos not in visited.keys():
                    visited[tailpos] = 0
                visited[tailpos] += 1

            #print(dump_positions(knot_positions))

    return len(visited)
    pass

def main(args):

    #parsed_input = parse_input("test_input.txt")
    #parsed_input = parse_input("test_input_2.txt")
    parsed_input = parse_input()
    part1_solution = part1(parsed_input)
    print(f"Part 1 Solution:\t{part1_solution}")

    part2_solution = part2(parsed_input)
    print(f"Part 2 Solution:\t{part2_solution}")

    print(f"Done!")

if __name__ == "__main__":
    main(sys.argv)
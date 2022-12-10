
import sys

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    grid = []

    for line in text:
        grid.append([])
        for char in line:
            grid[-1].append({
                'height': int(char),
                'vN': False,
                'vE': False,
                'vS': False,
                'vW': False
            })

    rowmin = 0
    colmin = 0
    rowmax = len(grid) - 1
    colmax = len(grid[0]) - 1
    for row in range(len(grid)):
        for col in range(len(grid[0])):

            # Check north
            if row == rowmin:
                grid[row][col]['vN'] = True
            else:
                grid[row][col]['vN'] = True
                for checkrow in range(row - 1, -1, -1):
                    checkheight = grid[checkrow][col]['height']
                    if checkheight >= grid[row][col]['height']:
                        grid[row][col]['vN'] = False
                        break

            # Check South
            if row == rowmax:
                grid[row][col]['vS'] = True
            else:
                grid[row][col]['vS'] = True
                for checkrow in range(row + 1, len(grid)):
                    checkheight = grid[checkrow][col]['height']
                    if checkheight >= grid[row][col]['height']:
                        grid[row][col]['vS'] = False
                        break

            if col == colmin:
                grid[row][col]['vW'] = True
            else:
                grid[row][col]['vW'] = True
                for checkcol in range(col - 1, -1, -1):
                    checkheight = grid[row][checkcol]['height']
                    if checkheight >= grid[row][col]['height']:
                        grid[row][col]['vW'] = False
                        break

            if col == colmax:
                grid[row][col]['vE'] = True
            else:
                grid[row][col]['vE'] = True
                for checkcol in range(col + 1, len(grid[0])):
                    checkheight = grid[row][checkcol]['height']
                    if checkheight >= grid[row][col]['height']:
                        grid[row][col]['vE'] = False
                        break

    parsed_input = grid

    print(f"Input parsed")

    return parsed_input

def is_visible(grid_node):
    return grid_node['vN'] or grid_node['vS'] or grid_node['vE'] or grid_node['vW']

def part1(parsed_input):

    grid = parsed_input

    num_visible = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            node = grid[row][col]
            if is_visible(node):
                num_visible += 1

    return num_visible

def calc_scenic_score(grid, row, col):

    rowmin = 0
    colmin = 0
    rowmax = len(grid) - 1
    colmax = len(grid[0]) - 1

    # Short-circuit if we're right on an edge
    if row == rowmin or row == rowmax or col == colmin or col == colmax:
        return 0
    
    my_height = grid[row][col]['height']
    # Look North
    north_score = 0
    for checkrow in range(row - 1, -1, -1):
        north_score += 1
        if grid[checkrow][col]['height'] >= my_height:
            break

    # Look West
    west_score = 0
    for checkcol in range(col - 1, -1, -1):
        west_score += 1
        if grid[row][checkcol]['height'] >= my_height:
            break

    # Look East
    east_score = 0
    for checkcol in range(col + 1, len(grid[0])):
        east_score += 1
        if grid[row][checkcol]['height'] >= my_height:
            break

    # Look South
    south_score = 0
    for checkrow in range(row + 1, len(grid)):
        south_score += 1 
        if grid[checkrow][col]['height'] >= my_height:
            break

    # Score is N*E*W*S
    return north_score * west_score * east_score * south_score 

def part2(parsed_input):

    grid = parsed_input

    max_score = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            score = calc_scenic_score(grid, row, col)
            if score >= max_score:
                print(f"Found new max score @ ({row}, {col})! {score} >= {max_score}")
                max_score = score

    return max_score

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
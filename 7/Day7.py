
import sys
import anytree

class state:
    def __init__(self):
        self.cwd = None
        self.filetree = None

def parse_cd(instate, targetdir):

    # Handle special case of cd'ing to root, which might not have been enconutered yet
    if targetdir == "/":
        if instate.filetree is None:
            instate.filetree = anytree.Node("root", nodetype="dir")
        instate.cwd = instate.filetree

        # We've handled this, so return
        return

    # Handle special case of cd'ing up
    elif targetdir == "..":
        if instate.cwd.is_root:
            print("Why are you trying to cd up from the root dir?")
        else:
            instate.cwd = instate.cwd.parent

    else: 
        # Try to find the target dir in cwd's children
        res = anytree.Resolver('name')
        try:
            instate.cwd = res.get(instate.cwd, targetdir)
        except anytree.resolver.ChildResolverError as e:
            print(f"Could not resolve targetdir \"{targetdir}\"")
            print(e)
            sys.exit(0)


def parse_ls(instate, ls_response):
    for node in ls_response:
        nodetype = node[0]
        nodename = node[1]
        if nodetype == "dir":
            newnode = anytree.Node(name=nodename, parent=instate.cwd, nodetype=nodetype, nodesize=0) 
        else:
            nodesize = int(nodetype)
            nodetype = "file"
            newnode = anytree.Node(name=nodename, parent=instate.cwd, nodetype=nodetype, nodesize=nodesize)

def parse_input(filename=None):
    if filename is None:
        filename = "./input.txt"

    with open(filename, 'r') as inputfile:
        text = [line.rstrip() for line in inputfile.readlines()]

    treestate = state()
    parsestate = "NewCmd"
    ls_response = []

    for idx in range(len(text)):
        line = text[idx]
        tokens = line.split()
        if parsestate == "NewCmd" and tokens[0] == "$":
            print("Found new cmd!")
            print(f"\t\"{line}\"")
            if tokens[1] == "cd":
                parse_cd(treestate, tokens[2])
            elif tokens[1] == "ls":
                parsestate = "ls_response"
                ls_response = []

        elif parsestate == "ls_response":
            if idx+1 < len(text):
                next_line = text[idx+1]

            ls_response.append(tokens)
            if idx+1 >= len(text) or next_line[0] == "$":
                print("\tReceived full ls response!")
                print(f"\t{ls_response}")
                parse_ls(treestate, ls_response)
                #print(f"New tree_state:")
                #print(anytree.RenderTree(treestate.filetree))
                ls_response = []
                parsestate = "NewCmd"


    parsed_input = treestate 

    print(f"Input parsed")
    print(anytree.RenderTree(treestate.filetree))

    return parsed_input

def calc_size(node):

    if len(node.children) == 0 and node.nodetype == "file":
        return node.nodesize

    else:
        mysize = 0
        for child in node.children:
            mysize += calc_size(child)
        node.nodesize = mysize
        return mysize

def part1(parsed_input):

    memoized_list = {}
    '''
    # First pass, grab all files
    for node in anytree.PostOrderIter(parsed_input.filetree):

        if node.is_root:
            continue

        if node.nodetype == "file":
            parent_dir_name = node.parent.name
            if parent_dir_name not in memoized_list.keys():
                memoized_list[parent_dir_name] = 0
            memoized_list[parent_dir_name] += node.nodesize
            node.parent.nodesize += node.nodesize
    
    # Second pass, tally up dirs
    for node in anytree.PostOrderIter(parsed_input.filetree):

        if node.is_root:
            continue

        if node.nodetype == "dir":
            parent_dir_name = node.parent.name
            assert(node.name in memoized_list.keys())
            cursize = memoized_list[node.name]
            if parent_dir_name not in memoized_list.keys():
                memoized_list[parent_dir_name] = 0
            memoized_list[parent_dir_name] += cursize
    '''
    calc_size(parsed_input.filetree) 

    accum = 0
    for node in anytree.PostOrderIter(parsed_input.filetree):

        if node.nodesize <= 100000 and node.nodetype == "dir":
            print(f"{node.name}: {node.nodesize} (New Accum: {accum + node.nodesize})")
            accum += node.nodesize 
        else:
            print(f"Ignoring {node.nodetype} {node.name}:\t\t\t{node.nodesize}")

    return accum

def part2(parsed_input):
    Capacity = 70000000
    NeededSpace = 30000000

    # Find the total current used space
    total_current_used = calc_size(parsed_input.filetree)
    total_current_unused = Capacity - total_current_used
    needed_new_space = NeededSpace - total_current_unused
    print(f"Need to find {needed_new_space} bytes!")

    cur_node = None
    cur_size = 70000000

    for node in anytree.PostOrderIter(parsed_input.filetree):

        # Is this a directory, and would deleting it be sufficient?
        if node.nodetype == "dir" and node.nodesize >= needed_new_space:

            print(f"Examining {node.name} ({node.nodesize})")

            # Is this new dir smaller than the one we've already identified? 
            if node.nodesize <= cur_size:

                print(f"\tFound new min!")
                cur_size = node.nodesize
                cur_node = node.name

    return cur_size

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
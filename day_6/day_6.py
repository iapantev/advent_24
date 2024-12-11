from itertools import chain, cycle

def process_input(filename:str = "test_6_1.txt"):
    dirs = {"^" : [(-1,0),0],
            ">" : [(0,1),1],
            "v" : [(1,0),2],
            "<" : [(0,-1),3]}
    with open(f"day_6/{filename}","r") as f:
        lines = list(map(lambda x: list(x.strip()),f.readlines()))
        for lidx,line in enumerate(lines):
            for pidx, position in enumerate(line):
                if position != "." and position != "#":
                    start_pos = (lidx,pidx)
                    start_dir = dirs[position][0]
                    turn_cycle = [(-1,0),(0,1),(1,0),(0,-1),(-1,0),(0,1),(1,0),(0,-1)]
                    turns = cycle(turn_cycle[dirs[position][1]:dirs[position][1]+4])
                    break
        # Count free positions on map
        # npos = sum((i!="#" and i!=lines[start_pos[0]][start_pos[1]]) for i in chain(*lines))
    return lines, start_pos, start_dir,turns

"""Follow the direction while possible, marking your trail, turn when not"""
def day_6_1(lines, start_pos, start_dir,turns):
    infield = True
    y_size, x_size = len(lines)-1,len(lines[0])-1
    curr_pos, curr_dir = start_pos, start_dir
    lines[curr_pos[0]][curr_pos[1]] = "X"
    while infield:
        ctr += 1
        trial_pos = (curr_pos[0]+curr_dir[0],curr_pos[1]+curr_dir[1])
        # If out of field, do not iterate more
        if trial_pos[0]>y_size or trial_pos[0]<0 or trial_pos[1]>x_size or trial_pos[1]<0:
            infield = False
        # If obstacle - turn right
        elif lines[trial_pos[0]][trial_pos[1]] == "#":
            curr_dir = next(turns)
        # If the new position is available, change symbol
        else:
            curr_pos = trial_pos
            lines[curr_pos[0]][curr_pos[1]] = "X"
    return sum(i=="X" for i in chain(*lines))

if __name__ == "__main__":
    # print(process_input()[1:],sep="\n")
    print(day_6_1(*process_input("input_6_1.txt")))
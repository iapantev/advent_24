import re
from operator import mul

def get_nums(input: str):
    return list(map(lambda x: list(map(int,x.replace("mul(","").replace(")","").split(","))),input))

def day_3_1(input_file:str = "day_3/test_3_1.txt"):
    with open(input_file,"r") as f:
        input = f.read()
    return sum(mul(*i) for i in get_nums(re.findall("mul\(\d{1,3},\d{1,3}\)",input)))

def day_3_2(input_file:str = "day_3/test_3_2.txt"):
    with open (input_file,"r") as f:
        input = f.read()
    commands = re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)",input)
    total = 0
    mode = True
    while len(commands)>0:
        cmd = commands.pop(0)
        if cmd == "don't()":
            mode = False
        if cmd == "do()":
            mode = True
        if cmd != "don't()" and cmd != "do()" and mode:
            total += mul(*list(map(int,cmd.replace("mul(","").replace(")","").split(","))))
    return total

if __name__ == "__main__":
    print("Day 3.1: ", day_3_1(input_file="day_3/input_3_1.txt"))
    print("Day 3.2: ", day_3_2(input_file="day_3/input_3_1.txt"))
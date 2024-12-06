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
    return re.findall("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)",input)

if __name__ == "__main__":
    # print(day_3_1(input_file="day_3/input_3_1.txt"))
    print(day_3_2())
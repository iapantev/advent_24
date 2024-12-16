from itertools import product, repeat
from operator import mul,add

""" Store inputs as a list of tuples (not dict as repetitions are possible)"""
def process_inputs(filename:str = "test_7_1.txt") -> list:
    with open (f"day_7/{filename}", "r") as f:
        inputs = list((int(i[0]),list(map(int,i[1].split()))) for i in list(map(lambda x: x.strip().split(":"),f.readlines())))
    return inputs

""" Concatenate function """
def concatenate(a: int,b :int) -> int:
    return int(str(a)+str(b))

""" Loop over all pairs of test value & numbers.
For each pair, generate all possible combinations of operators to place in the gaps"""
def day_7_1(inputs: list) -> int:
    grand_total = 0
    for target, nums in inputs:
        ops = product([mul,add],repeat = len(nums)-1)
        for opi in ops:
            total = nums[0]
            for num,opp in zip(nums[1:],opi):
                total = opp(total,num)
            if total == target:
                grand_total += target
                break
    return grand_total

""" Same as before but also considering concatenation - much slower performance"""
def day_7_2(inputs: list) -> int:
    grand_total = 0
    for target, nums in inputs:
        ops = product([mul,add,concatenate],repeat=len(nums)-1)
        for opi in ops:
            total = nums[0]
            for num, opp in zip(nums[1:],opi):
                total = opp(total,num)
                if total > target:
                    break
            if total == target:
                grand_total += target
                break 
    return grand_total

if __name__ == "__main__":
    # print(f"Day 7.1 : {day_7_1(process_inputs('input_7_1.txt'))}")
    print(f"Day 7.2 : {day_7_2(process_inputs('input_7_1.txt'))}")
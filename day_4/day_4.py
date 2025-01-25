from itertools import chain
with open("day_4/input_4_1.txt", "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))
    ncols, nrows = len(lines[0]), len(lines)

dici = {"X" : set(),
        "M" : set(),
        "A" : set(),
        "S" : set()}
for i, chr in enumerate(chain(*lines)):
    dici[chr].add(i)
count = 0
for i in range(ncols*nrows-1):
    # search horiz
    if i in dici["X"] and i+1 in dici["M"] and i+2 in dici["A"] and i+3 in dici["S"]:
        count +=1
    # search horiz reverse
    if i in dici["X"] and i-1

print(dici)
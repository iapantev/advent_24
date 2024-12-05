from collections import Counter

def list_prep(input_file: str = "day_1/input_1_1.txt"):
    with open(input_file, "r") as f:
        alist, blist = [], []
        for line in map(lambda x: x.strip(), f.readlines()):
            a, b = list(map(int,line.split()))
            alist.append(a)
            blist.append(b)
    return alist,blist

def day_1_1(a,b):
    return sum(abs(i-j) for i,j in zip(sorted(a),sorted(b)))

def day_1_2(a,b):
    bcount = Counter(b)
    return sum(i*bcount.get(i,0) for i in a)

if __name__ == "__main__":
    a,b = list_prep()
    print(f"Day 1.1 : {day_1_1(a,b)}")
    print(f"Day 1.2 : {day_1_2(a,b)}")
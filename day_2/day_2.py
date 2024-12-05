def list_diff(a):
    return list(j-i for i,j in zip(a[:-1],a[1:]))

def check_line(line):
    return all(map(lambda x: abs(x)<=3,list_diff(line))) and (all(map(lambda x: x>0,list_diff(line))) or all(map(lambda x: x<0,list_diff(line))))

def day_2_1(input_file: str = "day_2/test_2_1.txt"):
    with open(input_file,"r") as f:
        lines = list(list(map(int,line.strip().split())) for line in f.readlines())
    sumsum = 0
    for line in lines:
        sumsum += check_line(line) 
    return sumsum

def day_2_2(input_file: str = "day_2/test_2_1.txt"):
    with open(input_file,"r") as f:
        lines = list(list(map(int,line.strip().split())) for line in f.readlines())
    sumsum = 0
    for line in lines:
        if check_line(line):
            sumsum+=1
        else:
            for i in range(len(line)):
                newline = line.copy()
                newline.pop(i)
                if check_line(newline):
                    sumsum+=1
                    break
    return sumsum

if __name__ == "__main__":
    print("Day 2.1 :", day_2_1(input_file="day_2/input_2_1.txt"))
    print("Day 2.2 :", day_2_2(input_file="day_2/input_2_1.txt"))
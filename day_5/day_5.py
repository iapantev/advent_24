def process_input(filename: str = "test_5_1.txt"):
    with open(f"day_5/{filename}", "r") as f:
        mode = "setup"
        pairs = []
        checks = []
        lines = f.readlines()
        for line in lines:
            if line != "\n" and mode == "setup":
                pairs.append(list(map(int,line.strip().split("|"))))
            if line == "\n":
                mode = "check"
            if line != "\n" and mode == "check":
                checks.append(list(map(int,line.strip().split(","))))
    # Create a dictionary with sets of pages (items) which appear after each page (keys)
    order_dict = {}
    for pair in pairs:
        if pair[0] not in order_dict:
            order_dict[pair[0]] = set()
        if pair[1] not in order_dict:
            order_dict[pair[1]] = set()
        order_dict[pair[0]].add(pair[1])
    return order_dict, checks

def day_5_1(order_dict: dict, checks: list):
    total = 0
    for check in checks:
        # Rank the pages in the sequence
        ranks = dict((i,sum(i in order_dict[j] for j in check)) for i in check)
        true_check = sorted(check,key = lambda x: ranks[x])
        if true_check == check:
            total+= check[(len(check)-1)//2]
        # isgood = all((set(check[idx+1:]).issubset(order_dict.get(i,set(check[idx+1:]))) and i in order_dict) for idx,i in enumerate(check[:-1]))
    return total

def day_5_2(order_dict: dict, checks: list):
    total = 0
    for check in checks:
        # Rank the pages in the sequence
        ranks = dict((i,sum(i in order_dict[j] for j in check)) for i in check)
        true_check = sorted(check,key = lambda x: ranks[x])
        # isgood = all((set(check[idx+1:]).issubset(order_dict.get(i,set(check[idx+1:]))) and i in order_dict) for idx,i in enumerate(check[:-1]))
        if not check==true_check:
            # Sort according to rank and add middle to total
            total+= true_check[(len(true_check)-1)//2]
    return total

if __name__ == "__main__":
    print(day_5_1(*process_input("input_5_1.txt")))
    print(day_5_2(*process_input("input_5_1.txt")))


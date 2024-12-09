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
    # Stupid solution with dict (assumes every combo is described by a rule)
    order_dict = {}
    for pair in pairs:
        if pair[0] not in order_dict:
            order_dict[pair[0]] = set()
        order_dict[pair[0]].add(pair[1])
    return order_dict, checks

def day_5_1(order_dict: dict, checks: list):
    total = 0
    for check in checks:
        isgood = all((set(check[idx+1:]).issubset(order_dict.get(i,set(check[idx+1:]))) and i in order_dict) for idx,i in enumerate(check[:-1]))
        total+= isgood*check[(len(check)-1)//2]
    return total

if __name__ == "__main__":
    print(day_5_1(*process_input("input_5_1.txt")))


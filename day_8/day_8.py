def process_input(filename: str = 'test_8_1.txt') -> list:
    with open(f"day_8/{filename}","r") as f:
        lines = list(map(lambda x: x.strip(),f.readlines()))
    return lines

if __name__ == "__main__":
    print(*process_input(),sep="\n")
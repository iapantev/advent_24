def process_input(filename: str = "test_9_1.txt")->list:
    with open(f"day_9/{filename}","r") as f:
        disk_map = list(map(int,f.read().strip()))
    return disk_map

def reconstruct_disk(disk_map: list) -> list:
    disk = []
    fid = 0
    for idx,block in enumerate(disk_map):
        if idx%2 == 0 or idx==0:
            disk.extend([fid]*block)
            fid += 1
        elif idx%2 == 1 or idx==1:
            disk.extend(["."]*block)
    return disk

def day_9_1(disk: list) -> int:
    left,right = 0, len(disk)-1
    while not all(map(lambda x: x==".",disk[left:])):
        while disk[right]==".":
            right-=1
        if disk[left]==".":
            disk[left], disk[right] = disk[right], disk[left]
        left+=1
    return sum(i*idx for idx,i in enumerate(disk) if i!=".")

def day_9_2(disk: list) -> int:
    """Idea - keep track of blocks with (fid, start, len) and
    gaps with (-1, start, len)"""
    pass

if __name__ == "__main__":
    print(day_9_1(reconstruct_disk(process_input("input_9_1.txt"))))

def checkLevel(level):
    increasing = all(0 < b - a <= 3 for a, b in zip(level, level[1:]))
    decreasing = all(0 < a - b <= 3 for a, b in zip(level, level[1:]))
    return increasing or decreasing

def checkLevelWithDampener(level):
    for i in range(len(level)):
        levelY = level[:i] + level[i+1:]
        if checkLevel(levelY):
            return True
    return False

def __main__():
    with open("dia2.txt") as file:
        count = 0
        for line in file:
            line = [int(x) for x in line.split(' ')]
            if checkLevel(line) or checkLevelWithDampener(line):
                count += 1
        print(count)

if __name__ == "__main__":
    __main__()
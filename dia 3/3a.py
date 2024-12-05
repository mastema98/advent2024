import re

def getMults(line):
    mults = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", line)
    return mults

def multiply(mults):
    results = []
    for mult in mults:
        numbers = re.findall(r"[0-9]{1,3}", mult)
        result = int(numbers[0]) * int(numbers[1])
        results.append(result)
    return sum(results)

def __main__():
    with open("dia3.txt") as file:
        count = 0
        for line in file:
            mults = getMults(line)
            count += multiply(mults)
        print(count)

if __name__ == "__main__":
    __main__()
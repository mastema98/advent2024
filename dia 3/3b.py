import re

def getMults(line):
    multsDo = re.findall(r"mul\([0-9]{1,3},[0-9]{1,3}\)", (re.split(r"don't\(\)", line)[0]))
    multsDont = []
    segments = re.findall(r"don't\(\).*?do\(\)((?:.*?mul\(\d{1,3},\d{1,3}\))*)", line)
    for segment in segments:
        mults = re.findall(r"mul\(\d{1,3},\d{1,3}\)", segment)
        multsDont.extend(mults)

    return multsDo + multsDont

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
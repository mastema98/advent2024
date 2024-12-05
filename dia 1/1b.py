def getLists():
    with open("dia1.txt") as file:
        izq = []; dech = []
        for line in file:
            izq.append(int(line.split('   ')[0]))
            dech.append(int(line.split('   ')[1]))
        return izq, dech
    
def __main__():
    izq, dech = getLists()
    sum = 0
    for i in izq:
        sum += i * dech.count(i)
    print(sum)

if __name__ == "__main__":
    __main__()
def checker(list_1,list_2):
    return (list_1[0] <= list_2[0]) and (list_1[1] <= list_2[1]) and (list_1[2] <= list_2[2])

def mapped_print(safeseq):
    switcher = { 
        0: "P0", 
        1: "P3", 
        2: "P6",
        3: "P7",
        4: "P9" 
    }
    result = []
    for x in safeseq:
        result.append(switcher.get(x, "Default"))
    print("The safe sequence is",' '.join(result)) 

def main():
    res = 3
    n = 5

    # allocations = [[None for j in range(res)] for i in range(n)]
    # max = allocations[::]
    # available = [None for j in range(res)]
    
    # Hardcoded input
    allocations = [[2,1,0],[5,1,2],[4,5,0],[0,5,8],[7,5,0]]
    max = [[6,4,3],[7,8,9],[5,6,2],[4,6,9],[8,9,1]]
    available = [5,1,6]
    
    need = [[(max[i][j] - allocations[i][j]) for j in range(res)] for i in range(n)]
    safeseq = []
    i = 0

    while len(safeseq) != n:
        if (i not in safeseq) and checker(need[i],available):
            for j in range(3):
                available[j] += allocations[i][j]
            safeseq.append(i)
        i = (i + 1)%5

    mapped_print(safeseq)

if __name__ == '__main__':
    main()
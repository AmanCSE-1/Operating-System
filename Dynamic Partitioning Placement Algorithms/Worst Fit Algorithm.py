# Worst Fit Dynamic Partitioning Placement Algorithm in Python 

def worstFit(blockSize, processSize):
    allocate = [-1]*len(blockSize)
    for i in range(len(processSize)):
        worstIndex = -1
        for j in range(len(blockSize)):
            if blockSize[j] >= processSize[i]:
                if worstIndex == -1:
                    worstIndex = j
                elif blockSize[worstIndex] < blockSize[j]:
                    worstIndex = j

    if worstIndex != -1:
        allocate[i] = worstIndex
        blockSize[worstIndex] -= processSize[i]
        
        
    print("\n Process No\t Process Size \t Block Number")
    for i in range(n):
        print(" ", i + 1, "\t\t", processSize[i], "\t\t", end = " ")
        if allocate[i] != -1:
            print(allocate[i] + 1)
        else:
            print ("Not Allocated")
            

if __name__ == '__main__':
    blockSize = list(map(int, input("Enter the size of each block : ").strip().split()))
    processSize = list(map(int, input("Enter the size of each process : ").strip().split()))

    bestFit(blockSize, processSize)

# First Fit Dynamic Partitioning Placement Algorithm in Python

def FirstFit(blockSize, processSize):
    allocate = [-1]*len(blockSize)
    
        for i in range(len(processSize)):
            for j in range(len(blockSize)):
                if blockSize[j] >= processSize[i]:
                    allocate[i] = j
                    blockSize[j] -= processSize[i]
        break
    
    
    print(" Process No\t Process Size \t Block Number")
    
    for i in range(n):
        print(" ", i + 1, "\t\t", processSize[i], "\t\t", end = " ")
        if allocate[i] != -1:
            print(allocate[i] + 1)
            
        else:
            print ("Not Allocated")

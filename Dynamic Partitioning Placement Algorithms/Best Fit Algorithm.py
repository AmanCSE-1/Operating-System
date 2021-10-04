def bestFit(blockSize, processSize): 
    allocate = [-1]*len(blockSize) 

    for i in range(len(processSize)): 
        bestIndex = -1
        for j in range(len(blockSize)): 
            if blockSize[j] >= processSize[i]:  
                if bestIndex == -1:  
                    bestIndex = j  
                elif blockSize[bestIndex] > blockSize[j]:  
                    bestIndex = j 
                    
        if bestIndex != -1:    
            allocate[i] = bestIndex  
            blockSize[bestIndex] -= processSize[i] 

    print("\nFor Best Fit Algorithm")
    print(" Process No\t Process Size \t Block Number")
    for i in range(len(processSize)): 
        print(" ", i + 1, "\t\t", processSize[i], "\t\t", end = " ") 
        if allocate[i] != -1:  
            print(allocate[i] + 1)
        else: 
            print ("Not Allocated") 
    

if __name__ == '__main__':  
    blockSize = list(map(int, input("Enter the size of each block : ").strip().split()))    
    processSize = list(map(int, input("Enter the size of each process : ").strip().split()))    
    
    bestFit(blockSize, processSize) 
    
 # Sample User-Input -> blockSize = 100 500 200 300 600  
 # Sample User-Input -> processSize = 212 417 112 426
  
##### Note : The Output Image of the Program is also uploaded in the same directory.  #####

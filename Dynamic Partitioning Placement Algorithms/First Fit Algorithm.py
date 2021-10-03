# First Fit Dynamic Partitioning Placement Algorithm in Python

def FirstFit(blockSize, processSize):
    allocate = [-1]*len(blockSize)                          # Initializing allocate list 
    
        for i in range(len(processSize)):                   #
            for j in range(len(blockSize)):
                if blockSize[j] >= processSize[i]:          # if block size is greater than or equal to process size, then allocate the process
                    allocate[i] = j
                    blockSize[j] -= processSize[i]
        break
    
    
    # Display the processes with the blocks that are allocated to a respective process
    print(" Process No\t Process Size \t Block Number")
    for i in range(n):
        print(" ", i + 1, "\t\t", processSize[i], "\t\t", end = " ")
        if allocate[i] != -1:
            print(allocate[i] + 1)
            
        else:
            print ("Not Allocated")

            
# Driver code to run the Program
if __name__ == "__main__":
    
    # get the size of each block and process requests.
    blockSize = list(map(int, input("Enter the size of each block : ").strip().split()))        
    processSize = list(map(int, input("Enter the size of each process : ").strip().split()))
    
    # Call the function
    FirstFit(blockSize, processSize)

# FCFS Algorithm in Python

# This is the function: It takes input parameter process, and number of process
def FCFS(process, n):
    wait, time = 0,0                # Initailzing some variables that will be used in function
    waitSum, turnSum = 0,0          # Initializing Sum of Waiting-Time
                                    # Initializing Sum of Turnaround Time
    

    print("Process\t    Burst-Time\tWaiting-Time\tTurnaround-Time")
    for i in range(n):                                  # Iterating through all process
        turn = wait + process[i][1]                     # Turnaround-Time  = Waiting-Time + Burst-Time of Process
        
        print("P" + str(process[i][0]) + "\t\t" + str(process[i][1]) + "\t\t" + str(wait)+ "\t\t" + str(turn))
        wait += process[i][1]                           # Incrementing waiting-time with Burst-Time of current process
        waitSum += wait                                 # Incrementing Sum of Wait-Time
        turnSum += turn                                 # Incrementing Sum of Wait-Time

    waitSum -= wait
    avgWaitTime = round(waitSum/n, 3)                       # Rounding Average Waiting Time upto 3 decimal places
    avgTurnTime = round(turnSum/n, 3)                       # Rounding Average Turnaround-Time upto 3 decimal places
    
    return (avgWaitTime, avgTurnTime)
    

# Driver Code
if __name__ == "__main__":
    n=int(input("Enter the number of process: "))           # Number of processes
    process=[]                                              # Process is list for all the processes to be executed 

    for i in range(1, n+1):
        process.append([i, int(input("Enter Burst-Time for Process-"+str(i)+": "))])

    print("\n\nFirst Come First Served Scheduling: ")
    resultTuple = FCFS(process, n)
    print("\nAverage Waiting-Time is", resultTuple[0])
    print("Average Turnaround-Time is", resultTuple[1])

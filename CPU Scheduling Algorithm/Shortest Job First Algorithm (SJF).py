def SJF(process, n):
    process = sorted(process, key=lambda x:x[1])            # Sorting process according to their Burst Time
    wait= 0
    waitSum, turnSum = 0,0                                  # Initializng Sum of Wait-Time -> 0
                                                            # Initializng Sum of Tuenaround-Time -> 0


    print("Process\t    Burst-Time\tWaiting-Time\tTurnaround-Time")
    for i in range(n):                                      # Iterating through all processes
        turn = wait + process[i][1]                         # Turnaround-Time  = Wait-Time + Burst-Time
        
        print("P" + str(process[i][0]) + "\t\t" + str(process[i][1]) + "\t\t" + str(wait)+ "\t\t" + str(turn))
        wait += process[i][1]                               # Adding wait-time with burst time of current process
        waitSum += wait                                     # Incrementing Sum of Wait-Time
        turnSum += turn                                     # Incrementing Sum of Turnaround-Time

    waitSum -= wait
    
    avgWaitTime = round(waitSum/n, 3)                       # Rounding Average Waiting Time upto 3 decimal places
    avgTurnTime = round(turnSum/n, 3)                       # Rounding Average Turnaround-Time upto 3 decimal places
    
    return (avgWaitTime, avgTurnTime)
  
    

# Driver Code
if __name__ == "__main__":

    n=int(input("Enter the number of process: "))           # Number of processes
    process=[]

    for i in range(1, n+1):                                 # Taking user-input for Burst-Time of process
        process.append([i, int(input("Enter Burst-Time for Process-"+str(i)+": "))])

    print("\n\nShortest Job First Scheduling: ")
    resultTuple = SJF(process, n)
    print("\nAverage Waiting-Time is", resultTuple[0])
    print("Average Turnaround-Time is", resultTuple[1])

    
##### Note : The Output Image of the Program is also uploaded in the same directory.  #####

# FCFS Algorithm in Python

# This is the function: It takes input parameter process
def FCFS(process):
    wait, time = 0,0                # Initailzing some variables that will be used in function
    waitsum, turnsum = 0,0          # Waitsum -> Sum of Waiting Time
                                    # Turnsum -> Sum of Turnaround Time
    space = 2*" "                   # Used for printing values
    

    print("Process Burst-Time\tWaiting-Time\tTurnaround-Time")
    for i in range(n):                                  # Iterating through all process
        turn = wait + process[i][1]                     # Turnaround Time  = Waiting Time + Burst Time of Process
        print("P" + str(process[i][0]), space, process[i][1], space, wait, space, turn)
        wait += process[i][1]                           # Incrementing waiting time with Burst Time of current process
        waitsum += wait
        turnsum += turn

    waitsum -= wait
    print("\nAverage Waiting-Time is", round(waitsum/n, 3))
    print("Average Turnaround-Time is", round(turnsum/n, 3))
    

# Driver Code
if __name__ == "__main__":
    n=int(input("Enter the number of process: "))
    process=[]                                  # Process is list for all the processes to be executed 

    for i in range(1, n+1):
        process.append([i, int(input("Enter Burst-Time for Process-"+str(i)+": "))])

    print("\n\nFirst Come First Served Scheduling: ")
    FCFS(process)

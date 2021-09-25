n=int(input("Enter the number of process: "))
process=[]

for i in range(1, n+1):
    process.append([i, int(input("Enter Burst-Time for Process-"+str(i)+": "))])

def FCFS(process):
    wait, time = 0,0
    waitsum, turnsum = 0,0
    space = 2*" "

    print("Process Burst-Time\tWaiting-Time\tTurnaround-Time")
    for i in range(n):
        turn = wait + process[i][1]
        print("P" + str(process[i][0]), space, process[i][1], space, wait, space, turn)
        wait += process[i][1]
        waitsum += wait
        turnsum += turn

    waitsum -= wait
    print("\nAverage Waiting-Time is", round(waitsum/n, 3))
    print("Average Turnaround-Time is", round(turnsum/n, 3))
    

print("\n\nFirst Come First Served Scheduling: ")
FCFS(process)

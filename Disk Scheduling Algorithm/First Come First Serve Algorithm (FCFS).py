# FCFS Disk Scheduling Algorithm Program in Python 

def FCFS(seekSeq, head):
    seekTime = 0
    current = head
    for i in range(len(seekSeq)-1):
        seekTime += abs(seekSeq[i+1] - current)
        current = seekSeq[i+1]

    return seekTime
  
  
  if __name__ == "__main__":
    seekSeq = list(map(int, input("Enter the Seek Sequence : ").strip().split(',')))
    head = int(input("Enter the initial head position : "))
    
    print("\nThe Total Seek Time for given sequence for FCFS Algorithm is ", FCFS(seekSeq, head))

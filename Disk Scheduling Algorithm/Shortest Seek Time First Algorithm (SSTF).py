def SSTF(seekSeq, head):
    seekTime = 0
    current = head
    servedSeq = seekSeq.copy()

    while len(servedSeq)>0:
        minDiff, index = 99999, -1

        for i in servedSeq:
            currDiff = abs(head-i)
            if currDiff < minDiff:
                minDiff = currDiff
                index = servedSeq.index(i)

        seekTime += minDiff
        head = servedSeq[index]
        servedSeq.pop(index)

    return seekTime
  
  
if __name__ == "__main__":
    seekSeq = list(map(int, input("Enter the Seek Sequence : ").strip().split(',')))
    head = int(input("Enter the initial head position : "))
    
    print("\nThe Total Seek Time for given sequence for SSTF Algorithm is ", SSTF(seekSeq, head))

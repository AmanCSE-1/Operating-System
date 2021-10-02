# LRU 

def LRU(pages, capacity):
    memory=list()
    recentlyUsed = list()
    pageFault=0
    
    for page in pages:    
        if (page not in memory):
            pageFault+=1
            recentlyUsed.append(page)
            
            if (len(memory)<capacity):
                memory.append(page)
            else:
                memory.append(page)
                index = memory.index(recentlyUsed[0])
                memory.pop(index)
                recentlyUsed.pop(index)
                
        else:
            if page in recentlyUsed:
                recentlyUsed.pop(recentlyUsed.index(page))
                recentlyUsed.append(page)
            else:
                recentlyUsed.append(page)
                
    return pageFault
  
if __name__=="__main__":
    pages = list(map(int, input('Enter the sequence of Pages: ').strip().split()))
    capacity=int(input('Enter maximum number of pages in a frame: '))               # max pages in frame

    print("\nThe number of Page Faults occured in LRU are: ", LRU(pages, capacity))

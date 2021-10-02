# Least Recently Used Algorithm Implementation in Python 

# Note about Data Structures used in program :
#    1. Memory -> list that stores the pages
#    2. recentlyUsed -> list that stores the recentlyUsed pages. {The most recently used page is stored at end of the list; while the least recently used is at 0th index}


def LRU(pages, capacity):
    memory = list()                           # Initializing the memory
    recentlyUsed = list()                     # Initializing the list for storing recently used pages
    pageFault = 0                             # Count of number of page Faults
    
    for page in pages:    
        if (page not in memory):                # If page not found in memory
            pageFault+=1                        # Incrementing the count of Page faults
            recentlyUsed.append(page)           # Adding page to recently used list
            
            if (len(memory)<capacity):          # If free spaces are available in memory 
                memory.append(page)             # Then, add the page to memory
            else:
                memory.append(page)             # Add the page to memory, (but apply LRU Algorithm)
                
                # Find the page that is least recently used (page will be at 0th index of recentlyUsed list) 
                index = memory.index(recentlyUsed[0])           
                memory.pop(index)               # Pop the page from memory
                recentlyUsed.pop(index)         # Pop the page from recentlyUsed List 
                
        
        # If page found in memory, update the recentlyUsed list
        else:
            if page in recentlyUsed:                        # If page found in recentlyUsed list
                recentlyUsed.pop(recentlyUsed.index(page))  # Pop the page and append in recentlyUsed List
                recentlyUsed.append(page)
            else:
                recentlyUsed.append(page)                   # If page not found in recentlyUsed, append in recentlyUsed list
                    
    return pageFault                                # return the count of pageFault occured.
  
    
# Driver Code to run the program
if __name__=="__main__":
    pages = list(map(int, input('Enter the sequence of Pages: ').strip().split()))
    capacity=int(input('Enter maximum number of pages in a frame: '))               # max pages in frame

    print("\nThe number of Page Faults occured in LRU are: ", LRU(pages, capacity))

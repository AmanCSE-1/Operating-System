# FIFO Page Replacement Program In Python


def FIFO(pages, capacity):
    memory = list()           # Initializing the memory
    pageFaults = 0            # Count of number of page Faults
    
    for page in pages:
        if (page not in memory):                        # If page not found in memory
            pageFaults+=1                               # Incrementing the count of Page faults
            if (len(memory) < capacity):                # If Free spaces available in frames
                memory.append(page)                     # Add page to memory if free space exists
                
            else:                                       # If page not found in memory, apply FIFO Page Replacement Algorithm
                memory.pop(0)                           # Remove the page at first position of memory
                memory.append(page)                     # Adding current page in memory
    return pageFaults   


# Driver Code to run the program  
if __name__ == "__main__":
    pages = list(map(int, input('Enter the sequence of Pages: ').strip().split()))
    capacity = int(input('Enter maximum number of pages in a frame: '))                 # max pages in frame

    print("\nThe number of Page Faults occurred in FIFO are: ", FIFO(pages, capacity))
    
    
##### Note : The Output Image of the Program is also uploaded in the same directory.  #####

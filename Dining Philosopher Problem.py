import threading
import time

class Philosopher(threading.Thread):
    running = True
    
    def __init__(self, index, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.index = index
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
        
    def run(self):
        while(self.running):
            time.sleep(5)
            print('Philosopher %s is hungry.' %self.index)
            self.dine()
    
    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
        while(self.running):
            fork1.acquire()
            locked = fork2.acquire(False)
            if locked: break
                
            fork1.release()
            print('Philosopher %s swaps forks.' %self.index)
            fork1, fork2 = fork2, fork1
        
        else:
            return
        self.dining()
        fork2.release()
        fork1.release()

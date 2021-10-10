def check(i):
    for j in range(m):
        if need[i][j] > available[j]:
            return False
    return True

n = int(input("Enter the number of Processes: "))
m = int(input("Enter the number of Resources: "))
print()

allocation = []
for i in range(n):
    allocation.append(list(map(int, input('\nEnter the number of instances allocated for Process P'+str(i)+" : ").strip().split())))
    
maX = []
for i in range(n):
    maX.append(list(map(int, input("\nEnter Max matrix entry for Process P"+str(i)+" : ").strip().split())))

available = list(map(int, input("\nEnter the number of instances available of Resources : ").strip().split()))    


need = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    for j in range(m):
        need[i][j] = maX[i][j] - allocation[i][j]
      

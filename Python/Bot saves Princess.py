#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    #print all the moves here
    p1, p2, m1, m2 = 0, 0, 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'p': # find the pricess
                p1 = i
                p2 = j
            if grid[i][j] == 'm': # find the bot
                m1 = i
                m2 = j
    found = False
    moves = ''
    if p1 < m1:
        moves += 'UP\n' * (m1 - p1) # move by the difference
    else:
        moves += 'DOWN\n' * (p1 -m1) # move by the difference
    if p2 < m2:
        moves += 'LEFT\n' * (m2 - p2) # move by the difference
    else:
        moves += 'RIGHT\n' * (p2 - m2) # move by the difference
                        
    print(moves)
    
    
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)


''' 
example:

---
-m-
p--

'''
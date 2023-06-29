import math
def findheuristic(heuristic,node,goal):
    x=node[0]
    y=node[1]
    k=abs(x-goal[0])+abs(y-goal[1])
    heuristic[x][y]=math.floor( (k))
def search(grid, init, goal, cost, delta, heuristic):
    path = []
    val = 1
    order=[]
    visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[init[0]][init[1]] = 1
    expand = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    expand[init[0]][init[1]] = 0
    y = init[1]
    x = init[0]
    g = 0
    f = g + heuristic[x][y]
    minList = [f, g, x, y]
    while minList[2:] != goal:
        for i in range(len(delta)):
            x2 = x + delta[i][0]
            y2 = y + delta[i][1]
            if 0 <= x2 < len(grid) and 0 <= y2 < len(grid[0]):
                if visited[x2][y2] == 0 and grid[x2][y2] == 0:
                    g2 = g + cost
                    f2 = g2 + heuristic[x2][y2]
                    path.append([f2, g2, x2, y2])
                    visited[x2][y2] = 1

        if not path:
            return 'fail', expand
        del minList[:]
        minList = min(path)
        path.remove(minList)
        x = minList[2]
        y = minList[3]
        g = minList[1]
        expand[x][y] = val
        order.append([x,y])
        val += 1
    print(order)
    return minList, expand

if _name_ == '_main_':
    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]]
    heuristic = [[9, 3, 7, 6, 5, 4],
                 [6, 7, 6, 5, 4, 3],
                 [7, 6, 5, 4, 3, 2],
                 [6, 5, 4, 3, 2, 1],
                 [5, 4, 3, 2, 1, 0]]
    heuristi = [[0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0]]
    init = [0, 0]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1

    delta = [[-1, 0],  # go up
             [0, -1],  # go left
             [1, 0],  # go down
             [0, 1]]  # go right

    delta_name = ['^', '<', 'v', '>']
    row=len(heuristic)
    col=len(heuristic[0])

    for i in range(0,row):
        for j in range(0,col):
            findheuristic(heuristic,[i,j],goal)
    print(heuristic)
    path, expand = search(grid, init, goal, cost, delta, heuristic)
    print(path)
    for l in range(0,len(expand)):
        print(expand[l])

#Newer Version

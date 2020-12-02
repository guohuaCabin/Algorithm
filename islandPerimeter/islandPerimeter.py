def islandPerimeter(grid) :
    if len(grid) == 0:
        return 0
    sides = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                sides = dfs(grid,x, y,sides)

    return sides
        


def dfs(grid,x,y,sides):
    if(x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0 or grid[x][y] == 0):
        return 1
    
    if grid[x][y] == 2:
        return 0

    grid[x][y] = 2
    sides = dfs(grid,x,y-1,sides) + dfs(grid,x-1,y,sides) + dfs(grid,x,y+1,sides) + dfs(grid,x+1,y,sides)
    return sides 
    
  
grid = [[0,1,0,0],[0,1,1,0],[0,1,1,1],[0,1,0,0]]

print(islandPerimeter(grid))


grid = [[0,1,0,0],[0,1,1,0],[0,1,1,1],[0,1,0,0]]

def bfs(grid):
    if len(grid) == 0:
        return 0 

    sides = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 1:
                
                grid[x][y] = 2
                neighbors = []
                neighbors.append([x,y])
                while len(neighbors) > 0:
                    firstList = neighbors[0]
                    xValue = firstList[0]
                    yValue = firstList[1]
                    neighbors.pop(0)


                    if xValue-1 >= 0 and grid[xValue-1][yValue] == 1:
                        neighbors.append([xValue-1,yValue])
                        grid[xValue-1][yValue] = 2
                    elif(grid[xValue-1][yValue] == 0 or xValue-1 < 0):
                        sides += 1
                    
                    if xValue+1 < len(grid) and grid[xValue+1][yValue] == 1:
                        neighbors.append([xValue+1,yValue])
                        grid[xValue+1][yValue] = 2
                    elif(xValue+1 >= len(grid) or grid[xValue+1][yValue] == 0):
                        sides += 1

                    if yValue-1 >= 0 and grid[xValue][yValue-1] == 1:
                        neighbors.append([xValue,yValue-1])
                        grid[xValue][yValue-1] = 2
                    elif(grid[xValue][yValue-1] == 0 or yValue-1 < 0):
                        sides += 1

                    if yValue+1 < len(grid) and grid[xValue][yValue+1] == 1:
                        neighbors.append([xValue,yValue+1])
                        grid[xValue][yValue+1] = 2
                    elif(yValue+1 >= len(grid[0]) or grid[xValue][yValue+1] == 0 ):
                        sides += 1

    return sides
print(bfs(grid))

















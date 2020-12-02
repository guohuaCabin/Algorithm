#!/usr/bin/env python


def maxAreaOfIsland(gird):
	if len(gird) == 0 or len(gird[0]) == 0:
		return 0

	max = 0
	for x in range(len(gird)):
		for y in range(len(gird[0])):
			if gird[x][y] == "1":
				num = 0
				num = DFS(gird,x,y,num)
				if max < num:
					max = num

	return max
		


def DFS(gird,x,y,num):
	if x < 0 or x>=len(gird) or y < 0 or y >= len(gird[x]) or gird[x][y] == "0":
		return 0

	gird[x][y] = "0"
	num = 1+DFS(gird,x,y-1,num)+DFS(gird,x-1,y,num)+DFS(gird,x,y+1,num)+DFS(gird,x+1,y,num)

	return num

grid = [
  		["1","1","1","1","0"],
  		["1","1","0","1","0"],
  		["1","1","0","0","0"],
  		["0","0","0","0","0"]
	]

print (maxAreaOfIsland(grid))


#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @lc app=leetcode.cn id=463 lang=python3
#
# [463] 岛屿的周长
#
# https://leetcode-cn.com/problems/island-perimeter/description/
#
# algorithms
# Easy (68.19%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    57.4K
# Total Submissions: 80.3K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# 给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。
# 
# 网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。
# 
# 岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100
# 。计算这个岛屿的周长。
# 
# 
# 
# 示例 :
# 
# 输入:
# [[0,1,0,0],
# ⁠[1,1,1,0],
# ⁠[0,1,0,0],
# ⁠[1,1,0,0]]
# 
# 输出: 16
# 
# 解释: 它的周长是下面图片中的 16 个黄色的边：
# 
# 
# 
# 
#

# @lc code=start
#  class Solution:
#     def islandPerimeter(self,nums):
#         if len(nums) == 0:
#             return 0 
        
#         sides = 0
#         for x in range(len(nums)):
#             for y in range(len(nums[0])):
#                 if nums[x][y] == 1: #切入点
#                     nums[x][y] = -1
#                     nodeList = []#创建队列，用来记录节点
#                     nodeList.append([x,y])
#                     while len(nodeList) > 0:
#                         list = nodeList[0]
#                         xValue = list[0]
#                         yValue = list[1]
#                         nodeList.pop(0)#每次将队列中的第一个元素取出（取出该元素，说明这个元素已经搜索完成，从队列中移除），进行上下左右的查找，如果符合条件就添加到队列中去
#                         if xValue-1 >= 0 and nums[xValue-1][yValue] == 1:
#                             nodeList.append([xValue-1,yValue])#符合条件，加入队列中
#                             nums[xValue-1][yValue] = -1 #染色做标记，这里没有染色为0，是因为需要统计周围为0时的边，染为0会重复统计
#                         elif(xValue-1 < 0 or nums[xValue-1][yValue] == 0):
#                             sides += 1

#                         if xValue+1 < len(nums) and nums[xValue+1][yValue] == 1:
#                             nodeList.append([xValue+1,yValue])
#                             nums[xValue+1][yValue] = -1
#                         elif(xValue+1 >= len(nums) or nums[xValue+1][yValue] == 0):
#                             sides += 1
                        
#                         if yValue-1 >= 0 and nums[xValue][yValue-1] == 1:
#                             nodeList.append([xValue,yValue-1])
#                             nums[xValue][yValue-1] = -1
#                         elif(yValue-1 < 0 or nums[xValue][yValue-1] == 0):
#                             sides += 1

#                         if yValue+1 < len(nums[0]) and nums[xValue][yValue+1] == 1:
#                             nodeList.append([xValue,yValue+1])
#                             nums[xValue][yValue+1] = -1
#                         elif(yValue+1 >=
#                         len(nums[0]) or nums[xValue][yValue+1] == 0):
#                             sides += 1  
#         return sides

class Solution:
    def islandPerimeter(self,grid):
        if len(grid) == 0:
            return 0 
        sides = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    sides = self.dfs(grid,x,y)
        return sides
    
    def dfs(self,grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
            return 1
        
        if grid[x][y] == 2:
            return 0 
        
        grid[x][y] = 2
        return self.dfs(grid,x-1,y) + self.dfs(grid,x+1,y) + self.dfs(grid,x,y-1) + self.dfs(grid,x,y+1)
# @lc code=end


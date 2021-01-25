#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#
# https://leetcode-cn.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (46.52%)
# Likes:    132
# Dislikes: 0
# Total Accepted:    22.7K
# Total Submissions: 48.6K
# Testcase Example:  '["a==b","b!=a"]'
#
# 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或
# "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
# 
# 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：["a==b","b!=a"]
# 输出：false
# 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
# 
# 
# 示例 2：
# 
# 输入：["b==a","a==b"]
# 输出：true
# 解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
# 
# 
# 示例 3：
# 
# 输入：["a==b","b==c","a==c"]
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：["a==b","b!=c","c==a"]
# 输出：false
# 
# 
# 示例 5：
# 
# 输入：["c==c","b==d","x!=z"]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] 和 equations[i][3] 是小写字母
# equations[i][1] 要么是 '='，要么是 '!'
# equations[i][2] 是 '='
# 
# 
#

# @lc code=start

# class UnionFind:
#     father = []
#     rank = []
#     # 初始化，树的深度初始化值为1，都是以自己作为初始化值
#     def __init__():
#         for x in range(0,26):
#             father[x] = x
#             rank[x] = 1
    
#     #查找
#     def find(x):
#         if father[x] == x :
#             return x
#         else:
#             father[x] = find(father[x])
#             return father

#     #合并
#     def union(i,j):
#         x = self.find(i)
#         y = self.find(j)
#         if rank[x] < rank[y]:
#             father[x] = y
#         else:
#             father[y] = x

#         if rank[x] == rank[y] and x != y:
#             rank[y] += 1


class Solution:
    # import UnionFind
    # unionFind = UnionFind()
    def equationsPossible(self, equations: List[str]) -> bool:
        self.init11
        for str in  range(len(equations)):
            if (str[0] is str[-1]) and (str[1] is "=") :
                #为同一集合的，去合并
                self.union(ord(str[0]),ord(str[-1]))

        for str in  range(len(equations)): 
            if (self.find(ord(str[0])) is self.find(ord(str[-1]))) and (str[1] is "=") :
                return False
            
        return True


    father = []
    rank = []
    # 初始化，树的深度初始化值为1，都是以自己作为初始化值
    def init11():
        for x in range(0,26):
            father[x] = x
            rank[x] = 1
    
    #查找
    def find(x):
        if father[x] == x :
            return x
        else:
            father[x] = find(father[x])
            return father

    #合并
    def union(i,j):
        x = self.find(i)
        y = self.find(j)
        if rank[x] < rank[y]:
            father[x] = y
        else:
            father[y] = x

        if rank[x] == rank[y] and x != y:
            rank[y] += 1         


# @lc code=end


#!/usr/bin/python
# -*- coding: UTF-8 -*-


# father = [i for i in range(26)]
# rank =  [i for i in range(26)]
# father = []
# rank = []
class UnionFind():
    #初始化
    
    def __init__(self):
        self.father = [i for i in range(26)]
        self.rank =  [i for i in range(26)]

    #查找
    def find(self,x):
        if self.father[x] == x :
            return x
        else:
            self.father[x] = self.find(self.father[x])
            return self.father[x]

    #合并
    def union(self,i,j):
        x = UnionFind.find(self,i)
        y = UnionFind.find(self,j)
        if self.rank[x] < self.rank[y]:
            self.father[x] = y
        else:
            self.father[y] = x

        if self.rank[x] == self.rank[y] and x != y:
            self.rank[y] += 1         


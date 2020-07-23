#!usr/bin/python
# -*- coding: utf-8 -*-
# 

'''
给定三个字符串 s1, s2, s3, 验证 s3 是否是由 s1 和 s2 交错组成的。

示例 1：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false

来源：力扣（LeetCode）

'''

def isInterleave(s1,s2,s3):
	i,j,k = len(s1),len(s2),len(s3)

	if i+j != k:
		return False

	if i == 0 or j == 0:
		return s1+s2 == s3

	return (s1[0] == s3[0] and isInterleave(s1[1:],s2,s3[1:])) or (s2[0] == s3[0] and isInterleave(s1,s2[1:],s3[1:])) 



print (isInterleave("aabcc","dbbca","aadbbcbcac"))

print (isInterleave("aabcc","dbbca","aadbbbaccc"))
#!/usr/bin/env python

'''
递归乘法

 写一个递归函数，不使用 * 运算符， 实现两个正整数的相乘。可以使用加号、减号、位移，但要吝啬一些。

示例1:

 输入：A = 1, B = 10
 输出：10

示例2:

 输入：A = 3, B = 4
 输出：12

'''

def multiply_one(A, B):
    if B == 0:
        return 0
    
    return A + multiply(A,B-1)


def multiply(A, B):
    if B == 1:
        return A
    if (B % 2) == 0:
        return multiply((A << 1),(B >> 1))
    else:
        return A + multiply((A << 1),(B >> 1))

 
print(multiply_one(10,11)) 

print(multiply(5,3))
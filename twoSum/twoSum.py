#!/usr/bin/python  
# -*- coding: utf-8 -*- 


'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

'''

def twoSum(nums, target):
	for index in range(len(nums)):
		numB = target - nums[index]
		splitInt = index+1
		if numB in nums[splitInt:]:
			return [index,nums[splitInt:].index(numB)+splitInt]

def twoSum1(nums, target):
        for index in range(len(nums)):
        	numB = target - nums[index]
        	if(numB in nums and index != nums.index(numB)):
				return [index,nums.index(numB)]

print twoSum([3,3,2,4],6) 

print twoSum1([3,3,2,4],6) 
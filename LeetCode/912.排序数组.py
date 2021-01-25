#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (59.45%)
# Likes:    176
# Dislikes: 0
# Total Accepted:    94.7K
# Total Submissions: 159.1K
# Testcase Example:  '[5,2,3,1]'
#
# 给你一个整数数组 nums，请你将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 输入：nums = [5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 50000
# -50000 <= nums[i] <= 50000
# 
# 
#

# @lc code=start
class Solution:
    #冒泡排序
    def sortArray(self,nums):
        count = len(nums)
        if count == 0 or count == 1:
            return nums
          
        step = int(count / 2)

        while step > 0 :
            for i in range(step,count):
                value = nums[i]

                j = i - step
                while value < nums[j] and j >= 0:
                    nums[j+step] = nums[j]
                    j -= step
                nums[j+step] = value

            step = int(step / 2)
        return nums
# @lc code=end


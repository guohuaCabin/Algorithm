#!/usr/bin/python
#
'''
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：

输入：nums = [5,2,3,1]
输出：[1,2,3,5]
示例 2：

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
 

提示：

1 <= nums.length <= 50000
-50000 <= nums[i] <= 50000
'''

'''
冒泡排序

时间复杂度 n(n^2)
空间复杂度 n(1)

每次都从头开始循环，每次循环将最大的数值放到后面

'''
nums = [5,1,1,2,0,0]

def sortArray_bubble(nums):

	n = len(nums)

	for x in range(n):
		
		for y in range(0,n-x-1):

			if nums[y] > nums[y+1]:
				nums[y],nums[y+1] = nums[y+1],nums[y]
		
	
	return nums



# print(sortArray_bubble(nums))


'''
快速排序

1．先找一个基准数。
2．将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。

'''
def sortArray_quicksort(nums,left,right):
	if left > right:
		return

	#需要一个基准值
	baseValue = nums[left]
	i, j = left, right

	while i < j: ##i < j才符合条件
		##遍历右侧部分
		while i < j and nums[j] >= baseValue:
			j -= 1
		#符合条件的扔到左边
		nums[i] = nums[j]

		##遍历左侧部分
		while j < j and nums[i] <= baseValue:
			i += 1

		#符合条件的扔到右边
		nums[j] = nums[i]

	#重设基准值
	nums[i] = baseValue

	#递归
	sortArray_quicksort(nums,i+1,j) #递归左边
	sortArray_quicksort(nums,i,j-1) #递归右边

	return nums



# print(sortArray_quicksort(nums,0,len(nums)-1))

'''
插入排序

循环遍历，每次取出一个值，将该值与它前面的数值比较，直到找到符合的位置放入其中，它后面的数值一次往后移动。

'''

#[5,4,3,2,0,0]
#
def sortArray_insertsort(nums):
	count = len(nums)
	if count == 0 or count == 1:
		return nums
	
	for i in range(1,count):
		value = nums[i]
		j = i-1
		#遍历 i前面的数据，如果该数据大于value ，将该数据往后移
		while value < nums[j] and j >= 0:
			nums[j+1] = nums[j]
			j -= 1

		nums[j+1] = value

	return nums		

# nums = [5,1,1,2,0,0]
# print(sortArray_insertsort(nums))

'''
希尔排序

插入排序的一种改进方案

核心还是使用插入排序，但每次的比对下标使用动态改变，每次取下标的1/2，直到下标到1为止
'''
def sortArray_shellsort(nums):
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
# nums = [5,1,1,2,0,0]
# print(sortArray_shellsort(nums))



'''
冒泡排序
时间复杂度 n(n^2)
空间复杂度 n(1)
每次都从头开始循环，每次循环将最大的数值放到后面
'''
def sortArray_bubble(nums):
    n = len(nums)
    for x in range(n):
      for y in range(0,n-x-1):
        if nums[y] > nums[y+1]:
          nums[y],nums[y+1] = nums[y+1],nums[y]
    return nums

# nums = [5,1,1,2,0,0]
# print(sortArray_bubble(nums))

'''
快速排序
1．先找一个基准数。
2．将比这个数大的数全放到它的右边，小于或等于它的数全放到它的左边。
3．再对左右区间重复第二步，直到各区间只有一个数。
'''
def sortArray_quicksort(nums,left,right):
    if left > right:
    	return
    #需要一个基准值
    baseValue = nums[left]
    i, j = left, right
    while i < j: ##i < j才符合条件
        ##遍历右侧部分
        while i < j and nums[j] >= baseValue:
            j -= 1
        #符合条件的扔到左边
        nums[i] = nums[j]
        ##遍历左侧部分
        while j < j and nums[i] <= baseValue:
            i += 1
        #符合条件的扔到右边
        nums[j] = nums[i]
    #重设基准值
    nums[i] = baseValue
    #递归
    sortArray_quicksort(nums,i+1,j) #递归左边
    sortArray_quicksort(nums,i,j-1) #递归右边
    return nums
# 
# nums = [5,1,1,2,0,0]
# print(sortArray_quicksort(nums,0,len(nums)-1))
'''
插入排序
循环遍历，每次取出一个值，将该值与它前面的数值比较，直到找到符合的位置放入其中，它后面的数值一次往后移动。
'''
#[5,4,3,2,0,0]
def sortArray_insertsort(nums):
    count = len(nums)
    if count == 0 or count == 1:
        return nums
    
    for i in range(1,count):
        value = nums[i]
        j = i-1
        #遍历 i前面的数据，如果该数据大于value ，将该数据往后移
        while value < nums[j] and j >= 0:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = value
    return nums  
# nums = [5,1,1,2,0,0]   
# print(sortArray_insertsort(nums))
'''
希尔排序
插入排序的一种改进方案
核心还是使用插入排序，但每次的比对下标使用动态改变，每次取下标的1/2，直到下标到1为止
'''
def sortArray_shellsort(nums):
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

# nums = [5,1,1,2,0,0]
# print(sortArray_shellsort(nums))


'''
选择排序
将数据分为两部分：待排序 和 已排序，从待排序的数据中选出最小或者最大的元素，放到已排序的数据中，
然后再从待排序的数据中找最大或者最小的元素，放到已排序的数据中，一次类推，直到待排序的数据为空
'''

def sortArray_selectSort(nums):
	count = len(nums)
	if count == 0 or count == 1:
		return nums

	for i in range(count):
		minValue = nums[i]
		minIndex = i
		for j in range(i+1,count):
			if minValue > nums[j]:
				minValue = nums[j]
				minIndex = j
		nums[i],nums[minIndex] = nums[minIndex],nums[i]

	return nums
			

nums = [5,7,10,2,8,0,1,9]
print("选择排序：")
print(sortArray_selectSort(nums))


def sortArray_selectSort1(nums):
	count = len(nums)
	if count == 0 or count == 1:
		return nums

	for i in range(count):
		minIndex = i
		for j in range(i+1,count):
			if nums[minIndex] > nums[j]:
				minIndex = j
		nums[i],nums[minIndex] = nums[minIndex],nums[i]

	return nums
			

nums = [5,7,10,2,8,0,1,9]
print("选择排序：")
print(sortArray_selectSort(nums))


'''
计数排序
 将元素作为下标，该元素每出现一次，对应的下标的数值+1，存入新的list中，即：记录该元素出现的次数。
 然后将遍历新的list，拿到对应的元素就是排序好的数据
'''
def sortArray_countingSort(nums):
	count = len(nums)
	if count == 0 or count == 1:
		return nums

	newList = [0]*101 # 题目假设 nums中的元素 0<= value <= 100，也可以遍历找出最大值和最小值去创建新的list
	

	for i in range(count):
		value = nums[i]
		newList[value] += 1 

	res_list = []
	for i in range(len(newList)):
		for j in range(newList[i]):
			res_list.append(i)
	return res_list

nums = [5,7,10,2,8,0,0,1,5,7,9]
print("计数排序：")
print(sortArray_countingSort(nums))


'''
桶排序
将数据分类，每个类相当于一个桶，然后对每个桶里面的数据进行排序，最后将桶里的数据倒出来，组成结果数据
'''
def sortArray_bucketSort(nums):
	count = len(nums)
	if count == 0 or count == 1:
		return nums

	## 
	# 0 < value < 100
	# 100 <= value < 200
	# 200 <= value < 300
	# 300 <= value < 400
    
 	#创建桶
	bucketCount = 4
	bucketLists = [[] for i in range(bucketCount)]
 	
 	#分类，分别装入不同的桶中
	for i in range(len(nums)):
 		value = nums[i]
 		if value > 0 and value < 100:
 			bucketLists[0].append(value)
 		elif(value >= 100 and value < 200):
 			bucketLists[1].append(value)
 		elif(value >= 200 and value < 300):
 			bucketLists[2].append(value)
 		elif(value >= 300 and value < 400):
 			bucketLists[3].append(value)


	result_list = []
	# 将桶中的数据取出来
	for i in range(len(bucketLists)):
		#取出来之前先给每个桶中的数据排序
 		bucketList = sortArray_quicksort(bucketLists[i],0,len(bucketLists[i])-1)
 		for j in range(len(bucketList)):
 			result_list.append(bucketList[j])

	return result_list



nums = [5,7,10,100,101,101,300,301,302,301,303,305,200,207,201,201,204]
print("桶排序：")
print(sortArray_bucketSort(nums))


'''
堆排序

利用堆的结构体进行排序算法

堆的性质：子结点的值或者索引总是大于或者小于它的父结点

大顶堆：父结点大于子结点
小顶堆：子结点大于父结点
'''

# def sortArray_heapSort():
	#1.先将数据转化成堆的形式，初始堆
	#
	#2.将堆
	#
	#3.




# nums = [5 ,7,10,2,8,0,1,9]
# print("堆排序：")
# print(sortArray_heapSort(nums))





















	
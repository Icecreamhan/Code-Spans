# 问题
"""
给定一个整数数组 nums，其中每个元素的值在 [1, n] 之间（n 是数组的长度），某些元素可能出现了两次而其他元素则只出现了一次。
请找出所有出现次数超过一次的元素，并以列表形式返回这些元素。要求时间复杂度为 O(n)，空间复杂度为 O(1)（不考虑输出结果所占用的空间）。
输入: nums = [4,3,2,7,8,2,3,1]
输出: [2,3]
解释: 数组中 2 和 3 出现了两次。
"""

# 链接：442 数组中重复的数据
# https://leetcode.cn/problems/find-all-duplicates-in-an-array/description/
# 思路
"""
数组长度 n
每个元素的值在[1,n]范围内
某些数字出现了两次，有些只出现一次

核心思路：原地标记法

具体做法：
1、遍历数组中的每个元素 nums
2、将nums的元素值视作索引（注意取绝对值），即 index = abs(num)-1
3、将 nums[index]的值变为负数，表示这个数字已经被访问过一次了
4、那么，如果某次访问时发现 nums[index]<0，说明之前已经访问过这个数字了，它出现了重复

"""


def filterduplicate(nums):
    res = []
    for num in nums:
        index = abs(num)-1  # 找到对应的索引，为什么不直接用nums[num]呢？因为num可能是负数，但是他们的绝对值又是一样的，因此去绝对值就可以解决这个问题。
        if nums[index] < 0:
            res.append(abs(num))
        else:
            nums[index] = -nums[index]
    return res

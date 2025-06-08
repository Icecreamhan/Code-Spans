"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：

输入：nums = [1,0,1,2]
输出：3

提示：
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
# 题目：128 最长连续序列
# 链接
# https://leetcode.cn/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-100-liked
# 思路
"""
！！！ 先去重 ！！！
如果目标值 x 的前一位数字不在整数数组中，就把他添加到哈希表中，
然后遍历他的后面x+1、x+2、x+3……几位，直到？
如果 x 的前一位数字在整数数组中，说明他有和他的x-1构成过序列，因此，不考虑了

换句话说：
每个数都判断一次这个数是不是连续序列的开头那个数。

！！！注意！！！
实现循环的两种方式：
for循环：需要知道终止或者循环次数
whlie，只需要知道终止条件就可以！（更好用）
"""


def longestconsecutive(nums):
    nums_set = set(nums)
    longest = 0

    for num in nums_set:
        if num -1 not in nums_set:
            sublength = 1

            while num + sublength in nums_set:
                sublength += 1

            longest = max(longest, sublength)

    return longest


nums = [0,3,7,2,5,8,4,6,0,1]
res = longestconsecutive(nums)
print(res)
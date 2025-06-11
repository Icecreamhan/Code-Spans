"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
示例 1：
输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：
输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
提示：
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序
"""
# 题目：977.有序数组的平方
# 链接：
# https://leetcode.cn/problems/squares-of-a-sorted-array/description/
# 思路：
"""
# 方法一：
先全部平方，再排序

# 方法二：相向指针
    先初始化一个空数组，维度与给定数组相同，
    因为涉及负数，因此，初始化两个左右指针。
    - 比较左右指针位置处的平方值，依次从后向前放入初始化的空数组中
    - 比较左右指针位置处的值，-left与right的大小，依次从后向前放入初始化的空数组中，

    对于一个 非递减顺序的 整数数组
    如果 数组全部为正数时，
    i<j，-i<0<j，i^2 < j^2
    如果 数组全部为负数时，
    i<j，-i>0>j，i^2 > j^2
    如果 数组有正有负时，
    i<j，如果-i>j，那么i^2>j^2；如果-i<j，那么i^2<j^2
    
    
# 知识点：
1、排序函数j.sort()与 i = sorted(j)
    - sort是直接改变原始的；str_1.sort()会改变原始的字符串str_1，原地更改/原址排序
    - sorted是返回一个新的有序的列表。而sorted(str_1)是返回一个有序的副本，类型总是列表
"""


def sortedSquares(nums):
    # # 方法一：先全部平方，再排序
    # return sorted(num*num for num in nums)

    # # 方法二：双向指针
    # n = len(nums)
    # result_nums = [0] * n
    #
    # left = 0
    # right = n-1
    # pos = n-1
    #
    # while left <= right:
    #     x = nums[left] * nums[left]
    #     y = nums[right] * nums[right]
    #
    #     if x < y:
    #         result_nums[pos] = y
    #         right -= 1
    #     else:
    #         result_nums[pos] = x
    #         left += 1
    #     pos -= 1
    #
    # return result_nums

    # 方法三 双指针
    n = len(nums)

    result_nums = [0] * n

    left, right = 0, n - 1

    for index in range(n - 1, -1, -1):
        x, y = nums[left], nums[right]
        if -x < y:
            result_nums[index] = y * y
            right -= 1
        else:
            result_nums[index] = x * x
            left += 1

    return result_nums

    # for index in range(n-1,-1,-1):
    #     if -nums[left] < nums[right]:
    #         result_nums[index] = nums[right] * nums[right]
    #         right -= 1
    #     else:
    #         result_nums[index] = nums[left] * nums[left]
    #         left += 1

    # return result_nums

"""
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

提示：
你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
"""
# 题目:704.二分查找
# 链接：
# https://leetcode.cn/problems/binary-search/description/
# 思路
"""
1. 二分法
对于一个有序的数据集合，每次查找都将查找的范围缩小为原来的一半，直到找到目标值或确定目标值的存在。

因此，使用二分查找的前提条件，必须是：有序且不重复的数组，此时就可以考虑用二分法.

2.区间的定义
对于二分法，往往对于while循环的终止条件（left<right,还是left<=right）；
以及指针移动到中间元素的相邻元素的位置还是移动到中间元素。

因此，记住下面这两个区间，遇到二分法就根据这两个区间的性质进行解答。
- 左闭右闭[,]
    * [1,1]区间是有效的
- 左闭右开[,)
    * [1,1)区间是无效的；[1,2)区间是有效的

3. python的除法
除法：/；返回的是浮点数
取整：//；向下取整。返回的是小数点前的整数；3.75向下取整为3
取余：%；返回的是余数。

4.计算中间位置
推荐写法：防止整数溢出问题。
middle = left + (right-left)//2

"""


def search(nums,target):
    # n = len(nums)
    # # 先实现方法一：左闭右闭
    #
    # left = 0
    # right = n-1
    #
    # while left <= right:    # 区间[1,1]也是有效的
    #     middle = (left+right) // 2  # 整除，向下取整
    #     if nums[middle] > target:   # 三种情况1：目标值在左区间
    #         right = middle - 1  # 因为middle处的位置已经被排除了
    #     elif nums[middle] < target:     # 三种情况2：目标值在右区间
    #         left = middle + 1
    #     else:   # 三种情况3：刚好找到目标值，其实此时区间[target,target]
    #         return middle
    #
    # return -1
# =================================================
    n = len(nums)
    # 实现方法2 左闭右开，记住，取不到右边界的值！！

    left = 0
    right = n   # 此时区间[0,n)

    while left < right:  # 他俩绝不会相等！
        middle = (left+right)//2
        if nums[middle] < target:   # 目标值在右区间
            left = middle + 1  # 移动左指针，注意，是左闭右开，因此，下一次循环，要从middle+1开始，因为middle已经被否认了
        elif nums[middle] > target:  # 目标值在左区间
            right = middle     # 移动右指针，注意，右区间不会被遍历到
        else:
            return middle

    return -1




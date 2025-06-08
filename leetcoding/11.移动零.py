"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。


示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]

提示:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""
# 题目：283 移动0
# 链接
# https://leetcode.cn/problems/move-zeroes/description/?envType=study-plan-v2&envId=top-100-liked
# 思路
"""
双指针：左右指针

左指针：指向移动完成元素的末尾
右指针：指向待遍历数组元素的开始

那么，
左指针左边的元素都是已经处理好的非0 元素
右指针左边的元素，直到左指针的位置，元素值都是 0

# 方法二
逐个遍历元素，如果为0，则不管
如果不为0 ，则加入到目标列表中，
最后，按照原始数组长度，把目标列表按0填充。
"""


def movezeros(nums):
    n = len(nums)
    if n < 2:
        return nums

    # 方法1：快慢指针
    right = 0
    left = 0
    while right < n:
        if nums[right] != 0:
            nums[left],nums[right], = nums[right],nums[left]
            left += 1
        right += 1

    # 方法2：填充法:更快
    # index = 0
    # for num in nums:
    #     if num != 0:
    #         nums[index] = num
    #         index += 1
    #
    # if index < n:
    #     for i in range(index,n):
    #         nums[i] = 0

    return nums


nums_1 = [0,1,0,3,12]
res = movezeros(nums_1)
print(res)
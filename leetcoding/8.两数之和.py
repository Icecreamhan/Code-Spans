"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案


进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？
"""
# 1.两数之和
# 链接：https://leetcode.cn/problems/two-sum/description/
# 思路
"""
创建一个哈希表，对于每一个 x，我们首先查询哈希表中是否存在 target - x，
然后将 x 插入到哈希表中，即可保证不会让 x 和自己匹配。

"""

"""
考虑，两数之和是否可以使用双指针法进行解决？
双指针法要求排序，但是题目中要求返回的是索引下标。
那么，如果题目要求返回的是那两个数相加，返回两数的数值的话，就可以使用双指针法了。
"""


def twosum(nums, target):
    n = len(nums)
    other = {}
    if n < 2:
        return []

    for index in range(n):
        diff = target - nums[index]
        if diff in other:
            return [other[diff], index]

        other[nums[index]] = index
    # for index in range(n):
    #     diff = target - nums[index]
    #     if nums[index] in other:
    #         return [other[nums[index]], index]
    #
    #     other[diff] = index
    return []


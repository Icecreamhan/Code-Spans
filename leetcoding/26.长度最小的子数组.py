"""
给定一个含有 n 个正整数的数组和一个正整数 target 。
找出该数组中满足其总和大于等于 target 的长度最小的 子数组 [nums_l, nums_l+1, ..., nums_r-1, nums_r] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。


示例 1：
输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：
输入：target = 4, nums = [1,4,4]
输出：1
示例 3：
输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

提示：
1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104

进阶：
如果你已经实现 O(n) 时间复杂度的解法, 请尝试设计一个 O(n log(n)) 时间复杂度的解法。
"""
# 题目：209 长度最小的子数组
# 链接：
# https://leetcode.cn/problems/minimum-size-subarray-sum/description/
# 思路：
"""
【滑动窗口】

- 题目中要求返回 满足条件的 子数组的长度，并返回最小子数组的长度，
- 因此，只需要收集 满足条件的 子数组的长度，再从中找到（过滤剩下）最小的长度。

双指针——>滑动窗口（两边都移动的双指针）
右指针： 子数组的末尾
左指针： 子数组的起始位置

1. 初始化一个子数组，right, left = 0, 0
2. 右指针不断往后遍历新元素
3. 当左右指针的区间和大于等于target时，这个子数组就找到了，
4. 此时，获取子数组的长度，length = right-left+1
5. 接下来开始找下一个满足规则的子数组，并更新 子数组的最小长度值result = min(result,length)
6. 更新左指针的位置，直到子数组的元素和小于target，再去更新右指针，
7. 所以更新左指针的过程属于是while循环。

那么什么时候while，什么时候for循环？
while，给出条件，不知道计数次数时
for 有循环的次数时。

知识点：
python中表示无限大的数\python中表示无限小的数

import math
x = math.inf
print(x)

y = -math.inf
print(y)

x = float('inf')
y = float('-inf')

"""


def minSubArrayLen(target, nums):
    n = len(nums)
    left, right = 0, 0
    # 定义一个最大值
    result = float('inf')  # 或者result = n+1；因为如果存在，最小数组长度，不会超过总区间长度+1
    sum = 0

    while right < n:
        sum = sum + nums[right]
        while sum >= target:
            result = min(result, right - left + 1)
            # 更新左指针
            sum -= nums[left]
            left += 1

        right += 1

    return result if result != float('inf') else 0

    # # -------------------暴力求解，超时报错---------------
    # if not nums:
    #     return 0
    #
    # n = len(nums)
    # minlength = float('inf') # minlength = n+1
    #
    # for left in range(n):
    #     cur_sum = 0
    #     for right in range(left,n):
    #         cur_sum += nums[right]
    #         if cur_sum >= target:
    #             minlength = min(minlength,right-left+1)
    #             break
    #
    # return minlength if minlength != float('inf') else 0


tt = 11
ns = [1,1,1,1,1,1,1,1]
res = minSubArrayLen(tt, ns)
print(res)


"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。


示例 1：

输入：[1,8,6,2,5,4,8,3,7]
输出：49
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1

提示：
n == height.length
2 <= n <= 105
0 <= height[i] <= 104

"""
# 题目：11.盛最多水的容器
# 链接
# https://leetcode.cn/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-100-liked
# 思路
"""
初始化一个最小值为可以存储的最大水量maxWater
逐个遍历数组元素，算出位置i可以存储的最大水量，

左右指针，
    终止条件：两个指针相遇
    移动条件：哪一个指针的水柱越低，就移动哪一个

用max(A,B)更新最大水量
"""

from typing import List


def maxArea(height: List[int]) -> int:
    maxwater = 0  # -inf
    n = len(height)
    # 左右指针
    left,right = 0,n-1
    while left < right:
        maxwater = max(min(height[left], height[right]) * (right-left), maxwater)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maxwater


    # # 暴力求解,超时
    # for slow in range(n):
    #     for fast in range(slow,n):
    #         area = min(height[slow],height[fast]) * (fast-slow)
    #         maxwater = max(maxwater,area)

    return maxwater




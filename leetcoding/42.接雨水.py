"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

示例 1：
输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例 2：
输入：height = [4,2,0,3,2,5]
输出：9

提示：
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
# https://leetcode.cn/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-100-liked

# 思路
"""
1、动态规划
获取每个位置，的左边最大的柱子高度
获取每个位置，的右边最大的柱子高度
可以得到每个子柱子上面的雨水，将所有子柱子上面的雨水累加

2、单调栈
栈：先进后出
栈顶元素、当前元素

3、双指针
"""

from typing import Type,List
def trap(height: List[int]) -> int:
    # 动态规划：
    # 初始化两个数组，用来存储，每个位置i的左侧最高柱子的高度、右侧最高柱子的高度
    n = len(height)
    leftheight, rightheight = [0 for _ in range(n)], [0 for _ in range(n)]

    leftheight[0] = height[0]
    for i in range(1,n):
        leftheight[i] = max(leftheight[i-1], height[i])

    rightheight[n-1] = height[n-1]
    for j in range(n-2, -1,-1):
        rightheight[j] = max(rightheight[j+1],height[j])
        
    ans = 0
    for i in range(n):
        ans += min(leftheight[i], rightheight[i])-height[i]  # 应该是两侧的最小值-子水柱本身的高度
        
    return ans



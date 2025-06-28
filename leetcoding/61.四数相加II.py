"""
给你四个整数数组 nums1、nums2、nums3 和 nums4 ，数组长度都是 n ，请你计算有多少个元组 (i, j, k, l) 能满足：
0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
示例 1：
输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
示例 2：
输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
输出：1
  提示：
n == nums1.length
n == nums2.length
n == nums3.length
n == nums4.length
1 <= n <= 200
-228 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 228
"""
# 题目：454.四数相加II
# 链接
# https://leetcode.cn/problems/4sum-ii/description/
# 思路
"""
哈希表的使用场景：在一个集合中判断某个元素是否出现过。
对于四个列表A,B,C,D,暴力求解时，需要嵌套四个循环，取不同元素相加，count++。n^4。

我们只需要求出 目标元素和出现的次数，而不需要考虑这四个元素（来自不同列表）是否重复。
因此，可以考虑使用哈希表，我们先遍历2个列表，记录两个列表中的元素和以及元素和出现的次数，再去遍历剩余的两个列表。

剩余两个列表中是否有我们想要的元素（四个元素相加=0的匹配项），如果有我们想要的元素那么就找到了目标四个元素和，count=map{a+b}+1

哈希结构：数组（元素数要可控）、set、map(key-value的场景)
key:是否出现过的元素和。
value:出现的次数。
"""


def foursumcount(nums1,nums2,nums3,nums4):
    # 方法0:使用defaultdict
    count = 0
    from collections import defaultdict
    sumcount = defaultdict(lambda: 0)

    for i in nums1:
        for j in nums2:
            sumcount[i + j] += 1

    for i in nums3:
        for j in nums4:
            count += sumcount.get(0 - i - j, 0)

    return count

    # # 方法一 使用defaultdict
    # count = 0
    # from collections import defaultdict
    # sumcount = defaultdict(int)
    ## sumcount = defaultdict(lambda:0)

    # for i in nums1:
    #     for j in nums2:
    #         sumcount[i+j] += 1

    # for i in nums3:
    #     for j in nums4:
    #         target = 0-(i+j)
    #         if target in sumcount:
    #             count += sumcount[target]

    # return count

    # # 方法二：使用dict()
    # count = 0
    # sumcount = {}

    # for i in nums1:
    #     for j in nums2:
    #         sumcount[i+j] = sumcount.get(i+j, 0) + 1

    # for i in nums3:
    #     for j in nums4:
    #         target = 0-(i+j)
    #         if target in sumcount:
    #             count += sumcount[target]

    # return count

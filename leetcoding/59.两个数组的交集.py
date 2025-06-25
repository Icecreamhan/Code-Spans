"""
给定两个数组 nums1 和 nums2 ，返回 它们的 交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

示例 1：
输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2
输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的

提示：
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
"""
# 题目：349两个数组的交集
# 链接
# https://leetcode.cn/problems/intersection-of-two-arrays/description/
# 思路
"""
输出结果中的每一个元素一定是唯一的，也就是 输出的结果是去重的，同时可以不考虑输出结果的顺序。

什么时候用数组，什么时候用map
数组：使用数组来做哈希的题目，是因为题目都限制了数值的大小。
    - 如果哈希值比较少、特别分散、跨度非常大，使用数组就造成空间的极大浪费。
set：不仅占用空间比数组大，而且速度慢，set把数值映射到Key上都要做hash计算。对于数据量大的情况，差距比较明显。

但是这道题没有限制数组的大小，因此无法使用数组做哈希表。

知识点：
set集合的相关运算方式
- 添加
a = set()
a.add([1,2])
只能是数字、字符串、元组或布尔类型，不能添加可变的数据。
- 删除
a = {1,2,3}
a.remove(1)
要确保删除的元素包含在集合中。
a.discard()
即使删除的元素不在集合中也不会报错。

- 交集
set1 & set2
- 并集
set1|set2
- 差集
set1-set2
- 对称差集
set1^set2
"""


def intersection(nums1, nums2):
    # 方法一：使用字典和数组
    # 先构建一个空字典存储出现在第一个数组中的元素及其出现的次数
    table = {}
    for i in nums1:
        table[i] = table.get(i, 0) + 1
    # 因为结果不重复，所以使用一个集合存储结果
    result = set() # result = []
    # 遍历第二个数组
    for i in nums2:
        if i in table:
            result.add(i) # result.append(i)
            del table[i]

    return list(result)




    # # 方法二，使用数组，最后将两个结果集进行相乘，如果大于0 则添加进去
    # result = []
    # # 使用数组
    # nums_1 = [0] * 1001
    # nums_2 = [0] * 1001
    # for num1 in nums1:
    #     nums_1[num1] += 1
    # for num2 in nums2:
    #     nums_2[num2] += 1
    # for i in range(1001):
    #     if nums_1[i] * nums_2[i] > 0:
    #         result.append(i)
    # return result



    # 方法2 ，不建议
    # result = []
    # nums = [0]*1001
    # for i in set(nums1):
    #     nums[i] += 1
    # for i in set(nums2):
    #     nums[i] += 1
    # for i in nums:
    #     if i == 2:
    #         result.append(i)
    # return result

    # # 方式三：只使用集合
    # set_nums1 = set(nums1)
    # set_nums2 = set(nums2)
    #
    # return list(set_nums1 & set_nums2)

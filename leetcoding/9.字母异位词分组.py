"""
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]


提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母
"""
# 题目：49.字母异位词分组
# 链接
# https://leetcode.cn/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-100-liked
# 思路
"""
希尔排序
python中的希尔排序使用字典
思路一
将每个字符串进行排序，因为字母对应的是acsii编码，因此也可以使用sort进行排序，将排序后的字符作为键，原始的字符串作为值。

思路二
一共有26个英文字母，因此我们找一个一维数组（列表），字母出现，则对应的位置上的值为1，相同的字母组成的新单词，其一位数组一样。
注意，python的字典中，键的类型有整数、浮点数、字符串、元组
因此，我们使用tuple()将列表转为元组，作为字典的键
"""
# 注意
"""
1、sorted(str_1)返回的结果是list，因此需要用"".join()转为字符串
2、sort与sorted
    - str_1.sort()会改变原始的字符串str_1，原地更改/原址排序
    - 而sorted(str_1)是返回一个有序的副本，类型总是列表
3、普通字典dict 不能自动创建未定义的键值对。
    因此需要使用 defaultdict(list)来解决这个问题
    form collections import defaultdict
    
    result = defaultdict(list)
    
    这样我们创建的result就可以自动创建未定义的键值对了
4、获取的字典的值
    - dict_1.values() ，其类型为：<class 'dict_values'>
    获取字典的键
    - dict_1.keys(), 返回的是一个dict_keys类型的对象（可迭代），不是普通的列表，而是一个视图对象，这个对象会动态的反映字典的变化
    
    因此，我们是需要转为列表
    list(dict_1.keys())
    list(dict_1.values())

"""


def groupanagrams(strs):
    from collections import defaultdict
    n = len(strs)
    if n < 2:
        return [strs]
    result = defaultdict(list)
    for sub_str in strs:
        key = "".join(sorted(sub_str))
        # if key not in result:
        #     result[key] = []
        result[key].append(sub_str)
# # 将<class 'dict_values'>类型转为list

    # # 方法二：使用26维度的元组
    # for sub_str in strs:
    #     # 初始化一个26个元素的列表
    #     key = [0]*26
    #     # 获取每个元素的索引
    #     for i in sub_str:
    #         index = ord(i) - ord("a")
    #         key[index] += 1
    #     result[tuple(key)].append(sub_str)

    return list(result.values())



strs_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]

res = groupanagrams(strs_1)

print(res)

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
示例 1:
输入: s = "anagram", t = "nagaram"
输出: true
示例 2:
输入: s = "rat", t = "car"
输出: false
提示:
1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
"""
# 题目：242.有效的字母异位词
# 链接
# https://leetcode.cn/problems/valid-anagram/description/
# 思路：
"""
什么是有效字母异位词：
给定两个字符串，判定这两个字符串，是不是由相同的字母组成，但是字母的位置可以不一样。
重复的元素以及重复的次数也要保持一样。

使用[哈希表]
哈希表定义：根据关键码的值而直接进行访问的数据结构。
哈希表中关键码就是数组的索引下标，通过下标直接访问数组中的元素。
哈希表的用法：一般都是用来 快速判断一个元素是否出现在集合里。
特点：牺牲了空间换取时间。
哈希表的三种数据结构：数组、set(集合)、map(映射)
- 范围可控用数组
- 数值很大就用set
- 如果k对应的value的话就用map

注意双层循环和双循环是不一样的。
"""


def isAnagram(s: str, t: str) -> bool:
    # 方式1 使用map
    from collections import defaultdict

    # 定义两个字典
    dic_s, dic_t = defaultdict(int), defaultdict(int)

    for i in s:
        dic_s[i] += 1

    for i in t:
        dic_t[i] += 1

    return dic_s == dic_t

    # # 使用数组，因为都是小写英文字母，那么我们定义一个维度为26的数组，出现某个字母，就在这个字母索引/位置上+=1
    # record = [0]*26
    # for i in s:
    #     index = ord(i) - ord('a')
    #     record[index] += 1
    # for i in t:
    #     index = ord(i) - ord('a')
    #     record[index] -= 1
    #
    # for i in range(26):
    #     if record[i] != 0:
    #         return False
    #
    # return True
    #
    # # 方式3，使用counter
    # from collections import Counter
    # s_count = Counter(s)
    # t_count = Counter(t)
    # return s_count == t_count




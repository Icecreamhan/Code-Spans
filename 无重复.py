"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3
"""
""""
ord()

"""


def unduplicatestrs(strs):
    from collections import defaultdict
    strs_list = list(strs)
    n = len(strs)
    result = defaultdict(list)

    right = 0
    # left = 0
    while right < n:
        if strs_list[right] not in result:
            result[strs_list[right]] = 1
        else:
            result[strs_list[right]] += 1

    return len(result)


s = "abcabcbb"
res = unduplicatestrs(s)
print(res)
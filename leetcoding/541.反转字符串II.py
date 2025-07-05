"""
给定一个字符串 `s` 和一个整数 `k`，从字符串开头算起，每计数至 `2k` 个字符，就反转这 `2k` 字符中的前 `k` 个字符。
如果剩余字符少于 `k` 个，则将剩余字符全部反转。
如果剩余字符小于 `2k` 但大于或等于 `k` 个，则反转前 `k` 个字符，其余字符保持原样。

示例 1：
输入：s = "abcdefg", k = 2
输出："bacdfeg"

示例 2：
输入：s = "abcd", k = 2
输出："bacd"

提示：
- `1 <= s.length <= 10^4`
- `s` 仅由小写英文组成
- `1 <= k <= 10^4`
"""
# 链接
# https://leetcode.cn/problems/reverse-string-ii/description/
# 思路：
"""
要求计数2*k个字符时，就反转这2k个字符的前k个。
要找每2*k区间的起点。
那么在遍历字符串的过程中，让指针每次移动2*k个就可以，i+=(2*k)，
然后判断是否需要有反转的区间。
    - 剩余字符串大于等于k的情况
    - 剩余字符串不足k的情况
怎么知道剩余字符串长度呢？

** 当需要固定规律一段一段去处理字符串时，考虑在for循环表达式上进行界定。**
"""

"""
1. 使用range(start,end,step)来确定需要调换的初始位置
2. 对于字符串s = 'abc'，如果使用s[0:999]===>'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
3. 用切片整体替换，而不是一个个替换。

"""


def reverseStr(s,k):
    n = len(s)
    s = list(s)
    for i in range(0,n,2*k):
        if i+k <= n-1:
            left, right = i, i+k-1
            while left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1

        else:
            left = i
            right = n-1
            while left < right:
                s[left],s[right] = s[right],s[left]
                left += 1
                right -= 1

    return "".join(s)


def reverseStr(s,k):
    # 因为给的是字符串，因此需要先转为字典，字符串时不可更改的
    i = 0
    chars = list(s)

    while i < len(s): # 因为如果i+k超过字符串总长度了，那么也会取字符串最后一个值，
        # 所以末尾长度length如果length<k,那么只会是[i:length]的位置进行翻转，如果k<length<2k,那么只会[i:i+k]的字符串进行翻转
        chars[i,i+k] = chars[i,i+k][::-1] # 反转后，更改原值为反转后值
        i += 2*k

    return "".join(chars) # 需要返回字符串


# 先定义一个反转函数
def reverse_substr(lst):
    left,right = 0,len(lst)-1
    while left < right:
        lst[left],lst[right] = lst[right],lst[left]
        left += 1
        right -= 1

    return lst

def reverseStr(s,k):
    res = list(s)

    for cur in range(0,len(s),2*k):
        res[cur:cur+k] = reverse_substr(res[cur:cur+k]) # 对指定区间的列表进行反转

    # 返回字符串
    return "".join(res)



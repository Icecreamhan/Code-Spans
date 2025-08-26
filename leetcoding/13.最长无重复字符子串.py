"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3


示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""
# 题目：3.无重复字符的最长子串
# 链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-100-liked

# 思路：
"""
滑动窗口:左右指针，快慢指针。

设置一个字典 用来记录每个字符以及出现的索引
右指针逐个向右遍历
当出现重复字符时，左指针更显到重复字符的下一位。

列表都是左闭右开的[left,right)
s[1:1)

"""

# 不重复窗口的长度，因此每次移动都确保窗口内的元素不重复
def lengthoflongestsubstring(s):
    if not s:
        return 0
    maxlength = 0  # 每次更新max(A,B)
    n = len(s)
    if n == 1:
        return 1
    subindex = {s[0]: 0}  # 记录字符，及其索引，当出现重复字符时，更新索引值
    left, right = 0, 0
    while right < n - 1:  # 右指针向右逐个遍历
        if s[right + 1] in s[left:right + 1]:  # 当右指针的下一位重复出现时
            left = subindex.get(s[right + 1], right + 1) + 1  # 更新左指针
        right += 1  # 移动右指针
        subindex[s[right]] = right  # 更新字符及其索引值
        maxlength = max(maxlength, (right - left + 1))  # 记录不重复窗口的长度
    return maxlength


    # char_index = {}  # 存储字符最近出现的位置
    # left = 0  # 窗口左边界
    # max_len = 0  # 记录最大长度

    # for right in range(len(s)):
    #     if s[right] in char_index:
    #         # 如果字符重复，并且重复位置在窗口内，移动左边界
    #         left = max(left, char_index[s[right]] + 1)
    #     # 更新字符位置
    #     char_index[s[right]] = right
    #     # 更新最大长度
    #     max_len = max(max_len,right-left+1)

    # return max_len
    # 先设置一个最长子串长度


a = " "
print(len(a))
print(lengthoflongestsubstring(a))


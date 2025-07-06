"""
给你一个字符串 s ，请你反转字符串中 单词 的顺序。
单词 是由非空格字符组成的字符串。s 中使用至少一个空格将字符串中的 单词 分隔开。
返回 单词 顺序颠倒且 单词 之间用单个空格连接的结果字符串。
注意：输入字符串 s中可能会存在前导空格、尾随空格或者单词间的多个空格。返回的结果字符串中，单词间应当仅用单个空格分隔，且不包含任何额外的空格。

示例 1：
输入：s = "the sky is blue"
输出："blue is sky the"

示例 2：
输入：s = "  hello world  "
输出："world hello"
解释：反转后的字符串中不能存在前导空格和尾随空格。

示例 3：
输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，反转后的字符串需要将单词间的空格减少到仅有一个。

提示：
- 1 <= s.length <= 10^4
- s 包含英文大小写字母、数字和空格 ' '
- s 中 至少存在一个 单词

进阶：如果字符串在你使用的编程语言中是一种可变数据类型，请尝试使用 O(1) 额外空间复杂度的 原地 解法。
"""
# 链接
# https://leetcode.cn/problems/reverse-words-in-a-string/description/
# 思路
"""
1. 将原字符串进行一个整体反转
2. 再对每一个单词里面进行一次反转
3. 把多余的空格删除掉
    参考---移除元素：使用快慢指针

尝试一下：要求空间复杂度为o(1)

python中简单的操作方法：
1.先使用split(" "),将单词分隔开
2.再逆序存到结果字符串中。

--- 这样做就没有做题的意义了。
"""


def reverse_substr(lst):
    n = len(lst)
    left,right = 0,n-1
    while left < right:
        lst[left],lst[right] = lst[right],lst[left]
        left += 1
        right -= 1
    return lst

def reverseWord(s):
    n = len(s)
    s = list(s)
    # 1. 实现字符串的整体反转
    # 由于python中字符串的不可变性，因此只能转换为列表进行处理
    s = reverse_substr(s)
    result = ""

    # 2. 先实现移除多余的空格: 快慢指针
    fast = 0
    while fast < n:
        if s[fast] != " ":
            if len(result) != 0:
                result += " "
            while fast < len(s) and s[fast] != " " :
                result += s[fast]
                fast += 1
        else:
            fast += 1
            # print # drow olleh
    # 3. 实现每个单词的反转
    slow,fast = 0,0
    result = list(result)
    while fast <= len(result):
        if fast == len(result) or result[fast] == " ":
            result[slow:fast] = reverse_substr(result[slow:fast])
            fast += 1
            slow = fast
        else:
            fast += 1 # 只为了寻找空格
    return "".join(result)


# 方法三：利用字符串反转+split()
# 翻转字符串
# 按照空格切分字符串
# 反转每个单词
def reversewords(s):
    # 字符串反转
    s = s[::-1]
    # 将字符串拆分为单词，并反转每个单词
    # split()能够自动忽略多余的空白字符
    s = " ".join(word[::-1] for word in s.split())
    return s


# 方法二：利用python自带的split()函数 + 双指针
def reverseWord(s):
    # 删除多余空格
    words = s.split() # ["hello","word"]
    # 反转列表
    left,right = 0,len(words)-1
    while left < right:
        words[left],words[right] = words[right],words[left]
        left += 1
        right -= 1

    # 将列表组装成字符串
    return " ".join(words)


# 方法四 拆分字符串+ 反转列表
def reverseword(s):
    words = s.split()  # type(words) --- list ["hello","word"]
    words = words[::-1]  # 反转单词  --- list["word","hello"]
    return " ".join(words)   # 拼接为字符串


# 方法五：按顺序收集单词，再对单词列表进行反转
def reversewordss(s):
    words = []
    s += " " # 帮助处理最后一个单词
    word = "" # 用来收集出现的单词

    for char in s:
        if char == " ": # 说明前面有单词
            if word != "":
                words.append(word)
                word = ""
            continue
        word += char  # 收集空格前单词的字母

    words.reverse() # 对单词列表进行反转
    return " ".join(words)


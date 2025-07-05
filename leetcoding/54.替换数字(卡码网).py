"""
给定一个字符串 s，它包含小写字母和数字字符，请编写一个函数，将字符串中的字母字符保持不变，而将每个数字字符替换为number。 例如，对于输入字符串 "a1b2c3"，函数应该将其转换为 "anumberbnumbercnumber"。

输入描述
输入一个字符串 s,s 仅包含小写字母和数字字符。

输出描述
打印一个新的字符串，其中每个数字字符都被替换为了number

输入示例
a1b2c3

输出示例
anumberbnumbercnumber

提示信息
数据范围：
1 <= s.length < 10000。
"""

# 链接
# https://kamacoder.com/problempage.php?pid=1064
# 思路
"""
1. 扩充数组到每个数字字符替换成"number"之后的大小。
2. 从后向前替换数字字符，（双指针），过程如下：i指向新长度的末尾，j旧长度的末尾。
（为什么不是从前往后呢？）==>因为这样会导致每次添加元素都要将添加元素之后的所有元素整体向后移动。


总结：很多数组填充类的问题，都是先预先给数组扩容带填充后的大小，然后从后向前进行操作。
优势：1. 不用申请新数组。2. 从后向前填充元素，避免了从前向后填充元素时，每次添加元素都要将添加元素之后的所有元素向后移动的问题。
"""

"""
字符串和数组的差别：

字符串：若干字符组成的有限序列，是一个字符数组。

[""] * extend_len → 创建一个含有 extend_len 个空字符串的列表
[] * extend_len → 仍然是一个空列表，几乎没用

"""


class Solution(object):
    def subsitute_nums(self,s):
        n = len(s)
        # 1.先统计字符串中有几个数字,        # 先统计字符串中出现的数字个数
        count = sum(1 for char in s if char.isdigit())
        # 2. 我们定义一个新的空字符串，用来接收最终的结果
        # 扩展后的字符长度应该变为
        extend_len = n + (count*5)  # 计算扩充后的字符串大小 x->number,每有一个数字就要增加5个长度
        res = [""]*extend_len  # 使用新的空数组保存结果

        # 3.定义两个新旧指针，同时从后向前遍历进行填充。指针初始分别指向新旧字符串的末尾
        new,old = extend_len-1,n-1  # # 定义两个新旧指针，新指针指向 结果数组(扩充后字符串) 的末尾，旧指针指向旧数组(原字符串)的末尾
        # 从后向前遍历 原字符串
        while old >= 0:
            if s[old].isdigit():
                res[new-5:new+1] = "number"
                new -= 6
            else:
                res[new] = s[old]
                new -= 1
            old -= 1

        return "".join(res)


if __name__ == "__main__":
    solution = Solution()

    while True:
        try:
            s = input()
            result = solution.subsitute_nums(s)
            print(result)
        except EOFError:
            break



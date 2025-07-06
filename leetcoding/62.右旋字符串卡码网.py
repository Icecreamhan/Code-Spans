"""
题目描述
字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。
例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。

输入描述
输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。

输出描述
输出共一行，为进行了右旋转操作后的字符串。

输入示例
2
abcdefg

输出示例
fgabcde

提示信息
数据范围：
1 <= k < 10000,
1 <= s.length < 10000;
"""
# 链接
# https://kamacoder.com/problempage.php?pid=1065
# 思路
"""
# 面试遇到过这个题目。。。。哭泣

我先想想如何使用刚刚的方法做出来：
先把字符串改为列表，我先拼接后面长度为k字符串，再拼接剩余的字符串，也可以实现
但是这种方式申请了额外的空间。

那么是否可以不申请额外空间来实现呢？
方式一：先整体反转，再局部反转
s="abcdef",k=2
先整体反转==》rev_s ="fedcba" 
再局部反转==》rev_s_2 = "efabcd"就实现了我们的目标
方法二：先局部反转，再整体反转。
先局部反转==> rev_s = "dcbafe"
再整体反转==>rev_s_2 = "efabcd" 也实现了我们的目标

拓展：如果要求左旋转，怎么实现？
s= "abcdef",k=2,要求输出："cdefab"
同样，先整体反转，再局部反转
整体反转：fedcba,
再局部反转：cdefab
只是反转的区间不同。
当然，先局部翻转，再整体反转也可以
局部反转：dcbafe
整体反转：efabcd


整体反转不难，但是局部反转如何实现？确定区间，使用字符串反转[::-1]
"""

"""
知识点
字符串切片[start:end:step]
当step>0时，从左向右遍历，此时，start默认为0，end默认为len(s)，一般情况下：start<end,
当step<0时，start>end(start>0),从右向左遍历，此时，start默认为-1或者len(s)-1，end默认为-len(s)-1，比第一个字符前的位置，

当使用负步长（如 -1）时，确保 start > end，否则结果为空字符串。


Python 切片 s[start:end:step] 的行为如下：

- 当 step > 0:
  - 方向：从左向右
  - start 默认为 0
  - end 默认为 len(s)
  - 通常要求 start < end，否则结果为空字符串

- 当 step < 0:
  - 方向：从右向左
  - start 默认为 len(s) - 1（即最后一个字符）
  - end 默认为 -len(s) - 1（即比第一个字符的前一个位置）
  - 通常要求 start > end，否则结果为空字符串

注意：如果 start 和 end 的顺序与 step 的方向不一致，结果为空字符串。
"""

# 这种方式申请了额外的空间，
def rightsubstr(s,k):
    n = len(s)
    s = list(s)
    print("".join(s[n-k:]) + "".join(s[:n-k]))
    # print("".join(s[n - k:n]) + "".join(s[0:n - k]))


# 通过字符串切片实现
def right(s,k):
    n = len(s)
    # 先取出后k个字符串s[n-k:]/s[-k:]，再取出前面剩余的字符串[:n-k]/[:-k]
    s = s[n-k:] + s[:n-k]
    print(s)
    return s

def rightsub(s,k):
    print(s[-k:]+s[:-k])

if __name__ == "__main__":
    k = int(input())
    s = input()
    print(rightsub(s,k))

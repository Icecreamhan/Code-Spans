"""
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

示例 1：
输入：n = 19
输出：true
解释：
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
示例 2：
输入：n = 2
输出：false

提示：
1 <= n <= 231 - 1
"""
# 题目：202.快乐数
# 链接：
# https://leetcode.cn/problems/happy-number/description/
# 思路：
"""

divmod() 是 Python 的内置函数，用于同时返回除法和取余的结果。
它接受两个参数，表示被除数和除数，返回一个包含两个值的元组，第一个值表示相除的商，第二个值表示相除的余数
num1 = 10
num2 = 3
result = divmod(num1, num2)
print(result) # 输出: (3, 1)
"""


# 给定一个整数 求 这个数 每个位置上的数字的平方和：
def getsum(n):
    num_sum = 0
    while n:
        n,r = divmod(n,10)
        num_sum += r**2
    return num_sum

def getsum(n):
    return sum(int(i)**2 for i in str(n))

def getsum(n):
    num_sum = 0
    for i in str(n):
        num_sum += int(i)**2
    return num_sum


# 如果得到的数据和曾经出现过，那么说明会陷入死循环，因此把每次得到的新的结果存到一个集合中，每次计算得到新的值时都与原有的集合进行比较。
def isHappy(n: int) -> bool:
    result = set()
    while n not in result:
        result.add(n)
        numsum = getsum(n)
        if numsum == 1:
            return True
        n = numsum
    return False
    # seen = []
    # while n != 1:
    #     if n in seen:
    #         return False
    #     seen.append(n)
    #     n = getsum(n)

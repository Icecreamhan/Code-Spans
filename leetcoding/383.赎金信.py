"""
给你两个字符串：ransomNote 和 magazine ，判断 ransomNote 能不能由 magazine 里面的字符构成。
如果可以，返回 true ；否则返回 false 。
magazine 中的每个字符只能在 ransomNote 中使用一次。
示例 1：
输入：ransomNote = "a", magazine = "b"
输出：false
示例 2：
输入：ransomNote = "aa", magazine = "ab"
输出：false
示例 3：
输入：ransomNote = "aa", magazine = "aab"
输出：true
提示：
1 <= ransomNote.length, magazine.length <= 105
ransomNote 和 magazine 由小写英文字母组成
"""
# 题目：383.赎金信
# 链接：
# https://leetcode.cn/problems/ransom-note/description/
# 思路
"""
哈希表：在一个集合中，来判断一个元素是否出现过。
- magazine中的元素只能在ransomnote中使用一次
- 都是小写字母

因此可以考虑使用哈希法：但是使用数组还是map，数组是有范围的。
而map的空间消耗要比数组大，因为map要维护红黑树或者哈希表，而且还要做哈希函数，是费时的，数据量大的话，数组更有效。
# 方法一：数组

# 方法二：哈希表
先遍历ransomNote，记录字符以及出现的次数。map1
再遍历magazine，如果map1(magazine)，存在，map1-= 1，最后，看map1中的元素值是否都为0，如果都为0 ，那么返回true，否则返回false
"""

# 知识点
"""
计数：
.count()与counter
# .count()
是一个方法，属于某些内置数据类型，如list、str、tuple
作用：统计某个元素在序列中出现的次数
特点：1、只能用于查找某个特定元素出现的次数
2、是一个简单快速的统计方式。
3、不会返回所有元素的计数结果，只能查询单个元素
```
s = "hello world"
print(s.count('l'))  # 输出：3

lst = [1, 2, 3, 2, 2]
print(lst.count(2))  # 输出：3
```

# counter
是collections模块中的一个类，用于进行更复杂的计数操作。
作用：对整个可迭代对象（列表、字符串等）进行元素计数，并返回一个字典形式的对象，表示每个元素及其出现的次数。
特点：1、可以一次性统计所有元素的出现次数
2、支持一些高级操作，合并计数器、相减、交集、并集
3、结果是一个类似字典的对象，可以方便地访问各个元素的计数。
```
from collections import Counter

s = "hello world"
cnt = Counter(s)
print(cnt)

# 输出类似：
# Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ...})
```

```
lst = [1, 2, 3, 2, 2]
cnt = Counter(lst)
print(cnt)  # 输出：Counter({2: 3, 1: 1, 3: 1})
```

# 总结:
- 如果只想知道某个元素出现了几次 ，使用.count()
- 如果想知道所有元素各出现了多少次，使用counter

counter的减法

## Counter 减法的规则：
1. 对于每一个键（key)，如果在两个counter中都存在，则结果是它们的值相减。
2. 如果结果大于0，才保留这个键
3. 如果结果小于等于0，则不保留这个键。

## 总结
- Counter 的减法不会自动报错，而是默默地把负值去掉。
- Counter 只包含非零项。
"""


def canConstruct(ransomNote: str, magazine: str) -> bool:
    # 方法8:count
    if len(ransomNote) > len(magazine):
        return False
    return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote)) # 如果ransonNote中每个元素出现的次数都小于等于magazine时


    # # 方法9：使用count
    # for char in ransomNote:
    #     if char in magazine and ransomNote.count(char) <= magazine.count(char):
    #         continue
    #     else:
    #         return False
    #
    # return True

    # # 方法10：使用counter
    # from collections import Counter
    # return not Counter(ransomNote) - Counter(magazine)






    # # 方法七：使用defaultdict
    # from collections import defaultdict
    # if len(magazine) < len(ransomNote):
    #     return False
    #
    # cur = defaultdict(int) # cur = defaultdict(lambda:0)
    # for i in magazine:
    #     cur[i] += 1
    #
    # for j in ransomNote:
    #     value = cur.get(j)
    #     if not value:
    #         return False
    #     else:
    #         cur[j] -= 1 # 好奇，cur值不会为-1吗？
    #
    # return True


    # # 方法六：使用defaultdict
    # from collections import defaultdict
    # if len(magazine) < len(ransomNote):
    #     return False
    #
    # cur = defaultdict(int) # cur = defaultdict(lambda:0)
    # for i in magazine:
    #     cur[i] += 1
    #
    # for j in ransomNote:
    #     if j not in cur or cur[j] == 0:
    #         return False
    #     cur[j] -= 1
    #
    # return True


    # # 方法五，数组，使用两个数组
    # if len(magazine) < len(ransomNote):
    #     return False
    #
    # ran, mag = [0]*26, [0]*26
    # for i in ransomNote:
    #     ran[ord(i) - ord("a")] += 1
    #
    # for j in magazine:
    #     mag[ord(j) - ord("a")] += 1
    #
    # # for i in range(26):
    # #     if ran[i] > mag[i]:
    # #         return False
    # #
    # # return True
    # return all(ran[i] <= mag[i] for i in range(26))


    # # 方法四：数组，先遍历magazine
    # res = [0] * 26
    # for i in magazine:
    #     res[ord(i) - ord("a")] += 1
    #
    # for j in ransomNote:
    #     res[ord(j) - ord("a")] -= 1
    #
    # for i in res:
    #     if i < 0:
    #         return False
    #
    # return True

    # # 方法三：数组，先遍历ransomNote
    # res = [0] * 26
    # for i in ransomNote:
    #     res[ord(i) - ord("a")] += 1
    #
    # for j in magazine:
    #     res[ord(j) - ord("a")] -= 1
    #
    # for i in res:
    #     if i > 0:
    #         return False
    #
    # return True




    # # 方法一：map，先遍历magazine
    # if len(magazine) < len(ransomNote):
    #     return False
    #
    # cur = {}
    # for i in magazine:
    #     cur[i] = cur.get(i,0) + 1
    #
    # for j in ransomNote:
    #     if j in cur:
    #         cur[j] -= 1
    #         if cur[j] == 0:
    #             del cur[j]
    #     else:
    #         return False
    # return True

    # 方法二：map，先遍历ransomNote
    # if len(magazine) < len(ransomNote):
    #     return False
    # cur = {}
    #
    # for i in ransomNote:
    #     cur[i] = cur.get(i, 0) + 1
    #
    # for j in magazine:
    #     if j in cur:
    #         cur[j] -= 1
    #         if cur[j] <= 0:
    #             del cur[j]
    #
    # for i in cur:
    #     if cur[i] > 0:
    #         return False
    #
    # return True

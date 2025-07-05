"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。
不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

示例 1：
输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：
输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

提示：
1 <= s.length <= 105
s[i] 都是 ASCII 码表中的可打印字符
"""
# 题目 344.反转字符串
# 链接
# https://leetcode.cn/problems/reverse-string/description/
# 思路
"""
双向指针
"""

# 知识点
"""
reverse()与reversed()

1. reverse()
- 是列表(list)的方法
- 原地反转列表元素的顺序，没有返回值（返回None）
- 会修改原始列表
- 只能用于**可变列表**
- 不适用于字符串、元组等不可变类型
- 不会生成新对象

```python
lst = [1,2,3,4]
lst.reverse()
print(lst) # 输出：[4,3,2,1]
```

2. reversed()
- 是一个内置函数
- 接收任何 **可迭代对象（列表、字符串、元组、range等）**
- 返回一个 逆序迭代器对象（新的对象），不是列表或字符串本身
- 如果需要字符串结果，可以再用''.join()转换
- 不会修改原始对象
- 通常配合`list()`、`tuple()`或`for`循环使用

```python
s= "hello"
rev = reversed(s)
print(list(rev)) # 输出 ['o','l','l','e','h']
```

```python
lst = [1,2,3,4]
print(list(reversed(lst))) # 输出：[4,3,2,1]

```
python切片语法：s[::-1]
- s[start:end:step]表示从start到end(不包含)，以step为步长取元素
- 当step= -1时，表示从后往前取元素，即返回一个反转后的列表副本。
```python
list = [1,2,3,4,5,6]
print(list[-1:1:-1]) # [6,5,4,3]
```


s[:] = ...
- s[:]表示整个列表的切片
- 将s[:]赋值为另一个列表，会替换当前列表中所有元素
- 不会改变变量s的身份（内存地址），所以是原地修改


range()
- 用于生成一个不可变的整数序列，常用于for中控制循环次数
- 起点开，终点闭，步长决定方向和速度。

range(start,stop,step)
- start:可选，起始值（包含）,如果不写，默认为0
- stop：必填，结束值（不包含）
- step：可选，步长（每次增加或减少的值），默认为1

注意：
- 如果 start < stop 且 step > 0 ——>返回空序列
- 如果 start > stop 且 step < 0 ——>正常倒序输出
```python
range(5)
# 表示从 0 开始，到 5（不包括），步长为 1
# 实际上生成的是: 0, 1, 2, 3, 4
```

```python
range(2, 5)
# 表示从 2 开始，到 5（不包括），步长为 1
# 实际上生成的是: 2, 3, 4
```

```python
range(1, 10, 2)
# 表示从 1 开始，到 10（不包括），每次加 2
# 实际上生成的是: 1, 3, 5, 7, 9
```

```python
range(5, 0, -1)
# 表示从 5 开始，到 0（不包括），每次减 1
# 实际上生成的是: 5, 4, 3, 2, 1
```


"""

# 使用双指针
def reverseString(s):
    n = len(s)
    left,right = 0,n-1
    while left < right:
        s[left],s[right] = s[right],s[left]
        # temp = s[left]
        # s[left] = s[right]
        # s[right] = temp
        left += 1
        right -= 1

# 使用栈
def reverseString(s):
    # 栈的特征：先进后出
    stack = []
    for char in s:
        # 先压入栈内
        stack.append(char)

    # 再从栈内取出元素
    for i in range(len(s)):
        s[i] = stack.pop()


# 使用range:折半法
def reverseString(s):
    n = len(s)
    for i in range(n//2):
        s[i],s[n-i-1] = s[n-i-1],s[i]

# 使用列表推导式
def reverseString(s):
    # 创建一个与原列表内容相同但顺序相反的新列表
    s[:] = [s[i] for i in range(len(s)-1,-1,-1)]


# 使用切片
def reverseString(s):
    s[:] = s[::-1]



# 使用reverse()函数，修改原始列表
def reverseString(s):
# 原地反转，无返回值
    s.reverse()

"""
```python
s = [1, 2, 3]
print(reversed(s))       # <list_reverseiterator object at 0x...>
print(list(reversed(s))) # [3, 2, 1]
```
"""
# 使用reversed，返回一个逆序可迭代器
def reverseString(s):
    # s[:] 表示对整个列表进行“切片赋值”。
    # s[:] = reversed(s)
    s[:] = list(reversed(s))
    # 这种写法会替换列表中所有元素，但不会改变 s 的身份（即内存地址不变）。
    # 所以它和    s.reverse()    类似，都是原地修改列表。


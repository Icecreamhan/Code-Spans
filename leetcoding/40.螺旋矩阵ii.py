"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

示例 1：
1——>2——>3
        ↓
8——>9   4
↑       ↓
7<——6<——5
输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：
输入：n = 1
输出：[[1]]
提示：
1 <= n <= 20
"""
# 题目：59.螺旋矩阵II
# 链接
# https://leetcode.cn/problems/spiral-matrix-ii/description/
# 思路：
"""
- 循环不变量
- 模拟顺序画矩阵的过程：
    - 填充上行从左到右
    - 填充右列从上到下
    - 填充下行从右到左
    - 填充左列从下到上
由外向内一圈一圈这么画下去。

初始化一个二维矩阵，
根据递增的规则，填充到相应的位置，就是绕圈填充。
1、转几圈呢？
对于偶数边矩阵n，圈数为n//2
对于奇数边矩阵n，转完n//2后，总会余1个空位置，这个空位置的值，就是n^2。 nums[][]=n*n
那如何定位空位置的坐标？

2、由外向内画圈？
一圈下来，要画每四条边，每画一条边都要坚持一致的左闭右开，或者左开右闭的原则，保证这一圈能按照统一的规则画下来。
因此，接下来，要找到每一圈四条边的遍历规则。
如何?
主要找到四个顶点的坐标！，即四条边的起始节点和终止节点。
记住：左闭右开！这样四条规则才会保持一致：都是左闭右开。
拐角处让给新的一条边来继续画。
- 定义起始位置、终止位置
startx, starty = 0, 0
"""

"""
知识点：
创建二维数组的方法：

方法一：推荐写法
nums = [[0] * n for _ in range(n)]
方法二：
nums= [[0]*n]*n
看着两种方法都是创建一个n*n维的二维列表，但是由本质区别。

方法一：nums = [[0] * n for _ in range(n)]
- 使用列表推导式创建了一个包含n个子列表的二维列表
- 每个子列表都是独立的对象，在内存中位于不同的位置
- 当相对某一行进行修改时，不会影响到其他行。
```python
n = 3
nums = [[0] * n for _ in range(n)]
nums[0][1] = 5
print(nums)
# 输出: [[0, 5, 0], [0, 0, 0], [0, 0, 0]]
```
方法二：nums= [[0]*n]*n
- 先创建了一个子列表[0]*n，然后将这个同一个对象的引用复制了n次
- 所有子列表都指向同一块内存地址
- 当修改某一行的某个元素时，所有行都会变！
```python
n = 3
nums = [[0]*n] * n
nums[0][1] = 5
print(nums)
# 输出: [[0, 5, 0], [0, 5, 0], [0, 5, 0]] ← 所有行都被修改了！
```
"""


def generateMatrix(n):
    # 初始化一个n*n的二维矩阵
    result = [[0] * n for _ in range(n)]

    # 沿着边对这个矩阵进行填充
    # 需要一个每圈开始的位置指针，帮助我们定位到每次沿边走的开始坐标，我们把y沿着螺旋矩阵的横向，x沿着螺旋矩阵的纵向操作，这样x,y 刚好对应着位置和方向
    startx, starty = 0, 0
    # 需要一个移动步数的计数器，给每个坐标点进行赋值
    count = 1
    # 定义一个 应该转的圈数
    loop = n // 2

    # 首先需要一个表示第几圈（与最外边的偏移量）的标记，这个标记还可以帮助我们找到边的起始和终止位置
    # 我们找到循环的圈数，n//2,loop为已遍历的圈数
    for offset in range(1, loop + 1):
        # 顶部横向边 向右走,(用j跑横向边)
        for j in range(starty, n - offset):
            result[startx][j] = count
            count += 1
        # 左边竖向边，向下走,(用i跑竖边)
        for i in range(startx, n - offset):
            result[i][n - offset] = count
            count += 1
        # 底部横向边，向左走，(用j跑横向边)
        for j in range(n - offset, starty, -1):
            result[n - offset][j] = count
            count += 1
        # 右边竖向边，向上走，(用i跑竖边)
        for i in range(n - offset, startx, -1):
            result[i][starty] = count
            count += 1
        startx += 1
        starty += 1

    # 最后，如果为奇数，把最后位置的补齐
    if (n % 2) != 0:
        result[loop][loop] = n * n
    return result


# 方法二：定义4个边界
    # if n <= 0:
    #     return []
    #
    #     # 初始化 n x n 矩阵
    # matrix = [[0] * n for _ in range(n)]
    #
    # # 初始化边界和起始值
    # top, bottom, left, right = 0, n - 1, 0, n - 1
    # num = 1
    #
    # while top <= bottom and left <= right:
    #     # 从左到右填充上边界
    #     for i in range(left, right + 1):
    #         matrix[top][i] = num
    #         num += 1
    #     top += 1
    #
    #     # 从上到下填充右边界
    #     for i in range(top, bottom + 1):
    #         matrix[i][right] = num
    #         num += 1
    #     right -= 1
    #
    #     # 从右到左填充下边界
    #
    #     for i in range(right, left - 1, -1):
    #         matrix[bottom][i] = num
    #         num += 1
    #     bottom -= 1
    #
    #     # 从下到上填充左边界
    #
    #     for i in range(bottom, top - 1, -1):
    #         matrix[i][left] = num
    #         num += 1
    #     left += 1
    #
    # return matrix





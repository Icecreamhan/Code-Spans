"""
【题目描述】
在一个城市区域内，被划分成了n * m个连续的区块，每个区块都拥有不同的权值，代表着其土地价值。目前，有两家开发公司，A 公司和 B 公司，希望购买这个城市区域的土地。
现在，需要将这个城市区域的所有区块分配给 A 公司和 B 公司。
然而，由于城市规划的限制，只允许将区域按横向或纵向划分成两个子区域，而且每个子区域都必须包含一个或多个区块。
为了确保公平竞争，你需要找到一种分配方式，使得 A 公司和 B 公司各自的子区域内的土地总价值之差最小。
注意：区块不可再分。
【输入描述】
第一行输入两个正整数，代表 n 和 m。
接下来的 n 行，每行输出 m 个正整数。
【输出描述】
请输出一个整数，代表两个子区域内土地总价值之间的最小差距。
【输入示例】
3 3 1 2 3 2 1 3 1 2 3
【输出示例】
0
【提示信息】
如果将区域按照如下方式划分：
1 2 | 3 2 1 | 3 1 2 | 3
两个子区域内土地总价值之间的最小差距可以达到 0。
【数据范围】：
1 <= n, m <= 100；
n 和 m 不同时为 1。
"""
# 题目 开发商购买土地
# 链接：
# https://www.programmercarl.com/kamacoder/0044.%E5%BC%80%E5%8F%91%E5%95%86%E8%B4%AD%E4%B9%B0%E5%9C%9F%E5%9C%B0.html#%E6%80%9D%E8%B7%AF
# 思路
'''
因为题干说只能横向切或者竖向切一刀（划分为两个区间），
因此，需要将所有的行方向、列方向和都事先用求出来，再用前缀和的思想处理
'''
# ACM模式
import sys
def main():
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    m = int(data[1])

    # 先获取输入的n*m 的二维数组(还原)
    index = 2
    sum = 0 # 标识所有土地的总价值
    vec = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(int(data[index]))
            sum += int(data[index])
            index += 1
        vec.append(row)

    # 初始化一个n维列表，统计横向和
    horization = [0] * n
    for i in range(n):
        for j in range(m):
            horization[i] += vec[i][j]
        # subsum = 0
        # for j in range(m):
        #     subsum += vec[i][j]
        # horization[i] = subsum
    # 初始化一个m维列表，统计纵向和
    vertical = [0] * m
    for j in range(m):
        for i in range(n):
            vertical[j] += vec[i][j]

    result = float('inf') # 因为题中要求求最小差值，因此初始化一个最大值
    # 先进行横向切，找最小差值
    # 从前缀和索引为0处开始遍历，一直到n
    horizontalcut = 0
    for i in range(n):
        horizontalcut += horization[i]
        result = min(result,abs(sum - horizontalcut*2))

    # 再进行纵向切，找最小差值
    # 从前缀和索引为0处开始遍历，一直到m
    verticalcut = 0
    for j in range(m):
        verticalcut += vertical[j]
        result = min(result,abs(sum - verticalcut*2))

    print(result)


if __name__ == "__main__":
    main()

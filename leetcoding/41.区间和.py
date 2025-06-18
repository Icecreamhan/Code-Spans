"""
[题目描述]
给定一个整数数组 Array，请计算该数组在每个指定区间内元素的总和。
[输入描述]
第一行输入为整数数组 Array 的长度 n，接下来 n 行，每行一个整数，表示数组的元素。随后的输入为需要计算总和的区间，直至文件结束。
[输出描述]
输出每个指定区间内元素的总和。
[输入示例]
5
1
2
3
4
5
0 1
1 3
[输出示例]
3
9
[数据范围：]
0 < n <= 10000
"""
# 题目：58.区间和
# 链接：
# https://www.programmercarl.com/kamacoder/0058.%E5%8C%BA%E9%97%B4%E5%92%8C.html#%E6%80%9D%E8%B7%AF
# 思路
'''
前缀和

题目要求指定区间内的元素总和，并且不清楚指定区间的个数，
因此，为避免重复计算，
事先计算好，对于每个位置i，其及其前面所有元素的累加和
因此对于区间和，就是区间右边的元素前缀和-区间左边位置前一个元素的前缀和

前缀和的思想是重复利用计算过的子数组之和，从而降低区间查询需要累加计算的次数。

==》每次遇到计算区间和时，都使用前缀和！
index为[2,5]区间和
index=5的前缀和 = index0 + index1 + index2 + index3 + index4 + index5
index=2的前缀和 = index0 + index1 + index2

index=5的前缀和-index=1的前缀和


知识点
input()和stdin()的区别
- input()方法和stdin()类似，input()内可以直接填写说明文字
- sys.stdin.readline()会将标准的输入全部获取，包括末尾的`\n`，因此
用len()计算长度时，是把换行符`\n`算进去了
- 但input()获取输入时返回的结果是不包含末尾换行符的`\n`

因此使用sys.stdin.resaline()获取输入，需去掉末尾换行符
- sys.stdin.readline().strip('\n')
- sys.stdin.resdline()[:-1]


'''

import sys
input = sys.stdin.read


def main():
    data = input().split()  # 按下ctrl+D 输入结束
    n = int(data[0])
    # 获取原数组
    vec = []
    for i in range(n):
        vec.append(int(data[i+1]))

    # 计算前缀和
    presum = [int(data[1])] * n
    for index in range(1, n):
        presum[index] = presum[index-1] + int(data[index+1])

    result = []
    pre = n+1
    # 获取指定的区间（不定长）
    while pre < len(data):
        start = int(data[pre])
        end = int(data[pre+1])
        pre += 2
        if start == 0:
            sum_value = presum[end]
        else:
            sum_value = presum[end] - presum[start -1]

        result.append(sum_value)

    for res in result:
        print(res)


if __name__ == "__main__":
    main()

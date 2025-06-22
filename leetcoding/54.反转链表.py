"""
你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
示例 1：
输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
示例 2：
输入：head = [1,2]
输出：[2,1]
示例 3：
输入：head = []
输出：[]
提示：
链表中节点的数目范围是 [0, 5000]
-5000 <= Node.val <= 5000

进阶：链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？

"""


# 题目：206 反转链表
# 链接
# https://leetcode.cn/problems/reverse-linked-list/
# 思路
"""
先排除边界情况
size = 0 和 size = 1

【双指针】
遍历条件》cur=>null
临时指针》temp
先移动哪一个指针》pre、cur
返回新的头节点 pre

【递归的写法】
把大问题拆解为两个子问题，再把子问题拆解成两个相同思路的子问题，存在最小子问题
递归好难。。。。
"""

from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head:Optional[ListNode]):
    # 双指针
    # 定义一个pre指针，用于保存已经反转好的链表（从后向前）
    # 定义一个cur用于向前遍历原始链表节点
    pre = None
    cur = head
    # 一直遍历到尾节点的最后一位
    while cur:
        # 临时变量用于保存未遍历的原始链表节点,即cur的下一个节点，因为接下来 cur-》next
        temp = cur.next # 记录原始链表中剩余未翻转的节点头
        cur.next = pre # 完成反转操作
        # 更新两个指针,只能先更新pre，否则cur节点将不能被添加到翻转后的链表上
        pre = cur
        cur = temp
    return pre






"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
示例 1：
输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：
输入：head = []
输出：[]
示例 3：
输入：head = [1]
输出：[1]
提示：
链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
"""
from typing import Optional

# 题目 24.两两交换链表中的节点
# 链接
#https://leetcode.cn/problems/swap-nodes-in-pairs/description/
# 思路
"""
【画图】
1、定义虚拟/哨兵节点
2、操作的指针一定要指向待反转两个节点的前一个节点
【操作顺序】
cur
cur+1
cur+2
1. 先让cur指向cur+2
2. 再让cur+2指向cur+1
3. 再让cur+1指向cur+3
【注意：】
1、什么时候遍历终止
    - 如果链表节点数为偶数，当cur+1(cur.next)为空时结束，遍历结束。
    - 如果链表节点数为奇数，那么，cur+2(cur.next.next)为空，遍历结束。
    - 0 也是偶数，因此当链表为空时，cur.next也为NULL
    - 并且，在判断cur.next.next是否为空之前，需要先确保cur.next不为空，因此先写条件cur.next ！=None,再写cur.next.next != None
    - 那么，由于cur最初指向dummy_node，因此 cur不可能为空。
2、链表如何进行交换
    - 使用临时变量保存 cur.next
    - 使用临时变量保存 cur.next.next.next
3、怎么移动cur指针
    - cur = cur.next.next
4、最后return dummy_node.next


"""
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head: Optional[ListNode]):
    #先定义一个哨兵节点
    dummy_node = ListNode(0,head)

    # 定义一个遍历指针节点
    cur = dummy_node

    # 确定遍历条件,偶数节点下、奇数节点下（画图）
    while cur.next and cur.next.next:
        # dummy->1->2->3  ==》 dummy->2->1->3
        temp1 = cur.next # 存储cur+1，防止节点被更改
        cur.next = cur.next.next
        temp2 = cur.next.next.next # 存储cur+3
        cur.next.next = temp1
        temp1.next = temp2
        # cur.next.next.next = temp2
        # 移动指针节点
        cur = cur.next.next

    return dummy_node.next


# 看到一个有趣的递归
def swapPairsd(head: Optional[ListNode]):
    if head is None or head.next is None:
        return head
    temp1 = head
    temp2 = temp1.next
    temp3 = temp2.next

    temp2.next = temp1
    temp1.next = swapPairs(temp3)

    return temp2 # 因为翻转后的头结点必然是第二个节点








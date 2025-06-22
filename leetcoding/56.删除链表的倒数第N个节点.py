"""
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
示例 1：
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：
输入：head = [1], n = 1
输出：[]
示例 3：
输入：head = [1,2], n = 1
输出：[1]
提示：
链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""
from typing import Optional

# 题目：19.删除链表的倒数第N个节点
# 链接
# https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/
#思路
"""
看到链表就要想到：虚拟节点和操作节点
快慢指针的操作

1. 首先快慢指针都指向同一个位置
2. 快指针先走N步，接着，快慢指针一起移动，直到快指针指向null，None,此时就找到了倒数第N个节点，即慢指针的位置就是倒数第N个节点。
    - 倒数第n个，实际上是正数的第（size+1)-n个，这样fast与slow的差值是n
    - 当fast走n+1位置时，就找到了待删除节点
3. 但是对于删除一个节点来说，需要找到改节点的前驱节点和后继节点

4. 因此，我们需要使用快慢指针，找到，倒数第N+1个节点的位置。
    - 快指针多走N+1步
    - 快慢指针一起走，直到快指针指向空（size+1的位置）
    
[步骤]
1. 先使用快慢指针找到待删除节点的前驱节点
    - 定义一个快慢指针
    - 快指针向前移动N+1步
    - 快慢指针同时移动，直到快指针指向null
2. 进行节点删除操作
"""
class ListNode:
    def __init__(self,val=0,next = None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # 定义一个哨兵节点
    dummy_node = ListNode(0,head)
    fast, slow = dummy_node,dummy_node

    # 快指针先移动N+1步
    for _ in range(n+1):
        fast = fast.next

    # 同时移动两个指针，直到快指针达到链表末尾
    while fast:
        slow = slow.next
        fast = fast.next
    # 更新待删节点（n）的前驱节点的后继节点指向，删除倒数第n个节点
    slow.next = slow.next.next
    return dummy_node.next


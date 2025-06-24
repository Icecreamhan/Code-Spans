"""
给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
不允许修改 链表。
示例 1：
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。

提示：
链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
"""
from typing import Optional

# 题目：142.环形链表II
# 链接 ：
# https://leetcode.cn/problems/linked-list-cycle-ii/description/
# 思路：
"""
1. 判断一个链表是否有环
快慢指针，双指针，如果相遇就是有环
快指针的速度：每次走两个节点，
     - 快指针每次移动一个节点的相对速度去靠近慢指针。
     - 因此两个指针一定会在环里相遇，而不会让快指针直接跳过他。
慢指针每次只走一个节点。
为什么有环情况下，快指针一定会遇到慢指针：
快指针先进入这个环，慢指针之后才会进入这个环。
快指针其实在环内一直追慢指针的一个过程。
2. 找出环的入口
    - 假设从head，到环入口节点的节点数为 x,环入口到快慢指针相遇节点 的节点数为y，从相遇节点再到环形入口节点的节点数为z.
    - 那么当slow与fast时，slow走了x+y个节点，fast走了x+n*(y+z)+y个节点，n是fast在环内转过的圈数
    - 此时根据slow和fast移动距离建立关系 2(x+y) = x+ n*(y+z) +y
    - 对等式进行变换，因为我们最终是求x,那么 x = (n-1)(y+z) + z
    - 当n = 1 时，x = z，也即，此时一个指针从head，一个指针从相遇点出发，同时移动，那么一定会在环入口处相遇。
    - 当n > 1 时，fast指针 在环形转n圈之后才遇到slow指针，这种情况和n为1的效果一样，也可以通过这种方法找到环形入口，index1(相遇点出发的指针)在环内多转了（n-1）圈，然后再遇到index2.

【总体步骤：】
1.设置快慢指针，同时从head，慢指针每次移动一个节点，快指针每次移动两个节点。
2.先判断是否有环
    - fast != null && fast.next != null，这意味着快指针一直在转圈，才会有环
3. 进入环内，找两个指针（在环中）的相遇点。
    - 此时两个指针肯定在环内相遇，并且一定是在慢指针首次进入环内时相遇。
4.数学公式已经证明，一个指针从head出发、一个指针从相遇点出发，同时移动，将会在环的入口处再次相遇。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detecCycle(head: Optional[ListNode]) -> Optional[ListNode]:
    # 快慢指针法
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # 如果有环，快慢指针会在环内相遇
            index1 = fast  # 一个从相遇的点出发
            index2 = head  # 一个从头出发
            while index1 != index2: # 如果一直不相遇，则一直循环找下去
                index1 = index1.next
                index2 = index2.next
            # 当两个指针相遇时，跳出循环
            return index1
    # 如果快指针移动到了，链表尾部null，证明没环
    return None

# 使用集合法，记录走过的节点，如果新节点在集合中，那么有环，否则无环
    visited = set()
    while head:
        if head in visited:
            return head
        visited.add(head)
        head = head.next
    return None



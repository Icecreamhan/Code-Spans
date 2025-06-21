"""
给你一个链表的头节点 head 和一个整数 val ，请你删除链表中所有满足 Node.val == val 的节点，并返回 新的头节点 。

示例 1：
输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]
示例 2：
输入：head = [], val = 1
输出：[]
示例 3：
输入：head = [7,7,7,7], val = 7
输出：[]
"""
# 题目 203.移除链表元素
# 链接
# https://leetcode.cn/problems/remove-linked-list-elements/description/
# 思路
'''
移除链表元素：让节点`next`指针直接指向下下一个节点就可以。
因此，如果要删除节点node，必须在node的前一个节点执行删除操作。
例如链表1——>2——>3，要删除2，那需要节点1处操作，也就是把节点1的next更新为节点3

- 哨兵节点：
如果头节点可能被删除，那么要在头节点之前添加一个哨兵节点，这样无需判断头节点被删除的情况

[注意]

对于单链表，只能指向下一个元素，那如果移除的是头结点的话，如何处理？

# 两种方式
- 直接使用原来的链表来进行删除操作
    - 第一种方式，注意对头结点单独处理
- 设置一个虚拟头结点在进行删除操作（建议）
    - 第二种方式，最后需要返回真正的头结点，即虚拟节点的下一个节点 

方式三：通过**递归**的方式 移除链表元素。

基础情况：对于空链表，不需要移除元素。

递归情况：

- 首先检查头节点的值是否为val,如果是，则移除头节点，答案即为在头节点的后续节点上递归的结果。

- 如果头节点的值不为val,则答案为头节点与在头节点的后续节点上递归得到的新链表拼接的结果。
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head,val):
    # 设计一个虚拟节点，指针域指向头节点
    dummy_head = ListNode(next=head)

    # 遍历列表，并删除值为val的节点
    # 从虚拟节点开始遍历
    current = dummy_head
    while current.next: # 也会遍历尾节点
        if current.next.val == val:
            current.next = current.next.next # 如果current.next 是尾节点，那么就直接指向none
        else:
            current = current.next # 继续向后遍历链表

    return dummy_head.next


# 方法二 对头结点单独处理  迭代的方法
def removeElementsHead(head,val):
    # 这种情况，很有可能新的头节点（原链表的第二个节点）的值还是跟val相等，因此，if改为while
    while head.val == val and head:
        head = head.next

    if not head: return
    # 如果头节点，或前几个节点不为目标值
    current = head
    while current.next:  # 如果没遍历到尾节点
        if current.next.val == val:  # 因为我们已经排除head节点的val为目标值了，所以从下一个next节点开始
            current.next = current.next.next
        else:
            current = current.next
    return head


# 方法三：双指针
"""
先对头节点进行判断
定义两个快慢指针都指向头节点，
快的指针用来遍历后面的元素，
慢的指针表示完成移除后的链表

"""
# 方法二 对头结点单独处理  迭代的方法
def removeElementspq(head,val):
    # 这种情况，很有可能新的头节点（原链表的第二个节点）的值还是跟val相等，因此，if改为while
    while head.val == val and head:
        head = head.next
    # 定义两个快慢指针都指向头节点
    slow, fast = head, head
    while fast:
        if fast.val == val:
            slow.next = fast.next # 不更新慢指针
        else:
            slow = fast # 更新慢指针
        fast = fast.next

    return head


"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：
示例 1：
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
提示：
listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]
进阶：你能否设计一个时间复杂度 O(n) 、仅用 O(1) 内存的解决方案？
"""
# 题目：面试题0207链表相交
# 链接：
# https://leetcode.cn/problems/intersection-of-two-linked-lists-lcci/description/
# 思路
"""
【难以理解】
求两个链表交点节点的指针。交点并不是数值相等，而是指针相等？？（如何理解？？）
[**假设**节点元素数值相等，则节点指针相等。]

- 对于指针curA指向链表A的头节点，curB指向链表B的头节点。
- 求两个链表的长度，并求出这两个链表长度的差值，然后让curA移动到，和curB末尾对齐的位置。
- 此时，就可以比较curA和curB是否相同，如果不相同，同时向后移动curA和curB，
- 如果遇到curA== curB，则找到交点。
- 否则循环退出返回空指针。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    # 1. 获取两个链表的长度
    length_a, length_b = getlinklistlength(headA), getlinklistlength(headB)

    dis = length_a - length_b

    # 2. 移动较长的链表，使得两个链表的尾部对齐
    if dis > 0:# 链表a长
        headA = moveforward(headA, dis)
    else:
        headB = moveforward(headB, abs(dis))

    # 3. 同时向前移动两个头，直到它们相交，或者遍历结束
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None


# 1. 先计算链表的总节点数
def getlinklistlength(head:ListNode):
    cur = head
    length = 0
    while cur:
        cur = cur.next
        length += 1
    return length


# 2. 按指定步数，移动链表
def moveforward(head,step):
    for _ in range(step):
        head = head.next
    return head


# 方法2
"""
有点像相同速度，不同长度的两辆车进行追赶，画图理解一下。
设置 第一个公共节点为 node,找到这个公共节点
链表headA的节点数为 a
链表headB的节点数为 b
两个链表的公共尾部的节点数量为 c
则有：
头节点headA到node前，共有 a-c 个节点。
头节点headB到node前，共有 b-c 个节点。

考虑构建两个节点指针A，B分别指向两链表头节点headA,headB，做如下操作：
- 指针A先遍历完链表headA,再开始遍历链表headB,当走到node节点时，共走
a+(b-c)
- 指针B先遍历完链表headB,再开始遍历链表headA，当走到node时，共走
b+(a-c)
此时指针A,B重合，并有两种情况
a+(b-c) = b+(a-c)
1. 若两个链表有公共尾部，即c>0，指针A,B同时指向第一个公共节点 node.
2. 若两链表 无 公共尾部，即c=0，指针A,B同时指向null
因此，返回A即可。
"""


def getIntersectionNodeN(headA: ListNode, headB: ListNode) -> ListNode:
    # 处理边缘情况
    if not headA or not headB:
        return None
    # 在每个头节点初始化两个指针
    curA, curB = headA, headB

    # 遍历两个链表，直至链表相交
    while curA != curB:
        # 将指针向前移动一个节点
        curA = curA.next if curA else headB
        curB = curB.next if curB else headA

    # 如果相交，指针将位于交点节点，如果没有节点，值为None(此时，两个指针都同时遍历到最后。)
    return curA

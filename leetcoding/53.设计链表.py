"""
你可以选择使用单链表或者双链表，设计并实现自己的链表。

单链表中的节点应该具备两个属性：`val` 和 `next` 。`val` 是当前节点的值，`next` 是指向下一个节点的指针/引用。

如果是双向链表，则还需要属性 `prev` 以指示链表中的上一个节点。假设链表中的所有节点下标从 `0` 开始。

实现 `MyLinkedList` 类：

- `MyLinkedList()` 初始化 `MyLinkedList` 对象。
- `int get(int index) `获取链表中下标为 `index` 的节点的值。如果下标无效，则返回` -1 `。
- `void addAtHead(int val) `将一个值为` val `的节点插入到链表中第一个元素之前。在插入完成后，新节点会成为链表的第一个节点。
- `void addAtTail(int val) `将一个值为 `val` 的节点追加到链表中作为链表的最后一个元素。
- `void addAtIndex(int index, int val)` 将一个值为 val 的节点插入到链表中下标为` index` 的节点之前。如果 index 等于链表的长度，那么该节点会被追加到链表的末尾。如果` index` 比长度更大，该节点将 不会**插入** 到链表中。
- `void deleteAtIndex(int index)` 如果下标有效，则删除链表中下标为` index `的节点。

**示例：**
**输入**
`["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]`
`[[], [1], [3], [1, 2], [1], [1], [1]]`
**输出**
`[null, null, null, null, 2, null, 3]`

**解释**
```python
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // 链表变为 1->2->3
myLinkedList.get(1);              // 返回 2
myLinkedList.deleteAtIndex(1);    // 现在，链表变为 1->3
myLinkedList.get(1);              // 返回 3
```
"""
# 题目：707设计链表
# 链接
# https://leetcode.cn/problems/design-linked-list/description/
# 思路
"""
链表操作有两种方式：
- 直接使用原来的链表来进行操作
- 设置一个虚拟头节点再进行操作

链表的长度与节点个数有关：
size

【插入节点】
注意：
1、一定要先定义一个新的节点
2、插入顺序
    - 应先将 待插入节点的next 指向当前位置的下一个节点，
    - 再把当前位置的下一个next指向待插入节点。
    - 不然会把当前位置的下一个节点弄丢。
3、在头部插入元素
    - 先把待插入元素定义为一个新的节点
    - 一定要先把待插入元素的next指向当前位置的next
    - 再把当前位置的next指向待插入元素
4、在中间插入元素
    - 一定要先遍历到指定位置
    - 先把待插入元素定义为一个新的节点
    - 一定要先把待插入元素的next指向当前位置的next
    - 再把当前位置的next指向待插入元素
5、在尾部插入元素
    - 一定要先把指针遍历到尾部
    - 再进行插入操作
    
【踩得坑】
1、注意无效情况下的index，到底是[0,size)，还是[0,size]
2、找指定index节点时，注意从哨兵节点开始遍历还是从head节点开始遍历
"""


# 单链表版
class LinkNode:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:
    # 初始化一个哨兵节点和链表的大小/长度（0）
    def __init__(self):
        self.dummy_node = LinkNode()
        self.size = 0

# 获取索引为index位置的元素值，index=0，意味着head节点
    def get(self, index: int) -> int:
    #先处理无效情况，index=[0,size)，或者索引小于0，如果索引 超过或等于 链表长度，
        if index < 0 or index >= self.size: # 如果链表为空，size =0 也要报错
            return -1
    # 先找到索引/下标为index的节点
        cur = self.dummy_node.next # 指向头结点,index = 0，如果index = 3（链表第4个位置的元素），则为head节点后的第三个位置，因此，从头节点开始遍历index个位置后即可
        # 找到索引位置为index的节点
        for i in range(index): # [0,1,2]
            cur = cur.next
        return cur.val

        # cur = self.dummy_node
        # while index >= 0:
        #     cur = cur.next
        #     index -= 1
        # return cur.val

    def addAtHead(self, val: int) -> None:
        # 先定义一个新的节点
        new_node = LinkNode(val)

        # 先将新的节点next下一个指向head节点
        new_node.next = self.dummy_node.next
        # 再将哨兵节点的下一个节点next 指向新的节点new_node
        self.dummy_node.next = new_node
        # 最后，更新链表长度
        self.size += 1

        # # 或者直接一步到位
        # self.dummy_node.next = LinkNode(val,self.dummy_node.next)
        # self.size += 1

    def addAtTail(self, val: int) -> None:
        # 先用一个指针找到尾部节点
        cur = self.dummy_node # 为了防止头节点不存在，所以不是 cur = self.dummy_node.next
        while cur.next:
            cur = cur.next
        cur.next = LinkNode(val) # 指向 定义的新节点
        self.size += 1

# 将一个值为val的节点插入到链表中下标为index节点之前，那么先找到索引/下标为index-1的节点
    def addAtIndex(self, index: int, val: int) -> None:
        # 先判断失效的情况，index<0 或者index >size，此时该节点将不会插入到链表中
        if index < 0 or index > self.size:
            return

        # 先找到下标为index节点的前一个节点。
        cur = self.dummy_node # 因为不能range(-1)，因此需要从哨兵节点开始遍历
        for i in range(index):
            cur = cur.next
        # 先定义一个新的节点
        cur.next = LinkNode(val, cur.next)
        self.size += 1

# 如果下标有效，则删除链表中下标为index的节点
    def deleteAtIndex(self, index: int) -> None:
        # 先判断下标是否有效，# 排除无效情况,index=[0,size)
        if index < 0 or index >= self.size:
            return
        # 先找到索引/下标为index节点的前一个节点，再把前一个节点的next索引为index下一个节点
        cur = self.dummy_node # 因为不能range(-1)，因此需要从哨兵节点开始遍历
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

"""
[双向链表]
- 实现双向链表，每个节点要存储本身的值、后继节点、前驱节点。
- 此外，需要一个哨兵节点作为头节点dummy_node，
- 和一个哨兵节点作为尾节点tail_node
- 仍需要一个size参数保存有效节点数。

初始化时，只需创建头节点dummy_node和size即可。
- [实现get(index)]时，先判断有效性，再比较从dummy_node还是tail_node来遍历，会比较快找到目标，然后进行遍历
- [实现addAtIndex(index,val)]时，如果index是有效值，则需要找到原来下标为index的节点和前驱节点pre，并创建新节点，再通过各自prev和next变量的更新来增加节点，最后更新size
- [实现addAtHead(index)和addAtTail(index)时，可借助addAtIndex(index,val)来实现。
- [实现deleteAtHead(index)]，先判断参数有效性。然后找到下标为index节点的前驱节点prev和后继节点，再通过各自的prev和next变量的更新来删除节点，达到删除节点的效果。同时更新size.

"""

#双链表版

class LinkList:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class MyLinkedList:
    def __init__(self):
        self.dummy_node = LinkList(0)
        self.tail_node = LinkList(0)
        self.dummy_node.next = self.tail_node
        self.tail_node.prev = self.dummy_node
        self.size = 0

    def get(self, index: int) -> int:
        # 先排除无效区间，index = [0,size)
        if index < 0 or index >= self.size:
            return -1
        # 再判断从前往后找还是从后向前找 目标索引
        if index < self.size // 2:  # 从前向后找
            cur = self.dummy_node.next
            for i in range(index):
                cur = cur.next
            return cur.val
        else:  # 从后向前找
            cur = self.tail_node
            for i in range(self.size - index):  # 从后向前遍历的次数
                cur = cur.prev
            return cur.val

    def addAtHead(self, val: int) -> None:
        # 先定义一个新的节点
        # 将新节点的下一个节点指向头节点
        # 将哨兵节点指向新的节点
        # size += 1
        # return self.addAtIndex(0, val)
        new_node = LinkList(0,self.dummy_node,self.dummy_node.next)
        self.dummy_node.next = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = LinkList(val,self.tail_node.prev,self.tail_node)
        self.tail_node.prev.next = new_node
        self.tail_node.prev = new_node
        self.size += 1
        # return self.addAtIndex(self.size, val)

    # 先找到索引/下标为index的节点
    def addAtIndex(self, index: int, val: int) -> None:
        # 先判断索引/下标的有效性index=[0,size]
        if index < 0 or index > self.size:
            return

        # 先找到索引下标为index-1的节点
        # 判断从前往后找还是从后向前找
        if index < self.size - index:  # 从前向后找到index-1的节点和index节点
            # cur = self.dummy_node.next
            # for _ in range(index):
            #     cur = cur.next
            # pre = cur.prev
            pre = self.dummy_node
            for _ in range(index):
                pre = pre.next
            cur = pre.next
        else:  # 从后向前找到索引为index-1的节点和index节点
            cur = self.tail_node
            for _ in range(self.size - index):
                cur = cur.prev
            pre = cur.prev

        # 定义一个新的节点
        new_node = LinkList(val)
        # 新节点的前驱节点指向索引为index-1的节点
        new_node.prev = pre
        # 新节点的后继节点，指向索引为index的节点
        new_node.next = cur
        # 再，更新index-1节点的下一个节点（后继节点）指向新节点
        pre.next = new_node
        # 最后，更新index节点的上一个节点（前驱节点）指向新节点
        cur.prev = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        # 先判断区间的有效性 index=[0,size)
        if index < 0 or index >= self.size:
            return
            # 再找到索引/下标为index-1，和索引/下标为 index+1 的节点
        if index < self.size - index:  # 先判断从前往后找
            # 从哨兵节点开始找,索引为index-1的节点
            pre = self.dummy_node
            for _ in range(index):
                pre = pre.next
            suc = pre.next.next  # 索引为index+1的节点
        else:  # 从后往前找
            # 从尾部哨兵节点开始找，索引为index+1，和index-1的节点
            suc = self.tail_node
            for _ in range(self.size - index - 1):
                suc = suc.prev
            pre = suc.prev.prev

        # 将索引位置index-1的节点的下一位，指向索引位置为index+1节点
        # 将索引位置为index+1的节点的前驱节点，指向索引位置为index-1的节点
        pre.next = suc
        suc.prev = pre
        self.size -= 1
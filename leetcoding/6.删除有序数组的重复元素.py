# 看到一个双指针问题的思路，非常有意思
"""
题目：外面有宝，赶紧捡回来按序放好，不能重样哟
有点像小夫妻俩，老公q在外面淘宝，找到后运回来，找到一个新的宝，老婆p在家里就给挖个新坑放好，最后外面没宝了，就结束咯

中间对话

老公：老婆，这个家里有没？（if）
老婆：有了。（nums[p] == nums[q]）你再找找（q++）

老公：老婆，这个家里有没？（if）
老婆：有了。（nums[p] == nums[q]）你再找找（q++）

老公：老婆，这个家里有没？（if）
老婆：这个没有，拿回来吧 （nums[p] != nums[q]）
放好了，我到下一个位置等你（p++） 你再继续找吧(q++)

貌似双指针都可以这么理解
"""

# 题目
"""
给你一个 非严格递增排列 的数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。元素的 相对顺序 应该保持 一致 。然后返回 nums 中唯一元素的个数。

考虑 nums 的唯一元素的数量为 k ，你需要做以下事情确保你的题解可以被通过：

更改数组 nums ，使 nums 的前 k 个元素包含唯一元素，并按照它们最初在 nums 中出现的顺序排列。nums 的其余元素与 nums 的大小不重要。
返回 k 。
判题标准:

系统会用下面的代码来测试你的题解:

int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有断言都通过，那么您的题解将被 通过。

 

示例 1：

输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。
示例 2：

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
 

提示：

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums 已按 非严格递增 排列
"""
# 链接
# 26.删除有序数组中的重复项
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array/description/
# 思路1
"""
双指针的方法
慢指针，用来表示下一个元素要填入的下标位置
快指针，表示遍历数组到达的下标位置

当元素为1个时，不需要处理。
当元素大于1个时，开始进行比较。所以快慢指针都要从索引为1的位置开始。
"""


def removeduplicates(nums):
    n = len(nums)

    if n < 2:
        return n

    # slow = 1
    # fast = 1
    # while fast < n:
    #     if nums[fast] != nums[fast-1]:
    #         nums[slow] = nums[fast]
    #         slow += 1
    #     fast += 1
    #
    # return slow

    # 按照刚刚有趣的思路展开一下：
    woman = 0
    man = 1

    while man < n:
        if nums[woman] != nums[man]:
            woman += 1
            nums[woman] = nums[man]
        man += 1

    return woman+1


# # 方法二：使用两个索引
# k = 1
# for i in range(1, len(nums)):
#     if nums[i] != nums[i - 1]:  # 只有当前后两个元素的值不一致的时候，才会使用K索引去更新nums，
#         nums[k] = nums[i]  # 先将k位置的值置为最新获取的i位置的值
#         k += 1  # 再将索引k向前移动一位
# return k

# # 方法一：双指针
# N = len(nums)
# slow = 0
# fast = 1

# while fast < N:
#     if nums[slow] != nums[fast]:
#         slow += 1
#         nums[slow] = nums[fast]
#     fast += 1
# return slow +1






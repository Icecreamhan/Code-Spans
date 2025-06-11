"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素。元素的顺序可能发生改变。然后返回 nums 中与 val 不同的元素的数量。

假设 nums 中不等于 val 的元素数量为 k，要通过此题，您需要执行以下操作：

更改 nums 数组，使 nums 的前 k 个元素包含不等于 val 的元素。nums 的其余元素和 nums 的大小并不重要。
返回 k。
用户评测：

评测机将使用以下代码测试您的解决方案：

int[] nums = [...]; // 输入数组
int val = ...; // 要移除的值
int[] expectedNums = [...]; // 长度正确的预期答案。
                            // 它以不等于 val 的值排序。

int k = removeElement(nums, val); // 调用你的实现

assert k == expectedNums.length;
sort(nums, 0, k); // 排序 nums 的前 k 个元素
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
如果所有的断言都通过，你的解决方案将会 通过。
示例 1：
输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2,_,_]
解释：你的函数函数应该返回 k = 2, 并且 nums 中的前两个元素均为 2。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。
示例 2：
输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3,_,_,_]
解释：你的函数应该返回 k = 5，并且 nums 中的前五个元素为 0,0,1,3,4。
注意这五个元素可以任意顺序返回。
你在返回的 k 个元素之外留下了什么并不重要（因此它们并不计入评测）。

提示：
0 <= nums.length <= 100
0 <= nums[i] <= 50
0 <= val <= 100

"""
# 题目:27.移除元素
# 链接：
# https://leetcode.cn/problems/remove-element/description/
# 思路：
"""
快慢指针



"""


def removeElement(nums,val):
    # 方法四：左右指针法——相向双指针法
    n = len(nums)
    left, right = 0, n - 1
    while left <= right:
        while left <= right and nums[left] != val:  # 当左指针指向目标值时，跳出循环。如果左指针所指的位置不是目标值，那么左指针向左移动。
            left += 1
        while left <= right and nums[right] == val:  # 当右指针不指向目标值时，跳出循环。如果右指针处是目标值，则改变右指针的位置，右指针向左移动一位。
            right -= 1
        if left < right:  # 如果左指针在右指针左边，此时的情况是：左指针指向目标值，右指针不指向目标值。
            nums[left] = nums[right]  # 那么用右指针处的值替换左指针指向处。
            left += 1  # 之后向左指针继续向左移动
            right -= 1  # 右指针处因为被目标值替换掉了，所以，右指针要向左移动一位。
    return left  # 最后返回左指针所指向的位置

    # # 方法三：暴力求解
    # i, l = 0, len(nums)
    # while i < l:
    #     if nums[i] == val:
    #         for j in range(i+1,l):
    #             nums[j-1] = nums[j]
    #         l -= 1
    #         i -= 1  # 因为i要继续往后遍历，因此，如果当前i的位置为目标值，需要把目标值删掉，继续往后遍历。
    #     i += 1
    # return l

    # # 方法二：快慢指针法
    # slow = 0
    # fast = 0
    # N = len(nums)
    # while fast < N:
    #     if nums[fast] != val:
    #         nums[slow] = nums[fast]
    #         slow += 1
    #     fast += 1
    # return slow

    # # 方法一：快慢指针法
    # slowindex = 0
    # for fastindex in range(len(nums)):
    #     if nums[fastindex] != val:
    #         nums[slowindex] = nums[fastindex]
    #         slowindex += 1
    # return slowindex
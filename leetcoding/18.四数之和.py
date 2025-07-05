"""
给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
0 <= a, b, c, d < n
a、b、c 和 d 互不相同
nums[a] + nums[b] + nums[c] + nums[d] == target
你可以按 任意顺序 返回答案 。
示例 1：
输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
示例 2：
输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]
提示：
1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""
# 题目：18.四数之和
# 链接
# https://leetcode.cn/problems/4sum/description/
# 思路
"""
索引不同，值可以相同，也就是说四元组不能重复，但是四元组内的元素值可以重复
回忆一下三数之和，先排序，确定元素a，使用双指针。

那么四数之和，我们在三数之和的基础上，再多加一层循环。

剪枝的操作怎么理解？？
在每层循环中，遇到某些情况，可以直接跳出这一层循环。
例如，我们在遍历第一个元素时a，
如果：第一个元素nums[a]+第二个元素nums[a+1]+第三个元素nums[a+2]+第四个元素nums[a+3]>target,那么这个循环就可以跳出break。
如果，第一个元素nums[a]+倒数第一个元素nums[n-1]+倒数第二个元素nums[n-2]+倒数第三个元素nums[n-3]<target，这个循环也可以跳出，因为我们不可能找到了、

我们遍历第二个元素时b，
如果：前一个确定的元素nums[a]+遍历的元素nums[b]+第三个元素nums[b+1]+第四个元素nums[b+2]>target，时，那么这个循环就终止了。
如果：前一个确定的元素nums[a]+遍历的元素nums[b]+倒数第一个元素nums[n-1] +倒数第二个元素nums[n-2] <target时，那么这个循环也可以终止了。
如果，b元素重复，也即，b>a+1,nums[b]==nums[b-1]，就是我们在之前的循环中，遇到过b,此时，我们直接continue


剪枝的操作是，已经确定的元素之和，在什么情况下将永远满足不了四个元素之和为target
"""


def fourSum(nums, target: int):
    n = len(nums)
    nums.sort()
    result = []

    for i in range(n):
        # 剪枝 ：什么情况下跳过循环
        # 当排序后的第一个数大于目标值，且所有数和目标值都大于0时，是绝对不会有符合的结果的
        if nums[i] > target and nums[i] > 0 and target > 0:
            break
        # 去重，当a位置的第一轮和第二轮值重复时，我们跳过
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 开始确定b元素，和求三数之和一样
        for j in range(i+1,n):
            # 剪枝，已经排序的数组，前两个位置相加大于目标值时，且目标值>0，后面将不会再出现元素是的四个元素相加=target了，
            if nums[i] + nums[j] > target and target > 0:
                break
            # 去重，我们跳过继续遍历下一个b元素
            if j-1>i and nums[j] == nums[j-1]:
                continue
            # 使用双指针确定元素c和元素d
            left, right = j+1, n-1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    # 添加结果集
                    result.append([nums[i],nums[j],nums[left],nums[right]])
                    # 去重
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    # 此时，这个左指针位置和右指针位置的元素都被添加到结果中了，因此都需要更新
                    left += 1 # 更新到下一位
                    right -= 1 # 更新到下一位

    return result


# 使用字典
def sumfour(nums,target):
    # 创建一个字典来存储输入列表中每个数字的频率
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0) +1

    # 创建一个集合来存储最终的答案，并遍历4个数字的所有唯一组合
    ans = set()
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                val = target-(nums[i]+nums[j]+nums[k])
                if val in freq:
                    # 确保没有重复
                    count = (nums[i] == val) + (nums[j] == val) + (nums[k] == val)
                    if freq[val] > count:
                        ans.add(tuple(sorted([nums[i],nums[j],nums[k],val])))

    return [list(x) for x in ans]




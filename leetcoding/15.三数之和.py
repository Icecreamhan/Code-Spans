"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。

请你返回所有和为 0 且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：
输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：
输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。

提示：
3 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""
# 题目:15.三数之和
# 链接
# https://leetcode.cn/problems/3sum/description/
# 思路
"""
回忆一下，你还记得 两数之和吗？----使用哈希表来实现【a+b,map(0-a),对比已经遍历过的元素】
那么，三数之和，是否还可以使用哈希表来解决？
- 题目：一个数组中找到三个元素相加为0，找一个：三元组，并且三元组要去重，a+b+c=0
- 要求 三元组要去重，而哈希表很难处理去重的操作。
- 因此使用双指针的操作

用双指针法：
1、先排序：
    - 因为返回的是元素，而不是下标，所以我们可以进行排序的操作。
    - 为什么进行排序，排序带来了哪些方便？
        - 先nums[i]从index=0开始，接下来，分别在index后的元素中，最左端放置一个left指针，最右端放置一个right，让nums[left]+nums[right] = 0-nums[i]
        - 如果nums[left]+nums[right]>0-nums[i]，那么应该让right--,(右指针向前移动)
        - 如果nums[left]+nums[right]<0-nums[i]，那么应该让left++，(左指针让后移动)
        - 如果nums[left]+numns[right] == 0-nums[i]，那么此时我们找到了目标三元组
        - 所以排序好的数组方便我们进行上述操作。

2、考虑去重
    - 因为数组的元素可能会有重复值的情况，而题目中要求`返回所有和为0，且不重复的三元组`。
    - 如何去重？
    - nums[i]去重
    - nums[left]去重
    - nums[right]去重
        1. 不能重复的三元组，但是三元组内的元素可以重复
        注意判断，nums[i]与nums[i+1]还是nums[i]与nums[i-1]不能重复
        - nums[i] == nums[i+1]
            - nums[i]与其后一个数进行相等性判断，
            - 而前一个数nums[i+1]应该放的是left(另一个数)
            - 所以变成了判断一个结果集中的两个元素是否相等。
            - {-1,-1,2}
        - nums[i] == nums[i-1]
            - nums[i]与其前一个数进行相等性判断，
            - 所以判断的是nums[i]位置的前面是否出现过，
            - 因此应该是nums[i]与nums[i-1]进行相等性判断
            
        2. left & right
        if nums[left] == nums[left+1] left ++
        nums[right] == right[right-1] right --
    - 什么时候去重？
        - 先收获结果，再进行去重
    
"""

"""
# 排序：list.sort()，与sorted(list)
1. list.sort()方法
- 原地排序，直接修改原始列表
- 没有返回值
- 只能用于列表类型
```
words = ["banana", "apple", "cherry"]
words.sort(key=len)  # 按字符串长度排序
print(words)  # 输出：['apple', 'banana', 'cherry']
```

2. sorted(iterable, key=None, reverse=False)
- 不修改原始对象，而是返回一个新的排序后的列表
- 可以用于任何可迭代对象（元组、字典、字符串等）
- 返回的是一个新列表。
```
nums = (5, 2, 9, 1)  # 元组
sorted_nums = sorted(nums)
print(sorted_nums)  # 输出：[1, 2, 5, 9]
```

```
d = {'a': 3, 'b': 1, 'c': 2}
sorted_keys = sorted(d)  # 只对字典的键排序
print(sorted_keys)  # 输出：['a', 'b', 'c']

sorted_items = sorted(d.items(), key=lambda x: x[1])  # 按值排序
print(sorted_items)  # 输出：[('b', 1), ('c', 2), ('a', 3)]
```
"""


def threeSum(nums):
    result = []
    # 方法1：双指针
    # 1. 先进行排序
    nums.sort()
    n = len(nums)

    # 如果排序后的第一个元素已经 > 0，那直接返回空
    if nums[0] > 0:
        return result

    # 2. 用一个for循环，i从下标0的地方开始，同时定一个下标left在i+1位置上，下标right在数组结尾的位置上。
    # a=nums[i]，b = nums[left]， c= nums[right]
    # 逐个遍历nums[i]
    for i in range(n):
        # 先对a去重,
        if i-1 >= 0 and nums[i] == nums[i-1]:
            continue
        # 寻找b 和c
        left = i+1
        right = n-1
        while left < right:
            sumnums = nums[i] + nums[left] + nums[right]
            if sumnums > 0:
                right -= 1
            elif sumnums < 0:
                left += 1
            else:
                result.append([nums[i], nums[left], nums[right]]) # 返回的是元素而不是索引下标值
                # 对b 和 c 去重。(只有我们先找到 a+b+c=0的时候，才考虑去重)
                while right > left and nums[left] == nums[left+1]: # 确保左指针一直在右指针左边
                    left += 1
                while right > left and nums[right] == nums[right-1]: # 确保右指针一直在左指针右边
                    right -= 1
                # 继续移动，找另一组b,c，因为已经排序了，所以不会遇到 -5,2,3与-5,3,2的情况
                left += 1
                right -= 1

    return result


# 使用字典，查找b 和c元素，即给定target,找b和c的不重复值，没看懂
def threeSum(nums):
    result = []
    n = len(nums)
    # 先排序
    nums.sort() # nums = sorted(nums)

    # 先确定 a 元素
    for i in range(n):
        if nums[i] > 0:
            return result # 此时，肯定没有任何一个三元组，满足元素和为0

        # 对 a 元素进行去重,a与遍历过的a进行值对比
        if i-1 >= 0 and nums[i] == nums[i-1]:
            continue

        # 使用哈希法寻找b和c 元素，即寻找两数之和不重复的二元组
        cur = {} # 里面装的是遍历过的元素
        for j in range(i+1, n):
            # 先对b去重：
            if j > i+2 and nums[j] == nums[j-1] == nums[j-2]:
                continue
            target = 0 - nums[i] - nums[j]
            if target in cur:
                result.append([nums[i],nums[j],target])
                # c元素去重
                cur.pop(target) # 我已经找到c元素了，就把与c元素相同的值去掉
            else:
                cur[nums[j]] = j

        return result


# 方法3：力扣的官方解法
def threeSum(nums):
    result = []
    nums.sort()
    n = len(nums)

    # 先寻找元素a
    for i in range(n):
        if nums[i] > 0:
            return result

        # 对a 元素进行去重
        if i-1 >= 0 and nums[i] == nums[i-1]:
            continue

        # 此时，我们找 元素b和元素c,如果我们先对b进行去重，a+b+c = 0,我们找到a+b'+c'=0,b'>b，那么c'<c
        # 就是第二重循环的时候，我们从小到大枚举b，同时从大到小枚举c，

        # 将c 对应的指针初始指向数组最右端
        c = n-1
        target = 0 - nums[i]
        # 枚举b
        for b in range(i+1,n):
            # 需要确保b重复，也就是和上一次枚举的元素不同，从第2圈开始去重的
            if b > i+1 and nums[b] == nums[b-1]:
                continue
            # 先保证 b 的指针 在 c 的左侧
            while b < c and nums[b] + nums[c] > target:
                c -= 1
            # 如果指针重合，随着b后续的增加，就不会有满足 a+b+c=0，并且b<c的c了，可以推出循环
            if b == c:
                break
            if nums[b] + nums[c] == target:
                result.append([nums[i], nums[b], nums[c]]) # 如果b不重复，那么c一定不重复

    return result




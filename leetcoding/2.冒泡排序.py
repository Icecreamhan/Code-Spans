nums = [4,3,2,7,8,2,3,1]

"""
在待排序的一组数中，将相邻的两个数进行比较，若前面的数比后面的数大就交换两数，否则不交换。
如此重复遍历下去，直到没有再需要交互的元素，完成排序。

“大的数往下沉，小的数往上浮，就像是水中的气泡上升一样”

"""


def bubble_sort(nums):
    n = len(nums)

    for i in range(n-1):
        flag = False
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                flag = True

        if not flag:
            break

    return nums
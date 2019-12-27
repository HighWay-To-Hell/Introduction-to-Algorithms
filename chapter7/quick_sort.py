"""
quick_sort
最坏Theta(n^2)
最好O(nlgn)
平均O(nlgn), 任何一种常数比例的划分都会产生深度为Theta(lgn)的递归树, 其中每一层的时间代价都是O(n), 算法的运行时间总是O(nlgn)
"""
import random


def quick_sort(nums: list, l, r):
    if l < r:
        m = partition(nums, l, r)
        quick_sort(nums, l, m - 1)
        quick_sort(nums, m + 1, r)


def partition(nums, l, r):
    random_swap(nums, l, r)  # 随机主元， 以消除最差情况
    i = l - 1
    for j in range(l, r, 1):
        if nums[j] <= nums[r]:
            i += 1
            swap(nums, i, j)
    swap(nums, i + 1, r)
    return i + 1


def random_swap(nums, l, r):
    i = random.randint(l, r)
    swap(nums, i, r)


def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def main():
    nums = [-1, -2, 3, 4, 0, 4, 5, 8]
    print(nums)
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)


if __name__ == '__main__':
    main()

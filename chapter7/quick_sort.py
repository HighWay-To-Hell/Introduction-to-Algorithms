"""
quick_sort
"""


def quicksort(nums: list, l, r):
    if l < r:
        m = partion(nums, l, r)
        quicksort(nums, l, m)
        quicksort(nums, m + 1, r)


def partion(nums, l, r):
    i = l - 1
    for j in range(l, r, 1):
        if nums[j] <= nums[r]:
            i += 1
            swap(nums, i, j)
    swap(nums, i + 1, r)
    return i + 1


def swap(nums, i, j):
    tmp = nums[i]
    nums[i] = nums[j]
    nums[j] = tmp


def main():
    nums = [-1, 0, 1, 2, -3]
    print(nums)
    quicksort(nums, 0, len(nums) - 1)
    print(nums)


if __name__ == '__main__':
    main()

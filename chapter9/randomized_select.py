"""
期望为线性时间的选择算法：
利用修改快排为选择算法，
最坏为Theta(n^2), 期望为Theta(n)， 证明见9.2
"""
from chapter7.quick_sort import quick_sort
from chapter7.quick_sort import partition


def randomized_select(nums: list, l, r, i):
    """
    从nums[l:r+1]中找出第i小的元素
    """
    assert l <= r
    if l == r:
        return nums[l]
    m = partition(nums, l, r)
    k = m - l + 1
    if k == i:
        return nums[m]
    elif k < i:
        return randomized_select(nums, m + 1, r, i - k)
    return randomized_select(nums, l, m - 1, i)


def main():
    nums = [-1, -2, 3, 4, 0, 4, 5, 8]
    print(nums)
    print(randomized_select(nums, 0, len(nums) - 1, 4))
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)


if __name__ == '__main__':
    main()

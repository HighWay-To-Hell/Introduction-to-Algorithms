"""
连续子数组的最大乘积
"""


def find_max_subarray_product(nums: list):
    _max = nums[0]
    _min = nums[0]
    real_max = nums[0]
    for i in nums[1:]:
        tmp_max = _max
        _max = max(tmp_max * i, i, _min * i)
        _min = min(tmp_max * i, i, _min * i)
        real_max = max(real_max, _max)
    return real_max


def main():
    nums = [1, -1, -100, 0, 4, -1, -6, -7, 0, -110, -2, -2, 9, -1]
    print(find_max_subarray_product(nums))


if __name__ == '__main__':
    main()

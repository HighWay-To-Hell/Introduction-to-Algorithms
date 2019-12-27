"""
同时找出最大值和最小值
比较次数最多为 3*int(len(nums)/2)
"""


def find_max_and_min(nums: list):
    cnt = 0

    def _compare(i, j):
        if nums[i] > nums[j]:
            return nums[i], nums[j]
        else:
            return nums[j], nums[i]

    if len(nums) % 2 == 1:
        _max = _min = nums[0]
        p = 1
    else:
        _max, _min = _compare(0, 1)
        cnt += 1
        p = 2
    for i in range(p, len(nums), 2):
        tmp_max, tmp_min = _compare(i, i + 1)
        _max = max(_max, tmp_max)
        _min = min(_min, tmp_min)
        cnt += 3
    return _max, _min, cnt


def main():
    nums = [-1, 0, 10, 3, 9, 0, -1, -2]
    print(nums)
    print(len(nums))
    print(find_max_and_min(nums))


if __name__ == '__main__':
    main()

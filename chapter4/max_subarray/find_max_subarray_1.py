"""
连续子数组的最大和
分治法
find_max_cross_subarray 花费 Theta(n)
T(n) = 2T(n/2) + Theta(n)
时间复杂度为 Theta(nlgn)
"""


def find_max_crossing_subarray(num: list, l, m, r):
    """
    l: left_idx
    m: mid_idx
    r:
    """
    l_max = float("-inf")
    l_sum = 0
    l_max_idx = m
    for l_idx in range(m, l - 1, -1):
        l_sum += num[l_idx]
        if l_sum > l_max:
            l_max = l_sum
            l_max_idx = l_idx

    r_max = float('-inf')
    r_sum = 0
    r_max_idx = m + 1
    for r_idx in range(m + 1, r + 1, 1):
        r_sum += num[r_idx]
        if r_sum > r_max:
            r_max = r_sum
            r_max_idx = r_idx

    return l_max_idx, r_max_idx, l_max + r_max


def find_max_subarray(num: list, l, r):
    if num is None or len(num) == 0 or l > r:
        raise ValueError("error")
    if l == r:
        return l, r, num[l]
    else:
        m = int((l + r) / 2)
        l_low, l_high, l_max = find_max_subarray(num, l, m)
        r_low, r_high, r_max = find_max_subarray(num, m + 1, r)
        cross_low, cross_high, cross_max = find_max_crossing_subarray(num, l, m, r)
        all_max = max(l_max, r_max, cross_max)
        if l_max == all_max:
            return l_low, l_high, l_max
        if r_max == all_max:
            return r_low, r_high, r_max
        return cross_low, cross_high, cross_max


def main():
    nums = [[1],
            [-9, -10, -2, 10, 1, -3, 100, -3, -4],
            [1, 2, -3, 4, 5],
            [-2, 1]]
    for num in nums:
        print(num)
        print(find_max_subarray(num, 0, len(num) - 1))


if __name__ == '__main__':
    main()

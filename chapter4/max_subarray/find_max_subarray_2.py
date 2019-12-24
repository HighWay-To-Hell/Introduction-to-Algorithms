"""
连续子数组的最大和
若已知A[1..j]的最大子数组，则A[1...j+1]的最大子数组要么是A[1..j]的最大子数组， 要么是形如A[i...j+1]的子数组
"""


def find_max_subarray(array: list):
    _max = array[0]
    _sum = array[0]
    l = r = 0
    _sum_l = _sum_r = 0
    for i in range(1, len(array), 1):
        if _sum + array[i] < array[i]:
            _sum = array[i]
            _sum_l = _sum_r = i
        else:
            _sum += array[i]
            _sum_r = i
        if _sum > _max:
            _max = _sum
            l = _sum_l
            r = _sum_r
    return l, r, _max


def main():
    nums = [[5, -4, -2, 5, 6]]
    for num in nums:
        print(num)
        print(find_max_subarray(num))


if __name__ == '__main__':
    main()

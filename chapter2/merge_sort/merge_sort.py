"""
merge_sort
"""


def merge_sort(num: list, l: int, r: int):
    if l < r:
        mid = int((l + r) / 2)
        merge_sort(num, l, mid)
        merge_sort(num, mid + 1, r)
        merge(num, l, mid, r)


def merge(num: list, l: int, mid: int, r: int):
    tmp1 = num[l:mid + 1] + [float("inf")]
    tmp2 = num[mid + 1:r + 1] + [float("inf")]
    tmp_all = []
    i = j = 0
    while len(tmp_all) < r - l + 1:
        if tmp1[i] < tmp2[j]:
            tmp_all.append(tmp1[i])
            i = i + 1
        else:
            tmp_all.append(tmp2[j])
            j = j + 1
    num[l:r + 1] = tmp_all


def main():
    nums = [[],
            [1],
            [2, 1],
            [3, 1, 2],
            [10, -1, 100, 2, 9, 5]]
    for num in nums:
        print(num)
        merge_sort(num, 0, len(num) - 1)
        print(num)


if __name__ == '__main__':
    main()

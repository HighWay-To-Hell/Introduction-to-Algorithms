"""
insertion_sort
worst Θ(n^2) when all reversed
best Θ(n) when all sorted
"""


def insertion_sort(num: list):
    if num is None or len(num) <= 1:
        return
    for i in range(1, len(num), 1):
        j = i - 1
        tmp = num[i]
        while j > -1 and num[j] > tmp:
            num[j + 1] = num[j]
            j = j - 1
        num[j + 1] = tmp


def main():
    nums = [[],
            [1],
            [2, 1],
            [3, 1, 2],
            [10, -1, 100, 2, 9, 5]]
    for num in nums:
        print(num)
        insertion_sort(num)
        print(num)


if __name__ == '__main__':
    main()

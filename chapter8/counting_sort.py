"""
计数排序假设n个输入元素中的每一个都是在[0, k)区间的一个整数，其中k为某个整数，当k=O(n)时，排序的运行时间为Theta(n)

"""


def counting_sort(A, B, k):  # 此方法是稳定的
    C = [0] * k
    for num in A:  # Theta(n)
        C[num] += 1
    for i in range(1, k, 1):  # Theta(k)
        C[i] += C[i - 1]
    for i in reversed(range(len(A))):  # Theta(n), 共Theta(k + n)， 所以当k=O(n)时， 计数排序的运行时间为Theta(n)
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1


def main():
    nums = [0, 1, 0, 1, 2, 4, 5, 3, 3, 4]
    sorted_nums = ["none"] * len(nums)
    k = max(nums) + 1
    counting_sort(nums, sorted_nums, k)
    print(nums)
    print(sorted_nums)


if __name__ == '__main__':
    main()

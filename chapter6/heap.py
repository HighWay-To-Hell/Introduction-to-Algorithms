"""
堆排序的everything
以大顶堆为例
"""


class Heap:
    def max_heapify(self, nums: list, i, size):
        """
        maintain the heap
        时间复杂度为O(lgn)
        """
        left_v = nums[i * 2 + 1] if (i * 2 + 1) < size else float('-inf')
        right_v = nums[i * 2 + 2] if (i * 2 + 2) < size else float('-inf')
        _max = max(nums[i], left_v, right_v)
        if _max == left_v:
            self.swap(nums, i, i * 2 + 1)
            self.max_heapify(nums, i * 2 + 1, size)
        elif _max == right_v:
            self.swap(nums, i, i * 2 + 2)
            self.max_heapify(nums, i * 2 + 2, size)

    def swap(self, nums: list, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def bulid_max_heap(self, nums):
        """
        建堆
        子数组nums[int((len(nums)-1)/2)+1:]的元素都是树的叶节点, 可对其余节点都调用一次max_heapify
        时间复杂度为O(n), 即可以在线性时间内把一个无序数组构造成一个最大堆，证明见算法导论第三版P88
        """
        for i in range(int((len(nums) - 1) / 2), -1, -1):
            self.max_heapify(nums, i, len(nums))

    def heapsort(self, nums):
        """
        先建堆，然后将堆顶元素与最后一个交换后，再维护size-1的堆
        时间复杂度为O(nlgn), 因为n-1次调用max_heapify
        """
        self.bulid_max_heap(nums)
        size = len(nums) - 1
        for i in range(size, 0, -1):
            self.swap(nums, 0, i)
            self.max_heapify(nums, 0, size)
            size -= 1


def main():
    heap = Heap()
    nums = [1, 2, -1, 20, 3, 9, 10, -3, 0, -4]
    print(nums)
    heap.bulid_max_heap(nums)
    print(nums)
    heap.heapsort(nums)
    print(nums)


if __name__ == '__main__':
    main()

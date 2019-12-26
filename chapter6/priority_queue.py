"""
优先队列
一个最大优先队列支持以下操作
insert(S, x), 把元素x插入集合S中
maximum(S),
extract_max(S),
increase_key(S, x, k): 将元素x的关键字值增加到k，这里假设k的值不小于x的原关键字值
最大优先队列使用大顶堆实现
"""

from chapter6.heap import Heap


class PriorityQueue:
    def __init__(self):
        self.heap = Heap()

    def maximum(self, nums):
        return nums[0]

    def extract_max(self, nums: list):
        _max = nums[0]
        self.heap.swap(nums, 0, len(nums) - 1)
        nums.pop()
        self.heap.max_heapify(nums, 0, len(nums))
        return _max

    def insert(self, nums, x):
        nums.append(x)
        i = len(nums) - 1
        while i > 0 and nums[i] > nums[int((i - 1) / 2)]:
            self.heap.swap(nums, i, int((i - 1) / 2))
            i = int((i - 1) / 2)

    def increase_key(self, nums, i, k):
        if nums[i] > k:
            print("nums[i[ already big then k")
        else:
            nums[i] = k
            while i > 0 and nums[i] > nums[int((i - 1) / 2)]:
                self.heap.swap(nums, i, int((i - 1) / 2))
                i = int((i - 1) / 2)


def main():
    pq = PriorityQueue()
    nums = [-1, 2, 3, 0, 9, -3, -4, 8]
    print(nums)
    pq.heap.bulid_max_heap(nums)
    print(nums)
    print(pq.maximum(nums))
    print(pq.extract_max(nums))
    print(nums)
    pq.insert(nums, 100)
    print(nums)
    pq.increase_key(nums, len(nums) - 2, 1000)
    print(nums)


if __name__ == '__main__':
    main()

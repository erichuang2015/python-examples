"""标准库中的堆。
"""

import heapq


def main():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

    # 将 nums「堆」化，不会返回什么，而是在列表上调整
    # 如果不做这一步，下面几个函数是无效的，除非 nums 开始为空
    heapq.heapify(nums)
    print(nums)
    # 将元素压入堆中，堆会自动调整
    heapq.heappush(nums, -1)
    print(nums)
    # 弹出堆顶元素，永远是最小的
    print(heapq.heappop(nums))
    print(heapq.heappop(nums))
    print(nums)


if __name__ == '__main__':
    main()

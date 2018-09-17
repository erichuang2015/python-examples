"""利用 heapq 模块实现查找最大或最小 N 个元素。

当要查找的元素个数相对比较小的时候,函数 nlargest() 和 nsmallest() 是很
合适的。如果你仅仅想查找唯一的最小或最大(N=1)的元素的话,那么使用 min() 和
max() 函数会更快些。类似的,如果 N 的大小和集合大小接近的时候,通常先排序这个
集合然后再使用切片操作会更快点(sorted(items)[:N] 或者是 sorted(items)[-N:]
)。需要在正确场合使用函数 nlargest() 和 nsmallest() 才能发挥它们的优势(如果
N 快接近集合大小了,那么使用排序操作会更好些)。
"""

import heapq


def main():
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))
    print('*' * 50)

    # 两个函数都能接受一个关键字参数,用于更复杂的数据结构中
    portfolio = [
        {'name': 'IBM', 'shares': 100, 'price': 91.1},
        {'name': 'AAPL', 'shares': 50, 'price': 543.22},
        {'name': 'FB', 'shares': 200, 'price': 21.09},
        {'name': 'HPQ', 'shares': 35, 'price': 31.75},
        {'name': 'YHOO', 'shares': 45, 'price': 16.35},
        {'name': 'ACME', 'shares': 75, 'price': 115.65}
    ]
    cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
    expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
    print(cheap)
    print(expensive)
    print('*' * 50)


if __name__ == '__main__':
    main()
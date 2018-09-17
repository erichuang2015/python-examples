"""利用堆实现优先级队列。
"""

import heapq


class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # 插入堆时，先比优先级，若一样，则再比 index（插入顺序），
        # Python 在做元组比较时候，如果前面的比较已经可以确定结果了，后面的比较操作就不会发生了。
        # 因为 index 不可能一样，所以最多比两次（比三次的话，会出错，Item不能比较）
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def main():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    # 仔细观察可以发现,第一个 pop() 操作返回优先级最高的元素。
    # 另外注意到如果两个有着相同优先级的元素(foo 和 grok ),
    # pop 操作按照它们被插入到队列的顺序返回的。
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())


if __name__ == '__main__':
    main()

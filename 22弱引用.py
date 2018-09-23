"""
weakref 模块提供了对象的弱引用。
普遍的引用会增加对象的引用计数，使得它不被垃圾回收。
但当可能存在循环引用，或内存需要删除缓存对象时，
我们不希望这种情形发生。
而弱引用不会阻碍对象被自动回收。
"""

import weakref


class ExpensiveObject:

    def __del__(self):
        print('(Deleting {})'.format(self))


def main():
    obj = ExpensiveObject()
    r = weakref.ref(obj)
    # 注意这里，如果不用弱引用，直接用 `r` 指向 `obj`
    # 那么，下面执行 `del obj` 时，不会从内存中删除 `obj` 指向的对象
    # 因为引用计数不为 0。
    # 用弱引用不增加引用计数。

    print('obj:', obj)
    print('ref:', r)
    print('r():', r())

    print('deleting obj')
    del obj
    print('r():', r())


if __name__ == '__main__':
    main()

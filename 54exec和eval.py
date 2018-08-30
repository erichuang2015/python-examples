"""exec() 和 eval() 。

exec() 执行任意一段代码， 返回值永远是 None。
eval() 计算指定表达式的值（等式右边的），返回结果。

exec() 创建变量，有个作用域问题，
在全局调用 exec() 创建一个变量，会创建一个全局变量；
在函数内调用 exec()，却不会创建一个局部变量。

exec() 中使用变量，则先找当前上下文中的局部变量，找不到则找全局变量。

exec() 可以传入一个命名空间，指定使用命名空间的变量，
exec() 中创建的变量，会通过命名空间传出。
"""


e = 10
def main():
    # a = 1
    # b = 2

    # c = eval('a + b')
    # print(c)

    # d = eval('a + b')
    # exec('print(d)')

    # exec('print(e)')

    namespace = {'a': 1, 'b': 2}
    exec('c = a + b', namespace)
    print(namespace['c'])


if __name__ == '__main__':
    main()

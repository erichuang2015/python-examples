"""
高效数据结构，数组用法。
"""

import array


def main():
    # 显示所有数组所有可用的创建类型
    """
    Type code	C Type
    'b'	        signed char
    'B'	        unsigned char
    'u'	        Py_UNICOD
    'h'	        signed short
    'H'	        unsigned short
    'i'	        signed int
    'I'	        unsigned int
    'l'	        signed long
    'L'	        unsigned long
    'q'	        signed long long
    'Q'	        unsigned long long
    'f'	        float
    'd'	        double
    """
    print(array.typecodes)

    # 创建一个数组，支持如下方式
    # array('l')
    # array('u', 'hello \u2641')
    # array('l', [1, 2, 3, 4, 5])
    # array('d', [1.0, 2.0, 3.14])
    a = array.array('i')

    # 创建数组所用类型
    print(a.typecode)
    # 所用类型的大小（字节）
    print(a.itemsize)
    # 在数组尾添加元素
    a.append(10)
    # 删除元素，默认在最后，可指定位置
    a.pop()
    # 在指定位置插入值
    a.insert(0, 1)
    # 把一个列表添加到数组尾
    a.extend([1, 3, 2, 4, 3, 5])
    # 返回指定值的数量
    print(a.count(1))
    # 删除指定值，只删除第一个
    a.remove(3)
    # 反转数组
    a.reverse()
    # 指定值索引，返回第一个值的
    print(a.index(1))
    # 显示数组信息，返回一个双元组，（address, length）
    print(a.buffer_info())
    # 显示数组值
    for i in a:
        print(i, end='')
    print()
    # 转换成列表
    print(a.tolist())
    # 转换成字节
    print(a.tobytes())
    # 将内容写入文件
    with open('test.txt', 'wb') as f:
        a.tofile(f)

    """此外还有"""
    # a.fromlist(lst)
    # a.frombytes(s)
    # a.fromfile(f, n)  # n 指读取数量

if __name__ == '__main__':
    main()

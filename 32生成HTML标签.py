#!/usr/bin/env python3
# coding: utf-8

"""以tag函数示范Python函数参数相关问题."""


def tag(name, *content, c=None, **attrs):
    """生成HTML标签."""

    if c:
        attrs['class'] = c

    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, cc, name) for cc in content)
    else:
        return '<%s%s />' % (name, attr_str)


def main():
    # 传入单个位置参数, 生成一个指定名称的空标签
    print(tag('br'))
    print('*' * 60)
    # 第一个参数后面的任意个参数会被*content捕获, 存入一个元祖
    print(tag('p', 'hello', 'world'))
    print('*' * 60)
    # tag函数参数中没有明确指定名称的关键字参数会被**attrs捕获, 存入一个字典
    print(tag('p', 'hello', id=33))
    print('*' * 60)
    # c参数只能作为关键字参数传入
    print(tag('p', 'hello', 'world', c='sidebar'))
    print('*' * 60)
    # 第一个位置参数name也能作为关键字参数传入
    print(tag(content='world', name='img'))
    print('*' * 60)
    # 在my_tag前面加上**, 字典中所有的元素作为单个参数传入, 同名键会绑定到对应的具名参数上, 余下的则被*attrs捕获
    my_tag = {
        'name': 'img',
        'title': 'Sunset Boulevard',
        'src': 'sunset.jpg',
        'class': 'framed'
    }
    print(tag(**my_tag))
    print('*' * 60)
    

if __name__ == '__main__':
    main()

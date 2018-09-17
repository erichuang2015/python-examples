"""
使用type动态创建类.
"""


class Foo:
    bar = True


def echo_bar(self):
    print(self.bar)


# 三个参数分别是: 创建的类名, 继承的类(元组), 类的属性或方法(字典)
FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
fc = FooChild()
fc.echo_bar()
print('*' * 50)
# 类的类是元类(type)
print(FooChild.__class__.__name__)

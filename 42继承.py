#!/usr/bin/env python3
# coding: utf-8


class Person:
    def __init__(self, name, age, sex):
        # 通过调用方法初始化，可以对参数进行更好的控制
        self.setName(name)
        self.setAge(age)
        self.setSex(sex)

    def setName(self, name):
        if not isinstance(name, str):
            print('name must be string')
            self.__name = ''
        else:
            self.__name = name

    def setAge(self, age):
        if not isinstance(age, int):
            print('age must be integer')
            self.__age = 0
        else:
            self.__age = age

    def setSex(self, sex):
        if sex not in ('male', 'female'):
            print('sex must be "man" or "woman"')
            self.__sex = 'unkown'
        else:
            self.__sex = sex

    def show(self):
        print(self.__name, self.__age, self.__sex)

    def setDeapartment(self, department):
        """纯虚函数."""
        
        raise NotImplementedError


class Teacher(Person):
    def __init__(self, name, age, sex, deapartment):
        # 采用super()方式时，会自动找到第一个多继承中的第一个父类,
        # 但是如果还想强制调用其他父类的 init ()函数或两个父类的同名函数时,
        # 就要使用普通调用父类函数的方法了，如
        # A.__init__(self)    B.__init__(self)
        super().__init__(name, age, sex)
        self.setDeapartment(deapartment)
    
    def setDeapartment(self, department):
        if not isinstance(department, str):
            print('deparment must be str')
            self.__department = '' 
        else:
            self.__department = department

    def show(self):
        super().show()
        print(self.__department)
        

if __name__ == '__main__':
    xm = Person('xm', 19, 'male')
    xm.show()
    print('=' * 30)

    zs = Teacher('zs', 40, 'female', 'Math')
    zs.show()
    zs.setAge(30)
    zs.show()

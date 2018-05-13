#!/usr/bin/env python3
# coding:utf-8

"""用类实例化另一个类的属性, 使结构清晰."""
    
import collections


Grade = collections.namedtuple('Grade', ('score', 'weight'))


class Subject:
    def __init__(self):
        self._grades = []

    def report_grade(self, score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight


class Student:
    def __init__(self):
        self._subjects = {}

    def subject(self, name):
        if name not in self._subjects:
            self._subjects[name] = Subject() # 用Subject类实例化
        return self._subjects[name]

    def average_grade(self):
        total, count = 0, 0
        for subject in self._subjects.values():
            total += subject.average_grade()
            count += 1
        return total / count


class Gradebook:
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student() # 用Student类实例化
        return self._students[name]


if __name__ == '__main__':
    book = Gradebook()
    albert = book.student('Albert Einstein')
    math = albert.subject('Math')
    math.report_grade(80, 0.10)
    print(albert.average_grade())


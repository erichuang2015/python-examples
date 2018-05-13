#!/usr/bin/env python3
# coding: utf-8


class BySubjectGradeBook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name):
        self._grades[name] = {}

    def report_grade(self, name, subject, grade):
        # 这行很精彩
        self._grades[name].setdefault(subject, []).append(grade)

    def average_grade(self, name):
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count


book = BySubjectGradeBook()
book.add_student('ghf')
book.report_grade('ghf', 'Math', 70)
book.report_grade('ghf', 'Math', 88)
book.report_grade('ghf', 'Music', 60)
avg = book.average_grade('ghf')
print(book._grades)


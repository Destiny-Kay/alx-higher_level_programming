#!/usr/bin/python3
'''A student class'''


class Student:
    def __init__(self, first_name, last_name, age):
        '''
        class instantiator
        Args:
            first_name: first name of student
            last_name: last name of student
            age: age of the student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        retrieves a Student instance
        '''
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

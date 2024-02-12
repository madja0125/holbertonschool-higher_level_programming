#!/usr/bin/python3

"""module that retrieves a dictionary representation of
a Student instance"""


class Student:
    """class that define a student"""

    def __init__(self, first_name, last_name, age):
        """method that set first name, last name and age"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """method that return a dictionary"""
        return {'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
                }

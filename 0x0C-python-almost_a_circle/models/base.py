#!/usr/bin/python3
'''The base class definition'''
import json
import csv


class Base():
    '''
        Base class definition: handles the id attribute in all other classes
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''base class initializer'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns JSON representation of list_dictionaries'''
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the JSON string repr of list_objs to a file'''
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        '''returns list of json string representation'''
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''returns an instance with all attributes set'''
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        '''returns a list of instances'''
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dict = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dict]
        except IOError:
            return []

    def save_to_file_csv(cls, list_objs):
        '''serializes data in csv'''
        filename = cls.__name__ + '.csv'
        with open(filename, 'w', newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                writer = csv.DictWriter(f, fieldnames=fields)
                for obj in list_objs:
                    writer. writerow(obj.to_dictionary())

    def load_from_file_csv(cls):
        '''deserializes data in csv'''
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                else:
                    fields = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fields)
                list_dicts = [
                    dict([k, int(v)] for k, v in d.items()) for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

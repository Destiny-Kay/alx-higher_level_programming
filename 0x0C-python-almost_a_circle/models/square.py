#!/usr/bin/python3
'''defines a square class'''
from .rectangle import Rectangle


class Square(Rectangle):
    '''
        The  square class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        '''square class constructor'''
        super().__init__(id=id, width=size, height=size, x=x, y=y)

    @property
    def size(self):
        '''size getter'''
        return self.width

    @size.setter
    def size(self, value):
        '''size setter'''
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''updates a square instance'''
        if len(args) != 0:
            if len(args) <= 4:
                self.id = args[0] if len(args) >= 1 else self.id
                self.width = args[1] if len(args) >= 2 else self.width
                self.height = args[1] if len(args) >= 2 else self.height
                self.x = args[2] if len(args) >= 3 else self.x
                self.y = args[3] if len(args) == 4 else self.y
        else:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        '''returns the dictionary representation of a square'''
        dict_repr = {
            'id': self.id,
            'x':  self.x,
            'size': self.size,
            'y': self.y
            }
        return dict_repr

    def __str__(self):
        '''string representation of square'''
        return (
            "[square] ({}) {}/{} - {}"
            .format(self.id, self.x, self.y, self.width)
            )

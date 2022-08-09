#!/usr/bin/python3
"""base class file"""
import json
import os


class Base:
    """Base class definition"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset_base_obj(cls):
        """Resets the base object number for my tests"""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a json string"""

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves the list of objects to a file in json"""

        list_dict = []
        f_name = ''
        if list_objs is not None:
            for i in range(len(list_objs)):
                list_dict.append(list_objs[i].to_dictionary())

            f_name = list_objs[0].__class__.__name__

        with open(f'{f_name}.json', 'w') as f:
            json_str = Base.to_json_string(list_dict)
            return f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Returns a dict list from a json string"""

        list_dict = []
        if json_string is not None and json_string != '':
            list_dict.append(json.loads(json_string))
        
        return list_dict

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of a class"""

        if cls.__name__ == 'Rectangle':
         new_instance = cls(1,1)
        else:
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        '''
            loading dict representing the parameters for
            and instance and from that creating instances
        '''
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, encoding="UTF8") as fd:
                content = cls.from_json_string(fd.read())
        except:
            return []

        instances = []

        for instance in content:
            tmp = cls.create(**instance)
            instances.append(tmp)

        return instances

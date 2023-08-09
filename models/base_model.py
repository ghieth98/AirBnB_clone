#!/usr/bin/python3
"""
Base classes for the entire AIRBNB Consol project
"""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base for all the classes in the entire project

    
    Arttributes:
        id(str): Which handles unique user identity
        created_at: Which assigns current datetime
        updated_at: Which updates current datetime

        
    Methods:
        __str__: Which prints the class id, name and it creates dictionary
        representations of the input values
        save(self): Which updates instance arttributes with current datetime
        to_dict(self): Which returns the dictionary values of the instance obj

    """


    def __init__(self, *args, **kwargs):
        """The public instance artributes initialization
        after creation

        Args:
            *args(args): An arguments
            **kwargs(dict): An attrubute of values

        """
        DT_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(
                        value, DT_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """
        It returns a string representation of the class
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        It updates the public instance attribute:
        'updated_at' - with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        A method returns a dictionary containing all 
        keys/values of __dict__ instance
        """
        map_obj = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_obj[key] = value.isoformat()
            else:
                map_obj[key] = value
        map_obj["__class__"] = self.__class__.__name__
        return map_obj


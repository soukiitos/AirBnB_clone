#!/usr/bin/python3
'''The HBNBCCommand Class'''
import cmd
from models.base_model import BaseModel
import models
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    __classes = {"BaseModel": BaseModel, "User": User}

    '''Create a new instance of BaseModel, Save, Print id'''
    def do_create(self, arg):
        if arg:
            if arg in self.__classes:
                new_instance = self.__classes[arg]()
                new_instance.save()
                print(f"{new_instance.id}")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    '''Print the string representation of an instance'''
    def do_show(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            all_objects = models.storage.all()
            for key in all_objects.keys():
                class_name, obj_id = key.split('.')
                if args[0] == class_name and args[1] == obj_id:
                    print(all_objects[key])
                    return
            print("** no instance found **")

    '''Delete an instance'''
    def do_destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")
        else:
            all_objects = models.storage.all()
            for key in all_objects.keys():
                class_name, obj_id = key.split('.')
                if args[0] == class_name and args[1] == obj_id:
                    del all_objects[key]
                    models.storage.save()
                    return
            print("** no instance found **")

    '''Print all string representation of all instances'''
    def do_all(self, arg):
        args = arg.split()
        if len(args) == 0:
            all_objects = models.storage.all()
            for key in all_objects.keys():
                print(all_objects[key])
        elif len(args) == 1 and args[0] in self.__classes:
            all_objects = models.storage.all()
            for key in all_objects.keys():
                class_name, obj_id = key.split('.')
                if class_name == args[0]:
                    print(all_objects[key])
        else:
            print("** class doesn't exist **")

    '''Ubdate an instance'''
    def do_update(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.__classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        instance_key = f"{class_name}.{instance_id}"
        obj_dict = models.storage.all()
        if instance_key not in obj_dict:
            print("** no instance found **")
            return
        instance = obj_dict[instance_key]
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if attribute_name in ["id", "created_at", "updated_at"]:
            print("** can't update this attribute **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attribute_value = args[3].strip('"')
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    '''Quit command to exit the program'''
    def do_quit(self, arg):
        return True

    '''Exit the program using EOF'''
    def do_EOF(self, arg):
        print()
        return True

    '''Do nothing on an empty line'''
    def emptyline(self):
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

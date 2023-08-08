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



    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Exit the programm usinf EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()

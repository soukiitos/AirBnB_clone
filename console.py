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
import json


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
            }

    def do_create(self, arg):
        """
            it Creates a new instance, Saves it then Prints its 'id'.
        """
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
        """
            a method that Prints the string representation
            of a specific instance
        """
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

    def help_show(arg):
        """a help method which shows the Usage of 'show'"""
        print("Usage: show <class_name> <id> or <class>.show(<id>)")

    def do_destroy(self, arg):
        """a method that deletes an instance"""
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
        """a method that Prints the string representation of all instances"""
        args = arg.split()
        lst = []
        if len(args) == 0:
            all_objects = models.storage.all()
            for key in all_objects.keys():
                lst.append(str(all_objects[key]))
            if len(lst) >= 1:
                print(lst)
        elif len(args) == 1 and args[0] in self.__classes:
            all_objects = models.storage.all()
            for key in all_objects.keys():
                class_name, obj_id = key.split('.')
                if class_name == args[0]:
                    lst.append(str(all_objects[key]))
            if len(lst) >= 1:
                print(lst)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """ a method that updates an instance"""
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
        try:
            attribute_value = int(attribute_value)
        except ValueError:
            pass
            try:
                attribute_value = float(attribute_value)
            except ValueError:
                pass
        setattr(instance, attribute_name, attribute_value)
        instance.save()

    def do_count(self, arg):
        """
            a method that returns a number of instances
            of a specific class.
        """
        args = arg.split()
        if len(args) != 1:
            print("** Class name missing **")
        else:
            class_name = args[0]
            if class_name in self.__classes:
                all_objects = models.storage.all()
                count = sum(
                        1 for key in all_objects
                        if key.split('.')[0] == class_name
                        )
                print(count)
            else:
                print("** class doesn't exist **")

    def default(self, arg):
        """a default method which manipulates several commands"""
        cmdPattern = r"^([A-Za-z]+)\.([a-z]+)\(([^)]*)\)"
        meth = re.match(cmdPattern, arg)
        if not meth:
            super().default(arg)
            return
        class_name, method, j = meth.groups()
        if class_name not in self.__classes:
            print("** Unknown class:", class_name)
            return
        if method == 'all':
            self.do_all(class_name)
        if method == 'count':
            self.do_count(class_name)
        if method == 'show':
            instance_id = j.strip('"')
            if not instance_id:
                print("** Instance id missing **")
                return
            self.do_show("{} {}".format(class_name, instance_id))
        if method == 'destroy':
            instance_id = j.strip('"')
            if not instance_id:
                print("** Instance id missing **")
                return
            self.do_destroy("{} {}".format(class_name, instance_id))
        if method == 'update':
            instance_id, attrib_dict_str = j.split(',', 1)
            instance_id = instance_id.strip('"')
            attrib_dict_str = attrib_dict_str.replace('\'', '"')
            attrib_dict = json.loads(attrib_dict_str)
            for key, value in attrib_dict.items():
                self.do_update("{} {} {} {}".format(
                    class_name, instance_id, key, value)
                    )

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program using EOF"""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()

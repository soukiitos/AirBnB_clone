#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb)"
    __classes = {"BaseModel": BaseModel}

    def do_create(self, arg):
        if arg:
            if arg in self.__classes:
                base_model = self.__classes[arg]()
                base_model.save()
                print(f"{base_model.id}")
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

    def destroy(self, arg):
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) != 2:
            print("** instance id missing **")








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

#!/usr/bin/python3
"""
Defines the hbnb console.
Entry point to the command interpreter.
"""
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
import cmd
from models.place import Place
import re
from models.review import Review
from models.user import User
from models.state import State


#def parser(args):
#    curly_braces = re.search(r"\{(.*?)\}", args)
#    brackets = re.search(r"\[(.*?)\]", args)
#    if curly_braces is None:
#        if brackets is None:
#            return [words.strip(",") for words in args.split()]
#        else:
#            lexer = split(args[:brackets.span()[0]])
#            retl = [words.strip(",") for words in lexer]
#            retl.append(brackets.group())
#            return retl
#    else:
#        lexer = re.split(args[:curly_braces.span()[0]])
#        retl = [words.strip(",") for words in lexer]
#        retl.append(curly_braces.group())
#        return retl

def extract_braces_contents(args):
    braces_pattern = r"\{(.*?)\}"
    braces_match = re.search(braces_pattern, args)
    if braces_match:
        return braces_match.group(1)
    else:
        return None

def extract_brackets_contents(args):
    brackets_pattern = r"\[(.*?)\]"
    brackets_match = re.search(brackets_pattern, args)
    if brackets_match:
        return brackets_match.group(1)
    else:
        return None

def parser(args):
    args_list = []
    braces_contents = extract_braces_contents(args)
    if braces_contents:
        args_list.append(braces_contents)
    args_list.extend(args.split(","))
    brackets_contents = extract_brackets_contents(args)
    if brackets_contents:
        args_list.append(brackets_contents)
    return args_list


class HBNBCommand(cmd.Cmd):
    """
    Defines the hbnb command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def do_create(self, args):
        """
        Usage: create <class>
        Creates a new instance of BaseModel, saves it to the JSON file
        and prints the id.
        """
        arg_list = parser(args)
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            models.storage.save()

    def do_show(self, args):
        """
        Usage: show <class> <id> or <class>.show(<id>)
        Prints the string representation of an instance based on the class
        name and id.
        """
        arg_list = parser(args)
        obj_dict = models.storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, args):
        """
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        Deletes an instance based on the class name & id
        and saves the change into the JSON file.
        """
        arg_list = parser(args)
        obj_dict = models.storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            models.storage.save()

    def do_all(self, args):
        """
        Usage: all or all <class> or <class>.all()
        Prints all string representation of all instances based or not on
        the class name.
        If no class is specified, displays all instantiated objects.
        """
        arg_list = parser(args)
        if len(arg_list) > 0 and arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in models.storage.all().values():
                if len(arg_list) > 0 and arg_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(arg_list) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, args):
        """
        Usage:
        update <class> <id> <attribute_name> "<attribute_value>" or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Updates an instance based on the class name and id by adding or
        updating attribute and saves the changes into the JSON file.
        """
        arg_list = parser(args)
        obj_dict = models.storage.all()

        if len(arg_list) == 0:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                type(eval(arg_list[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_list) == 4:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            if arg_list[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[arg_list[2]] = val_type(arg_list[3])
            else:
                obj.__dict__[arg_list[2]] = arg_list[3]
        elif type(eval(arg_list[2])) == dict:
            obj = obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            for key, value in eval(arg_list[2]).items():
                if (key in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[key]) in
                        {str, int, float}):
                    val_type = type(obj.__class__.__dict__[key])
                    obj.__dict__[key] = val_type(value)
                else:
                    obj.__dict__[key] = value
        models.storage.save()

    def do_count(self, args):
        """
        Usage: count <class> or <class>.count()
        Retrieves the number of instances of a given class.
        """
        arg_list = parser(args)
        count = 0
        for obj in models.storage.all().values():
            if arg_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, args):
        """
        Default behavior for cmd module when input is invalid.
        """
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", args)
        if match is not None:
            arg_list = [args[:match.span()[0]], args[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(args))
        return False

    def emptyline(self):
        """
        Empty line handler - prohibits empty line + ENTER from execution.
        """
        pass

    def do_quit(self, line):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, line):
        """
        Exits the command interpreter when ctrl+d is typed.
        EOF signal to exit the program.
        """
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

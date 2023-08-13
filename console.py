#!/usr/bin/python3
"""
Entry point to the command interpreter.
"""
import cmd
from modules.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter implementation for Airbnb clone.
    """
    prompt = "(hbnb) "

    def do_create(self):
        pass

    def do_show(self):
        pass

    def do_destroy(self):
        pass

    def do_all(self):
        pass

    def do_update(self):
        pass

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

    def help_quit(self):
        print("Quit command to exit the program.")

    def do_EOF(self, line):
        """
        Exits the command interpreter when ctrl+d is typed.
        """
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

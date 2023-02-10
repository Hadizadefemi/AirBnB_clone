#!/usr/bin/python3
""" Module console
the entry point of the command interpreter
"""
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ the entry point of the command interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""

        sys.exit(1)

    def do_EOF(self, line):
        """ Exit interpreter If a command handler returns true"""

        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

from __future__ import absolute_import, print_function

from myext.command import MyextCommand


def main():
    try:
        myext = MyextCommand()
        myext.execute_from_commandline()
    except:
        raise


if __name__ == "__main__":
    main()

"""
Usage:
    cli.py (-i | --interactive)
    cli.py (-h | --help | --version)
Options:
    --i Input Bucket
    --o Output Bucket
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
    --baud=<n>  Baudrate [default: 9600]
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from pyfiglet import Figlet


def docopt_cmd(func):

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class MyInteractive (cmd.Cmd):
    f = Figlet(font='slant')
    print(f.renderText('Sanity'))
    intro = 'Welcome to Sanity!' \
        + ' (type help for a list of commands.)'
    prompt = '(Sanity) '
    file = None

    @docopt_cmd
    def do_create(self, arg):
        """Usage:
create --i <input> --o <output>
Options:
--i    Input Bucket
--o    Output Bucket
        """

        print(arg)

    @docopt_cmd
    def do_serial(self, arg):
        """Usage: serial <port> [--baud=<n>] [--timeout=<seconds>]
Options:
    --baud=<n>  Baudrate [default: 9600]
        """

        print(arg)

    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])
#print(opt)
if opt['--interactive']:
    MyInteractive().cmdloop()

#print(opt)
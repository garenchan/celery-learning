from __future__ import absolute_import, print_function

from celery.bin.base import Command

from . import __version__


class MyextCommand(Command):


    def add_arguments(self, parser):
        c = self.app.conf
        opts = parser.add_argument_group('Myext Options')
        opts.add_argument('-t', '--test', type=float)
        opts.add_argument('-l', '--loglevel', default='WARN')
        
    def execute_from_commandline(self):
        print("Just to show how to extend Celery's subcommands!")
        
    def run(self, *args, **options):
        self.execute_from_commandline()
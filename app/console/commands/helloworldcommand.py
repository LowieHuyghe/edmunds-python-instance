
from edmunds.console.command import Command
import click


class HelloWorldCommand(Command):
    """
    Prints Hello World!
    """

    @click.option('--what', default='World', help='Hello what?')
    def run(self, what):
        """
        Run the command
        :param what:    Hello what?
        :type what:     str
        :return:    void
        """

        print('Hello %s!' % what)

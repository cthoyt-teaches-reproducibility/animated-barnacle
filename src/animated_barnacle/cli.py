import pickle
import sys

import click

from . import reanimate


def bury_bodies(bodies, file):
    """Dumps the bodies in a pickle object

    :param bodies: An iterator of strings. Can be a list, file, file-like, or any iterable
    :type bodies: iter of str
    :param file: A writable stream
    :type file: file or file-like
    """
    bodies = reanimate.build_bodies(line.strip() for line in bodies)
    pickle.dump(bodies, file)


@click.command(help="A command line tool to help bury your bodies into a pickled grave")
@click.option('-i', '--input-file', type=click.File('r'), default=sys.stdin, help='Input file path')
@click.option('-o', '--output-file', type=click.File('wb'), default=sys.stdout, help='Output file path')
def main(input_file, output_file):
    bury_bodies(input_file, output_file)


if __name__ == '__main__':
    main()

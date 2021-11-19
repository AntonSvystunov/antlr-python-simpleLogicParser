from .cli import start

import argparse


def main():
    parser=argparse.ArgumentParser()

    parser.add_argument('--inputFile', help='Input file with grammar expression')
    parser.add_argument('--trues', help='Variable names equals true as comma separated list (ex. a,b,c)')
    parser.add_argument('--expr', help='Expression (ex. (a AND b))')

    args=vars(parser.parse_args())

    print(start(**args))
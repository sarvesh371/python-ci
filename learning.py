import argparse

import args

parser = argparse.ArgumentParser()
parser.add_argument("--inputString", default='Type What you want to print', type=str, required=True,
                    help="Input String")
input = args.inputString
print(input)

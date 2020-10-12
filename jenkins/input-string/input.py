import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--inputString", default='Type What you want to print', type=str, required=True,
                    help="Input String")
args = parser.parse_args()
input = args.inputString
print(input)
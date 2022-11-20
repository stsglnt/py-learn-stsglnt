import argparse


parser = argparse.ArgumentParser(description="Calculate sum of integers")
parser.add_argument('input', action='store', type=int, nargs="*")
args = parser.parse_args()
args_sum = sum(args.input)
print(args_sum)

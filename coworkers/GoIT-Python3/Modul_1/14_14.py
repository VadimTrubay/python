import sys


def parse_args():
    result = ""
    for arg in sys.argv[1:]:
        result += arg
        result += " "
    return result[:-1]
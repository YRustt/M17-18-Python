
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Arguments for model module.")
    parser.add_argument('-i', '--iterations', type=int, help='number of iterations')
    parser.add_argument('-c', '--config', help='path to the config file')
    parser.add_argument('-w', '--write', help='path to file with result')
    parser.add_argument('-r', '--read', help='path to file with input')

    args = parser.parse_args()

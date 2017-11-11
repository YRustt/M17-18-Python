
import argparse


from model_gui import gui
from model import (
    init,
    generate_ocean,
    read_ocean,
    write_ocean,
    run
)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Arguments for model module.")
    parser.add_argument(
        '-i', '--iterations',
        type=int,
        required=False,
        help='number of iterations'
    )
    parser.add_argument(
        '-s', '--size',
        type=int,
        required=False,
        help='ocean size'
    )
    parser.add_argument(
        '-c', '--config',
        required=False,
        help='path to the config file'
    )
    parser.add_argument(
        '-w', '--write',
        required=False,
        help='path to file with result'
    )
    parser.add_argument(
        '-r', '--read',
        required=False,
        help='path to file with input'
    )
    parser.add_argument(
        '-g', '--gui',
        action='store_true',
        help='visualization'
    )

    args = parser.parse_args()

    if args.config is not None:
        init(args.config)

    if args.read is not None:
        ocean = read_ocean(args.read, args.size)
    else:
        ocean = generate_ocean(args.size)

    if args.gui:
        gui(ocean, args.iterations)
    else:
        run(ocean, args.iterations)

    if args.write is not None:
        write_ocean(args.write, ocean)

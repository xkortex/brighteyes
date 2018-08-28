from __future__ import print_function
import argparse

from brighteyes.xrandr import Xrandr
from brighteyes.monitors import Monitors
from brighteyes.config import cfgget, cfgset

def set_arg_parser():
    parser = argparse.ArgumentParser(description='Brighteyes - better command line tool for monitor control')
    parser.add_argument("-v", "--verbose", action="store_true",
                    help="output verbosity")
    parser.add_argument("-b", "--bright", type=float,
                        help="Specify brightness")
    parser.add_argument("-k", "--colortemp", type=int, default=6000,
                        help="Specify the color temperature (in K)")
    parser.add_argument("-q", "--query", action="store_true",
                        help="Query the attached monitors")
    parser.add_argument("-u", "--up", action="store_true",
                        help="Increase brightness one tick")
    parser.add_argument("-d", "--down", action="store_true",
                        help="Decrease brightness one tick")
    return parser

def main():
    parser = set_arg_parser()
    args = parser.parse_args()
    verbose = args.verbose
    xr = Xrandr(verbose=verbose)
    mons = Monitors(verbose=verbose)
    print(mons.active)
    print(mons.brightness)

    if args.bright:
        print('set brightness', args.bright)
        mons.brightness = args.bright
        return

    if args.up:
        mons.inc_bright()
        return

    if args.down:
        mons.dec_bright()
        return

if __name__ == "__main__":
    main()
#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2016 Sept. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : vaudice
    Script Name  : dcli.py
    License      : GNU General Public License v3.0


    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
import dice
import argparse as ap

CORRECT_USAGE = False


def check_if_incorrect_usage():
    if not CORRECT_USAGE:
        message = """WARNING: This script is meant for using from the CLI.
    It is not meant for importing into your code. Import "dice.py"
    directly into your code for all the remaining purposes. 
    """
        print(message)
        exit(1)
    else:
        return
    return


def main(no_of_rolls=1):
    check_if_incorrect_usage()
    the_dice = dice.Dice()
    no_of_rolls = 1 if no_of_rolls <= 0 else no_of_rolls
    return [the_dice.roll for _ in range(no_of_rolls)]


if __name__ == '__main__':
    CORRECT_USAGE = True
    parser = ap.ArgumentParser(prog='dice-cli',
                               usage='%(prog)s [options]',
                               description='Dice Simulator.',
                               epilog="Dice Simulator written in Python"
                               )
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 0.0.1 (Unstable Alpha)')
    parser.add_argument('-n', "--nos",
                        help="Number of dice(s) to roll",
                        required=False,
                        type=int,
                        default=1)
    args = parser.parse_args()
    result = main(args.nos)
    print(result)
else:
    CORRECT_USAGE = False

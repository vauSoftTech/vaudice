#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2016 Sept. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : vaudice
    Script Name  : dice.py
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

from time import time
from random import SystemRandom
from pathlib import Path


class Dice:
    """A Class that mimics a physical dice used in board games."""

    def __init__(self):
        super().__init__()
        self._seed = int(time() * 100_000)
        self._generator = SystemRandom(self._seed)
        self.last_result = None
        return

    @property
    def roll(self):
        self.last_result = self._generator.randint(1, 6)
        return self.last_result

    def __str__(self):
        s = "Dice Object" if self.last_result is None else \
            "Dice that last rolled to {}".format(self.last_result)
        return s

    def __repr__(self):
        return "Dice()"

    @property
    def picture_file_name(self):
        folder = Path(__file__).absolute().parent
        file_name = folder / Path("config/D{}.png".format(self.last_result))
        file_name = file_name if file_name.exists() else Path("")
        return file_name


def main():
    """
    When this unit is run as script from command line, this main method is
    called. It just simulates 20 rolls of Dice.
    """
    d = Dice()
    for i in range(1, 11):
        print("Dice rolled to {}.".format(d.roll))
        x = d.picture_file_name
        y = Path.cwd()
        try:
            z = x.relative_to(y)
        except ValueError:
            z = x.absolute()
        print("     picture \"{}\".".format(z))
    return


if __name__ == '__main__':
    main()

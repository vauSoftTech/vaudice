#!/usr/bin/env python3
# -*- coding: utf_8 -*-
"""

    Copyright    : 2016 Sept. A. R. Bhatt.
    Organization : VAU SoftTech
    Project      : vaudice
    Script Name  : dgui.py
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
from tkinter import *
from tkinter.ttk import *
import diceframe


class DiceApp(Frame):
    """GUI to interface with dice.py """

    def __init__(self, parent=None, app_title=None, app_icon=None,
                 app_height=-1, app_width=-1, **kw):

        def create_widgets(container):
            container.dice_1 = diceframe.DiceFrame("Dice One")
            container.dice_2 = diceframe.DiceFrame("Dice Two")
            return

        def widget_placement(place_on):
            place_on.dice_1.grid(row=2, column=0, ipadx=5, ipady=5)
            place_on.dice_2.grid(row=2, column=1, ipadx=5, ipady=5)
            return

        if parent is not None:
            self.parent = parent
        else:
            self.parent = Tk()

        super().__init__(**kw)

        if app_title is None:
            self.master.title("Dice Simulator by VAU")
        else:
            self.master.title("{} by VAU".format(app_title))

        create_widgets(self)
        widget_placement(self)
        self.grid()
        return

    def run(self):
        self.parent.mainloop()
        return


def main():
    app = DiceApp()
    app.run()
    return


if __name__ == '__main__':
    main()

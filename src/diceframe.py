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
# from tkinter.tix import *
import dice


class DiceFrame(Frame):

    def __init__(self, dice_name=None):
        super().__init__()
        self._dice_name = StringVar()
        self._result = StringVar()

        if dice_name is None:
            dice_name = "Unnamed"
        if dice_name.strip() == "":
            dice_name = "Unnamed"

        self._dice_name.set(dice_name)

        self._dice_instance = dice.Dice()
        self._last_roll = None

        self.lbl = Label(self, textvariable=self._dice_name)
        self.lbl.grid(row=0, column=0, padx=5, pady=(10, 0), sticky=(W, E))
        self.lbl.configure(anchor="center")

        self.septop = Separator(self, orient='horizontal')
        self.septop.grid(row=1, column=0, sticky=(W, E))

        self.dice_pic = Label(self)
        self.dice_pic.grid(row=2, column=0, padx=5, pady=10,
                           sticky=(N, E, S, W))

        self.dice_pic.bind("<Button-3>", self.do_popup)

        self.sepbottom = Separator(self, orient='horizontal')
        self.sepbottom.grid(row=3, column=0, sticky=(W, E))

        self.lbl_result = Label(self, textvariable=self._result)
        self.lbl_result.grid(row=4, column=0, padx=5, pady=(0, 0),
                             sticky=(W, E))
        self.lbl_result.configure(anchor="center")

        self.roll_button = Button(self, text="Roll",
                                  underline=0, command=self.roll)
        self.roll_button.grid(row=5, column=0, padx=5, pady=(0, 10),
                              sticky=(W, E))

        self.r_click_menu = Menu(self, tearoff=0)
        self.r_click_menu.add_command(label="Roll", command=self.roll)

        self.configure(relief="groove", borderwidth=3)
        return

    def result_as_text(self):
        tmp = ("", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX")
        self._result.set(tmp[self._last_roll])
        return

    def display_picture(self):
        img = PhotoImage(file=self._dice_instance.picture_file_name)
        self.dice_pic.configure(image=img)
        self.dice_pic.image = img
        self.result_as_text()
        return

    def roll(self):
        self._last_roll = self._dice_instance.roll
        self.display_picture()
        return self._last_roll

    def show_dice_name(self):
        self.lbl.grid(row=0, column=0, padx=5, pady=(10, 0), sticky=(W, E))
        self.lbl.configure(anchor="center")
        self.septop.grid(row=1, column=0, sticky=(W, E))
        return

    def hide_dice_name(self):
        self.lbl.grid_forget()
        self.septop.grid_forget()
        return

    def show_result_text(self):
        self.lbl_result.grid(row=4, column=0, padx=5, pady=(0, 0),
                             sticky=(W, E))
        return

    def hide_result_text(self):
        self.lbl_result.grid_forget()
        return

    def show_roll_btn(self):
        self.roll_button.grid(row=5, column=0, padx=5, pady=(0, 10),
                              sticky=(W, E))
        return

    def hide_roll_btn(self):
        self.roll_button.grid_forget()
        return

    def do_popup(self, event):
        try:
            self.r_click_menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.r_click_menu.grab_release()
        return


def main():
    root = Tk()
    df1 = DiceFrame("First Dice")
    df1.grid(row=0, column=0, padx=5, pady=5)
    df2 = DiceFrame()
    df2.grid(row=0, column=1, padx=5, pady=5)
    root.mainloop()
    return


if __name__ == '__main__':
    main()

#-----------------------------------------------------------------------------
# SAMM - Skype Available Mouse Movement
# GUI Version
# v 2020FEB02
#
# This program assists with keeping Skype
# status as 'available' instead of looking
# 'away' after a few minutes of non-use.
# Code is based on PyTutorials YouTube video
# https://youtu.be/2BXr9U6ZL8Y
# Please review this video for more information
# Ctrl+C to end the program
# 
# This program was programmed with Python 3.
# You will need to use pip to install pynput.
#
# (C) 2020 Lorne Cammack, USA
# email lowcam.socailvideo@gmail.com
# Released under GNU Public License (GPL) v3
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#-----------------------------------------------------------------------------



from appJar import gui
import pynput
import time

from pynput.mouse import Button, Controller

#print ("")
#print ("SAMM Copyright (C) 2020 Lorne Cammack")
#print ("This program comes with ABSOLUTELY NO WARRANTY;")
#print ("This is free software, and you are welcome to redistribute it")
#print ("under certain conditions. See https://www.gnu.org/licenses/ for more details.")
#print ("")

app = gui("SAMM", "100x50")
app.setBg("#d5c798")
app.setFg("black")
app.setFont(10)

mouse = Controller()
mouse.position = (100,100)

def press(button):
    if button == "Exit":
        app.stop()
    else:
        i=0
        while i < 1:
            #app.yesNoBox("Stop?","Press Yes To Stop") 
            time.sleep(10)
            mouse.move(0,100)
            mouse.click(Button.left,1)
            time.sleep(10)
            mouse.move(100,0)
            mouse.click(Button.left,1)
            time.sleep(10)
            mouse.move(0,-100)
            mouse.click(Button.left,1)
            time.sleep(10)
            mouse.move(-100,0)
            mouse.click(Button.left,1)
  
app.addButtons(["Start", "Exit"], press)

# start the GUI
app.go()
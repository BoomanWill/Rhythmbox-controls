#!/usr/bin/env python

import tkinter as tk
import os
import subprocess
import yaml

absolute_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(absolute_path, 'config.yml')

with open(config_path) as conf:
    config = yaml.load(conf, Loader=yaml.FullLoader)

os.system('rhythmbox-client --pause')


# window settings
window = tk.Tk()
window.wait_visibility(window)
window.wm_attributes('-alpha', config['Appearance']['transparency'])
window.title(string='Rhythmbox Controls')
window.attributes('-topmost', True)
hs = window.winfo_screenheight()
ws = window.winfo_screenwidth()
h, w = 50, 340
bottomright = dict()
bottomright['coords'] = [ws - w, hs - h]
topright = dict()
topright['coords'] = [ws - w, 0]
bottomleft = dict()
bottomleft['coords'] = [0, hs - h]
topleft = dict()
topleft['coords'] = [0, 0]
corner = {'bottom-right': bottomright, 'top-right': topright,
          'bottom-left': bottomleft, 'top-left': topleft}

geometry = (w, h, corner[config['Appearance']['corner']]['coords']
            [0], corner[config['Appearance']['corner']]['coords'][1])

window.geometry('%dx%d+%d+%d' % geometry)
window.config(bg=config['Appearance']['backgroundcolour'])


playing = subprocess.getoutput('rhythmbox-client --print-playing')

# find images
pauseimage = tk.PhotoImage(file=config['Icons']['pause'])
nextimage = tk.PhotoImage(file=config['Icons']['next'])
previousimage = tk.PhotoImage(file=config['Icons']['previous'])
playimage = tk.PhotoImage(file=config['Icons']['play'])
playpauselist = [pauseimage, playimage]
playpauseindex = 0

# create things
song = tk.Label(window, text=playing, bg=config['Appearance']
                ['backgroundcolour'], fg=config['Appearance']['textcolour'])
playpause = tk.Button(window, image=playimage, width=20, height=20)
next = tk.Button(window, image=nextimage, width=20, height=20)
previous = tk.Button(window, image=previousimage, width=20, height=20)


# define buttons
def playpausepress(event):
    global playpauseindex
    os.system('rhythmbox-client --play-pause')
    if playpauseindex > 1:
        playpauseindex = 0
    playpause.config(image=playpauselist[playpauseindex])
    playpauseindex += 1


def nextpress(event):
    os.system('rhythmbox-client --next')
    playing = subprocess.getoutput('rhythmbox-client --print-playing')
    song.config(text=playing)


def previouspress(event):
    os.system('rhythmbox-client --previous')
    playing = subprocess.getoutput('rhythmbox-client --print-playing')
    song.config(text=playing)


def updatesongname():
    window.after(1000, updatesongname)
    playing = subprocess.getoutput('rhythmbox-client --print-playing')
    song.config(text=playing)


updatesongname()


# bind buttons
playpause.bind('<Button-1>', playpausepress)
next.bind('<Button-1>', nextpress)
previous.bind('<Button-1>', previouspress)


# position everything
next.place(x=190, y=h - 26)
playpause.place(x=160, y=h - 26)
previous.place(x=130, y=h - 26)
song.place(x=0, y=0)


window.mainloop()

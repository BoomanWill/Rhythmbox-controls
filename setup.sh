#!/bin/bash

sudo apt-get install python3-tk
pip install pyyaml

sudo mkdir ~/.rhythmboxcontrols
sudo mv images ~/.rhythmboxcontrols
sudo mv musiccontrols.py ~/.rhythmboxcontrols
sudo mv config.yml ~/.rhythmboxcontrols
sudo mv musiccontrols.desktop /usr/share/applications
sudo mv musiccontrols ~/.rhythmboxcontrols
sudo chmod +x ~/.rhythmboxcontrols/musiccontrols
sudo ln -s ~/.rhythmboxcontrols/musiccontrols /usr/local/bin/musiccontrols

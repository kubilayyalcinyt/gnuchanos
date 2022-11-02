#!/bin/bash
yay -S python-pip 
python -m pip install psutil python-magic pyinstaller  cairocffi cffi xcffib
sudo pacman -S tk

#PyInstaller tutorial1.py --onefile
#!/bin/bash

# Install development tools and GUI
dnf groupinstall 'Development Tools' -y
dnf groupinstall 'Fedora Workstation' -y

# Enable GUI
systemctl set-default graphical.target
systemctl enable sshd.service

dnf install boost-devel qt5-qtbase-devel gcc-c++ qt5-qtx11extras-devel -y

# install required packages for building dwm
#dnf install libX11-devel libXft-devel libXinerama-devel -y

# required packages for using this build
#dnf install dmenu terminus-fonts xsel i3lock wmname -y


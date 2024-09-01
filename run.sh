#!/bin/bash

git clone https://github.com/thatCleverNerd/PYboard ~/.config/pyboard

folder_path="$HOME/.fonts"

if [ -d "$folder_path" ]; then
	echo -e "\n ADDING FONTS... \n"
	cp $HOME/.config/pyboard/assets/fonts/* $folder_path && echo -e "\n [+] FONTS ADDED"
else
	echo -e "\n CREATING .FONTS DIRECTORY AND ADDING FONTS \n"
	mkdir $HOME/.fonts/ && cp $HOME/.config/pyboard/assets/fonts/* $folder_path && echo -e "\n [+] FONTS ADDED"

fi

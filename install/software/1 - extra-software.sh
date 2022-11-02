#!/bin/bash


#bchunk cd1.bin cd1.cue cd1.iso





################################################################################################
echo  "#[multilib]"
echo  "#Include = /etc/pacman.d/mirrorlist"
read -rsn1 -p "dont forget open nano edit and delete this //Press Enter  "

sudo nano /etc/pacman.conf
echo  "install starting..."
sudo pacman -Syyu
################################################################################################




################################################################################################
sudo pacman -S zip unzip p7zip  expac jshon gvfs-mtp mtpfs exfat-utils a52dec faac fuse-exfat faad2 jasper lame libdca libdv gst-libav libmad libtheora libmpeg2 wavpack x264 xvidcore libdvdcss  libdvdread  libdvdnav dvd+rw-tools dvdauthor dvgrab lib32-alsa-lib  lib32-alsa-plugins  lib32-libpulse  lib32-alsa-oss  net-tools  
sudo pacman -S gparted vlc conky leafpad arandr btop jdk-openjdk bchunk
sudo pacman -S archlinux-keyring


sudo pacman -S noto-fonts-cjk noto-fonts-emoji noto-fonts #japonca font
################################################################################################



################################################################################################
#                   terminal        - file manager  -  music player  - Notification  - wallpaper
sudo pacman -S   cool-retro-term        ranger            cmus           dunst         nitrogen
------------------------------------------------------------------------------------------------
#                        pdf UWU             -  image wiewer
sudo pacman -S zathura-pdf-poppler  zathura      ristretto
------------------------------------------------------------------------------------------------
#                       program başlatıcı    -  Themes Changer  -   Screen Shoot
sudo pacman -S picom      rofi dmenu             lxappearance          scrot
################################################################################################

sudo pacman -S irqbalance #don't forger this
systemctl enable --now irqbalance


PS3='Please enter your choice: '
options=("amd" "intel" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "AMD")
        echo "you chose AMD"
            sudo pacman -S amd-ucode
            break
            ;;

        "intel")
        echo "you chose intel"
            sudo pacman -S intel-ucode
            break
            ;;

        "Quit")
            break
            ;;
    esac
done





read -rsn1 -p "install your browser QuteBrowser is default //Press Enter" variable; echo

PS3='Please enter your choice: '
options=("QuteBrowser" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "QuteBrowser")
        echo "you choose QuteBrowser"
        sudo pacman -S qutebrowser
	    sudo pacman -S python-adblock
            break
            ;;

        "Quit")
            break
            ;;
    esac
done



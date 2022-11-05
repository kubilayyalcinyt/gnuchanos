#!/bin/bash
echo "if you see this ## press enter"

sudo localectl --no-convert set-x11-keymap tr

################################################################################################################
read -rsn1 -p "###### LOCAL TIME #################################################" variable; echo
read -rsn1 -p "Select Time Zone  Europe/Istanbul My zone //Press Enter" variable; echo

echo "timedatectl list-timezones"
sleep 2
timedatectl list-timezones

read -rsn1 -p "Dont Forget Time Zone :----> "
read -p 'Enter Time Zone Name : ' timezone

echo "timedatectl set-timezone $timezone"
sleep 2
timedatectl set-timezone $timezone


echo "timedatectl set-local-rtc 1"
sleep 2
timedatectl set-local-rtc 0
echo "timedatectl set-ntp true"
sleep 2
timedatectl set-ntp true 


echo "timedatectl status"
sleep 2
timedatectl status


read -rsnl -p "if you see your time zone NICE! if you not report please"
read -rsn1 -p "Timezone Completed! //Press Enter" variable; echo

echo "locale-gen"
sleep 2
locale-gen




read -rsn1 -p "###################### FINISH : PRESS ENTER #########################" variable; echo
################################################################################################################
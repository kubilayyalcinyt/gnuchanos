#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}




picom --config ~/.config/qtile/picom.conf &
nitrogen --restore &
#sh ~/.config/qtile/display.sh  &

#start the conky to learn the shortcuts
killall conky
(conky -c ~/.config/qtile/system-overview) &

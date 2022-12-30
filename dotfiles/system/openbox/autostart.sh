#!/usr/bin/env sh



function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}




picom --config ~/.config/openbox/picom.conf &
nitrogen --restore &
sh ~/.config/openbox/display.sh  &

#start the conky to learn the shortcuts
killall conky
(conky -c ~/.config/openbox/system-overview) &

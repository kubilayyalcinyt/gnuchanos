tar -vxf GnuChanOS-icons.tar
tar -vxf GnuchanCursors.tar
sudo rm -r  /usr/share/icons/
sudo mkdir /usr/share/icons/
sudo mv GnuChanOS-icons/ /usr/share/icons/
sudo mv GnuchanCursors/ /usr/share/icons/
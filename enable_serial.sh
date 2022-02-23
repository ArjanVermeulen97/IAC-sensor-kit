sudo groupadd dialout
sudo gpasswd -a arjan dialout
sudo usermod -a -G dialout arjan
sudo chmod a+rw /dev/ttyACM0

#!/bin/bash
touch conf.txt
hostname >> conf.txt
echo '------------------------' >> conf.txt
ifconfig wlan0 >> conf.txt;
python BlueTeam.py conf.txt
rm conf.txt
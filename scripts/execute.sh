#!/bin/bash

echo "Running the test bash script........."

username=$(git config user.name)

echo "HELLO $username !!!"

echo "Thank you $username for using this test script."

echo "WARNING: $username, this script will restart your system/server provided root password in config.txt file."

source config.txt

echo "Restarting Server...."

echo "Goodbye $username. Exiting........."

sleep 5

echo $ROOT_PASSWORD | sudo -S sudo reboot now

# to run this script, type;
# source start-server.sh
# for some reason, just using ./start-server.sh seems to skip any 'source' 
# keywords in this script, thus not activating the virtual env (see 
# https://stackoverflow.com/questions/7369145/activating-a-virtualenv-using-a-shell-script-doesnt-seem-to-work)

#!/bin/sh

# get which os
unameOut="$(uname -s)"
echo ${unameOut}

# activate virtual environment ("No-Toil-Part-Tracker")
# delete this part of the script when running on deployed server
echo "activating virtual environment..."
source bin/activate

# # show some info
# echo "current directory:"
# pwd
# echo "directory contents:"
# ls -l
# echo "python version and dependencies:"
# python3 --version
# pip list

# # change to server directory to access App and Site in main dir
# cd PartTrackerBack/

# # get my ip address
# ip4 = $(ipconfig getifaddr en0)
# echo "ip4 $ip4"

# # start django server
# python3 manage.py runserver "$ip4":8000

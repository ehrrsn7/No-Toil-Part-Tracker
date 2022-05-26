# to run this script, type;
# source start-server.sh
# for some reason, just using ./start-server.sh seems to skip any 'source' 
# keywords in this script, thus not activating the virtual env (see 
# https://stackoverflow.com/questions/7369145/activating-a-virtualenv-using-a-shell-script-doesnt-seem-to-work)

#!/bin/sh

# get which os
uname="$(uname -s)"
echo "uname: "${uname}"\n"

# linux / unix(mac):
if [ "$(uname)" == "Darwin" ] || 
[ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
  # display some info about the current directory
  echo "current directory:"; pwd;    echo ""
  echo "directory contents:"; ls -l; echo ""

  # activate virtual environment ("No-Toil-Part-Tracker")
  echo "activating virtual environment...\n"
  source bin/activate

# windows
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ] || 
[ "$(expr substr $(uname -s) 1 10)" == "MINGW64_NT" ]; then
  # display some info about the current directory
  echo "current directory:"; cd;   echo ""
  echo "directory contents:"; dir; echo ""

  # activate virtual environment ("No-Toil-Part-Tracker")
  echo "activating virtual environment...\n"
  bin/activate

fi # end if sequence

# python information
echo "python version and dependencies:"
python3 --version
pip list --format=json # non-verbose..
echo ""

# # change to server directory to access App and Site in main dir
# cd PartTrackerBack/

# get my ip address
ip4=$(ipconfig getifaddr en0)
echo "ip4 $ip4"

# start django server
python3 PartTrackerBack/manage.py runserver $(ipconfig getifaddr en0):8000

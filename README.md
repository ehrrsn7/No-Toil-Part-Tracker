# No Toil Part Tracker

Welcome to the part tracker! This repository works as a django server that can be easily hosted from any computer. 

NOTE: STILL UNDER DEVELOPMENT. 

(The html framework and css are basically developed site-wide. Also, the site is basically designed. However, the site design )

Instructions:

1. Clone this repository to anyplace on your machine. I recommend somewhere like documents or someplace where you won't accidentally delete it routinely. it's not necessary to put this in your applications/program files folder. 
1. Run `start-server.sh`
    - open this folder in your computer's terminal 
      - on mac or linux: let's say you cloned this folder to `~/Documents/`, then open terminal and type `cd ~/Documents/No-Toil-Part-Tracker`
      - on windows: tbd
    - Type `source start-server.sh`
    - This will run a series of commands that (1) starts a new python virtual environment, (2) changes the directory
      - (note: the reason you need to type `source` and not `.` is because for some reason bash ignores the activate python virtual environment. This isn't critical however, so you can skip it, but the environment will default to the global dependencies)
1. You're in! The server should be open at the specified IP that's listed in the terminal window until you close the terminal window and/or machine stops running.

NOTE: `start-server.sh` IS CURRENTLY ONLY CONFIGURED TO RUN ON UNIX/LINUX TERMINALS. THE SCRIPT HAS NOT BEEN WRITTEN FOR COMMAND LINE YET.
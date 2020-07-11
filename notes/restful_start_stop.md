Starting and stoping the service from the website is going to be interesting

use keyed ssh for communication
need the following scripts on server:
  - start
    - check status down
    - tmux window
    - start server
    - wait
    - check status loop
    - error if failed to start
  - stop
    - check status up
    - tmux send server message
    - tmux send stop command
    - wait
    - check status
    - if needed kill
    - check status
    - error
  - status
    - check for process
    - check for tmux window
    - try server command
    - check for server response
minimize back and fourth
track process stat on web server
website rest and frontend only pull stat info from database
poll the minecraft server state in sperate process filtered not direct
  - poll status ever 5 seconds until state matches
avoid running shell commands use these modules
  - https://github.com/Dinnerbone/mcstatus
  - https://github.com/tmux-python/libtmux
  - https://github.com/giampaolo/psutil
ensure multiple start stop commands are safe

use POST for new server

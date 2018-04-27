# cs2951k
empty chair detection

main.py: detecting chairs in the map

chair_display.py: displaying all the chairs after exploring

person_detection.py: detecting person in the mid of the frame, send person counter to nav.py

nav.py: finite state machine that checks if there is person detected, if so navigate to the closest chair



## exploring phase
* 'roslaunch movo_remote_teleop movo_remote_teleop.launch'
* 'roslaunch movo_demos mapping.launch'
* 'roslaunch movo_viz view_robot.launch function:=mapping'
* 'rosrun movo_detect main.py'

## after navigate through the environment

### save map amd move map file to the right folder
* 'rosrun map_server map_saver -f mapname'
### save chair
* 'python ./tools/chair_saver.py' after seeing 'here', quit the program

## navigation phase
close mapping.launch and rviz

* 'roslaunch movo_demos map_nav.launch map_file:=mapname'
* 'roslaunch movo_viz view_robot.launch function:=map_nav'
* 'python ./tools/chair_display.py'
* 'python ./tools/person_detection.py'
* 'python ./tools/nav.py"


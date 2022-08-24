TIAGO README
============

# Start the robot
Press the Red button.
Press the Green button, wait for the robot to twitch.


# Disable head movement
Go to http://tiago.ai.loc:8080/
Press the Stop button next to "head_manager: Running".
It should change into "Stopped Stopped by user request.".

# Disable localization on the robot
Press the Stop button next to "localizer"

# Use Joystick
To move the robot base, press the Start button to enable base movement, then use the little joysticks.
Press the Start button again to deactivate base movement before you start Giskard.


# Upload the kitchen URDF and state publisher
$ roslaunch cram_projection_demos everything.launch tiago:=true apartment:=true upload_robot:=false
# If you're only logging projection NEEMs, say upload_robot:=true

# Start the localization
$ roslaunch iai_tiago_bringup localization.launch

# Start knowrob
$ roslaunch knowrob knowrob.launch

# If knowrob complains about rosprolog or mongo, start mongo
$ sudo systemctl status mongod  # to check the status
$ sudo systemctl start mongod


# Start giskard
$ roslaunch giskardpy giskardpy_tiago.launch

# Start robokudo
$ rosrun robokudo start_rk_query.sh

# Start cram
$ emacs &
> Ctrl-c l
CL-USER> (ros-load:load-system "cram_projection_demos" :cram-projection-demos)
;; If you're only logging projection, don't do the next thing:
CL-USER> (ros-load:load-system "cram_tiago_process_modules" :cram-tiago-process-modules)

# If you need to log, load the cloud logger
CL-USER> (ros-load:load-system "cram_cloud_logger" :cram-cloud-logger)
# set TF broadcasting to true
CL-USER> (setf cram-tf:*tf-broadcasting-enabled* t)

# Start the ros node
CL-USER> (roslisp-utilities:startup-ros)

# if you're logging, start the episode
CL-USER> (ccl::start-episode)

# Start demo
CL-USER> (demos::apartment-demo)

# If you need to log, stop the episode:
CL-USER> (ccl::stop-episode)

# The logs are located in `echo $KNOWROB_MEMORY_DIR`


# Turn off the robot
Move the robot so he has 2 meters around him free space.
Press the Home button on the LCD screen on the robot base.
Press the Green button for a second or two until it starts blinking.
When the robot goes limp, put the robot's hands on the black squishy pads on the base.
Press the Red button.



# When last to leave on the ground floor of TAB, close all windows in apartment, lock the apartment door, double check everyone left and turn on the alarm.

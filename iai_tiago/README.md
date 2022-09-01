TIAGO README
============

# Start the robot
Press the Red button.
Press the Green button, wait for the robot to twitch.


# Disable head movement
Go to http://tiago.ai.loc:8080/
Press the Stop button next to "head_manager: Running".
It should change into "Stopped Stopped by user request.".

# Switch to impedance controller for the arms
Go to http://tiago.ai.loc:8080/
In the left menu, choose "Impedance controller".
There click on "Impedance controller both".

# Use Joystick
To move the robot base, press the Start button to enable base movement, then use the little joysticks.
Press the Start button again to deactivate base movement before you command a Giskard goal.


# Start the incrementer gripper action for the left gripper.
# It's best to run it on tiago directly, but generally it doesn't matter.
  $ rosrun joy_teleop incrementer_server __ns:=gripper_left_controller

# Upload the kitchen URDF and state publisher
  $ roslaunch cram_projection_demos everything.launch tiago:=true apartment:=true upload_robot:=false

# Start giskard
  $ roslaunch giskardpy giskardpy_tiago.launch

# Start robokudo
  $ rosrun robokudo start_rk_query.sh

# Start cram
  $ emacs &
> Ctrl-c l
  CL-USER> (ros-load:load-system "cram_projection_demos" :cram-projection-demos)
  CL-USER> (ros-load:load-system "cram_tiago_process_modules" :cram-tiago-process-modules)
  CL-USER> (roslisp-utilities:startup-ros)
  CL-USER> (demos::apartment-demo)


# Turn off the robot
Move the robot so he has 2 meters around him free space.
Press the Home button on the LCD screen on the robot base.
Press the Green button for a second or two until it starts blinking.
When the robot goes limp, put the robot's hands on the black squishy pads on the base.
Press the Red button.




Logging on real robot
=====================

Start everything as explained above.

In addition, do the following:

# Start knowrob:
  $ roslaunch knowrob knowrob.launch

# If knowrob complains about rosprolog or mongo, start mongo.
# If knowrob doesn't complain, mongo is already started.
  $ sudo systemctl status mongod  # to check the status
  $ sudo systemctl start mongod

# In CRAM, do the following:
  CL-USER> (ros-load:load-system "cram_cloud_logger" :cram-cloud-logger)
  CL-USER> (setf cram-tf:*tf-broadcasting-enabled* nil)
  CL-USER> (roslisp-utilities:startup-ros)
  CL-USER> (ccl::start-episode)
  CL-USER> (demos::apartment-demo)
  CL-USER> (ccl::stop-episode)

# The logs are located in `echo $KNOWROB_MEMORY_DIR`




Logging in Projection
=====================

# Make sure the real robot is not running. If it is, you'll have to export ROS_MASTER_URI to localhost or so.

# Upload the kitchen URDF and state publisher, and robot URDF
  $ roslaunch cram_projection_demos everything.launch tiago:=true apartment:=true upload_robot:=true

# Start knowrob:
  $ roslaunch knowrob knowrob.launch

# If knowrob complains about rosprolog or mongo, start mongo.
# If knowrob doesn't complain, mongo is already started.
  $ sudo systemctl status mongod  # to check the status
  $ sudo systemctl start mongod

# Start cram
  $ emacs &
Press Ctrl-c l
  CL-USER> (ros-load:load-system "cram_projection_demos" :cram-projection-demos)
  CL-USER> (ros-load:load-system "cram_cloud_logger" :cram-cloud-logger)
  CL-USER> (setf cram-tf:*tf-broadcasting-enabled* t)
  CL-USER> (roslisp-utilities:startup-ros)
  CL-USER> (ccl::start-episode)
  CL-USER> (demos::apartment-demo)
  CL-USER> (ccl::stop-episode)

# The logs are located in `echo $KNOWROB_MEMORY_DIR`









# When last to leave on the ground floor of TAB, close all windows in apartment, lock the apartment door, double check everyone left and turn on the alarm.

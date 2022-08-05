
# Start the robot
Press the Red button, wait for ??
Press the Green button, wait for the robot to twitch.


# Disable head movement
Go to http://tiago.ai.loc:8080/
Press the Stop button next to "head_manager: Running".
It should change into "Stopped Stopped by user request.".


# Use Joystick
To move the robot base, press the Start button to enable base movement, then use the little joysticks.
Press the Start button again to deactivate base movement before you start Giskard.


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



# Turn off the robot
Move the robot so he has 2 meters around him free space.
Press the Home button on the LCD screen on the robot base.
Press the Green button for a second or two until it starts blinking.
When the robot goes limp, put the robot's hands on the black squishy pads on the base.
Press the Red button.

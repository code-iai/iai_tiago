#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy
import numpy as np

from giskardpy.python_interface import GiskardWrapper

#usage: press a,b,x,y, start or cross to cancel giskard goals

class MUH:
    cancel_msg = 'Canceling all Giskard goals.'

    def __init__(self):
        self.joystick_active = False
        self.cmd_vel_called = False
        self.giskard = GiskardWrapper()
        self.joy_sub = rospy.Subscriber('/joy', Joy, self.joy_cb)
        self.cmd_vel_sub = rospy.Subscriber('/mobile_base_controller/cmd_vel', Twist, self.cmd_vel_cb)
        self.timer = rospy.Timer(rospy.Duration(1), self.timer_cb)

    def timer_cb(self, msg):
        if self.cmd_vel_called:
            self.cmd_vel_called = False
        elif self.joystick_active:
            rospy.loginfo('joy stick deactivated')
            self.joystick_active = False

    def cmd_vel_cb(self, msg):
        if not self.joystick_active:
            rospy.logwarn('joystick got activated')
            rospy.logwarn(self.cancel_msg)
            self.giskard.cancel_all_goals()
        self.joystick_active = True
        self.cmd_vel_called = True

    def joy_cb(self, joy_msg: Joy):
        buttons = np.array(joy_msg.buttons)
        axis = np.array(joy_msg.axes)
        if np.any(buttons[:4] != 0) or np.any(axis[-2:] != 0):
            rospy.logwarn(self.cancel_msg)
            self.giskard.cancel_all_goals()


rospy.init_node('giskard_e_stop')
muh = MUH()
rospy.spin()

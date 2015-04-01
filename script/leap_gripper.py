#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rospkg
import tf
import math
import actionlib
from control_msgs.msg import GripperCommandAction, GripperCommandGoal

class LeapGripper:
    def __init__(self):
        self.listener = tf.TransformListener()
        self.ac = actionlib.SimpleActionClient('/gripper_controller/gripper_cmd', GripperCommandAction)
        rospy.loginfo('Waiting for gripper command action...')
        self.ac.wait_for_server()
        rospy.loginfo('Found gripper action!')

    def update(self):
        try:
            (pos, rot) = self.listener.lookupTransform('/right_hand_thumb_tip', '/right_hand_pinky_tip', rospy.Time(0))

            dist = math.sqrt(pos[0]**2+pos[1]**2+pos[2]**2)
            goal = GripperCommandGoal()
            goal.command.position = 5*(dist - 0.03);
            self.ac.send_goal(goal)
            rospy.loginfo("dist: %s", dist)
        except (tf.Exception):
            pass

if __name__ == '__main__':
    rospy.init_node('leap_gripper')
    leap_gripper = LeapGripper()
    rate = rospy.Rate(50.0)
    while not rospy.is_shutdown():
        try:
            leap_gripper.update()
        except rospy.ROSInterruptException:
            pass
        rate.sleep()

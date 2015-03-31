#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import rospkg
import tf
import math

class LeapGripper:
    def __init__(self):
        self.listener = tf.TransformListener()
    def update(self):
        try:
            (r_pos, r_rot) = self.listener.lookupTransform('/right_hand_thumb_tip', '/right_hand_pinky_tip', rospy.Time(0))
            (l_pos, l_rot) = self.listener.lookupTransform('/left_hand_thumb_tip', '/left_hand_pinky_tip', rospy.Time(0))
            r_dist = math.sqrt(r_pos[0]**2+r_pos[1]**2+r_pos[2]**2)
            l_dist = math.sqrt(l_pos[0]**2+l_pos[1]**2+l_pos[2]**2)
            rospy.loginfo("r_dist: %s", r_dist)
            rospy.loginfo("l_dist: %s", l_dist)

        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            pass

if __name__ == '__main__':
    rospy.init_node('leap_gripper')
    leap_gripper = LeapGripper()
    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            leap_gripper.update()
        except rospy.ROSInterruptException:
            pass
        rate.sleep()

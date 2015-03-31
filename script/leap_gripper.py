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
            (pos,rot) = self.listener.lookupTransform('/left_hand_thumb_tip', '/left_hand_pinky_tip', rospy.Time(0))
            dist = math.sqrt(pos[0]**2+pos[1]**2+pos[2]**2)
            rospy.loginfo("dist: %s", dist)
            

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

#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from pnf_agv.msg import redhead
class PID:
    def __init__(self):
        self.msg = Twist()
        self.x = 0
        print("PID START")
        self.pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        rospy.init_node('move_test', anonymous=True)
        self.sub = rospy.Subscriber("/agv_redhead", redhead, self.callback)
        self.r = rospy.Rate(100) #10hzk
        flag = 0
        kp = 0.45
        self.pid()
    def callback(self, data):
        self.x = data.redhead_data.x_offset




    def pid(self):
        while True:
            if self.x > 1:
                self.msg.linear.y = -self.x * self.kp
                self.msg.angular.x = 0
                self.pub.publish(self.msg)
            elif self.x < -1:
                self.msg.linear.y = -self.x * self.kp
                self.msg.angular.x = 0
                self.pub.publish(self.msg)
            else:
                self.msg.linear.y = 0
                self.msg.angular.x = 0
                self.pub.publish(self.msg)
                break



   
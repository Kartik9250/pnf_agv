#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from pnf_agv.msg import redhead
from matrix_fix import PID
msg = Twist()
x = 0
kp = 0.65
tag = False
def callback(data):
    global x, tag
    x = int(data.redhead_data.x_offset)
    tag = data.redhead_data.tag


pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
rospy.init_node('move_test', anonymous=True)
sub = rospy.Subscriber("/agv_redhead", redhead, callback)
r = rospy.Rate(100) #10hzk
def pid():
    while True:
        if x > 3:
            msg.linear.y = x * kp
            msg.angular.x = 0
            pub.publish(msg)
        elif x < -3:
            msg.linear.y = -x * kp
            msg.angular.x = 0
            pub.publish(msg)
        else:
            msg.linear.y = 0
            msg.angular.x = 0
            pub.publish(msg)
            break

flag = 0
while True:
    print(flag)
    if tag == False:
        msg.linear.x = 5
        pub.publish(msg)
    if flag == 0 and x != 0:
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(1.5)
        flag += 1
    if flag == 1 and x != 0:
        # msg.linear.x = 0
        # pub.publish(msg)
        # rospy.sleep(2)
        pid()
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(2)
        flag += 1
    if flag == 2 and x != 0:
        msg.linear.x = 0
        pub.publish(msg)
        rospy.sleep(2)
        pid()
        msg.angular.z = -24
        pub.publish(msg)
        rospy.sleep(2.2)
        msg.angular.z = 0
        msg.linear.x = 5
        pub.publish(msg)
        flag += 1            


#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from pnf_agv.msg import redhead
from matrix_fix import PID
msg = Twist()
x = 0
kp = 0.45
tag = False
def callback(data):
    global x, tag, y
    x = data.redhead_data.x_offset
    y = data.redhead_data.y_offset
    tag = data.redhead_data.tag


pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
rospy.init_node('move_test', anonymous=True)
sub = rospy.Subscriber("/agv_redhead", redhead, callback)
r = rospy.Rate(100) #10hzk
def pid_x():
    while True:
        msg.linear.y = 0
        msg.angular.x = 0
        pub.publish(msg)
        if x > 1:
            msg.linear.y = x * kp
            msg.angular.x = 0
            pub.publish(msg)
        elif x < -1:
            msg.linear.y = x * kp
            msg.angular.x = 0
            pub.publish(msg)
        else:
            msg.linear.y = 0
            msg.angular.x = 0
            pub.publish(msg)
            break
def pid_x2():
    while True:
        msg.linear.y = 0
        msg.angular.x = 0
        pub.publish(msg)
        if x > 1:
            msg.linear.y = -x * kp
            msg.angular.x = 0
            pub.publish(msg)
        elif x < -1:
            msg.linear.y = -x * kp
            msg.angular.x = 0
            pub.publish(msg)
        else:
            msg.linear.y = 0
            msg.angular.x = 0
            pub.publish(msg)
            break
def pid_y():
    while True:
        msg.linear.y = 0
        msg.angular.x = 0
        pub.publish(msg)
        if y > 1:
            msg.linear.y = -x * kp
            msg.angular.x = 0
            pub.publish(msg)
        elif y < -1:
            msg.linear.y = x * kp
            msg.angular.x = 0
            pub.publish(msg)
        else:
            msg.linear.y = 0
            msg.angular.x = 0
            pub.publish(msg)
            break

flag = 0
while not rospy.is_shutdown():
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
        pid_x()
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(2)
        flag += 1
    if flag == 2 and x != 0:
        msg.linear.x = 0
        pub.publish(msg)
        rospy.sleep(2)
        msg.angular.z = 24
        pub.publish(msg)
        rospy.sleep(2.35)
        msg.angular.z = 0
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(1)
        flag += 1
    if flag == 3 and x != 0:
        # msg.linear.x = 0
        # pub.publish(msg)
        # rospy.sleep(2)
        pid_y()
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(2)
        flag += 1
    if flag == 4 and x != 0:
        msg.linear.x = 0
        pub.publish(msg)
        rospy.sleep(2)
        msg.angular.z = 24
        pub.publish(msg)
        rospy.sleep(2.35)
        msg.angular.z = 0
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(1)
        flag += 1
    if flag == 5 and x != 0:
        # msg.linear.x = 0
        # pub.publish(msg)
        # rospy.sleep(2)
        pid_x2()
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(2)
        flag += 1
    if flag == 6 and x > 0:
        msg.linear.x = 0
        pub.publish(msg)
        rospy.sleep(2)
        msg.angular.z = 24
        pub.publish(msg)
        rospy.sleep(2.35)
        msg.angular.z = 0
        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(1)
        flag += 1
    if flag == 7 and x > 0:
        msg.linear.x = 0
        pub.publish(msg)
        rospy.sleep(2)
        msg.angular.z = 24
        pub.publish(msg)
        rospy.sleep(2.35)
        msg.angular.z = 0
        pub.publish(msg)
        pid_y()

        msg.linear.x = 5
        pub.publish(msg)
        rospy.sleep(1)
        flag += 1
    if flag == 8 and x != 0:
        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0
        pub.publish(msg)
        flag += 1


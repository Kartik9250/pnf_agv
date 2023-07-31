#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from pnf_agv.msg import redhead
msg = Twist()
x = 0
kp = 0.65
tag = False
def callback(data):
    global x, tag, y
    x = int(data.redhead_data.x_offset)
    y = int(data.redhead_data.y_offset)
    tag = data.redhead_data.tag


pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
rospy.init_node('move_test', anonymous=True)
sub = rospy.Subscriber("/agv_redhead", redhead, callback)
r = rospy.Rate(100) #10hzk

def pid_x():
    while True:
        if x > 3:
            msg.linear.x = x * kp
            msg.angular.y = 0
            pub.publish(msg)
        elif x < -3:
            msg.linear.x = -x * kp
            msg.angular.x = 0
            pub.publish(msg)
        else:
            msg.linear.x = 0
            msg.angular.y = 0
            pub.publish(msg)
            break

def pid_y():
    while True:
        if y > 3:
            msg.linear.y = x * kp
            msg.angular.x = 0
            pub.publish(msg)
        elif y < -3:
            msg.linear.y = -x * kp
            msg.angular.x = 0
            pub.publish(msg)
        else:
            msg.linear.y = 0
            msg.angular.x = 0
            pub.publish(msg)
            break    

def tag_detect_x(dir):
    if dir == pov:
        msg.linear.x = 0
        msg.linear.y = 0
        pub.publish(msg)
        while tag == True:
            pid_y()  
            msg.linear.x = 4.5
    if dir == neg:
        msg.linear.x = 0
        msg.linear.y = 0
        pub.publish(msg)
        while tag == True:
            pid_y()  
            msg.linear.x = -4.5

def tag_detect_y(dir):
    if dir == str(pov):
        msg.linear.x = 0
        msg.linear.y = 0
        pub.publish(msg)
        while tag == True:
            pid_x()  
            msg.linear.y = 4.5
    if dir == str(neg):
        msg.linear.x = 0
        msg.linear.y = 0
        pub.publish(msg)
        while tag == True:
            pid_x()  
            msg.linear.y = -4.5

        


flag = 0
while not rospy.is_shutdown():
    print(flag)
    
    if tag == False:
        msg.linear.x = 5
        pub.publish(msg)
    if tag == True and flag == 0:
        tag_detect_x(dir=str(pov))
        flag += 1
    elif tag == True and flag == 1:
        tag_detect_y(dir=str(pov))
        flag += 1
    elif tag == True and flag == 2:
        tag_detect_x(dir=str(neg))
    elif tag == True and flag == 3:
        tag_detect_y(dir=str(neg))
    
             


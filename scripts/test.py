#!/usr/bin/env python3
import rospy
from aruco_navigation.msg import Holo_agv, Motor_desc
from geometry_msgs.msg import Twist
vel_x = 0
vel_y = 0
def cmd_cb(data):
    global vel_x, vel_y
    vel_x = data.linear.x * 200
    
def talker():
    pub = rospy.Publisher('pnf_agv', Holo_agv)
    sub = rospy.Subscriber("/cmd_vel", Twist, cmd_cb)
    rospy.init_node('pgv_controller', anonymous=True)
    r = rospy.Rate(100) #10hz
    msg = Holo_agv()
    

    while not rospy.is_shutdown():
        if vel_x < 0:
          msg.motor_A.dor = 1
        else:
            msg.motor_A.dor = 0  
        msg.motor_A.pwm = int(vel_x)
        
        # msg.motor_B.pwm = 150
        # msg.motor_B.dor = 0
        # msg.motor_C.pwm = 200
        # msg.motor_C.dor = 1
        # msg.motor_D.pwm = 11
        # msg.motor_D.dor = 1
        pub.publish(msg)
        print("message published")
        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass
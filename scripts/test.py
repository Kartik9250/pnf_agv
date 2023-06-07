#!/usr/bin/env python3
import rospy
from pnf_agv.msg import Holo_agv
from geometry_msgs.msg import Twist

WHEEL_SEPARATION_WIDTH = 0.297
WHEEL_SEPARATION_LENGTH = 0.283
WHEEL_GEOMETRY = (WHEEL_SEPARATION_WIDTH + WHEEL_SEPARATION_LENGTH) / 2
WHEEL_RADIUS = 0.08

class controller:
    def __init__(self):
        self.front_left = 0
        self.front_right = 0
        self.back_left = 0
        self.back_right = 0

        self.abs_front_left = 0
        self.abs_front_right = 0
        self.abs_back_left = 0
        self.abs_back_right = 0

    def cmd_cb(self,data):
        x = data.linear.x
        y = data.linear.y
        rot = data.angular.z

        self.front_left = int((x - y - rot * WHEEL_GEOMETRY) / WHEEL_RADIUS)
        self.front_right = int((x + y + rot * WHEEL_GEOMETRY) / WHEEL_RADIUS)
        self.back_left = int((x + y - rot * WHEEL_GEOMETRY) / WHEEL_RADIUS)
        self.back_right = int((x - y + rot * WHEEL_GEOMETRY) / WHEEL_RADIUS)

        
        
        self.abs_front_right = max(min(abs(self.front_right), 255), 0)
        self.abs_front_left = max(min(abs(self.front_left), 255), 0)
        self.abs_back_right = max(min(abs(self.back_right), 255), 0)
        self.abs_back_left = max(min(abs(self.back_left), 255), 0)

        
    def main(self):
        pub = rospy.Publisher('agv_controller', Holo_agv)
        sub = rospy.Subscriber("/cmd_vel", Twist, self.cmd_cb)
        rospy.init_node('pgv_controller', anonymous=True)
        r = rospy.Rate(100) #10hz
        msg = Holo_agv()
        

        while not rospy.is_shutdown():
            
            if self.abs_front_left and self.abs_front_right == 0:
                msg.motor_driver_front.stby = 0
            else:
                msg.motor_driver_front.stby = 1


            if self.front_right > 0:
                msg.motor_driver_front.motor_right.IN1 = 1
                msg.motor_driver_front.motor_right.IN2 = 0
            else:
                msg.motor_driver_front.motor_right.IN1 = 0
                msg.motor_driver_front.motor_right.IN2 = 1
            msg.motor_driver_front.motor_right.pwm = self.abs_front_right

            if self.front_left > 0:
                msg.motor_driver_front.motor_left.IN1 = 1
                msg.motor_driver_front.motor_left.IN2 = 0
            else:
                msg.motor_driver_front.motor_left.IN1 = 0
                msg.motor_driver_front.motor_left.IN2 = 1
            msg.motor_driver_front.motor_left.pwm = self.abs_front_left



            if self.abs_back_left and self.abs_back_right == 0:
                msg.motor_driver_back.stby = 0
            else:
                msg.motor_driver_back.stby = 1

            if self.back_right > 0:
                msg.motor_driver_back.motor_right.IN1 = 1
                msg.motor_driver_back.motor_right.IN2 = 0
            else:
                msg.motor_driver_back.motor_right.IN1 = 0
                msg.motor_driver_back.motor_right.IN2 = 1
            msg.motor_driver_back.motor_right.pwm = self.abs_back_right

            if self.back_left > 0:
                msg.motor_driver_back.motor_left.IN1 = 1
                msg.motor_driver_back.motor_left.IN2 = 0
            else:
                msg.motor_driver_back.motor_left.IN1 = 0
                msg.motor_driver_back.motor_left.IN2 = 1
            msg.motor_driver_back.motor_left.pwm = self.abs_back_left


            pub.publish(msg)
            print("message published")
            r.sleep()

if __name__ == '__main__':
    obj = controller()
    try:
        obj.main()
    except rospy.ROSInterruptException: pass
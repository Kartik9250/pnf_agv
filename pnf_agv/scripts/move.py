#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
        
def main():
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
    rospy.init_node('move_test', anonymous=True)
    r = rospy.Rate(100) #10hzk
    
    count = 0
    msg = Twist()

    while not rospy.is_shutdown():
        if count == 0:
            rospy.loginfo("starting...")
            msg.linear.x = 0
            msg.linear.y = 0
            pub.publish(msg)
            rospy.sleep(0.5)

        if count == 1:
            rospy.loginfo("moving forward")
            msg.linear.x = 8
            msg.linear.y = 0
            pub.publish(msg)
            rospy.sleep(3.5)
            
        elif count == 2:
            rospy.loginfo("moving left")
            msg.linear.x = 0
            msg.linear.y = -7
            pub.publish(msg)
            rospy.sleep(4)

        elif count == 3:
            rospy.loginfo("moving backwards")
            msg.linear.x = -8
            msg.linear.y = 0
            pub.publish(msg)
            rospy.sleep(3.5)

        elif count == 4:
            rospy.loginfo("moving right")
            msg.linear.x = 0
            msg.linear.y = 7
            pub.publish(msg)
            rospy.sleep(4)


        elif count == 5:
            rospy.loginfo("moving forward-left")
            msg.linear.x = 5.5
            msg.linear.y = -5.5
            pub.publish(msg)
            rospy.sleep(3.5)
        
        elif count == 6:
            rospy.loginfo("moving backward-right")
            msg.linear.x = -5.5
            msg.linear.y = 5.5
            pub.publish(msg)
            rospy.sleep(3.5)
        

        msg.linear.x = 0
        msg.linear.y = 0
        msg.angular.z = 0
        pub.publish(msg)

        count += 1

        r.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException: pass
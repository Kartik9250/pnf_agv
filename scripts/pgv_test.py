#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from pnf_agv.msg import redhead
msg = Twist()
x = 0
def callback(data):
    global x
    # global y
    x = int(data.redhead_data.x_offset)




    # elif x < 0:
    #     rospy.loginfo("moving forward")
    #     msg.linear.x = -8
    #     msg.linear.y = 0
    #     pub.publish(msg)

pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
rospy.init_node('move_test', anonymous=True)
sub = rospy.Subscriber("/agv_redhead", redhead, callback)
r = rospy.Rate(100) #10hzk

flag = 0

while True:
    if flag == 0:
        msg.linear.x = 7
        pub.publish(msg)
    if x != 0:
        flag += 1
        msg.linear.y = 0
        msg.linear.x = 0
        pub.publish(msg)
        rospy.sleep(2)
    if flag == 1:
        msg.linear.y = -6
        msg.linear.x = 0
        pub.publish(msg)
        rospy.sleep(1.5)
    elif flag == 2:
        msg.linear.x = -5
        msg.linear.y = 1
        pub.publish(msg)
        rospy.sleep(1.5)
    elif flag == 3:
        msg.linear.x = -2
        msg.linear.y = 6
        pub.publish(msg)
        rospy.sleep(1.5)
    elif flag == 4:
        msg.linear.y = 0
        msg.linear.x = 0
        pub.publish(msg)




    # y = data.redhead_data.y_offset

# def main():
    
    
    # count = 0

    # while not rospy.is_shutdown():
        # global x
        # global y

            # rospy.sleep(0.5)

        
            # rospy.sleep(3.5)
            
        # elif y < 0:
        #     rospy.loginfo("moving left")
        #     msg.linear.x = 0
        #     msg.linear.y = -7
        #     pub.publish(msg)
            # rospy.sleep(4)

        # elif y > 0:
        #     rospy.loginfo("moving backwards")
        #     msg.linear.x = -8
        #     msg.linear.y = 0
        #     pub.publish(msg)
            # rospy.sleep(3.5)


        
        
        # count += 1

        # r.sleep()

# if __name__ == '__main__':
#     try:
#         main()
#     except rospy.ROSInterruptException: pass
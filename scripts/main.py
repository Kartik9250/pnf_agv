#!/usr/bin/env python3

from bitmanipulation import BitManipulation
from client import Client
from pnf_agv.msg import redhead
import rospy


cl = Client()
dm = BitManipulation()

def main():
    pub = rospy.Publisher('agv_redhead', redhead)
    rospy.init_node('pgv_redhead', anonymous=True)
    r = rospy.Rate(100)
    msg = redhead()

    while True:
        red_output = cl.output()
        print(red_output)
        try:
            msg.redhead_data.tag = dm.tag_data(str(red_output)[2:4])
            msg.redhead_data.x_offset = float(dm.x_pos(str(red_output)[4:12]))
            msg.redhead_data.y_offset = float(dm.y_pos(str(red_output)[12:16]))
            msg.redhead_data.theta_offset = float(dm.angle_degree(str(red_output)[16:20]))
            pub.publish(msg)
        except:
            pass



main()




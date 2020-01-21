#!/usr/bin/env python

import rospy
from visualization_msgs.msg import Marker
import tf

HUMAN_HEAD_FRAME = "human_0"



def publish_head_marker():
    rospy.init_node('head_marker_pub', anonymous=True)

    pub = rospy.Publisher('head_marker_pub', Marker, queue_size=10)
    tl = tf.TransformListener()

    rate = rospy.Rate(1) # 10hz
    head_marker = Marker()
    head_marker.header.frame_id = HUMAN_HEAD_FRAME

    head_marker.ns = "human"
    head_marker.action = Marker.MODIFY
    head_marker.type = Marker.MESH_RESOURCE
    head_marker.mesh_resource = "package://head_marker_publisher/res/head.dae"
    head_marker.id = 0
    head_marker.scale.x = 0.2
    head_marker.scale.y = 0.2
    head_marker.scale.z = 0.2
    head_marker.color.a = 1.0
    head_marker.color.r = 1.0
    head_marker.color.g = 1.0
    head_marker.color.b = 1.0
    head_marker.pose.orientation.x = 0.5
    head_marker.pose.orientation.y = -0.5
    head_marker.pose.orientation.z = 0.5
    head_marker.pose.orientation.w = 0.5

    while not rospy.is_shutdown():
        try:
            time = rospy.Time.now() - tl.getLatestCommonTime("map", HUMAN_HEAD_FRAME)
            if time >= rospy.Duration(3):
                head_marker.action = Marker.DELETE
                head_marker.header.frame_id = "map"
            head_marker.header.stamp = rospy.Time.now()
            pub.publish(head_marker)
        except Exception as e:
            print(e)
            pass
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_head_marker()
    except rospy.ROSInterruptException:
        pass

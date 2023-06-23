import rospy
from arm_rviz.rviz_animation_controller import RvizAnimationController
from visualization_msgs.msg import Marker


def simple_usage():
    rospy.init_node("test_animation_controller")

    r = RvizAnimationController(n_time_steps=10, ns='trajs')
    while not r.done:
        t = r.t()
        print(t)
        r.step()


def main():
    rospy.init_node("test_animation_controller")

    marker_pub = rospy.Publisher("visualization_marker", Marker, queue_size=10)
    trajs_viz = RvizAnimationController(n_time_steps=10, ns='trajs')
    time_viz = RvizAnimationController(n_time_steps=100, ns='time')
       
    while not trajs_viz.done:
        traj_idx = trajs_viz.t()
        time_viz.reset()
        while not time_viz.done:
            t = time_viz.t()

            print(traj_idx, t)
            msg = Marker()
            msg.action = Marker.ADD
            msg.type = Marker.SPHERE
            msg.header.frame_id = 'world'
            msg.pose.orientation.w = 1
            msg.color.r = 1
            msg.color.a = 1
            msg.scale.x = 0.05
            msg.scale.y = 0.05
            msg.scale.z = 0.05
            msg.pose.position.x = t * 0.01
            msg.pose.position.y = traj_idx * 0.1
            msg.pose.position.z = 0
            marker_pub.publish(msg)

            time_viz.step()
        trajs_viz.step()


if __name__ == '__main__':
    main()

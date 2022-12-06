cmake_minimum_required(VERSION 2.8.3)
project(arm_rviz_msgs)

find_package(catkin REQUIRED
  message_generation
  geometry_msgs
  std_msgs)

add_message_files(
  FILES
  AnimationControl.msg
  AnimControllerState.msg
  VoxelgridStamped.msg
  SparseVoxel.msg
  SparseVoxelgridStamped.msg
)

add_service_files(
        FILES
        GetAnimControllerState.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
  geometry_msgs
)

catkin_package(
  CATKIN_DEPENDS
    message_runtime
)
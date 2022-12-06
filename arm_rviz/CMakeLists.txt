cmake_minimum_required(VERSION 3.0.2)
project(arm_rviz)

find_package(Qt5 COMPONENTS Core Widgets REQUIRED)
find_package(catkin REQUIRED COMPONENTS
  arm_rviz_msgs
  rospy
  rviz
)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

catkin_python_setup()

catkin_package()

set(rviz_animation_controller_src
        src/rviz_animation_controller.cpp
        include/arm_rviz/rviz_animation_controller.h)
add_library(rviz_animation_controller ${rviz_animation_controller_src})
target_include_directories(rviz_animation_controller PUBLIC include ${catkin_INCLUDE_DIRS})
target_link_libraries(rviz_animation_controller PUBLIC Qt5::Core Qt5::Widgets ${catkin_LIBRARIES} uuid)
add_dependencies(rviz_animation_controller ${catkin_EXPORTED_TARGETS})


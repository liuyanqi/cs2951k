# Install script for directory: /home/andrewandjasmine/movo_ws/src/movo_common/movo_ros

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/andrewandjasmine/movo_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  include("/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/movo_ros" TYPE FILE FILES "/home/andrewandjasmine/movo_ws/devel/include/movo_ros/movoConfig.h")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/movo_ros" TYPE FILE FILES "/home/andrewandjasmine/movo_ws/devel/lib/python2.7/dist-packages/movo_ros/__init__.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/andrewandjasmine/movo_ws/devel/lib/python2.7/dist-packages/movo_ros/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages/movo_ros" TYPE DIRECTORY FILES "/home/andrewandjasmine/movo_ws/devel/lib/python2.7/dist-packages/movo_ros/cfg")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_marker_ctrl")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_voice")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_pan_tilt")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_teleop_full_system")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_config_eth")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_arm_ctl")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_head_ctl")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_move_base")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_wd")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_odom_test")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_faultlog_parser")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/robotiq_85_driver")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_driver")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_torso_ctl")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_ros" TYPE PROGRAM FILES "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/installspace/movo_teleop")
endif()


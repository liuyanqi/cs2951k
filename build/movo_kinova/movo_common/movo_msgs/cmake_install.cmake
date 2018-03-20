# Install script for directory: /home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/movo_msgs/msg" TYPE FILE FILES
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/ConfigCmd.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/Battery.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/Status.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/Propulsion.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/Dynamics.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/Configuration.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/CtlParams.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/Faultlog.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/JacoJointCmd.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/JacoStatus.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/GripperCmd.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/GripperStat.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/LinearActuatorCmd.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/JacoCartesianVelocityCmd.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/MotionTestCmd.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/KinovaActuatorFdbk.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/PanTiltActuatorFdbk.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/PVA.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/PanTiltCmd.msg"
    "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/msg/PanTiltFdbk.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/movo_msgs/cmake" TYPE FILE FILES "/home/andrewandjasmine/movo_ws/build/movo_kinova/movo_common/movo_msgs/catkin_generated/installspace/movo_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/andrewandjasmine/movo_ws/devel/include/movo_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/andrewandjasmine/movo_ws/devel/share/roseus/ros/movo_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/andrewandjasmine/movo_ws/devel/share/common-lisp/ros/movo_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/andrewandjasmine/movo_ws/devel/lib/python2.7/dist-packages/movo_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/andrewandjasmine/movo_ws/devel/lib/python2.7/dist-packages/movo_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/andrewandjasmine/movo_ws/build/movo_kinova/movo_common/movo_msgs/catkin_generated/installspace/movo_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/movo_msgs/cmake" TYPE FILE FILES "/home/andrewandjasmine/movo_ws/build/movo_kinova/movo_common/movo_msgs/catkin_generated/installspace/movo_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/movo_msgs/cmake" TYPE FILE FILES
    "/home/andrewandjasmine/movo_ws/build/movo_kinova/movo_common/movo_msgs/catkin_generated/installspace/movo_msgsConfig.cmake"
    "/home/andrewandjasmine/movo_ws/build/movo_kinova/movo_common/movo_msgs/catkin_generated/installspace/movo_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/movo_msgs" TYPE FILE FILES "/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_common/movo_msgs/package.xml")
endif()


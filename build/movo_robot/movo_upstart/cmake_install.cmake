# Install script for directory: /home/andrewandjasmine/movo_ws/src/movo_robot/movo_upstart

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/andrewandjasmine/movo_ws/build/movo_robot/movo_upstart/catkin_generated/installspace/movo_upstart.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/movo_upstart/cmake" TYPE FILE FILES
    "/home/andrewandjasmine/movo_ws/build/movo_robot/movo_upstart/catkin_generated/installspace/movo_upstartConfig.cmake"
    "/home/andrewandjasmine/movo_ws/build/movo_robot/movo_upstart/catkin_generated/installspace/movo_upstartConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/movo_upstart" TYPE FILE FILES "/home/andrewandjasmine/movo_ws/src/movo_robot/movo_upstart/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  include("/home/andrewandjasmine/movo_ws/build/movo_robot/movo_upstart/catkin_generated/safe_execute_install.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/movo_upstart" TYPE PROGRAM FILES
    "/home/andrewandjasmine/movo_ws/src/movo_robot/movo_upstart/scripts/getifip"
    "/home/andrewandjasmine/movo_ws/src/movo_robot/movo_upstart/scripts/mutate_files"
    "/home/andrewandjasmine/movo_ws/src/movo_robot/movo_upstart/scripts/mkxacro"
    "/home/andrewandjasmine/movo_ws/src/movo_robot/movo_upstart/scripts/mklaunch"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/movo_upstart" TYPE DIRECTORY FILES "/home/andrewandjasmine/movo_ws/src/movo_robot/movo_upstart/templates")
endif()


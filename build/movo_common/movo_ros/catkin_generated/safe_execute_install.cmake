execute_process(COMMAND "/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/andrewandjasmine/movo_ws/build/movo_common/movo_ros/catkin_generated/python_distutils_install.sh) returned error code ")
endif()

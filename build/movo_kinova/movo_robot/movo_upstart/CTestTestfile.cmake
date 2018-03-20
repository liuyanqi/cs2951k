# CMake generated Testfile for 
# Source directory: /home/andrewandjasmine/movo_ws/src/movo_kinova/movo_robot/movo_upstart
# Build directory: /home/andrewandjasmine/movo_ws/build/movo_kinova/movo_robot/movo_upstart
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_movo_upstart_roslint_package "/home/andrewandjasmine/movo_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/indigo/share/catkin/cmake/test/run_tests.py" "/home/andrewandjasmine/movo_ws/build/test_results/movo_upstart/roslint-movo_upstart.xml" "--working-dir" "/home/andrewandjasmine/movo_ws/build/movo_kinova/movo_robot/movo_upstart" "--return-code" "/opt/ros/indigo/share/roslint/cmake/../../../lib/roslint/test_wrapper /home/andrewandjasmine/movo_ws/build/test_results/movo_upstart/roslint-movo_upstart.xml make roslint_movo_upstart")
add_test(_ctest_movo_upstart_nosetests_test "/home/andrewandjasmine/movo_ws/build/catkin_generated/env_cached.sh" "/usr/bin/python" "/opt/ros/indigo/share/catkin/cmake/test/run_tests.py" "/home/andrewandjasmine/movo_ws/build/test_results/movo_upstart/nosetests-test.xml" "--return-code" "/usr/bin/cmake -E make_directory /home/andrewandjasmine/movo_ws/build/test_results/movo_upstart" "/usr/bin/nosetests-2.7 -P --process-timeout=60 --where=/home/andrewandjasmine/movo_ws/src/movo_kinova/movo_robot/movo_upstart/test --with-xunit --xunit-file=/home/andrewandjasmine/movo_ws/build/test_results/movo_upstart/nosetests-test.xml")

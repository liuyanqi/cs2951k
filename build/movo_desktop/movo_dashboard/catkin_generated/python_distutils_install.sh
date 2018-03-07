#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/andrewandjasmine/movo_ws/src/movo_desktop/movo_dashboard"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/andrewandjasmine/movo_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/andrewandjasmine/movo_ws/install/lib/python2.7/dist-packages:/home/andrewandjasmine/movo_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/andrewandjasmine/movo_ws/build" \
    "/usr/bin/python" \
    "/home/andrewandjasmine/movo_ws/src/movo_desktop/movo_dashboard/setup.py" \
    build --build-base "/home/andrewandjasmine/movo_ws/build/movo_desktop/movo_dashboard" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/andrewandjasmine/movo_ws/install" --install-scripts="/home/andrewandjasmine/movo_ws/install/bin"

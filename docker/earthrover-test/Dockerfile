FROM ros:kinetic-ros-base

# create user ros
RUN adduser --uid 1010 --home /home/earthrover --system --shell /bin/bash --group --gecos "earthrover" earthrover

USER earthrover
WORKDIR /home/earthrover
RUN mkdir /home/earthrover/ros_build

# get the code
RUN cd /home/earthrover/ros_build && git clone --recursive --depth 1 --branch master https://github.com/earthrover/earth-rover-ugv.git
RUN /bin/bash -c "source /opt/ros/kinetic/setup.sh && cd /home/earthrover/ros_build/earth-rover-ugv/workspace && catkin_make"

# install code
USER root

RUN mkdir -p /opt/earthrover_ros/kinetic
RUN /bin/bash -c "source /opt/ros/kinetic/setup.sh && cd /home/earthrover/ros_build/earth-rover-ugv/workspace && catkin_make -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic install"

# clean up
RUN rm -fr /home/earthrover/ros_build



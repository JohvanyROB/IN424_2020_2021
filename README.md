# IN424_2020_2021

## ROS Installation
Open a terminal (Ctrl + T) and paste the different steps ONE AFTER THE OTHER:

```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

sudo apt update

sudo apt install ros-melodic-desktop-full

source /opt/ros/melodic/setup.bash

sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

sudo apt install python-rosdep

sudo rosdep init

rosdep update
```

Now, create a directory for ROS applications as follow:
```bash
mkdir -p ~/catkin_ws/src

cd ~/catkin_ws/

catkin_make

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
```


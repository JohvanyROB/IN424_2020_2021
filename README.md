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

sudo rosdep init

rosdep update
```

### Catkin workspace
Now, create a directory for ROS applications as follow:
```bash
mkdir -p ~/catkin_ws/src

cd ~/catkin_ws/ && catkin_make

echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc

source ~/.bashrc
```

### ROS dependencies with Python 3
In a terminal, paste the following instructions ONE AFTER THE OTHER:
```bash
sudo apt install python3-pip

sudo pip3 install --upgrade pip

sudo pip3 install rospkg
```

## Clone the Project repository
In a terminal, paste the following instructions:

```bash
cd ~/catkin_ws/src && git clone https://github.com/JohvanyROB/IN424_2020_2021.git

cd ~/catkin_ws && catkin_make

source ~/catkin_ws/devel/setup.bash
```

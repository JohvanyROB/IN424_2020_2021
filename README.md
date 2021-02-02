# IN424_2020_2021

### ROS dependencies with Python 3

Connect to [RDS](https://app.theconstructsim.com/#/) with your user and password
Go to "My rosjects" and run the project that you created.

In a terminal, follow the instructions **ONE AFTER THE OTHER**:
```bash
sudo apt update && sudo apt install python3-pip

sudo pip3 install --upgrade pip

sudo pip3 install rospkg
```

## Clone the Project repository
In the same terminal, follow the instructions **ONE AFTER THE OTHER**:

```bash
cd ~/catkin_ws/src && git clone https://github.com/JohvanyROB/IN424_2020_2021.git

cd ~/catkin_ws && catkin_make && source ~/catkin_ws/devel/setup.bash
```

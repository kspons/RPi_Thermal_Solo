# rpi_thermal_solo

### Overview

This is a ros package for using the ThermApp camera on a 3DR Solo.

**Author: Keith Sponsler
Affiliation: [Unmanned Systems Laboratory](https://unmanned.tamu.edu/)**

rpi_thermal_solo has been tested under [ROS] kinetic and ubuntu-mate for rpi. This is research code and it changes frequently.

### This package also includes support for point grey cameras and GPS logging

#### Dependencies

- [Robot Operating System (ROS)](http://wiki.ros.org) (middleware for robotics)
- [MAVROS] (MAVLink extendable communication node for ROS with proxy for Ground Control Station.)
- [v4l2loopback](https://github.com/Pidbip/ThermAppCam/tree/master/thermapp) (allows the ThermApp cam to stream)


# Setup
This package requires use of v4l2loopback and ThermAppCam 
First, download and install [v4l2loopback](https://github.com/Pidbip/ThermAppCam/tree/master/thermapp)
Second, download and build thermapp from https://github.com/Pidbip/ThermAppCam/tree/master/thermapp
Make sure that thermapp is working and you can see a live feed from the Thermapp camera. To do this, use
```
sudo modprobe videodev
cd ~/v4l2loopback
sudo insmod ./v4l2loopback.ko devices=2
cd ~/ThermAppCam/thermapp
sudo ./thermapp
```
using vlc, or other video stream viewer, you should be able to see the live feed from the thermal camera.

Start a rosmaster, or use the cameras.launch to begin using the package.

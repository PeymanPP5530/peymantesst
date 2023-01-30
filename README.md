[Università degli studi di Genova](https://unige.it/en/ "University of Genoa")

Professor: [Carmine Recchiuto](https://github.com/CarmineD8 "Carmine Recchiuto")

Student: Peyman Peyvandi Pour  - 5573284 - Robotics Engineering 

First assignment of Research Track 1 course
------------
[TOC]


## Aims of the assignment:

A simple, portable robot simulator is developed by [Student Robotics](https://studentrobotics.org).
An arena has been modified for the first assignment of the Research Track I course.
Now we should write a Python node that:
- Search and find a silver token in the environment
- Put this silver token close to a golden token

In the end, we have to have silver and golden boxes distributed in pairs.

## Installing and running

The simulator requires a Python 2.7 installation, the [pygame](http://pygame.org/) library, [PyPyBox2D](https://pypi.python.org/pypi/pypybox2d/2.1-r331), and [PyYAML](https://pypi.python.org/pypi/PyYAML/).

Pygame, unfortunately, can be tricky (though [not impossible](http://askubuntu.com/q/312767)) to install in virtual environments. If you are using `pip`, you might try `pip install hg+https://bitbucket.org/pygame/pygame`, or you could use your operating system's package manager. Windows users could use [Portable Python](http://portablepython.com/). PyPyBox2D and PyYAML are more forgiving, and should install just fine using `pip` or `easy_install`.

**Open a shell and execute the following command:**
```shell
sudo apt-get udpate
sudo apt-get install git
sudo apt-get install python-dev python-pip python-pygame
sudo pip install pypybox2d
```
Now, you should [download](https://github.com/PeymanPP5530/research-track-1-assignment1.git "download") a simple robotic simulator with the solution:
```shell
cd
git clone https://github.com/PeymanPP5530/research-track-1-assignment1.git
```
Then, move to the simulator folder:
```shell
cd ~/research-track-1-assignment1/robot-sim
```
Now, run the simulation:
```shell
python2 run.py assignment.py
```
The following simulation will be show:
>  ![initial](https://github.com/PeymanPP5530/research-track-1-assignment1/blob/main/README%20images/initial.png?raw=true "initial")

## How it works
In order to accomplish the assignment, the robot will look for tokens in front of it and grab the nearest one. Once the robot has grabbed the silver token, it will look for a gold token in front of it, move near it, and release the silver token once it is close enough. Silver tokens will be placed next to gold tokens until every silver token is next to a different gold token.

The flowchart of the algorithm is:
> ![flowchart](https://github.com/PeymanPP5530/research-track-1-assignment1/blob/main/README%20images/flowchart.jpg?raw=true "flowchart")

As we can see in the images, the robot performs the following actions to achieve the goal of the assignment:
1. Robot is in its initial position:
![initial](https://github.com/PeymanPP5530/research-track-1-assignment1/blob/main/README%20images/initial.png?raw=true "initial")

1. Robot grabbed a silver token:
![grab silver token](https://github.com/PeymanPP5530/research-track-1-assignment1/blob/main/README%20images/grab.png?raw=true "grab silver token")

1. Robot release a silver token next to a silver token:
![release](https://github.com/PeymanPP5530/research-track-1-assignment1/blob/main/README%20images/release.png?raw=true "release")

1. Ultimately, each silver token is placed next to a gold token
![final](https://github.com/PeymanPP5530/research-track-1-assignment1/blob/main/README%20images/final.png?raw=true "final")
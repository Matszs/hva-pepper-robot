# Mirai (Pepper Robot)

This repository contains the code to make a Pepper Robot (of SoftBank Robots)
perform a speech.

The repository consist of a few parts:

- mirai (Python application to control the robot)
- pepper app (Choregraphe application)
- web (Web pages for display on the tablet of the robot)


### Installation

To start working with the robot it is required to follow the quick-start of NaoQI 2.5.
Make sure to install the Python-SDK

Upgrade PIP:
`pip install --user --upgrade "pip==20.3.4"`

Install Paho-MQTT on Pepper robot:

`/home/nao/.local/bin/pip install --user paho-mqtt`

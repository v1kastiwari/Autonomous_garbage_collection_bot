# 🗑️ Autonomous Garbage Collection Robot 🤖

A smart robotics solution designed to automate garbage collection using computer vision, ultrasonic sensing, and robotic actuation. Built as a final-year engineering project to promote cleaner and greener smart cities.

## 📌 Overview

This project integrates **image processing**, **object detection**, and **robotics control** to autonomously:
- Navigate using lane detection
- Detect garbage bins using an ultrasonic sensor
- Identify bin type using a color sensor
- Collect garbage using a 4-DOF robotic arm

## 🚀 Features
- **Real-time lane detection** using camera and OpenCV
- **Ultrasonic sensor integration** for bin distance detection
- **Color-based bin classification** for smart segregation
- **Robotic arm (Arduino-controlled)** for object pickup and placement
- Modular Python code structure for easy development and testing

---

## 🧠 System Architecture

| Component | Description |
|----------|-------------|
| `MainRobot.py` | Main control loop; coordinates sensing, detection, and robotic actuation |
| `LaneModule.py` | Image processing module for lane detection |
| `WebcamModule.py` | Camera interface for capturing video frames |
| `utils.py` | Utility functions for processing, filtering, and decision-making logic |
| `robotic_arm_arduino.c` | C code uploaded to Arduino to control a 4-DOF robotic arm based on distance and color input |

---

## 🖥️ Technologies Used

- **Python 3.7+**
- **OpenCV**
- **NumPy**
- **Arduino C (for arm control)**
- **Raspberry Pi 4B** for camera and logic processing
- **Arduino Uno** for robotic arm control

---

## ⚙️ Hardware Components

- Raspberry Pi 4B
- Arduino Uno
- USB Camera
- Ultrasonic Sensor (HC-SR04)
- Color Sensor (TCS3200 or similar)
- 4-DOF Robotic Arm with Servo Motors
- Motor Driver (L298N or similar)
- Chassis and wheels for robot movement

---

## 🛠️ Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/v1kastiwari/Autonomous_garbage_collection_bot.git
   cd Autonomous_garbage_collection_bot

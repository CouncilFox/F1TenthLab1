# lab1_pkg

## Overview

`lab1_pkg` is a ROS 2 package developed for educational purposes, demonstrating basic ROS 2 concepts including creating publishers and subscribers, working with parameters, and using custom messages. This package includes examples of a minimal publisher/subscriber using `rclpy` and the `ackermann_msgs` message for Ackermann steering vehicles.

## Features

- **Talker Node**: Publishes `AckermannDriveStamped` messages with configurable speed and steering angle parameters.
- **Relay Node**: Subscribes to `AckermannDriveStamped` messages, modifies the values, and republishes them.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- ROS 2 Foxy Fitzroy (or later) installed on your system
- Basic knowledge of ROS 2 concepts and command-line tools

## Installation

To install `lab1_pkg`, follow these steps:

1. Navigate to your ROS 2 workspace's `src` directory:

    ```bash
    cd ~/ros2_ws/src
    ```

2. Clone the repository:

    ```bash
    git clone https://github.com/CouncilFox/F1TenthLab1.git lab1_pkg
    ```

3. Build the package:

    ```bash
    cd ~/ros2_ws
    colcon build --packages-select lab1_pkg
    ```

4. Source the ROS 2 environment:

    ```bash
    source ~/ros2_ws/install/setup.bash
    ```

## Usage

To use `lab1_pkg`, run the following commands in separate terminals:

- To launch the talker node:

    ```bash
    ros2 run lab1_pkg talker
    ```

- To launch the relay node:

    ```bash
    ros2 run lab1_pkg relay
    ```

- To set parameters for the talker node:

    ```bash
    ros2 param set /talker v 1.0
    ros2 param set /talker d 0.5
    ```

## Launching with a Launch File

You can also launch both nodes using the provided launch file:

```bash
ros2 launch lab1_pkg lab1_launch.py

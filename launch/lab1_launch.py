from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('lab1_pkg'),
        'config',
        'talker_params.yaml'
    )
    
    return LaunchDescription([
        Node(
            package='lab1_pkg',
            executable='talker',
            name='talker',
            parameters=[config],
            output='screen'
        ),
        Node(
            package='lab1_pkg',
            executable='relay',
            name='relay',
            output='screen'
        )
    ])

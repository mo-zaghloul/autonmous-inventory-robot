import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    
    slam_params = os.path.join(
        get_package_share_directory('bumperbot_slam'),
        'config', 'mapper_params_online_async.yaml'
    )

    slam_node = Node(
        package='slam_toolbox',
        executable='async_slam_toolbox_node',
        name='slam_toolbox',
        output='screen',
        parameters=[
            slam_params,
            {'use_sim_time': True}
            ],
    )

    return LaunchDescription([
        slam_node,
    ])
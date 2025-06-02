from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_path = get_package_share_directory('kruger_guariste_pkg')

    rosbag_path = os.path.join('/root/ros2_ws/src/kruger_guariste_pkg', 'dataset')
    rviz_config_path = os.path.join(pkg_path, 'rviz', 'config.rviz')
    rqt_config_path = os.path.join(pkg_path, 'rqt', 'config.perspective')

    return LaunchDescription([
        ExecuteProcess(
            cmd=[
                'ros2', 'bag', 'play', rosbag_path,
                '-r', '2.0',
                '--read-ahead-queue-size', '1000',
                '--loop'
            ],
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen'
        ),
        Node(
            package='rqt_gui',
            executable='rqt_gui',
            arguments=['--perspective-file', rqt_config_path],
            output='screen'
        )
    ])

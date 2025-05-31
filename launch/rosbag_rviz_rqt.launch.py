from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

def generate_launch_description():
    bag_path = os.path.join(
                     os.getenv('HOME'),
                     'ros2_ws', 'src', 'kruger_guariste_pkg', 'dataset')

    return LaunchDescription([
        # Ejecutar el rosbag
        ExecuteProcess(
            cmd=['ros2', 'bag', 'play', bag_path],
            output='screen'
        ),

        # Lanzar RViz con una configuración guardada
        ExecuteProcess(
            cmd=['rviz2', '-d', os.path.join(
                os.getenv('HOME'),
                'ros2_ws', 'src', 'kruger_guariste_pkg', 'rviz', 'config.rviz')],
            output='screen'
        ),

        # Lanzar RQT con una perspectiva guardada
        ExecuteProcess(
            cmd=['rqt', '--perspective-file',
                 os.path.join(
                     os.getenv('HOME'),
                     'ros2_ws', 'src', 'kruger_guariste_pkg', 'rqt', 'config.perspective')],
            output='screen'
        ),
    ])

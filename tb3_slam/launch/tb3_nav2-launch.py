import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import (DeclareLaunchArgument, GroupAction,
                            IncludeLaunchDescription, SetEnvironmentVariable)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression
from launch_ros.actions import Node
from launch_ros.actions import PushRosNamespace
from launch_ros.descriptions import ParameterFile
from nav2_common.launch import RewrittenYaml, ReplaceString

def generate_launch_description():
    ld = LaunchDescription()

    pkg_dir = get_package_share_directory('tb3_sim')
    map_server_params = os.path.join(pkg_dir, 'config/nav2', 'map_server_params.yaml')

    remappings = [('/tf', 'tf'),
        ('/tf_static', 'tf_static')]
    
    nav2_cmd_group = GroupAction([
        Node(
            package='nav2_map_server',
            executable='map_server',
            output='screen',
            respawn_delay=2.0,
            parameters=[map_server_params])
    ])
    
    ld.add_action(nav2_cmd_group)

    return ld
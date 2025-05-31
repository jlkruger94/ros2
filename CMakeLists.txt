cmake_minimum_required(VERSION 3.5)
project(kruger_guariste_pkg)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch
  rviz
  rqt
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

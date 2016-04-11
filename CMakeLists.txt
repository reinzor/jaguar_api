cmake_minimum_required(VERSION 2.8.3)
project(jaguar_api)

find_package(catkin REQUIRED)

catkin_add_env_hooks(99.jaguar_console SHELLS bash DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/env-hooks)
catkin_python_setup()

catkin_package()

cmake_minimum_required(VERSION 3.10)

# 1. Name your project
project(HelloWorld)

# 2. Use Modern C++ (C++20)
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 3. This generates the map for Zed's autocomplete
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# 4. Define your executable
# "main" is the name of the output file
# "main.cpp" is your source file. Add other files here (e.g., "utils.cpp")
add_executable(main main.cpp)
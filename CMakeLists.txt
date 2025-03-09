cmake_minimum_required(VERSION 3.16.3)
project(pytracer)

# pybind11
set(PYBIND_DIR ${CMAKE_CURRENT_SOURCE_DIR}/pybind11)
add_subdirectory(${PYBIND_DIR})
pybind11_add_module(pytracer src/pytracer.cpp)


set(TRACER_TOOL_LIB_DIR ${CMAKE_CURRENT_SOURCE_DIR}/tracer_tool)
set(TRACER_TOOL_INCLUDE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/tracer_tool)
target_include_directories(pytracer PRIVATE ${TRACER_TOOL_INCLUDE_DIR})
target_link_directories(pytracer PRIVATE ${TRACER_TOOL_LIB_DIR})
target_link_libraries(pytracer PRIVATE tracer_tool)

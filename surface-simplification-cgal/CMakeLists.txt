# Created by the script cgal_create_cmake_script_with_options
# This is the CMake script for compiling a set of CGAL applications.

cmake_minimum_required(VERSION 3.1...3.23)
project(Surface_Mesh_Simplification)

# CGAL and its components
find_package(CGAL REQUIRED)

# Boost and its components
find_package(Boost)
if(NOT Boost_FOUND)
  message(
    STATUS "This project requires the Boost library, and will not be compiled.")
  return()
endif()
find_package(Eigen3 REQUIRED)
include_directories(${Eigen3_INCLUDE_DIRS})
find_package( TBB QUIET )

if( TBB_FOUND )
  include(${TBB_USE_FILE})
  list(APPEND CGAL_3RD_PARTY_LIBRARIES ${TBB_LIBRARIES})
endif()
find_package(OpenMesh QUIET)

# Creating entries for all .cpp/.C files with "main" routine
# ##########################################################

create_single_source_cgal_program("edge_collapse.cpp")

find_package(Eigen3 3.1.0 QUIET) #(3.1.0 or greater)
include(CGAL_Eigen3_support)
if(TARGET CGAL::Eigen3_support)
  create_single_source_cgal_program("edge_collapse_garland_heckbert.cpp")
  target_link_libraries(edge_collapse_garland_heckbert PUBLIC CGAL::Eigen3_support)
else()
  message(STATUS "NOTICE: Garland-Heckbert polices require the Eigen library, which has not been found; related examples will not be compiled.")
endif()
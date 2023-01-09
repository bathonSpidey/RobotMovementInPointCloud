# Distributed under the OSI-approved BSD 3-Clause License.  See accompanying
# file Copyright.txt or https://cmake.org/licensing for details.

cmake_minimum_required(VERSION 3.5)

file(MAKE_DIRECTORY
  "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/third-party/libusb"
  "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/libusb-prefix/src/libusb-build"
  "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/libusb-prefix"
  "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/libusb-prefix/tmp"
  "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/libusb-prefix/src/libusb-stamp"
  "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/libusb-prefix/src"
  "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/libusb-prefix/src/libusb-stamp"
)

set(configSubDirs Debug;Release;MinSizeRel;RelWithDebInfo)
foreach(subDir IN LISTS configSubDirs)
    file(MAKE_DIRECTORY "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/libusb-prefix/src/libusb-stamp/${subDir}")
endforeach()
if(cfgdir)
  file(MAKE_DIRECTORY "C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/libusb-prefix/src/libusb-stamp${cfgdir}") # cfgdir has leading slash
endif()

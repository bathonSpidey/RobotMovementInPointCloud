// All included firmware files are
// INTEL CORPORATION PROPRIETARY INFORMATION
// Copyright(c) 2019 Intel Corporation. All Rights Reserved
const int fw_L53X_FW_Image_version[4] = {3,5,5,1};
#ifndef _MSC_VER
__asm__(
    "#version 9bc28aaf079b105d9a20a0bd845ea222b8754571\n"
#ifdef __APPLE__
    ".const_data\n"
#define _ "_"
#else
    ".section .rodata\n"
#define _ ""
#endif
    ".global "_"fw_L53X_FW_Image_data\n"
    _"fw_L53X_FW_Image_data:\n"
    ".incbin \"C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/common/fw/L53X_FW_Image-3.5.5.1.bin\"\n"
    ".global "_"fw_L53X_FW_Image_size\n"
    _"fw_L53X_FW_Image_size:\n"
    "1:\n"
    ".int 1b - "_"fw_L53X_FW_Image_data\n"
    ".previous"
);
#undef _
#endif

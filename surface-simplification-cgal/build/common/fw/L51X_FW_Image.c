// All included firmware files are
// INTEL CORPORATION PROPRIETARY INFORMATION
// Copyright(c) 2019 Intel Corporation. All Rights Reserved
const int fw_L51X_FW_Image_version[4] = {1,5,8,1};
#ifndef _MSC_VER
__asm__(
    "#version ab73e5bfc520c0aa0340cada4b3e317b8fd31a4d\n"
#ifdef __APPLE__
    ".const_data\n"
#define _ "_"
#else
    ".section .rodata\n"
#define _ ""
#endif
    ".global "_"fw_L51X_FW_Image_data\n"
    _"fw_L51X_FW_Image_data:\n"
    ".incbin \"C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/common/fw/L51X_FW_Image-1.5.8.1.bin\"\n"
    ".global "_"fw_L51X_FW_Image_size\n"
    _"fw_L51X_FW_Image_size:\n"
    "1:\n"
    ".int 1b - "_"fw_L51X_FW_Image_data\n"
    ".previous"
);
#undef _
#endif

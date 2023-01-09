// All included firmware files are
// INTEL CORPORATION PROPRIETARY INFORMATION
// Copyright(c) 2019 Intel Corporation. All Rights Reserved
const int fw_target_version[4] = {0,2,0,951};
#ifndef _MSC_VER
__asm__(
    "#version c3940ccbb0e3045603e4aceaa2d73427f96e24bc\n"
#ifdef __APPLE__
    ".const_data\n"
#define _ "_"
#else
    ".section .rodata\n"
#define _ ""
#endif
    ".global "_"fw_target_data\n"
    _"fw_target_data:\n"
    ".incbin \"C:/Users/lukam/Desktop/RobotMovementInPointCloud/surface-simplification-cgal/build/common/fw/target-0.2.0.951.mvcmd\"\n"
    ".global "_"fw_target_size\n"
    _"fw_target_size:\n"
    "1:\n"
    ".int 1b - "_"fw_target_data\n"
    ".previous"
);
#undef _
#endif

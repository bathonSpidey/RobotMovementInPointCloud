#pragma once

#define FW_TARGET_VERSION "0.2.0.951"

extern "C" const unsigned char fw_target_data[];
extern "C" const int           fw_target_size;
extern "C" const int           fw_target_version[4];

#ifdef _MSC_VER
#include <windows.h>
extern "C" IMAGE_DOS_HEADER __ImageBase;
#endif

static inline const unsigned char *fw_get_target(int &size)
{
#ifdef _MSC_VER
    HRSRC rc = ::FindResourceA((HMODULE)&__ImageBase, "TARGET_DATA" , "TARGET_RC");
    HGLOBAL data = ::LoadResource((HMODULE)&__ImageBase, rc);
    size = ::SizeofResource((HMODULE)&__ImageBase, rc);
    return static_cast<const unsigned char*>(::LockResource(data));
#else
    size = fw_target_size;
    return fw_target_data;
#endif
}

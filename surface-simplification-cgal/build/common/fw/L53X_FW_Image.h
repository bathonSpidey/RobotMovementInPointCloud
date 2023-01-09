#pragma once

#define FW_L53X_FW_IMAGE_VERSION "3.5.5.1"

extern "C" const unsigned char fw_L53X_FW_Image_data[];
extern "C" const int           fw_L53X_FW_Image_size;
extern "C" const int           fw_L53X_FW_Image_version[4];

#ifdef _MSC_VER
#include <windows.h>
extern "C" IMAGE_DOS_HEADER __ImageBase;
#endif

static inline const unsigned char *fw_get_L53X_FW_Image(int &size)
{
#ifdef _MSC_VER
    HRSRC rc = ::FindResourceA((HMODULE)&__ImageBase, "L53X_FW_IMAGE_DATA" , "L53X_FW_IMAGE_RC");
    HGLOBAL data = ::LoadResource((HMODULE)&__ImageBase, rc);
    size = ::SizeofResource((HMODULE)&__ImageBase, rc);
    return static_cast<const unsigned char*>(::LockResource(data));
#else
    size = fw_L53X_FW_Image_size;
    return fw_L53X_FW_Image_data;
#endif
}

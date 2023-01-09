#pragma once

#define FW_SR3XX_FW_IMAGE_VERSION "3.26.1.0"

extern "C" const unsigned char fw_SR3XX_FW_Image_data[];
extern "C" const int           fw_SR3XX_FW_Image_size;
extern "C" const int           fw_SR3XX_FW_Image_version[4];

#ifdef _MSC_VER
#include <windows.h>
extern "C" IMAGE_DOS_HEADER __ImageBase;
#endif

static inline const unsigned char *fw_get_SR3XX_FW_Image(int &size)
{
#ifdef _MSC_VER
    HRSRC rc = ::FindResourceA((HMODULE)&__ImageBase, "SR3XX_FW_IMAGE_DATA" , "SR3XX_FW_IMAGE_RC");
    HGLOBAL data = ::LoadResource((HMODULE)&__ImageBase, rc);
    size = ::SizeofResource((HMODULE)&__ImageBase, rc);
    return static_cast<const unsigned char*>(::LockResource(data));
#else
    size = fw_SR3XX_FW_Image_size;
    return fw_SR3XX_FW_Image_data;
#endif
}

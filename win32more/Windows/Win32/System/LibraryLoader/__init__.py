from __future__ import annotations
from win32more import ARCH, Boolean, Byte, Bytes, Char, ComPtr, Double, EasyCastStructure, EasyCastUnion, FAILED, Guid, Int16, Int32, Int64, IntPtr, MissingType, POINTER, SByte, SUCCEEDED, Single, String, UInt16, UInt32, UInt64, UIntPtr, Void, VoidPtr, cfunctype, cfunctype_pointer, commethod, make_ready, winfunctype, winfunctype_pointer
import win32more.Windows.Win32.Foundation
import win32more.Windows.Win32.System.LibraryLoader
FIND_RESOURCE_DIRECTORY_TYPES: UInt32 = 256
FIND_RESOURCE_DIRECTORY_NAMES: UInt32 = 512
FIND_RESOURCE_DIRECTORY_LANGUAGES: UInt32 = 1024
RESOURCE_ENUM_LN: UInt32 = 1
RESOURCE_ENUM_MUI: UInt32 = 2
RESOURCE_ENUM_MUI_SYSTEM: UInt32 = 4
RESOURCE_ENUM_VALIDATE: UInt32 = 8
RESOURCE_ENUM_MODULE_EXACT: UInt32 = 16
SUPPORT_LANG_NUMBER: UInt32 = 32
GET_MODULE_HANDLE_EX_FLAG_PIN: UInt32 = 1
GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT: UInt32 = 2
GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS: UInt32 = 4
CURRENT_IMPORT_REDIRECTION_VERSION: UInt32 = 1
LOAD_LIBRARY_OS_INTEGRITY_CONTINUITY: UInt32 = 32768
@winfunctype('KERNEL32.dll')
def DisableThreadLibraryCalls(hLibModule: win32more.Windows.Win32.Foundation.HMODULE) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindResourceExW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, wLanguage: UInt16) -> win32more.Windows.Win32.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def FreeLibraryAndExitThread(hLibModule: win32more.Windows.Win32.Foundation.HMODULE, dwExitCode: UInt32) -> Void: ...
@winfunctype('KERNEL32.dll')
def FreeResource(hResData: win32more.Windows.Win32.Foundation.HGLOBAL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetModuleFileNameA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetModuleFileNameW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpFilename: win32more.Windows.Win32.Foundation.PWSTR, nSize: UInt32) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleA(lpModuleName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HMODULE: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleW(lpModuleName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HMODULE: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleExA(dwFlags: UInt32, lpModuleName: win32more.Windows.Win32.Foundation.PSTR, phModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetModuleHandleExW(dwFlags: UInt32, lpModuleName: win32more.Windows.Win32.Foundation.PWSTR, phModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetProcAddress(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpProcName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.FARPROC: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryExA(lpLibFileName: win32more.Windows.Win32.Foundation.PSTR, hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> win32more.Windows.Win32.Foundation.HMODULE: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryExW(lpLibFileName: win32more.Windows.Win32.Foundation.PWSTR, hFile: win32more.Windows.Win32.Foundation.HANDLE, dwFlags: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> win32more.Windows.Win32.Foundation.HMODULE: ...
@winfunctype('KERNEL32.dll')
def LoadResource(hModule: win32more.Windows.Win32.Foundation.HMODULE, hResInfo: win32more.Windows.Win32.Foundation.HRSRC) -> win32more.Windows.Win32.Foundation.HGLOBAL: ...
@winfunctype('KERNEL32.dll')
def LockResource(hResData: win32more.Windows.Win32.Foundation.HGLOBAL) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def SizeofResource(hModule: win32more.Windows.Win32.Foundation.HMODULE, hResInfo: win32more.Windows.Win32.Foundation.HRSRC) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def AddDllDirectory(NewDirectory: win32more.Windows.Win32.Foundation.PWSTR) -> VoidPtr: ...
@winfunctype('KERNEL32.dll')
def RemoveDllDirectory(Cookie: VoidPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDefaultDllDirectories(DirectoryFlags: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesExA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PSTR, lpName: win32more.Windows.Win32.Foundation.PSTR, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESLANGPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesExW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESLANGPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesExA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PSTR, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESNAMEPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesExW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESNAMEPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesExA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESTYPEPROCA, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesExW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESTYPEPROCW, lParam: IntPtr, dwFlags: UInt32, LangId: UInt16) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def FindResourceW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpName: win32more.Windows.Win32.Foundation.PWSTR, lpType: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryA(lpLibFileName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HMODULE: ...
@winfunctype('KERNEL32.dll')
def LoadLibraryW(lpLibFileName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.HMODULE: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESNAMEPROCW, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceNamesA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PSTR, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESNAMEPROCA, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def LoadModule(lpModuleName: win32more.Windows.Win32.Foundation.PSTR, lpParameterBlock: VoidPtr) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def LoadPackagedLibrary(lpwLibFileName: win32more.Windows.Win32.Foundation.PWSTR, Reserved: UInt32) -> win32more.Windows.Win32.Foundation.HMODULE: ...
@winfunctype('KERNEL32.dll')
def FindResourceA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpName: win32more.Windows.Win32.Foundation.PSTR, lpType: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def FindResourceExA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PSTR, lpName: win32more.Windows.Win32.Foundation.PSTR, wLanguage: UInt16) -> win32more.Windows.Win32.Foundation.HRSRC: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESTYPEPROCA, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceTypesW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESTYPEPROCW, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PSTR, lpName: win32more.Windows.Win32.Foundation.PSTR, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESLANGPROCA, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EnumResourceLanguagesW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, lpEnumFunc: win32more.Windows.Win32.System.LibraryLoader.ENUMRESLANGPROCW, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def BeginUpdateResourceA(pFileName: win32more.Windows.Win32.Foundation.PSTR, bDeleteExistingResources: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def BeginUpdateResourceW(pFileName: win32more.Windows.Win32.Foundation.PWSTR, bDeleteExistingResources: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.HANDLE: ...
@winfunctype('KERNEL32.dll')
def UpdateResourceA(hUpdate: win32more.Windows.Win32.Foundation.HANDLE, lpType: win32more.Windows.Win32.Foundation.PSTR, lpName: win32more.Windows.Win32.Foundation.PSTR, wLanguage: UInt16, lpData: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def UpdateResourceW(hUpdate: win32more.Windows.Win32.Foundation.HANDLE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, wLanguage: UInt16, lpData: VoidPtr, cb: UInt32) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EndUpdateResourceA(hUpdate: win32more.Windows.Win32.Foundation.HANDLE, fDiscard: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def EndUpdateResourceW(hUpdate: win32more.Windows.Win32.Foundation.HANDLE, fDiscard: win32more.Windows.Win32.Foundation.BOOL) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDllDirectoryA(lpPathName: win32more.Windows.Win32.Foundation.PSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def SetDllDirectoryW(lpPathName: win32more.Windows.Win32.Foundation.PWSTR) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype('KERNEL32.dll')
def GetDllDirectoryA(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PSTR) -> UInt32: ...
@winfunctype('KERNEL32.dll')
def GetDllDirectoryW(nBufferLength: UInt32, lpBuffer: win32more.Windows.Win32.Foundation.PWSTR) -> UInt32: ...
@winfunctype_pointer
def ENUMRESLANGPROCA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PSTR, lpName: win32more.Windows.Win32.Foundation.PSTR, wLanguage: UInt16, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESLANGPROCW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, wLanguage: UInt16, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESNAMEPROCA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PSTR, lpName: win32more.Windows.Win32.Foundation.PSTR, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESNAMEPROCW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lpName: win32more.Windows.Win32.Foundation.PWSTR, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESTYPEPROCA(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PSTR, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def ENUMRESTYPEPROCW(hModule: win32more.Windows.Win32.Foundation.HMODULE, lpType: win32more.Windows.Win32.Foundation.PWSTR, lParam: IntPtr) -> win32more.Windows.Win32.Foundation.BOOL: ...
class ENUMUILANG(EasyCastStructure):
    NumOfEnumUILang: UInt32
    SizeOfEnumUIBuffer: UInt32
    pEnumUIBuffer: POINTER(UInt16)
LOAD_LIBRARY_FLAGS = UInt32
DONT_RESOLVE_DLL_REFERENCES: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 1
LOAD_LIBRARY_AS_DATAFILE: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 2
LOAD_WITH_ALTERED_SEARCH_PATH: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 8
LOAD_IGNORE_CODE_AUTHZ_LEVEL: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 16
LOAD_LIBRARY_AS_IMAGE_RESOURCE: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 32
LOAD_LIBRARY_AS_DATAFILE_EXCLUSIVE: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 64
LOAD_LIBRARY_REQUIRE_SIGNED_TARGET: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 128
LOAD_LIBRARY_SEARCH_DLL_LOAD_DIR: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 256
LOAD_LIBRARY_SEARCH_APPLICATION_DIR: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 512
LOAD_LIBRARY_SEARCH_USER_DIRS: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 1024
LOAD_LIBRARY_SEARCH_SYSTEM32: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 2048
LOAD_LIBRARY_SEARCH_DEFAULT_DIRS: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 4096
LOAD_LIBRARY_SAFE_CURRENT_DIRS: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 8192
LOAD_LIBRARY_SEARCH_SYSTEM32_NO_FORWARDER: win32more.Windows.Win32.System.LibraryLoader.LOAD_LIBRARY_FLAGS = 16384
@winfunctype_pointer
def PGET_MODULE_HANDLE_EXA(dwFlags: UInt32, lpModuleName: win32more.Windows.Win32.Foundation.PSTR, phModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
@winfunctype_pointer
def PGET_MODULE_HANDLE_EXW(dwFlags: UInt32, lpModuleName: win32more.Windows.Win32.Foundation.PWSTR, phModule: POINTER(win32more.Windows.Win32.Foundation.HMODULE)) -> win32more.Windows.Win32.Foundation.BOOL: ...
class REDIRECTION_DESCRIPTOR(EasyCastStructure):
    Version: UInt32
    FunctionCount: UInt32
    Redirections: POINTER(win32more.Windows.Win32.System.LibraryLoader.REDIRECTION_FUNCTION_DESCRIPTOR)
class REDIRECTION_FUNCTION_DESCRIPTOR(EasyCastStructure):
    DllName: win32more.Windows.Win32.Foundation.PSTR
    FunctionName: win32more.Windows.Win32.Foundation.PSTR
    RedirectionTarget: VoidPtr


make_ready(__name__)

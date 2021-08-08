import ctypes
import ctypes.wintypes
import math
import msvcrt
import os
import re
import regex
import requests
import sys
import tarfile
import time
import yaml
import zipfile



__file__=os.path.abspath(__file__).replace("\\","/")
__file_base_dir__=__file__[:-len(__file__.split("/")[-1])-4].rstrip("/")+"/"
__executable__=os.path.abspath(sys.executable).replace("\\","/")[:-len(sys.executable.split("/")[-1].split("\\")[-1])].rstrip("/")+"/python.exe"
__headless_executable__=__executable__[:-4]+"w.exe"
if (not os.path.exists(__file_base_dir__+"data")):
	os.mkdir(__file_base_dir__+"data")



ARDUINO_CACHE={}
ARDUINO_COMMAND_FORMAT_REGEX=re.compile(r"\{(.+?)\}")
ARDUINO_CPP_INCLUDE_FILE_REGEX=re.compile(r"^\s*#\s*include\s*[<\"]([^>\"]+)[>\"]",re.M)
ARDUINO_CUSTOM_WARNING_LEVEL=""
ARDUINO_DATA_LINE_SEPARATOR_REGEX=re.compile(r"\r(\n|$)")
ARDUINO_DIRECTORY_PATH_REGEX=re.compile(r"/$")
ARDUINO_HOST_SYSTEM="i686-mingw32"
ARDUINO_OPTIMIZE_FOR_DEBUG=False
ARDUINO_OS_TYPE="windows"
ARDUINO_REPLACE_INCLUDE_REGEX=re.compile(br"""^\s*#\s*include\s*(<[^>]+>|"[^"]+")""",re.M)
ARDUINO_SERIAL_PLOT_DATA_REGEX=re.compile(r"^(?:-?[0-9]+(?:\.[0-9]+)?(?:,|$))+(?<!,)$")
BASE64_ALPHABET="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
BLENDER_FILE_PATH="C:/Program Files/Blender Foundation/Blender/blender.exe"
GIMP_FILE_PATH="C:/Program Files/GIMP 2/bin/gimp-2.10.exe"
CHROME_FILE_PATH="C:/Program Files/Google/Chrome Dev/Application/chrome.exe"
CMD_FILE_PATH=os.path.abspath(os.getenv("ComSpec","cmd.exe"))
CONSOLE_APP_FRAME_RATE=60
CUSTOM_ICON_FILE_PATH="rsrc/icon.ico"
EDITOR_FILE_PATH="C:/Program Files/Sublime Text 3/sublime_text.exe"
FILE_READ_CHUNK_SIZE=16384
GITHUB_API_QUOTA=5000
GITHUB_DEFAULT_BRANCH_NAME="main"
GITHUB_EMAIL="krzem5.dev@gmail.com"
GITHUB_EMPTY_FILE_HASH="e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
GITHUB_HEADERS="application/vnd.github.v3+json"
GITHUB_INVALID_NAME_CHARACTER_REGEX=re.compile(r"[^A-Za-z0-9_\.\-]")
GITHUB_MAX_FILE_SIZE=52428800
GITHUB_NAME="Krzem"
GITHUB_PROJECT_BRANCH_LIST_FILE_PATH="data/github-branches.dt"
GITHUB_PUSHED_PROJECT_LIST_FILE_PATH="data/github.dt"
with open(__file_base_dir__+"data/github-secret.dt","r") as f:
	GITHUB_TOKEN=f.read().strip()
GITHUB_USERNAME="Krzem5"
GITIGNORE_FILE_PATH_REGEX=re.compile(r"[\\/]([!# ])")
GITIGNORE_SPECIAL_SET_CHARCTERS_REGEX=re.compile(r"([&~|])")
with open(__file_base_dir__+"data/gpg-secret.dt","r") as f:
	GPG_LOCAL_KEY_ID,GPG_PASSPHRASE=list(map(str.strip,f.read().replace("\r\n","\n").split("\n")))[:2]
HOTKEY_HANDLER_END_MESSAGE=0x401
JSON_STRING_ESCAPE_CHAR_BYTES_REGEX=re.compile(br'([\\"]|[^\x20-\x7e])')
JSON_STRING_ESCAPE_CHAR_REGEX=re.compile(r'([\\"]|[^\x20-\x7e])')
JSON_STRING_MIN_SURROGATE_PAIR=65536
MINECRAFT_JAVA_RUNTIME_FILE_PATH="C:/Program Files/Java/jdk-16.0.1/bin/java.exe"
MINECRAFT_JAVA_RUNTIME_MEMORY="8G"
MINECRAFT_LAUNCHER_FILE_PATH="C:/Program Files (x86)/Minecraft Launcher/MinecraftLauncher.exe"
MINECRAFT_SKIP_UPDATE=[]
MOVE_TO_DESKTOP_LIBRARY_PATH="lib/move_to_desktop.dll"
PRINT_ADD_COLOR_REGEX=re.compile(r"'[^']*'|-?[0-9]+(?:\.[0-9]+)?(?:%|\b)|[0-9a-fA-F]+\b")
PROJECT_DIR=os.path.abspath(__file_base_dir__+"../k/code").replace("\\","/").rstrip("/")+"/"
REMOVE_COLOR_FORMATTING_REGEX=re.compile(r"\x1b\[[^m]*m")
REPO_STATS_COMMON_REGEX=re.compile(r";|\{|\}|\(|\)|\[|\]|[\w\.\@\#\/\*]+|\<\<?|\+|\-|\*|\/|%|&&?|\|\|?")
REPO_STATS_DEFAULT_COLOR=(240,240,240)
REPO_STATS_IGNORE_REGEX=re.compile(r"""[ \t]*(\/\/|--|\#|%|\").*?$|/\*(?:.)*?\*/|<!--(?:.)*?-->|\{-(?:.)*?-\}|\(\*(?:.)*?\*\)|(?P<ml_c>[\'\"]|\'{3}|\"{3})(?:\\[\'\"]|.)*?(?P=ml_c)|(0x[0-9a-fA-F]([0-9a-fA-F]|\.)*|[0-9]([0-9]|\.)*)([uU][lL]{0,2}|([eE][-+][0-9]*)?[fFlL]*)""",re.M|re.S)
REPO_STATS_LANGUAGE_DATABASE_FILE="data/git-languages-db.db"
REPO_STATS_LANGUAGE_HEURISTIC_FILE="data/git-languages-h.db"
REPO_STATS_LANGUAGE_LIST_FILE="data/git-languages.db"
REPO_STATS_LANGUAGE_TYPE=["data","programming","markup","prose"]
REPO_STATS_MAX_READ=65536
REPO_STATS_MAX_TOKEN_LEN=32
REPO_STATS_SHEBANG_REGEX=re.compile(r"#!\s*?([^ \t\v\n\r]*?)(?:$|[ \t]+(.*?)$|[ \t\v\n\r])",re.M|re.S)
REPO_STATS_TAG_ATTR_REGEX=re.compile(r"""([\w\$\.]+)(?:\s*=?(?:[\w\$\.]+(?:\s|$)|\"(?:\\\"|.)*?\"))?""",re.M|re.S)
REPO_STATS_TAG_REGEX=re.compile(r"<\s*\??\s*([\w\$\.]+)(.*?)\??\s*>")
REPO_STATS_XML_REGEX=re.compile(r"<\?xml version=")
ROOT_FILE_PATH=os.path.abspath(__file_base_dir__+"../k").replace("\\","/").rstrip("/")+"/"
SERIAL_BAUD=9600
SERIAL_TIMEOUT=5000
SERIAL_VALID_DEVICE_NAME_REGEX=re.compile(r"vif_([0-9a-f]{4})\+pid_([0-9a-f]{4})")
SERIAL_VALID_DEVICE_NAME_USB_REGEX=re.compile(r"vif_([0-9a-f]{4})&pid_([0-9a-f]{4})")
SHA1_START_VALUE=[0x67452301,0xefcdab89,0x98badcfe,0x10325476,0xc3d2e1f0]
TEMP_DIR=os.path.abspath(os.getenv("TEMP",os.getenv("TMP"))).replace("\\","/").rstrip("/")+"/"
UTC_OFFSET=7200
VALID_PROGRAM_TYPES=["arduino","assembly","c","cpp","css","java","javascript","php","processing","python"]
VK_CONTROL=17
VK_MENU=18
VK_SHIFT=16



CREATE_NEW_CONSOLE=0x10
CREATE_NEW_PROCESS_GROUP=0x200
DICS_FLAG_GLOBAL=1
DIGCF_PRESENT=2
DIREG_DEV=1
DTR_CONTROL_ENABLE=1
DUPLICATE_SAME_ACCESS=2
ERROR_IO_INCOMPLETE=0x3e4
ERROR_IO_PENDING=0x3e5
ERROR_OPERATION_ABORTED=0x3e3
ERROR_SUCCESS=0
EV_ERR=0x80
EWX_FORCE=0x4
EWX_FORCEIFHUNG=0x10
EWX_LOGOFF=0x0
EWX_POWEROFF=0x8
EWX_SHUTDOWN=0x1
FILE_ATTRIBUTE_ARCHIVE=0x20
FILE_ATTRIBUTE_HIDDEN=0x2
FILE_ATTRIBUTE_NORMAL=0x80
FILE_FLAG_OVERLAPPED=0x40000000
GENERIC_READ=0x80000000
GENERIC_WRITE=0x40000000
GWL_EXSTYLE=-20
GWL_STYLE=-16
HWND_TOP=0
ICON_BIG=1
ICON_SMALL=0
IDYES=6
IMAGE_ICON=1
INFINITE=4294967295
INVALID_HANDLE_VALUE=0xffffffffffffffff
KEY_READ=0x20019
LLKHF_ALTDOWN=0x20
LLKHF_INJECTED=0x10
LLKHF_UP=0x80
LR_LOADFROMFILE=0x10
MB_DEFBUTTON2=0x100
MB_ICONQUESTION=0x20
MB_SYSTEMMODAL=0x1000
MB_YESNO=0x4
MONITOR_DEFAULTTONEAREST=2
NOPARITY=0
ONESTOPBIT=0
OPEN_EXISTING=3
PROCESS_PER_MONITOR_DPI_AWARE=2
PURGE_RXABORT=2
PURGE_RXCLEAR=8
PURGE_TXABORT=1
PURGE_TXCLEAR=4
RTS_CONTROL_ENABLE=1
SE_PRIVILEGE_ENABLED=0x2
SE_SHUTDOWN_NAME="SeShutdownPrivilege"
SHTDN_REASON_FLAG_PLANNED=0x80000000
SHTDN_REASON_MAJOR_OTHER=0
SHTDN_REASON_MINOR_OTHER=0
SPDRP_HARDWAREID=1
STARTF_USESTDHANDLES=0x100
STD_INPUT_HANDLE=-10
STD_OUTPUT_HANDLE=-11
SW_SHOWMAXIMIZED=3
SWP_SHOWWINDOW=0x40
TOKEN_ADJUST_PRIVILEGES=0x20
TOKEN_QUERY=0x8
VK_PACKET=0xe7
WH_KEYBOARD_LL=13
WM_KEYDOWN=0x100
WM_KILLFOCUS=0x8
WM_SETICON=0x80
WM_SYSKEYDOWN=0x104
WS_EX_TOPMOST=0x8
WS_VISIBLE=0x10000000



ctypes.wintypes.HCURSOR=ctypes.wintypes.HICON
ctypes.wintypes.HDEVINFO=ctypes.c_void_p
ctypes.wintypes.HRESULT=ctypes.c_long
ctypes.wintypes.LONG_PTR=ctypes.c_int64
ctypes.wintypes.LowLevelKeyboardProc=ctypes.WINFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
ctypes.wintypes.LRESULT=ctypes.c_int64
ctypes.wintypes.PCWSTR=ctypes.c_wchar_p
ctypes.wintypes.PROCESS_DPI_AWARENESS=ctypes.c_int
ctypes.wintypes.ULONG_PTR=ctypes.c_uint64
ctypes.wintypes.WNDPROC=ctypes.WINFUNCTYPE(ctypes.wintypes.LRESULT,ctypes.wintypes.HWND,ctypes.wintypes.UINT,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
ctypes.wintypes.CHAR_INFO_CHAR=type("CHAR_INFO_CHAR",(ctypes.Union,),{"_fields_":[("UnicodeChar",ctypes.wintypes.WCHAR),("AsciiChar",ctypes.wintypes.CHAR)]})
ctypes.wintypes.CHAR_INFO=type("CHAR_INFO",(ctypes.Structure,),{"_fields_":[("Char",ctypes.wintypes.CHAR_INFO_CHAR),("Attributes",ctypes.wintypes.WORD)],"_anonymous_":("Char",)})
ctypes.wintypes.COMMTIMEOUTS=type("COMMTIMEOUTS",(ctypes.Structure,),{"_fields_":[("ReadIntervalTimeout",ctypes.wintypes.DWORD),("ReadTotalTimeoutMultiplier",ctypes.wintypes.DWORD),("ReadTotalTimeoutConstant",ctypes.wintypes.DWORD),("WriteTotalTimeoutMultiplier",ctypes.wintypes.DWORD),("WriteTotalTimeoutConstant",ctypes.wintypes.DWORD)]})
ctypes.wintypes.COMSTAT=type("COMSTAT",(ctypes.Structure,),{"_fields_":[("fCtsHold",ctypes.wintypes.DWORD,1),("fDsrHold",ctypes.wintypes.DWORD,1),("fRlsdHold",ctypes.wintypes.DWORD,1),("fXoffHold",ctypes.wintypes.DWORD,1),("fXoffSent",ctypes.wintypes.DWORD,1),("fEof",ctypes.wintypes.DWORD,1),("fTxim",ctypes.wintypes.DWORD,1),("fReserved",ctypes.wintypes.DWORD,25),("cbInQue",ctypes.wintypes.DWORD),("cbOutQue",ctypes.wintypes.DWORD)]})
ctypes.wintypes.CONSOLE_CURSOR_INFO=type("CONSOLE_CURSOR_INFO",(ctypes.Structure,),{"_fields_":[("dwSize",ctypes.wintypes.DWORD),("bVisible",ctypes.wintypes.BOOL)]})
ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO=type("CONSOLE_SCREEN_BUFFER_INFO",(ctypes.Structure,),{"_fields_":[("dwSize",ctypes.wintypes._COORD),("dwCursorPosition",ctypes.wintypes._COORD),("wAttributes",ctypes.wintypes.WORD),("srWindow",ctypes.wintypes.SMALL_RECT),("dwMaximumWindowSize",ctypes.wintypes._COORD)]})
ctypes.wintypes.DCB=type("DCB",(ctypes.Structure,),{"_fields_":[("DCBlength",ctypes.wintypes.DWORD),("BaudRate",ctypes.wintypes.DWORD),("fBinary",ctypes.wintypes.DWORD,1),("fParity",ctypes.wintypes.DWORD,1),("fOutxCtsFlow",ctypes.wintypes.DWORD,1),("fOutxDsrFlow",ctypes.wintypes.DWORD,1),("fDtrControl",ctypes.wintypes.DWORD,2),("fDsrSensitivity",ctypes.wintypes.DWORD,1),("fTXContinueOnXoff",ctypes.wintypes.DWORD,1),("fOutX",ctypes.wintypes.DWORD,1),("fInX",ctypes.wintypes.DWORD,1),("fErrorChar",ctypes.wintypes.DWORD,1),("fNull",ctypes.wintypes.DWORD,1),("fRtsControl",ctypes.wintypes.DWORD,2),("fAbortOnError",ctypes.wintypes.DWORD,1),("fDummy2",ctypes.wintypes.DWORD,17),("wReserved",ctypes.wintypes.WORD),("XonLim",ctypes.wintypes.WORD),("XoffLim",ctypes.wintypes.WORD),("ByteSize",ctypes.wintypes.BYTE),("Parity",ctypes.wintypes.BYTE),("StopBits",ctypes.wintypes.BYTE),("XonChar",ctypes.c_char),("XoffChar",ctypes.c_char),("ErrorChar",ctypes.c_char),("EofChar",ctypes.c_char),("EvtChar",ctypes.c_char),("wReserved1",ctypes.wintypes.WORD)]})
ctypes.wintypes.GUID=type("GUID",(ctypes.Structure,),{"_fields_":[("Data1",ctypes.wintypes.DWORD),("Data2",ctypes.wintypes.WORD),("Data3",ctypes.wintypes.WORD),("Data4",ctypes.wintypes.BYTE*8)]})
ctypes.wintypes.KBDLLHOOKSTRUCT=type("KBDLLHOOKSTRUCT",(ctypes.Structure,),{"_fields_":[("vkCode",ctypes.wintypes.DWORD),("scanCode",ctypes.wintypes.DWORD),("flags",ctypes.wintypes.DWORD),("time",ctypes.c_int),("dwExtraInfo",ctypes.wintypes.ULONG_PTR)]})
ctypes.wintypes.LUID=type("LUID_",(ctypes.Structure,),{"_fields_":[("LowPart",ctypes.wintypes.DWORD),("HighPart",ctypes.wintypes.LONG)]})
ctypes.wintypes.LUID_AND_ATTRIBUTES=type("LUID_AND_ATTRIBUTES",(ctypes.Structure,),{"_fields_":[("Luid",ctypes.wintypes.LUID),("Attributes",ctypes.wintypes.DWORD)]})
ctypes.wintypes.MONITORINFO=type("MONITORINFO",(ctypes.Structure,),{"_fields_":[("cbSize",ctypes.wintypes.DWORD),("rcMonitor",ctypes.wintypes.RECT),("rcWork",ctypes.wintypes.RECT),("dwFlags",ctypes.wintypes.DWORD)]})
ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME=type("OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME",(ctypes.Structure,),{"_fields_":[("Offset",ctypes.wintypes.DWORD),("OffsetHigh",ctypes.wintypes.DWORD)]})
ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME=type("OVERLAPPED_DUMMYUNIONNAME",(ctypes.Union,),{"_fields_":[("_0",ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME),("Pointer",ctypes.wintypes.LPVOID)],"_anonymous_":["_0"]})
ctypes.wintypes.OVERLAPPED=type("OVERLAPPED",(ctypes.Structure,),{"_fields_":[("Internal",ctypes.wintypes.ULONG_PTR),("InternalHigh",ctypes.wintypes.ULONG_PTR),("_0",ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME),("hEvent",ctypes.wintypes.HANDLE)],"_anonymous_":["_0"]})
ctypes.wintypes.PROCESS_INFORMATION=type("PROCESS_INFORMATION",(ctypes.Structure,),{"_fields_":[("hProcess",ctypes.wintypes.HANDLE),("hThread",ctypes.wintypes.HANDLE),("dwProcessId",ctypes.wintypes.DWORD),("dwThreadId",ctypes.wintypes.DWORD)]})
ctypes.wintypes.SECURITY_ATTRIBUTES=type("SECURITY_ATTRIBUTES",(ctypes.Structure,),{"_fields_":[("nLength",ctypes.wintypes.DWORD),("lpSecurityDescriptor",ctypes.wintypes.LPVOID),("bInheritHandle",ctypes.wintypes.BOOL)]})
ctypes.wintypes.SP_DEVINFO_DATA=type("SP_DEVINFO_DATA",(ctypes.Structure,),{"_fields_":[("cbSize",ctypes.wintypes.DWORD),("ClassGuid",ctypes.wintypes.GUID),("DevInst",ctypes.wintypes.DWORD),("Reserved",ctypes.wintypes.ULONG_PTR)]})
ctypes.wintypes.STARTUPINFOW=type("STARTUPINFOW",(ctypes.Structure,),{"_fields_":[("cb",ctypes.wintypes.DWORD),("lpReserved",ctypes.wintypes.LPWSTR),("lpDesktop",ctypes.wintypes.LPWSTR),("lpTitle",ctypes.wintypes.LPWSTR),("dwX",ctypes.wintypes.DWORD),("dwY",ctypes.wintypes.DWORD),("dwXSize",ctypes.wintypes.DWORD),("dwYSize",ctypes.wintypes.DWORD),("dwXCountChars",ctypes.wintypes.DWORD),("dwYCountChars",ctypes.wintypes.DWORD),("dwFillAttribute",ctypes.wintypes.DWORD),("dwFlags",ctypes.wintypes.DWORD),("wShowWindow",ctypes.wintypes.WORD),("cbReserved2",ctypes.wintypes.WORD),("lpReserved2",ctypes.wintypes.LPBYTE),("hStdInput",ctypes.wintypes.HANDLE),("hStdOutput",ctypes.wintypes.HANDLE),("hStdError",ctypes.wintypes.HANDLE)]})
ctypes.wintypes.TOKEN_PRIVILEGES=type("TOKEN_PRIVILEGES",(ctypes.Structure,),{"_fields_":[("PrivilegeCount",ctypes.wintypes.DWORD),("Privileges",ctypes.wintypes.LUID_AND_ATTRIBUTES*1)]})
ctypes.wintypes.WNDCLASSEXW=type("WNDCLASSEXW",(ctypes.Structure,),{"_fields_":[("cbSize",ctypes.wintypes.UINT),("style",ctypes.wintypes.UINT),("lpfnWndProc",ctypes.wintypes.WNDPROC),("cbClsExtra",ctypes.c_int),("cbWndExtra",ctypes.c_int),("hInstance",ctypes.wintypes.HINSTANCE),("hIcon",ctypes.wintypes.HICON),("hCursor",ctypes.wintypes.HCURSOR),("hbrBackground",ctypes.wintypes.HBRUSH),("lpszMenuName",ctypes.wintypes.LPCWSTR),("lpszClassName",ctypes.wintypes.LPCWSTR),("hIconSm",ctypes.wintypes.HICON)]})
ctypes.wintypes.LPCOMMTIMEOUTS=ctypes.POINTER(ctypes.wintypes.COMMTIMEOUTS)
ctypes.wintypes.LPCOMSTAT=ctypes.POINTER(ctypes.wintypes.COMSTAT)
ctypes.wintypes.LPDCB=ctypes.POINTER(ctypes.wintypes.DCB)
ctypes.wintypes.LPMONITORINFO=ctypes.POINTER(ctypes.wintypes.MONITORINFO)
ctypes.wintypes.LPOVERLAPPED=ctypes.POINTER(ctypes.wintypes.OVERLAPPED)
ctypes.wintypes.LPPROCESS_INFORMATION=ctypes.POINTER(ctypes.wintypes.PROCESS_INFORMATION)
ctypes.wintypes.LPSECURITY_ATTRIBUTES=ctypes.POINTER(ctypes.wintypes.SECURITY_ATTRIBUTES)
ctypes.wintypes.LPSTARTUPINFOW=ctypes.POINTER(ctypes.wintypes.STARTUPINFOW)
ctypes.wintypes.OPT_PSMALL_RECT=ctypes.c_void_p
ctypes.wintypes.PCHAR_INFO=ctypes.POINTER(ctypes.wintypes.CHAR_INFO)
ctypes.wintypes.PCONSOLE_CURSOR_INFO=ctypes.POINTER(ctypes.wintypes.CONSOLE_CURSOR_INFO)
ctypes.wintypes.PCONSOLE_SCREEN_BUFFER_INFO=ctypes.POINTER(ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO)
ctypes.wintypes.PGUID=ctypes.POINTER(ctypes.wintypes.GUID)
ctypes.wintypes.PHANDLE=ctypes.POINTER(ctypes.wintypes.HANDLE)
ctypes.wintypes.PHHOOK=ctypes.POINTER(ctypes.wintypes.HHOOK)
ctypes.wintypes.PLUID=ctypes.POINTER(ctypes.wintypes.LUID)
ctypes.wintypes.PSMALL_RECT=ctypes.POINTER(ctypes.wintypes.SMALL_RECT)
ctypes.wintypes.PSP_DEVINFO_DATA=ctypes.POINTER(ctypes.wintypes.SP_DEVINFO_DATA)
ctypes.wintypes.PTOKEN_PRIVILEGES=ctypes.POINTER(ctypes.wintypes.TOKEN_PRIVILEGES)
ctypes.wintypes.PWNDCLASSEXW=ctypes.POINTER(ctypes.wintypes.WNDCLASSEXW)



advapi32=ctypes.windll.advapi32
gdi32=ctypes.windll.gdi32
kernel32=ctypes.windll.kernel32
move_to_desktop=ctypes.windll.LoadLibrary(__file_base_dir__+MOVE_TO_DESKTOP_LIBRARY_PATH)
setupapi=ctypes.windll.setupapi
shcore=ctypes.windll.shcore
shell32=ctypes.windll.shell32
user32=ctypes.windll.user32
advapi32.AdjustTokenPrivileges.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.BOOL,ctypes.wintypes.PTOKEN_PRIVILEGES,ctypes.wintypes.DWORD,ctypes.wintypes.PTOKEN_PRIVILEGES,ctypes.wintypes.PDWORD)
advapi32.AdjustTokenPrivileges.restype=ctypes.wintypes.BOOL
advapi32.LookupPrivilegeValueW.argtypes=(ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.PLUID)
advapi32.LookupPrivilegeValueW.restype=ctypes.wintypes.BOOL
advapi32.OpenProcessToken.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD,ctypes.wintypes.PHANDLE)
advapi32.OpenProcessToken.restype=ctypes.wintypes.BOOL
advapi32.RegCloseKey.argtypes=(ctypes.wintypes.HKEY,)
advapi32.RegCloseKey.restype=ctypes.wintypes.LONG
advapi32.RegQueryValueExW.argtypes=(ctypes.wintypes.HKEY,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPDWORD,ctypes.c_void_p,ctypes.wintypes.LPDWORD)
advapi32.RegQueryValueExW.restype=ctypes.wintypes.LONG
gdi32.CreateSolidBrush.argtypes=(ctypes.wintypes.COLORREF,)
gdi32.CreateSolidBrush.restype=ctypes.wintypes.HBRUSH
kernel32.CancelIoEx.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPOVERLAPPED)
kernel32.CancelIoEx.restype=ctypes.wintypes.BOOL
kernel32.ClearCommError.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPCOMSTAT)
kernel32.ClearCommError.restype=ctypes.wintypes.BOOL
kernel32.CloseHandle.argtypes=(ctypes.wintypes.HANDLE,)
kernel32.CloseHandle.restype=ctypes.wintypes.BOOL
kernel32.CreateEventW.argtypes=(ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.BOOL,ctypes.wintypes.BOOL,ctypes.wintypes.LPCWSTR)
kernel32.CreateEventW.restype=ctypes.wintypes.HANDLE
kernel32.CreateFileW.argtypes=(ctypes.wintypes.LPCWSTR,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.HANDLE)
kernel32.CreateFileW.restype=ctypes.wintypes.HANDLE
kernel32.CreatePipe.argtypes=(ctypes.wintypes.PHANDLE,ctypes.wintypes.PHANDLE,ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.DWORD)
kernel32.CreatePipe.restype=ctypes.wintypes.BOOL
kernel32.CreateProcessW.argtypes=(ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPWSTR,ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.LPSECURITY_ATTRIBUTES,ctypes.wintypes.BOOL,ctypes.wintypes.DWORD,ctypes.wintypes.LPVOID,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPSTARTUPINFOW,ctypes.wintypes.LPPROCESS_INFORMATION)
kernel32.CreateProcessW.restype=ctypes.wintypes.BOOL
kernel32.DuplicateHandle.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.HANDLE,ctypes.wintypes.HANDLE,ctypes.wintypes.PHANDLE,ctypes.wintypes.DWORD,ctypes.wintypes.BOOL,ctypes.wintypes.DWORD)
kernel32.DuplicateHandle.restype=ctypes.wintypes.BOOL
kernel32.ExitProcess.artypes=(ctypes.wintypes.UINT,)
kernel32.ExitProcess.restype=None
kernel32.FillConsoleOutputAttribute.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.WORD,ctypes.wintypes.DWORD,ctypes.wintypes._COORD,ctypes.wintypes.LPDWORD)
kernel32.FillConsoleOutputAttribute.restype=ctypes.wintypes.BOOL
kernel32.FillConsoleOutputCharacterA.argtypes=(ctypes.wintypes.HANDLE,ctypes.c_char,ctypes.wintypes.DWORD,ctypes.wintypes._COORD,ctypes.wintypes.LPDWORD)
kernel32.FillConsoleOutputCharacterA.restype=ctypes.wintypes.BOOL
kernel32.GetCommState.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDCB)
kernel32.GetCommState.restype=ctypes.wintypes.BOOL
kernel32.GetCommTimeouts.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPCOMMTIMEOUTS)
kernel32.GetCommTimeouts.restype=ctypes.wintypes.BOOL
kernel32.GetConsoleCursorInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PCONSOLE_CURSOR_INFO)
kernel32.GetConsoleCursorInfo.restype=ctypes.wintypes.BOOL
kernel32.GetConsoleScreenBufferInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PCONSOLE_SCREEN_BUFFER_INFO)
kernel32.GetConsoleScreenBufferInfo.restype=ctypes.wintypes.BOOL
kernel32.GetConsoleWindow.argtypes=tuple()
kernel32.GetConsoleWindow.restype=ctypes.wintypes.HWND
kernel32.GetExitCodeProcess.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDWORD)
kernel32.GetExitCodeProcess.restype=ctypes.wintypes.BOOL
kernel32.GetLastError.argtypes=tuple()
kernel32.GetLastError.restype=ctypes.wintypes.DWORD
kernel32.GetModuleHandleW.argtypes=(ctypes.wintypes.LPCWSTR,)
kernel32.GetModuleHandleW.restype=ctypes.wintypes.HMODULE
kernel32.GetOverlappedResult.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPOVERLAPPED,ctypes.wintypes.LPDWORD,ctypes.wintypes.BOOL)
kernel32.GetOverlappedResult.restype=ctypes.wintypes.BOOL
kernel32.GetStdHandle.argtypes=(ctypes.wintypes.DWORD,)
kernel32.GetStdHandle.restype=ctypes.wintypes.HANDLE
kernel32.PurgeComm.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD)
kernel32.PurgeComm.restype=ctypes.wintypes.BOOL
kernel32.ReadFile.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPVOID,ctypes.wintypes.DWORD,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPOVERLAPPED)
kernel32.ReadFile.restype=ctypes.wintypes.BOOL
kernel32.ResetEvent.argtypes=(ctypes.wintypes.HANDLE,)
kernel32.ResetEvent.restype=ctypes.wintypes.BOOL
kernel32.ScrollConsoleScreenBufferW.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PSMALL_RECT,ctypes.wintypes.OPT_PSMALL_RECT,ctypes.wintypes._COORD,ctypes.wintypes.PCHAR_INFO)
kernel32.ScrollConsoleScreenBufferW.restype=ctypes.wintypes.BOOL
kernel32.SetCommMask.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD)
kernel32.SetCommMask.restype=ctypes.wintypes.BOOL
kernel32.SetCommState.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDCB)
kernel32.SetCommState.restype=ctypes.wintypes.BOOL
kernel32.SetCommTimeouts.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPCOMMTIMEOUTS)
kernel32.SetCommTimeouts.restype=ctypes.wintypes.BOOL
kernel32.SetConsoleCursorInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PCONSOLE_CURSOR_INFO)
kernel32.SetConsoleCursorInfo.restype=ctypes.wintypes.BOOL
kernel32.SetConsoleCursorPosition.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes._COORD)
kernel32.SetConsoleCursorPosition.restype=ctypes.wintypes.BOOL
kernel32.SetConsoleMode.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD)
kernel32.SetConsoleMode.restype=ctypes.wintypes.BOOL
kernel32.SetConsoleScreenBufferSize.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes._COORD)
kernel32.SetConsoleScreenBufferSize.restype=ctypes.wintypes.BOOL
kernel32.SetConsoleTitleW.argtypes=(ctypes.wintypes.LPCWSTR,)
kernel32.SetConsoleTitleW.restype=ctypes.wintypes.BOOL
kernel32.SetConsoleWindowInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.BOOL,ctypes.wintypes.PSMALL_RECT)
kernel32.SetConsoleWindowInfo.restype=ctypes.wintypes.BOOL
kernel32.SetFileAttributesW.argtypes=(ctypes.wintypes.LPCWSTR,ctypes.wintypes.DWORD)
kernel32.SetFileAttributesW.restype=ctypes.wintypes.BOOL
kernel32.SetupComm.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD)
kernel32.SetupComm.restype=ctypes.wintypes.BOOL
kernel32.WaitForSingleObject.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD)
kernel32.WaitForSingleObject.restype=ctypes.wintypes.DWORD
kernel32.WriteFile.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPCVOID,ctypes.wintypes.DWORD,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPOVERLAPPED)
kernel32.WriteFile.restype=ctypes.wintypes.BOOL
move_to_desktop.move_to_desktop.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.UINT)
move_to_desktop.move_to_desktop.restype=ctypes.wintypes.BOOL
move_to_desktop.switch_to_desktop.argtypes=(ctypes.wintypes.UINT,)
move_to_desktop.switch_to_desktop.restype=ctypes.wintypes.BOOL
setupapi.SetupDiClassGuidsFromNameW.argtypes=(ctypes.wintypes.PCWSTR,ctypes.wintypes.PGUID,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD)
setupapi.SetupDiClassGuidsFromNameW.restype=ctypes.wintypes.BOOL
setupapi.SetupDiDestroyDeviceInfoList.argtypes=(ctypes.wintypes.HDEVINFO,)
setupapi.SetupDiDestroyDeviceInfoList.restype=ctypes.wintypes.BOOL
setupapi.SetupDiEnumDeviceInfo.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.DWORD,ctypes.wintypes.PSP_DEVINFO_DATA)
setupapi.SetupDiEnumDeviceInfo.restype=ctypes.wintypes.BOOL
setupapi.SetupDiGetClassDevsW.argtypes=(ctypes.wintypes.PGUID,ctypes.wintypes.PCWSTR,ctypes.wintypes.HWND,ctypes.wintypes.DWORD)
setupapi.SetupDiGetClassDevsW.restype=ctypes.wintypes.HDEVINFO
setupapi.SetupDiGetDeviceRegistryPropertyW.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.PSP_DEVINFO_DATA,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD,ctypes.c_void_p,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD)
setupapi.SetupDiGetDeviceRegistryPropertyW.restype=ctypes.wintypes.BOOL
setupapi.SetupDiOpenDevRegKey.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.PSP_DEVINFO_DATA,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD)
setupapi.SetupDiOpenDevRegKey.restype=ctypes.wintypes.HKEY
shcore.SetProcessDpiAwareness.argtypes=(ctypes.wintypes.PROCESS_DPI_AWARENESS,)
shcore.SetProcessDpiAwareness.restype=ctypes.wintypes.HRESULT
shell32.ShellExecuteW.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.INT)
shell32.ShellExecuteW.restype=ctypes.wintypes.HINSTANCE
user32.CallNextHookEx.argtypes=(ctypes.wintypes.PHHOOK,ctypes.c_int,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
user32.CallNextHookEx.restype=ctypes.wintypes.LRESULT
user32.CreateWindowExW.argtypes=(ctypes.wintypes.DWORD,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.DWORD,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.wintypes.HWND,ctypes.wintypes.HMENU,ctypes.wintypes.HINSTANCE,ctypes.wintypes.LPVOID)
user32.CreateWindowExW.restype=ctypes.wintypes.HWND
user32.DefWindowProcW.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.UINT,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
user32.DefWindowProcW.restype=ctypes.wintypes.LRESULT
user32.DestroyWindow.argtypes=(ctypes.wintypes.HWND,)
user32.DestroyWindow.restype=ctypes.wintypes.BOOL
user32.DispatchMessageW.argtypes=(ctypes.wintypes.LPMSG,)
user32.DispatchMessageW.restype=ctypes.wintypes.LRESULT
user32.ExitWindowsEx.argtypes=(ctypes.wintypes.UINT,ctypes.wintypes.DWORD)
user32.ExitWindowsEx.restype=ctypes.wintypes.BOOL
user32.GetAsyncKeyState.artypes=(ctypes.c_int,)
user32.GetAsyncKeyState.restype=ctypes.wintypes.SHORT
user32.GetMessageW.argtypes=(ctypes.wintypes.LPMSG,ctypes.wintypes.HWND,ctypes.c_uint,ctypes.c_uint)
user32.GetMessageW.restype=ctypes.wintypes.BOOL
user32.GetMonitorInfoW.argtypes=(ctypes.wintypes.HMONITOR,ctypes.wintypes.LPMONITORINFO)
user32.GetMonitorInfoW.restype=ctypes.wintypes.BOOL
user32.LoadImageW.argtypes=(ctypes.wintypes.HINSTANCE,ctypes.wintypes.LPCWSTR,ctypes.c_uint,ctypes.c_int,ctypes.c_int,ctypes.c_uint)
user32.LoadImageW.restype=ctypes.wintypes.HANDLE
user32.MessageBoxW.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.c_uint)
user32.MessageBoxW.restype=ctypes.c_int
user32.MonitorFromWindow.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.DWORD)
user32.MonitorFromWindow.restype=ctypes.wintypes.HMONITOR
user32.PostMessageW.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.UINT,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
user32.PostMessageW.restype=ctypes.wintypes.BOOL
user32.RegisterClassExW.argtypes=(ctypes.wintypes.PWNDCLASSEXW,)
user32.RegisterClassExW.restype=ctypes.wintypes.ATOM
user32.SendMessageW.argtypes=(ctypes.wintypes.HWND,ctypes.c_uint,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
user32.SendMessageW.restype=ctypes.wintypes.LRESULT
user32.SetWindowLongPtrW.argtypes=(ctypes.wintypes.HWND,ctypes.c_int,ctypes.wintypes.LONG_PTR)
user32.SetWindowLongPtrW.restype=ctypes.wintypes.LONG_PTR
user32.SetWindowPos.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.HWND,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.c_int,ctypes.wintypes.UINT)
user32.SetWindowPos.restype=ctypes.wintypes.BOOL
user32.SetWindowsHookExW.argtypes=(ctypes.c_int,ctypes.wintypes.LowLevelKeyboardProc,ctypes.wintypes.HINSTANCE,ctypes.wintypes.DWORD)
user32.SetWindowsHookExW.restype=ctypes.wintypes.HHOOK
user32.ShowCursor.argtypes=(ctypes.wintypes.BOOL,)
user32.ShowCursor.restype=ctypes.c_int
user32.TranslateMessage.argtypes=(ctypes.wintypes.LPMSG,)
user32.TranslateMessage.restype=ctypes.wintypes.BOOL
user32.UnhookWindowsHookEx.argtypes=(ctypes.wintypes.HHOOK,)
user32.UnhookWindowsHookEx.restype=ctypes.wintypes.BOOL
user32.UnregisterClassW.argtypes=(ctypes.wintypes.LPCWSTR,ctypes.wintypes.HINSTANCE)
user32.UnregisterClassW.restype=ctypes.wintypes.BOOL



def _print(*a,df=False):
	a=" ".join([str(e) for e in a])
	if (df is False):
		i=0
		while (i<len(a)):
			m=REMOVE_COLOR_FORMATTING_REGEX.match(a[i:])
			if (m is not None):
				i+=len(m.group(0))
			if (a[i] in "'-" or i==0 or a[i-1] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"):
				m=PRINT_ADD_COLOR_REGEX.match(a[i:])
				if (m is not None):
					if (m.group(0)[0]=="'"):
						o=f"\x1b[38;2;91;216;38m{m.group(0)}\x1b[0m"
					elif (m.group(0)[0] in "-0123456789" and (m.end(0)==1 or m.group(0)[1:].isnumeric())):
						o=f"\x1b[38;2;48;109;206m{m.group(0)}\x1b[0m"
					elif (m.group(0)[0] in "-0123456789" and m.group(0)[-1]=="%"):
						o=f"\x1b[38;2;245;103;245m{m.group(0)}\x1b[0m"
					else:
						o=f"\x1b[38;2;227;204;59m{m.group(0)}\x1b[0m"
					a=a[:i]+o+a[i+len(m[0]):]
					i+=len(o)-1
			i+=1
	tm=time.time()+UTC_OFFSET
	t=f"\x1b[38;2;50;50;50m[{str(int((tm//3600)%24)).rjust(2,'0')}:{str(int((tm//60)%60)).rjust(2,'0')}:{str(int(tm%60)).rjust(2,'0')}]\x1b[0m "
	sys.__stdout__.write(t+a.replace("\n","\n"+" "*len(REMOVE_COLOR_FORMATTING_REGEX.sub(r"",t)))+"\x1b[0m\n")



def _sha1_chunk(h,dt):
	w=[]
	for i in range(0,64,4):
		w.append((dt[i]<<24)|(dt[i+1]<<16)|(dt[i+2]<<8)|dt[i+3])
	for i in range(16,80):
		v=w[i-3]^w[i-8]^w[i-14]^w[i-16]
		w.append(((v<<1)|(v>>31))&0xffffffff)
	a,b,c,d,e=h
	for i in range(80):
		if (i<20):
			f=d^(b&c)^(b&d)
			k=0x5a827999
		elif (i<40):
			f=b^c^d
			k=0x6ed9eba1
		elif (i<60):
			f=(b&c)|(b&d)|(c&d)
			k=0x8f1bbcdc
		else:
			f=b^c^d
			k=0xca62c1d6
		a,b,c,d,e=(((((a<<5)|(a>>27))&0xffffffff)+f+e+k+w[i])&0xffffffff,a,((b<<30)|(b>>2))&0xffffffff,c,d)
	return [(h[0]+a)&0xffffffff,(h[1]+b)&0xffffffff,(h[2]+c)&0xffffffff,(h[3]+d)&0xffffffff,(h[4]+e)&0xffffffff]



def _encode_json_str(m):
	c=ord(m.group(0))
	if (c<JSON_STRING_MIN_SURROGATE_PAIR):
		return f"\\u{c:04x}"
	c-=JSON_STRING_MIN_SURROGATE_PAIR
	return f"\\u{0xd800|((c>>10)&0x3ff):04x}\\u{0xdc00|(c&0x3ff):04x}"



def _encode_json_str_bytes(m):
	c=ord(m.group(0))
	if (c<JSON_STRING_MIN_SURROGATE_PAIR):
		return bytes(f"\\u{c:04x}","utf-8")
	c-=JSON_STRING_MIN_SURROGATE_PAIR
	return bytes(f"\\u{0xd800|((c>>10)&0x3ff):04x}\\u{0xdc00|(c&0x3ff):04x}","utf-8")



def _encode_json(e):
	if (type(e)==dict):
		return "{"+",".join(["\""+(JSON_STRING_ESCAPE_CHAR_REGEX.sub(_encode_json_str,k) if type(k)==str else JSON_STRING_ESCAPE_CHAR_BYTES_REGEX.sub(_encode_json_str_bytes,k).decode("utf-8"))+"\":"+_encode_json(v) for k,v in e.items()])+"}"
	elif (type(e)==list or type(e)==tuple):
		return "["+",".join([_encode_json(k) for k in e])+"]"
	elif (type(e)==str):
		return "\""+JSON_STRING_ESCAPE_CHAR_REGEX.sub(_encode_json_str,e)+"\""
	elif (type(e)==bytes):
		return "\""+JSON_STRING_ESCAPE_CHAR_BYTES_REGEX.sub(_encode_json_str_bytes,e).decode("utf-8")+"\""
	elif (type(e)==int or type(e)==float):
		return str(e)
	elif (e is True):
		return "true"
	elif (e is False):
		return "false"
	elif (e is None):
		return "null"
	else:
		raise RuntimeError(f"Unable to Serialize Type '{e.__class__.__name__}'")



def _decode_json_str(e):
	i=0
	o=""
	while (e[i]!="\""):
		if (e[i]!="\\"):
			o+=e[i]
		else:
			i+=1
			if (e[i] in ["\\'\""]):
				o+=chr(e[i])
			elif (e[i]=="b"):
				o+="\b"
			elif (e[i]=="f"):
				o+="\f"
			elif (e[i]=="n"):
				o+="\n"
			elif (e[i]=="r"):
				o+="\r"
			elif (e[i]=="t"):
				o+="\t"
			elif (e[i]=="v"):
				o+="\v"
			elif (e[i]=="x"):
				v=0
				i+=1
				for _ in range(0,2):
					v=v*16+(ord(e[i])-48 if ord(e[i])>47 and ord(e[i])<58 else (ord(e[i])-55 if ord(e[i])>64 and ord(e[i])<71 else ord(e[i])-87))
					i+=1
				o+=chr(v)
				continue
			elif (e[i]==b"u"):
				v=0
				i+=1
				for _ in range(0,4):
					v=v*16+(ord(e[i])-48 if ord(e[i])>47 and ord(e[i])<58 else (ord(e[i])-55 if ord(e[i])>64 and ord(e[i])<71 else ord(e[i])-87))
					i+=1
				o+=chr(v)
				continue
			else:
				v=0
				while (ord(e[i])>47 and ord(e[i])<56):
					v=v*8+(ord(e[i])-48)
					i+=1
				o+=chr(v)
				continue
		i+=1
	return (o,i)



def _decode_json(e):
	if (e[0]=="{"):
		o={}
		i=1
		while (e[i]!="}"):
			while (e[i-1]!="\""):
				i+=1
			k,j=_decode_json_str(e[i:])
			i+=j+1
			while (e[i-1]!=":"):
				i+=1
			v,j=_decode_json(e[i:])
			o[k]=v
			i+=j
			while (e[i-1]!=","):
				if (e[i]=="}"):
					break
				i+=1
		return (o,i)
	if (e[0]=="["):
		o=[]
		i=1
		while (e[i]!="]"):
			k,j=_decode_json(e[i:])
			i+=j
			o.append(k)
			while (e[i-1]!=","):
				if (e[i]=="]"):
					break
				i+=1
		return (o,i)
	if (e[0]=="\"" or e[0]=="'"):
		o,i=_decode_json_str(e[1:])
		return (o,i+1)
	if (e[:4]=="true"):
		return (True,4)
	if (e[:5]=="false"):
		return (False,5)
	if (e[:4]=="null"):
		return (None,4)
	s=1
	i=0
	if (e[0]=="-"):
		s=-1
		i=1
	o=0
	while (ord(e[i])>47 and ord(e[i])<58):
		o=o*10+(ord(e[i])-48)
		i+=1
	if (e[i]=="."):
		pw=0.1
		i+=1
		while (ord(e[i])>47 and ord(e[i])<58):
			o+=pw*(ord(e[i])-48)
			pw*=0.1
			i+=1
		if (e[i]=="e"):
			i+=1
			pw_s=1
			if (e[i]=="-"):
				pw_s=-1
				i+=1
			pw=0
			while (ord(e[i])>47 and ord(e[i])<58):
				pw=pw*10+(ord(e[i])-48)
				i+=1
			o*=pow(10,pw*pw_s)
	o*=s
	return (o,i-1)



def _create_gitignore_pattern(p):
	p=p.replace("\\","/").lower()
	ol=[]
	i=0
	while (i<len(p)):
		c=p[i]
		i+=1
		if (c=="*"):
			if (len(ol)==0 or ol[-1] is not None):
				ol.append(None)
		elif (c=="?"):
			ol.append(r".")
		elif (c=="["):
			j=i
			if (j<len(p) and p[j]=="!"):
				j+=1
			if (j<len(p) and p[j]=="]"):
				j+=1
			while (j<len(p) and p[j]!="]"):
				j+=1
			if (j>=len(p)):
				ol.append(r"\\[")
			else:
				l=p[i:j]
				if ("--" in l):
					cl=[]
					k=(i+2 if p[i]=="!" else i+1)
					while (True):
						k=p[k:j].find("-")
						if (k==-1):
							break
						cl.append(p[i:k])
						i+=1
						k+=3
					cl.append(p[i:j])
					l="-".join([e.replace("\\","\\\\").replace("-","\\-") for e in cl])
				else:
					l=l.replace("\\","\\\\")
				l=GITIGNORE_SPECIAL_SET_CHARCTERS_REGEX.sub(r"\\\1",l)
				i=j+1
				if (l[0]=='!'):
					ol.append(fr"[^{l[1:]}]")
				elif (l[0] in ("^","[")):
					ol.append(fr"[{chr(92)+l}]")
				else:
					ol.append(fr"[{l}]")
		else:
			ol.append(re.escape(c))
	o=""
	i=0
	while (i<len(ol) and ol[i] is not None):
		o+=ol[i]
		i+=1
	j=0
	while (i<len(ol)):
		i+=1
		if (i==len(ol)):
			o+=r".*"
			break
		l=""
		while (i<len(ol) and ol[i] is not None):
			l+=ol[i]
			i+=1
		if (i==len(ol)):
			o+=r".*"+l
		else:
			o+=fr"(?=(?P<_tmp_{j}>.*?{l}))(?P=_tmp_{j})"
			j+=1
	return re.compile(fr"{o}\Z",re.S)



def _match_gitignore_path(gdt,fp):
	fnm=fp.lower().replace("\\","/").split("/")
	ig=False
	for p in gdt:
		if ((ig is False or p[0] is True)):
			if (len(fnm)<len(p[1])):
				continue
			if (len(p[1][0].pattern)==2):
				ok=True
				for r,sfnm in zip(p[1],fnm):
					if (r.match(sfnm) is None):
						ok=False
						break
				if (ok is False):
					continue
			else:
				ok=False
				for i in range(0,len(fnm)-len(p[1])+1):
					for r,sfnm in zip(p[1],fnm[i:]):
						if (r.match(sfnm) is None):
							break
					else:
						ok=True
						break
				if (ok is False):
					continue
			if (p[0] is True):
				return False
			ig=True
	if (ig is True):
		return True
	return False



def _is_binary(fp):
	with open(fp,"rb") as f:
		dt=f.read(4096)
	if (len(dt)==0):
		return False
	r1=len(dt.translate(None,b"\b\t\n\f\r !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"))/len(dt)
	r2=len(dt.translate(None,bytes(range(127,256))))/len(dt)
	if (r1>0.9 and r2>0.9):
		return True
	enc_u=True
	try:
		dt.decode(encoding="utf-8")
	except UnicodeDecodeError:
		enc_u=False
	if ((r1>0.3 and r2<0.05) or (r1>0.8 and r2>0.8)):
		return (False if enc_u is True else True)
	else:
		return (True if enc_u is False and (b"\x00" in dt or b"\xff" in dt) else False)



def _github_api_request(m,**kw):
	kw["headers"]={**kw.get("headers",{}),"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Update API"}
	r=getattr(requests,m)(**kw)
	if ("X-RateLimit-Remaining" in r.headers.keys() and r.headers["X-RateLimit-Remaining"]=="0"):
		print(r.headers)
		input()
		kernel32.ExitProcess(1)
	time.sleep(3600/GITHUB_API_QUOTA)
	o=r.json()
	if (type(o)==dict and "message" in o.keys() and o["message"]=="Server Error"):
		print(o)
		kernel32.ExitProcess(1)
	return o



def _get_project_tree(a_nm,r_nm,sha,p,o):
	_print(f"\x1b[38;2;100;100;100mReading Tree \x1b[38;2;65;118;46m'{p}'\x1b[38;2;100;100;100m...",df=True)
	for e in _github_api_request("get",url=f"https://api.github.com/repos/{a_nm}/{r_nm}/git/trees/{sha}")["tree"]:
		if (e["type"]=="tree"):
			_get_project_tree(a_nm,r_nm,e["sha"],p+"/"+e["path"],o)
		else:
			o[(p+"/"+e["path"])[2:]]={"sz":e["size"],"sha":e["sha"]}



def _push_single_project(p,b_nm):
	b_nm=b_nm.split("-")[0].title()+("" if b_nm.count("-")==0 else "-"+b_nm.split("-")[1].replace("_"," ").title().replace(" ","_"))
	nm=GITHUB_INVALID_NAME_CHARACTER_REGEX.sub(r"",b_nm)
	with open(__file_base_dir__+GITHUB_PROJECT_BRANCH_LIST_FILE_PATH,"r") as f:
		gr_dt={k.strip().split(":")[0]:k.strip().split(":")[1] for k in f.read().strip().split("\n") if len(k)>0}
	cr=False
	if (nm not in gr_dt):
		cr=True
		gr_dt[nm]=GITHUB_DEFAULT_BRANCH_NAME
		_print(f"\x1b[38;2;100;100;100mCreating Project \x1b[38;2;65;118;46m'{nm}'\x1b[38;2;100;100;100m...",df=True)
		try:
			_github_api_request("post",url="https://api.github.com/user/repos",data=_encode_json({"name":nm,"description":nm.replace("-"," - ")}))
		except requests.exceptions.ConnectionError:
			_print("\x1b[38;2;200;40;20mNo Internet Connection.\x1b[0m Quitting\x1b[38;2;100;100;100m...",df=True)
			return False
	a_nm=GITHUB_USERNAME
	if (os.path.exists(os.path.join(p,".gitrepo"))):
		_print(f"\x1b[38;2;100;100;100mParsing Gitrepo File...",df=True)
		with open(os.path.join(p,".gitrepo"),"r") as f:
			dt=f.read().strip().split(":")
		a_nm=dt[0].split("/")[0].strip()
		nm=dt[0].split("/")[1].strip()
		br=dt[1].strip()
		b_nm=nm
	else:
		br=gr_dt[nm]
	gdt=[]
	if (os.path.exists(os.path.join(p,".gitignore"))):
		_print(f"\x1b[38;2;100;100;100mParsing Gitignore File...",df=True)
		with open(os.path.join(p,".gitignore"),"r") as f:
			for ln in f.read().replace("\r\n","\n").split("\n"):
				if (ln.endswith("\n")):
					ln=ln[:-1]
				ln=ln.lstrip()
				if (not ln.startswith("#")):
					iv=False
					if (ln.startswith("!")):
						ln=ln[1:]
						iv=True
					while (ln.endswith(" ") and ln[-2:]!="\\ " and ln[-2:]!="/ "):
						ln=ln[:-1]
					ln=GITIGNORE_FILE_PATH_REGEX.sub(r"\1",ln)
					if (len(ln)>0):
						if ("**/" in ln):
							gdt.append([iv,tuple(_create_gitignore_pattern(e) for e in ln.replace("**/","").split("/"))])
						gdt.append([iv,tuple(_create_gitignore_pattern(e) for e in ln.split("/"))])
	c_tm=int(time.time())
	msg=time.strftime("Push Update %d/%m/%Y, %H:%M:%S",time.gmtime(c_tm+UTC_OFFSET))
	_print(f"\x1b[38;2;100;100;100mCommiting to Branch \x1b[38;2;65;118;46m'{a_nm}/{nm}:{br}'\x1b[38;2;100;100;100m with Message \x1b[38;2;65;118;46m'{msg}'\x1b[38;2;100;100;100m...",df=True)
	try:
		bt_sha=_github_api_request("get",url=f"https://api.github.com/repos/{a_nm}/{nm}/git/ref/heads/{br}")["object"]["sha"]
	except KeyError:
		_github_api_request("put",url=f"https://api.github.com/repos/{a_nm}/{nm}/contents/_",data=f"{{\"message\":\"{msg}\",\"content\":\"\"}}")
		bt_sha=_github_api_request("get",url=f"https://api.github.com/repos/{a_nm}/{nm}/git/ref/heads/{br}")["object"]["sha"]
	_print(f"\x1b[38;2;100;100;100mReading Recursive Tree...",df=True)
	t_dt=_github_api_request("get",url=f"https://api.github.com/repos/{a_nm}/{nm}/git/trees/{bt_sha}?recursive=true")
	r_t={}
	if (t_dt["truncated"]):
		_print(f"\x1b[38;2;118;42;38mRecursive Tree Truncated. \x1b[38;2;100;100;100mFalling Back to Standard Tree...",df=True)
		_get_project_tree(a_nm,nm,bt_sha,".",r_t)
	else:
		_print(f"\x1b[38;2;100;100;100mFound Tree \x1b[38;2;65;118;46m'.'\x1b[38;2;100;100;100m...",df=True)
		for k in t_dt["tree"]:
			if (k["type"]=="blob"):
				r_t[k["path"]]={"sz":k["size"],"sha":k["sha"]}
			else:
				_print(f"\x1b[38;2;100;100;100mFound Tree \x1b[38;2;65;118;46m'./{k['path']}'\x1b[38;2;100;100;100m...",df=True)
	_print(f"\x1b[38;2;100;100;100mCreating Commit...",df=True)
	bl=[]
	cnt=[0,0,0,0]
	p=os.path.abspath(p).replace("\\","/").rstrip("/")+"/"
	for r,_,fl in os.walk(p):
		r=r.replace("\\","/").rstrip("/")+"/"
		for f in fl:
			if (r==p and f==".gitrepo"):
				continue
			fp=r[len(p):]+f
			if (_match_gitignore_path(gdt,fp) is True):
				cnt[2]+=1
				_print(f"\x1b[38;2;190;0;220m! {b_nm}/{fp}\x1b[0m",df=True)
				continue
			f_sz=os.stat(r+f).st_size
			if (fp in list(r_t.keys())):
				if (_is_binary(r+f) is False):
					try:
						with open(r+f,"r",encoding="cp1252") as rf:
							h=SHA1_START_VALUE.copy()
							dt=rf.read().replace("\r\n","\n")
							if (len(dt)==r_t[fp]["sz"]):
								dt=f"blob {len(dt)}\x00{dt}".encode("cp1252")
								l=len(dt)
								dt+=b"\x80"+b"\x00"*((56-(l+1)%64)%64)+bytes([l>>53,(l>>45)&0xff,(l>>37)&0xff,(l>>29)&0xff,(l>>21)&0xff,(l>>13)&0xff,(l>>5)&0xff,(l<<3)&0xff])
								i=0
								while (i<len(dt)):
									h=_sha1_chunk(h,dt[i:i+64])
									i+=64
								if (f"{h[0]:08x}{h[1]:08x}{h[2]:08x}{h[3]:08x}{h[4]:08x}"==r_t[fp]["sha"]):
									cnt[1]+=1
									bl.append([fp,None])
									_print(f"\x1b[38;2;230;210;40m? {b_nm}/{fp}\x1b[0m",df=True)
									continue
					except UnicodeDecodeError:
						if (f_sz==r_t[fp]["sz"]):
							_print(f"\x1b[38;2;100;100;100mHashing Binary File \x1b[38;2;65;118;46m'{fp}'\x1b[38;2;100;100;100m ({f_sz} bytes)...",df=True)
							with open(r+f,"rb") as rf:
								h=SHA1_START_VALUE.copy()
								dt=f"blob {f_sz}\x00".encode("cp1252")+rf.read()
								l=len(dt)
								dt+=b"\x80"+b"\x00"*((56-(l+1)%64)%64)+bytes([l>>53,(l>>45)&0xff,(l>>37)&0xff,(l>>29)&0xff,(l>>21)&0xff,(l>>13)&0xff,(l>>5)&0xff,(l<<3)&0xff])
								i=0
								while (i<len(dt)):
									h=_sha1_chunk(h,dt[i:i+64])
									i+=64
								if (f"{h[0]:08x}{h[1]:08x}{h[2]:08x}{h[3]:08x}{h[4]:08x}"==r_t[fp]["sha"]):
									cnt[1]+=1
									bl.append([fp,None])
									_print(f"\x1b[38;2;230;210;40m? {b_nm}/{fp}\x1b[0m",df=True)
									continue
				elif (f_sz==r_t[fp]["sz"]):
					_print(f"\x1b[38;2;100;100;100mHashing Binary File \x1b[38;2;65;118;46m'{fp}'\x1b[38;2;100;100;100m ({f_sz} bytes)...",df=True)
					with open(r+f,"rb") as rf:
						h=SHA1_START_VALUE.copy()
						dt=f"blob {f_sz}\x00".encode("cp1252")+rf.read()
						l=len(dt)
						dt+=b"\x80"+b"\x00"*((56-(l+1)%64)%64)+bytes([l>>53,(l>>45)&0xff,(l>>37)&0xff,(l>>29)&0xff,(l>>21)&0xff,(l>>13)&0xff,(l>>5)&0xff,(l<<3)&0xff])
						i=0
						while (i<len(dt)):
							h=_sha1_chunk(h,dt[i:i+64])
							i+=64
						if (f"{h[0]:08x}{h[1]:08x}{h[2]:08x}{h[3]:08x}{h[4]:08x}"==r_t[fp]["sha"]):
							cnt[1]+=1
							bl.append([fp,None])
							_print(f"\x1b[38;2;230;210;40m? {b_nm}/{fp}\x1b[0m",df=True)
							continue
			cnt[0]+=1
			_print(f"\x1b[38;2;70;210;70m+ {b_nm}/{fp}\x1b[0m",df=True)
			dt=f"File too Large (size = {f_sz} b)"
			b_sha=False
			if (os.stat(r+f).st_size<=GITHUB_MAX_FILE_SIZE):
				b64=True
				if (_is_binary(r+f) is False):
					try:
						with open(r+f,"r",encoding="utf-8") as rbf:
							dt=rbf.read().replace("\r\n","\n")
						b64=False
					except UnicodeDecodeError:
						pass
				if (b64 is True):
					if (len(dt)*4//3>GITHUB_MAX_FILE_SIZE):
						b_sha=False
					else:
						b_sha=True
						with open(r+f,"rb") as rbf:
							dt="{\"content\":\""
							i=0
							b_dt=rbf.read()
							while (i<len(b_dt)-2):
								dt+=BASE64_ALPHABET[b_dt[i]>>2]+BASE64_ALPHABET[((b_dt[i]<<4)&0x3f)|(b_dt[i+1]>>4)]+BASE64_ALPHABET[((b_dt[i+1]<<2)&0x3f)|(b_dt[i+2]>>6)]+BASE64_ALPHABET[b_dt[i+2]&0x3f]
								i+=3
							if (i==len(b_dt)-2):
								dt+=BASE64_ALPHABET[b_dt[i]>>2]+BASE64_ALPHABET[((b_dt[i]<<4)&0x3f)|(b_dt[i+1]>>4)]+BASE64_ALPHABET[(b_dt[i+1]<<2)&0x3f]+"="
							elif (i==len(b_dt)-1):
								dt+=BASE64_ALPHABET[b_dt[i]>>2]+BASE64_ALPHABET[(b_dt[i]<<4)&0x3f]+"=="
							b=_github_api_request("post",url=f"https://api.github.com/repos/{a_nm}/{nm}/git/blobs",data=dt+"\",\"encoding\":\"base64\"}")
							if (b is None):
								b_sha=False
								dt="Github Server Error"
							else:
								dt=b["sha"]
			bl.append([fp,({"path":fp,"mode":"100644","type":"blob","content":dt} if b_sha is False else {"path":fp,"mode":"100644","type":"blob","sha":dt})])
	for fp in r_t.keys():
		rm=True
		for e in bl:
			if (e[0] is not None and e[0]==fp):
				rm=False
				break
		if (rm is True):
			if (fp!="_"):
				_print(f"\x1b[38;2;210;40;40m- {b_nm}/{fp}\x1b[0m",df=True)
				cnt[3]+=1
			bl.append([None,{"path":fp,"mode":"100644","type":"blob","sha":None}])
	_print(f"\x1b[38;2;40;210;190m{b_nm} => \x1b[38;2;70;210;70m+{cnt[0]}\x1b[38;2;40;210;190m, \x1b[38;2;230;210;40m?{cnt[1]}\x1b[38;2;40;210;190m, \x1b[38;2;190;0;220m!{cnt[2]}\x1b[38;2;40;210;190m, \x1b[38;2;210;40;40m-{cnt[3]}\x1b[0m",df=True)
	if (any([(True if b[1] is not None else False) for b in bl]) and (cnt[0]>0 or cnt[3]>0)):
		_print(f"\x1b[38;2;100;100;100mUploading Changes...",df=True)
		tr_sha=_github_api_request("post",url=f"https://api.github.com/repos/{a_nm}/{nm}/git/trees",data=_encode_json({"base_tree":bt_sha,"tree":[b[1] for b in bl if b[1] is not None]}))["sha"]
		bf=bytes(f"tree {tr_sha}\nparent {bt_sha}\nauthor {GITHUB_USERNAME} <{GITHUB_EMAIL}> {c_tm} {('-' if UTC_OFFSET<0 else '')}{abs(UTC_OFFSET)//3600:-02d}{abs(UTC_OFFSET//60)%60:02d}\ncommitter {GITHUB_NAME} <{GITHUB_EMAIL}> {c_tm} {('-' if UTC_OFFSET<0 else '')}{abs(UTC_OFFSET)//3600:-02d}{abs(UTC_OFFSET//60)%60:02d}\n\n{msg}","utf-8")
		import subprocess
		sig=subprocess.Popen(["gpg","--status-fd=2","-bsau",GPG_LOCAL_KEY_ID,"--pinentry-mode=loopback","--passphrase",GPG_PASSPHRASE],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate(bf)[0]
		print(bf,sig)
		_github_api_request("patch",url=f"https://api.github.com/repos/{a_nm}/{nm}/git/refs/heads/{br}",data=_encode_json({"sha":_github_api_request("post",url=f"https://api.github.com/repos/{a_nm}/{nm}/git/commits",data=_encode_json({"message":msg,"tree":tr_sha,"parents":[bt_sha],"signature":sig}))["sha"],"force":True}))
		_print(f"\x1b[38;2;100;100;100mChanges Uploaded",df=True)
	else:
		_print(f"\x1b[38;2;100;100;100mNo Changes to Upload",df=True)
	if (cr is True):
		_print(f"\x1b[38;2;100;100;100mDeleting Temporary File...",df=True)
		_github_api_request("delete",url=f"https://api.github.com/repos/{a_nm}/{nm}/contents/_",data=f"{{\"message\":\"{msg}\",\"sha\":\"{GITHUB_EMPTY_FILE_HASH}\"}}")
		with open(__file_base_dir__+GITHUB_PROJECT_BRANCH_LIST_FILE_PATH,"w") as f:
			f.write("\n".join([f"{k}:{v}" for k,v in gr_dt.items()]))
	return True



def _push_all_github_projects(f=False):
	tm=int((time.time()//86400+4)//7)
	uc=0
	sc=0
	with open(__file_base_dir__+GITHUB_PUSHED_PROJECT_LIST_FILE_PATH,"r") as rf:
		b_dt=rf.read().replace("\r\n","\n").split("\n")
	with open(__file_base_dir__+GITHUB_PUSHED_PROJECT_LIST_FILE_PATH,"w") as wf:
		if (len(b_dt[0])==0 or int(b_dt[0])<tm):
			b_dt=[None]
		wf.write(str(tm)+"\n")
		wf.flush()
		for p in sorted(os.listdir(PROJECT_DIR)):
			if (f is False and p in b_dt[1:]):
				sc+=1
				wf.write(p+"\n")
				wf.flush()
				continue
			uc+=1
			if (_push_single_project(PROJECT_DIR+p,p) is False):
				return
			wf.write(p+"\n")
			wf.flush()
		if (f is False and "Boot_Program" in b_dt[1:]):
			sc+=1
			wf.write("Boot_Program\n")
			wf.flush()
		else:
			uc+=1
			if (_push_single_project(__file_base_dir__,"Boot_Program") is False):
				return
			wf.write("Boot_Program\n")
			wf.flush()
	_print(f"Finished Github Project Push Check, {uc} Projects Updated, {sc} Skipped.")



def _tokenize_file(dt,el=None):
	o=[]
	i=0
	sl=True
	ig=0
	t=min(REPO_STATS_MAX_READ,len(dt))
	while (i<t):
		sl=(True if i==0 or dt[i-1] in "\r\n" else False)
		if (sl is True):
			m=REPO_STATS_SHEBANG_REGEX.match(dt[i:])
			if (m is not None):
				i+=m.end(0)
				if (m.group(1).split("/")[-1]=="env"):
					o+="~~SHEBANG"+m.group(2)
				else:
					o+="~~SHEBANG"+m.group(1).split("/")[-1]
				continue
		m=REPO_STATS_IGNORE_REGEX.match(dt[i:])
		if (m is not None):
			ig+=m.end(0)
			if (ig/t>0.25):
				return []
			i+=m.end(0)
			continue
		m=REPO_STATS_TAG_REGEX.match(dt[i:])
		if (m is not None):
			i+=m.end(0)
			o.append("<"+m.group(1)+">")
			if (len(m.group(2))>0):
				o+=REPO_STATS_TAG_ATTR_REGEX.findall(m.group(2).strip())
			continue
		m=REPO_STATS_COMMON_REGEX.match(dt[i:])
		if (m is not None):
			i+=m.end(0)
			if (m.end(0)<=REPO_STATS_MAX_TOKEN_LEN):
				o.append(m.group(0))
			continue
		i+=1
	return o



def _project_stats_detect_file(r,f,ll,hdt,db,zt):
	if (os.stat(r+f).st_size==0 or _is_binary(r+f) is True):
		return None
	o=list(ll.keys())
	c=[]
	for k in db["languages"]:
		if (f in db["filenames"][k]):
			c.append(k)
	if (len(c)>0):
		o=c[:]
	if (len(o)==1):
		return o[0]
	ex="."+f.split(".")[-1].lower()
	c.clear()
	for k in o:
		if (ex in ll[k][0]):
			c.append(k)
	if (len(c)>0):
		o=c[:]
	if (len(o)==1):
		return o[0]
	dt=None
	try:
		with open(r+f,"rb") as rf:
			dt=rf.read().decode("utf-8",errors="replace")
	except PermissionError:
		return None
	if (REPO_STATS_XML_REGEX.search("\n".join(dt.split("\n")[:2])) is not None):
		return "XML"
	c.clear()
	for k in hdt:
		if (ex in k[0]):
			for e in k[1]:
				if (e[1] is None):
					c.append(e[0])
					break
				ok=True
				for p in e[1]:
					if ((p[0].match(dt) is not None)!=p[1]):
						ok=False
						break
				if (ok is False):
					continue
				c.append(e[0])
				break
			break
	if (len(c)>0):
		o=c[:]
	if (len(o)==1):
		return o[0]
	if (len(o)==0):
		return None
	tl=_tokenize_file(dt,el)
	if (len(tl)==0):
		return None
	tc={}
	for t in tl:
		if (t not in tc):
			tc[t]=1
		else:
			tc[t]+=1
	mx=0
	op=None
	for l in o:
		if (l not in db["languages"]):
			continue
		lp=math.log(db["languages"][l]/db["languages_total"])
		for k,v in tc.items():
			lp+=v*(math.log(db["tokens"][l][k]/db["language_tokens"][l]) if k in db["tokens"][l] else zt)
		if (op is None or lp>mx):
			mx=lp
			op=l
	return op



def _project_stats(p_fp,ll,hdt,db,el,zt):
	gdt=[]
	with open(p_fp+".gitignore","r") as f:
		for ln in f.read().replace("\r\n","\n").split("\n"):
			if (ln.endswith("\n")):
				ln=ln[:-1]
			ln=ln.lstrip()
			if (not ln.startswith("#")):
				iv=False
				if (ln.startswith("!")):
					ln=ln[1:]
					iv=True
				while (ln.endswith(" ") and ln[-2:]!="\\ " and ln[-2:]!="/ "):
					ln=ln[:-1]
				ln=GITIGNORE_FILE_PATH_REGEX.sub(r"\1",ln)
				if (len(ln)>0):
					if ("**/" in ln):
						gdt.append([iv,tuple(_create_gitignore_pattern(e) for e in ln.replace("**/","").split("/"))])
					gdt.append([iv,tuple(_create_gitignore_pattern(e) for e in ln.split("/"))])
	for r,_,fl in os.walk(p_fp):
		r=r.replace("\\","/").rstrip("/")+"/"
		if (r[len(p_fp):].strip("/")[:4]=="docs"):
			continue
		if ("/build" not in r.lower()):
			for f in fl:
				if (_match_gitignore_path(gdt,r[len(p_fp):]+f) is True):
					continue
				_print(f"\x1b[38;2;100;100;100mDetecting File \x1b[38;2;65;118;46m'{r+f}'\x1b[38;2;100;100;100m...",df=True)
				l=_project_stats_detect_file(r,f,ll,hdt,db,zt)
				if (l is None):
					continue
				if (l not in el):
					el[l]=[0,0]
				sz=os.stat(r+f).st_size
				el[l][0]+=sz
				with open(r+f,"rb") as fo:
					for k in fo.read().replace(b"\r\n",b"\n").split(b"\n"):
						if (len(k.strip())>0):
							el[l][1]+=1



def _arduino_clone_file(url,fp,sz):
	t=0
	at=0
	sys.__stdout__.write(f"{fp.split('/')[-1]} [....................] 0/{sz} 0%")
	with requests.get(url,stream=True) as r,open(fp,"wb") as f:
		for dt in r.iter_content(chunk_size=4096):
			f.write(dt)
			at+=len(dt)
			if (at>sz):
				sz=at
			t=min(t+len(dt),sz)
			p=int(t/sz*20)
			sys.__stdout__.write(f"\x1b[0G\x1b[2K{fp.split('/')[-1]} [{'='*(p-1)}{('>' if p>0 and p<20 else '')}{'.'*(20-p)}] {t}/{sz} {float(t*10000//sz)/100}%")
			sys.__stdout__.flush()
	sys.__stdout__.write("\n")



def _init_arduino_cache():
	_print("Initialising Arduino Data Cache\x1b[38;2;100;100;100m...")
	if (not os.path.exists(__file_base_dir__+"arduino")):
		os.mkdir(__file_base_dir__+"arduino")
	if (not os.path.exists(__file_base_dir__+f"arduino/cache")):
		os.mkdir(__file_base_dir__+f"arduino/cache")
	if (not os.path.exists(__file_base_dir__+f"arduino/cache/index")):
		with open(__file_base_dir__+f"arduino/cache/index","w"):
			pass
	else:
		with open(__file_base_dir__+f"arduino/cache/index","r") as f:
			for k in f.read().replace("\r","").split("\n"):
				if (len(k)>0):
					ARDUINO_CACHE[k.split(":")[0]]=float(k.split(":")[1])
	u=False
	_print("Reading Cache Index\x1b[38;2;100;100;100m...")
	for k in list(ARDUINO_CACHE.keys()):
		if (ARDUINO_CACHE[k]<time.time() or not os.path.exists(__file_base_dir__+f"arduino/cache/{k}")):
			if (os.path.exists(__file_base_dir__+f"arduino/cache/{k}")):
				os.remove(__file_base_dir__+f"arduino/cache/{k}")
			del ARDUINO_CACHE[k]
			u=True
	_print("Removing Old Cache\x1b[38;2;100;100;100m...")
	for k in os.listdir(__file_base_dir__+f"arduino/cache/"):
		if (k=="index" or k in list(ARDUINO_CACHE.keys())):
			continue
		os.remove(__file_base_dir__+f"arduino/cache/{k}")
	if (u is True):
		with open(__file_base_dir__+f"arduino/cache/index","w") as f:
			f.write("\n".join([f"{e[0]}:{e[1]}" for e in ARDUINO_CACHE.items()]))



def _list_arduino_boards(p=True):
	if (p is True):
		_print("Listing Arduino Boards Attached to the System\x1b[38;2;100;100;100m...")
	pg=(ctypes.wintypes.GUID*8)()
	pg_l=ctypes.wintypes.DWORD()
	setupapi.SetupDiClassGuidsFromNameW("Ports",pg,ctypes.sizeof(pg),ctypes.byref(pg_l))
	mg=(ctypes.wintypes.GUID*8)()
	mg_l=ctypes.wintypes.DWORD()
	setupapi.SetupDiClassGuidsFromNameW("Modem",mg,ctypes.sizeof(mg),ctypes.byref(mg_l))
	o=[]
	for k in (pg[:pg_l.value]+mg[:mg_l.value]):
		di_g=setupapi.SetupDiGetClassDevsW(ctypes.byref(k),None,0,DIGCF_PRESENT)
		di=ctypes.wintypes.SP_DEVINFO_DATA()
		di.cbSize=ctypes.sizeof(di)
		i=0
		while (setupapi.SetupDiEnumDeviceInfo(di_g,i,ctypes.byref(di))!=0):
			i+=1
			hkey=setupapi.SetupDiOpenDevRegKey(di_g,ctypes.byref(di),DICS_FLAG_GLOBAL,0,DIREG_DEV,KEY_READ)
			nm=ctypes.create_unicode_buffer(256)
			advapi32.RegQueryValueExW(hkey,"PortName",None,None,ctypes.byref(nm),ctypes.byref(ctypes.wintypes.ULONG(ctypes.sizeof(nm))))
			advapi32.RegCloseKey(hkey)
			if (nm.value[:3]=="LPT"):
				continue
			hw_id=ctypes.create_unicode_buffer(250)
			setupapi.SetupDiGetDeviceRegistryPropertyW(di_g,ctypes.byref(di),SPDRP_HARDWAREID,None,ctypes.byref(hw_id),ctypes.sizeof(hw_id)-1,None)
			m=(SERIAL_VALID_DEVICE_NAME_USB_REGEX if hw_id.value[:3]=="USB" else SERIAL_VALID_DEVICE_NAME_REGEX).search(hw_id.value.lower())
			if (m is not None):
				f_nm=f"vid_pid-0x{hex(int(m.group(1),16))[2:].rjust(4,'0')}-0x{hex(int(m.group(2),16))[2:].rjust(4,'0')}.json"
				r=None
				if (ARDUINO_CACHE.get(f_nm,0)==0):
					r=requests.get(f"https://builder.arduino.cc/v3/boards/byVidPid/0x{hex(int(m.group(1),16))[2:].rjust(4,'0')}/0x{hex(int(m.group(2),16))[2:].rjust(4,'0')}",headers={"Content-Type":"application/json"}).text
					ARDUINO_CACHE[f_nm]=int(time.time()+2592000)
					with open(__file_base_dir__+"arduino/cache/index","w") as f:
						f.write("\n".join([f"{e[0]}:{e[1]}" for e in ARDUINO_CACHE.items()]))
					with open(__file_base_dir__+"arduino/cache/"+f_nm,"w") as f:
						f.write(r)
				else:
					with open(__file_base_dir__+"arduino/cache/"+f_nm,"r") as f:
						r=f.read()
				if (len(r)==0):
					continue
				r=_decode_json(r)
				o.append({"arch":r["architecture"],"fqbn":r["fqbn"],"name":r["name"],"location":nm.value.replace("\\","/").split("/")[-1]})
			else:
				continue
		setupapi.SetupDiDestroyDeviceInfoList(di_g)
	return o



def _install_arduino_package(b,force=False):
	if (type(b)==str):
		_print(f"Searching For Package '{b}'\x1b[38;2;100;100;100m...")
		i_pkg=[]
		if (os.path.exists(__file_base_dir__+f"arduino/packages/index")):
			with open(__file_base_dir__+f"arduino/packages/index","r") as f:
				i_pkg=f.read().replace("\r\n","\n").split("\n")
		_print(f"Querying 'https://api.github.com/repos/arduino/{b}/releases/latest' for Package Metadata\x1b[38;2;100;100;100m...")
		dt=requests.get(f"https://api.github.com/repos/arduino/{b}/releases/latest").json()
		if (force is False and f"arduino-{b}-{dt['tag_name']}" in i_pkg):
			_print(f"\x1b[38;2;200;40;20mPackage 'arduino:{b}:{dt['tag_name']}' already Installed.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			return
		_print(f"Searching for '{ARDUINO_OS_TYPE}' Release\x1b[38;2;100;100;100m...")
		for k in dt["assets"]:
			if (k["name"].startswith(b+"-") and (k["name"].endswith(".zip") or k["name"].endswith(".tar.bz2")) and "mingw32" in re.sub(r"(\.zip|\.tar\.bz2)$","",k["name"][len(b)+1:])):
				_print(f"Found Release '{k['name']}'.\nCloning to File '{TEMP_DIR}{k['name']}' ...")
				_arduino_clone_file(k["browser_download_url"],f"{TEMP_DIR}{k['name']}",int(k["size"]))
				with open(f"{TEMP_DIR}{k['name']}","wb") as f:
					f.write(requests.get(k["browser_download_url"]).content)
				if (k["name"].endswith(".tar.bz2")):
					_print("Using Extractor 'tar/r:bz2'\x1b[38;2;100;100;100m...")
					_print("Extracting Files\x1b[38;2;100;100;100m...")
					with tarfile.open(f"{TEMP_DIR}{k['name']}","r:bz2") as tf:
						tf.extractall(__file_base_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}")
						off=len(__file_base_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}/")
						_print("Copying Extracted Files\x1b[38;2;100;100;100m...")
						for r,_,fl in os.walk(__file_base_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}"):
							for f in fl:
								fp=os.path.join(r,f)
								os.makedirs(os.path.dirname(__file_base_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}"),exist_ok=True)
								try:
									with open(fp,"rb") as rf,open(__file_base_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}","wb") as wf:
										wf.write(rf.read())
								except (OSError,IOError,PermissionError) as e:
									_print(f"\x1b[38;2;200;40;20mError while Copying File '{fp}' to '{__file_base_dir__}arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
						rm_fp=__file_base_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}"
						dl=[rm_fp]
						for r,ndl,fl in os.walk(rm_fp):
							r=r.replace("\\","/").rstrip("/")+"/"
							for d in ndl:
								dl.insert(0,r+d)
							for f in fl:
								os.remove(r+f)
						for e in dl:
							os.rmdir(e)
				elif (k["name"].endswith(".zip")):
					_print("Using Extractor 'zip'\x1b[38;2;100;100;100m...")
					_print("Extracting Files\x1b[38;2;100;100;100m...")
					with zipfile.ZipFile(f"{TEMP_DIR}{k['name']}","r") as zf:
						zf.extractall(__file_base_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}")
				else:
					_print(f"\x1b[38;2;200;40;20mUnknown File Extractor for File Extensions '{k['name'][len(k['name'].split('.')[0]):]}'.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
					kernel32.ExitProcess(1)
				_print("Removing Archive\x1b[38;2;100;100;100m...")
				os.remove(f"{TEMP_DIR}{k['name']}")
		_print("Indexing Package\x1b[38;2;100;100;100m...")
		with open(__file_base_dir__+f"arduino/packages/index","a") as f:
			f.write(f"arduino-{b}-{dt['tag_name']}\n")
		return
	_print(f"Searching For Package '{b['pkg']}:{b['arch']}{(':'+b['ver'] if b['ver'] is not None else '')}'...\nReading Package Index Cache\x1b[38;2;100;100;100m...")
	dt=None
	if (ARDUINO_CACHE.get("package_index.json",0)==0):
		_print("\x1b[38;2;200;40;20mPackage Index Cache not Found.\x1b[0m Downloaing It\x1b[38;2;100;100;100m...")
		dt=requests.get("https://downloads.arduino.cc/packages/package_index.json",headers={"Content-Type":"application/json"}).text
		ARDUINO_CACHE["package_index.json"]=int(time.time()+2592000)
		with open(__file_base_dir__+"arduino/cache/index","w") as f:
			f.write("\n".join([f"{e[0]}:{e[1]}" for e in ARDUINO_CACHE.items()]))
		with open(__file_base_dir__+"arduino/cache/package_index.json","w") as f:
			f.write(dt)
	else:
		with open(__file_base_dir__+"arduino/cache/package_index.json","r") as f:
			dt=f.read()
	p={e["name"]:e for e in _decode_json(dt)["packages"]}
	dl=[b]
	o=[]
	while (len(dl)>0):
		d,dl=dl[0],dl[1:]
		_print(f"Searching For Package '{d['pkg']}:{(d['name'] if 'name' in list(d.keys()) else d['arch'])}{(':'+d['ver'] if d['ver'] is not None else '')}'\x1b[38;2;100;100;100m...")
		l=[]
		for k in p[d["pkg"]]["platforms"]:
			if (("arch" in list(d.keys()) and k["architecture"]==d["arch"]) or ("arch" not in list(d.keys()) and k["name"]==d["name"])):
				l.append((k["version"],k,False))
		for k in p[d["pkg"]]["tools"]:
			if (("name" in list(d.keys()) and k["name"]==d["name"])):
				l.append((k["version"],k,True))
		e=(sorted(l,key=lambda e:e[0],reverse=True)[0] if d["ver"] is None else [e for e in l if e[0]==d["ver"]][0])
		if (e[2] is False):
			o.append((d["pkg"],(d["arch"] if "arch" in list(d.keys()) else d["name"]),e[1]["version"],e[1]["url"],e[1]["archiveFileName"],"hardware",int(e[1]["size"])))
			if (len(e[1]["toolsDependencies"])>0):
				_print(f"Found Dependencies: ('{(chr(39)+', '+chr(39)).join([k['packager']+':'+k['name']+':'+k['version'] for k in e[1]['toolsDependencies']])}')")
			for k in e[1]["toolsDependencies"]:
				dl.append({"pkg":k["packager"],"name":k["name"],"ver":k["version"]})
		else:
			for k in e[1]["systems"]:
				if (k["host"]==ARDUINO_HOST_SYSTEM):
					o.append((d["pkg"],(d["arch"] if "arch" in list(d.keys()) else d["name"]),e[1]["version"],k["url"],k["archiveFileName"],"tools",k["size"]))
	if (not os.path.exists(__file_base_dir__+f"arduino/packages")):
		os.mkdir(__file_base_dir__+f"arduino/packages")
	i_pkg=[]
	if (os.path.exists(__file_base_dir__+f"arduino/packages/index")):
		with open(__file_base_dir__+f"arduino/packages/index","r") as f:
			i_pkg=f.read().replace("\r\n","\n").split("\n")
	else:
		with open(__file_base_dir__+f"arduino/packages/index","w"):
			pass
	for k in o:
		if (force is False and f"{k[0]}-{k[1]}-{k[2]}" in i_pkg):
			_print(f"\x1b[38;2;200;40;20mPackage '{k[0]}:{k[1]}:{k[2]}' already Installed.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
			continue
		if (not os.path.exists(__file_base_dir__+f"arduino/packages/{k[0]}")):
			os.mkdir(__file_base_dir__+f"arduino/packages/{k[0]}")
		if (not os.path.exists(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}")):
			os.mkdir(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}")
		if (not os.path.exists(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}")):
			os.mkdir(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}")
		if (not os.path.exists(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")):
			os.mkdir(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
		_print(f"Cloning to File '{TEMP_DIR}{k[4]}' ...")
		_arduino_clone_file(k[3],TEMP_DIR+"/"+k[4],int(k[6]))
		if (k[4].endswith(".tar.bz2")):
			_print("Using Extractor 'tar/r:bz2'\x1b[38;2;100;100;100m...")
			_print("Extracting Files\x1b[38;2;100;100;100m...")
			with tarfile.open(TEMP_DIR+"/"+k[4],"r:bz2") as tf:
				tf.extractall(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
				off=len(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}/")
				_print("Copying Extracted Files\x1b[38;2;100;100;100m...")
				for r,_,fl in os.walk(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}"):
					for f in fl:
						fp=os.path.join(r,f)
						os.makedirs(os.path.dirname(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}"),exist_ok=True)
						try:
							with open(fp,"rb") as rf,open(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}","wb") as wf:
								wf.write(rf.read())
						except (OSError,IOError,PermissionError) as e:
							_print(f"\x1b[38;2;200;40;20mError while Copying File '{fp}' to '{__file_base_dir__}arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
				rm_fp=__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}"
				dl=[rm_fp]
				for r,ndl,fl in os.walk(rm_fp):
					r=r.replace("\\","/").rstrip("/")+"/"
					for d in ndl:
						dl.insert(0,r+d)
					for f in fl:
						os.remove(r+f)
				for e in dl:
					os.rmdir(e)
		elif (k[4].endswith(".zip")):
			_print("Using Extractor 'zip'\x1b[38;2;100;100;100m...")
			_print("Extracting Files\x1b[38;2;100;100;100m...")
			with zipfile.ZipFile(TEMP_DIR+"/"+k[4],"r") as zf:
				zf.extractall(__file_base_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
		_print("Removing Archive\x1b[38;2;100;100;100m...")
		os.remove(TEMP_DIR+"/"+k[4])
		_print("Indexing Package\x1b[38;2;100;100;100m...")
		with open(__file_base_dir__+f"arduino/packages/index","a") as f:
			f.write(f"{k[0]}-{k[1]}-{k[2]}\n")



def _get_inner_dir(fp):
	return fp+os.listdir(fp)[0]+"/"



def _replace_arduino_include(dt):
	i=0
	while (i<len(dt)):
		m=ARDUINO_REPLACE_INCLUDE_REGEX.search(dt[i:])
		if (m is None):
			break
		dt=dt[:i+m.start(0)]+b"#include <"+m.group(1)[1:-1].replace(b"\\",b"/").replace(b"/",b"$")+b">"+dt[i+m.end(0)-1:]
		i+=m.end(0)
	return dt



def _run_process(a):
	si=ctypes.wintypes.STARTUPINFOW()
	si.cb=ctypes.sizeof(ctypes.wintypes.STARTUPINFOW)
	si.lpReserved=None
	si.lpDesktop=None
	si.lpTitle=None
	si.dwFlags=0
	si.cbReserved2=0
	si.lpReserved2=None
	pi=ctypes.wintypes.PROCESS_INFORMATION()
	kernel32.CreateProcessW(None,a,None,None,True,0,None,None,ctypes.byref(si),ctypes.byref(pi))
	kernel32.CloseHandle(pi.hThread)
	kernel32.WaitForSingleObject(pi.hProcess,INFINITE)
	ec=ctypes.wintypes.DWORD()
	kernel32.GetExitCodeProcess(pi.hProcess,ctypes.byref(ec))
	kernel32.CloseHandle(pi.hProcess)
	if (ec.value!=0):
		kernel32.ExitProcess(ec)



def _create_process(a):
	si=ctypes.wintypes.STARTUPINFOW()
	si.cb=ctypes.sizeof(ctypes.wintypes.STARTUPINFOW)
	si.lpReserved=None
	si.lpDesktop=None
	si.lpTitle=None
	si.dwFlags=0
	si.cbReserved2=0
	si.lpReserved2=None
	pi=ctypes.wintypes.PROCESS_INFORMATION()
	kernel32.CreateProcessW(None,a,None,None,False,CREATE_NEW_CONSOLE|CREATE_NEW_PROCESS_GROUP,None,None,ctypes.byref(si),ctypes.byref(pi))
	kernel32.CloseHandle(pi.hProcess)
	kernel32.CloseHandle(pi.hThread)



def _compile_arduino_files(bp,i_fp,o_fp,inc_l,rc):
	l=([],[],[])
	for r,_,fl in os.walk(i_fp):
		for f in fl:
			if (f.lower().endswith(".s")):
				l[0].append(os.path.join(r,f))
			elif (f.lower().endswith(".c")):
				l[1].append(os.path.join(r,f))
			elif (f.lower().endswith(".cpp")):
				l[2].append(os.path.join(r,f))
		if (rc is False):
			break
	o=[]
	for i in range(0,3):
		for f in l[i]:
			c_bp={**bp,"compiler.warning_flags":bp.get("compiler.warning_flags","")+("."+ARDUINO_CUSTOM_WARNING_LEVEL if ARDUINO_CUSTOM_WARNING_LEVEL!="" else ""),"includes":" ".join([f"\"-I{re.sub('('+chr(92)+r'|/)$','',e)}\"" for e in inc_l]),"source_file":f,"object_file":o_fp+f[len(i_fp):]+".o"}
			if (not os.path.exists(o_fp+"/".join(f[len(i_fp):].split("/")[:-1]))):
				os.makedirs(o_fp+"/".join(f[len(i_fp):].split("/")[:-1]))
			cmd=c_bp[("recipe.S.o.pattern","recipe.c.o.pattern","recipe.cpp.o.pattern")[i]]
			while ("{" in cmd):
				cmd=ARDUINO_COMMAND_FORMAT_REGEX.sub(lambda m:(c_bp[m.group(1)] if m.group(1) in c_bp else ""),cmd)
			_run_process(cmd)
			o.append(o_fp+f[len(i_fp):]+".o")
	return o



def _compile_arduino_prog(s_fp,o_fp,fqbn,inc_l):
	fqbn=fqbn.split(":")
	s_fp=os.path.abspath(s_fp).replace("\\","/").rstrip("/")+"/"
	o_fp=os.path.abspath(o_fp).replace("\\","/").rstrip("/")+"/"
	if (not os.path.exists(s_fp)):
		_print(f"\x1b[38;2;200;40;20mProgram '{s_fp}'\x1b[38;2;200;40;20m doesn't Exist.")
		kernel32.ExitProcess(1)
	if (not os.path.isdir(s_fp)):
		_print("\x1b[38;2;200;40;20mProgram Path must Be a Directory.")
		kernel32.ExitProcess(1)
	_print(f"Compiling Program '{s_fp}' to Directory '{o_fp}' with Architecture '{':'.join(fqbn)}'\x1b[38;2;100;100;100m...")
	if (not os.path.exists(o_fp)):
		os.mkdir(o_fp)
	else:
		dl=[]
		for r,ndl,fl in os.walk(o_fp):
			r=r.replace("\\","/").strip("/")+"/"
			if ("/core/" in r):
				continue
			for d in ndl:
				if (d!="core"):
					dl.insert(0,r+d)
			for f in fl:
				if (f!="last-build.dt"):
					os.remove(r+f)
		for k in dl:
			os.rmdir(k)
	m_fp=s_fp+"main.ino"
	_print("Searching For Main File\x1b[38;2;100;100;100m...")
	if (os.path.exists(m_fp) is False or os.path.isdir(m_fp) is True):
		_print("\x1b[38;2;200;40;20mProgram doesn't Contain a Main Program")
		kernel32.ExitProcess(1)
	_print("Loading Packages\x1b[38;2;100;100;100m...")
	if (not os.path.exists(__file_base_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/")):
		_print(f"\x1b[38;2;200;40;20mPackage '{fqbn[0]}:{fqbn[1]}'\x1b[38;2;200;40;20m isn't Installed.")
		kernel32.ExitProcess(1)
	h_fp=os.path.abspath(__file_base_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"+sorted(os.listdir(__file_base_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"),reverse=True)[0])+"/"
	_print(f"Reading '{h_fp}boards.txt'\x1b[38;2;100;100;100m...")
	with open(h_fp+"boards.txt","r") as hb_f:
		h_pm={}
		for k in hb_f.read().replace("\r\n","\n").split("\n"):
			if (len(k.strip())==0 or k.strip()[0]=="#"):
				continue
			if (k.split(".")[0] not in list(h_pm.keys())):
				h_pm[k.split(".")[0]]={}
			h_pm[k.split(".")[0]][".".join(k.split("=")[0].split(".")[1:])]=k[len(k.split("=")[0])+1:]
	if (fqbn[2] not in list(h_pm.keys())):
		_print(f"\x1b[38;2;200;40;20mInvalid FQBN '{':'.join(fqbn)}'\x1b[38;2;200;40;20m.")
		kernel32.ExitProcess(1)
	_print(f"Reading '{h_fp}platform.txt'\x1b[38;2;100;100;100m...")
	with open(h_fp+"platform.txt","r") as hp_f:
		p_pm={k.split("=")[0]:k[len(k.split("=")[0])+1:] for k in hp_f.read().replace("\r\n","\n").split("\n") if len(k.strip())>0 and k.strip()[0]!="#"}
	_print(f"Creating Build Properties\x1b[38;2;100;100;100m...")
	bp={"software":"ARDUINO",**p_pm,**h_pm[fqbn[2]],"build.path":ARDUINO_DIRECTORY_PATH_REGEX.sub("",o_fp),"build.project_name":m_fp.split("/")[-1],"build.arch":fqbn[1].upper(),"archive_file":"core/core.a","archive_file_path":o_fp+"core/core.a"}
	bp.update({"build.core.path":h_fp+"cores/"+bp["build.core"],"build.system.path":h_fp+"system","runtime.platform.path":ARDUINO_DIRECTORY_PATH_REGEX.sub(r"",h_fp),"runtime.hardware.path":ARDUINO_DIRECTORY_PATH_REGEX.sub("",os.path.abspath(__file_base_dir__+f"arduino/packages/{fqbn[0]}/hardware/")),"runtime.ide.version":"10607","runtime.ide.path":__file_base_dir__+"","build.fqbn":":".join(fqbn),"ide_version":"ide_version","runtime.os":ARDUINO_OS_TYPE,"build.variant.path":("" if bp["build.variant"]=="" else h_fp+"variants/"+bp["build.variant"]),"build.source.path":ARDUINO_DIRECTORY_PATH_REGEX.sub("",s_fp),"extra.time.utc":str(int(time.time())),"extra.time.local":str(int(time.time())),"extra.time.zone":"0","extra.time.dst":"0"})
	if (ARDUINO_OPTIMIZE_FOR_DEBUG is True):
		if ("compiler.optimization_flags.debug" in list(bp.keys())):
			bp["compiler.optimization_flags"]=bp["compiler.optimization_flags.debug"]
	else:
		if ("compiler.optimization_flags.release" in list(bp.keys())):
			bp["compiler.optimization_flags"]=bp["compiler.optimization_flags.release"]
	_print("Loading Tools\x1b[38;2;100;100;100m...")
	for pkg in os.listdir(__file_base_dir__+f"arduino/packages/"):
		if (os.path.exists(__file_base_dir__+f"arduino/packages/{pkg}/tools/")):
			for t in os.listdir(__file_base_dir__+f"arduino/packages/{pkg}/tools/"):
				for v in os.listdir(__file_base_dir__+f"arduino/packages/{pkg}/tools/{t}/"):
					bp[f"runtime.tools.{t}-{v}.path"]=_get_inner_dir(__file_base_dir__+f"arduino/packages/{pkg}/tools/{t}/{v}/")
				bp[f"runtime.tools.{t}.path"]=_get_inner_dir(__file_base_dir__+f"arduino/packages/{pkg}/tools/{t}/{v}/")
	_print("Expanding Build Properties\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		while (True):
			l=len(v)
			v=ARDUINO_COMMAND_FORMAT_REGEX.sub(lambda m:(bp[m.group(1)] if m.group(1) in bp else m.group(0)),v)
			if (len(v)==l):
				break
		bp[k]=v
	_print("Comparing Old Build Properties\x1b[38;2;100;100;100m...")
	dt=b",".join([bytes(f"'{k}'='{v}'","utf-8") for k,v in bp.items() if not k.startswith("extra.time")])
	h=SHA1_START_VALUE.copy()
	l=len(dt)
	dt+=b"\x80"+b"\x00"*((56-(l+1)%64)%64)+bytes([l>>53,(l>>45)&0xff,(l>>37)&0xff,(l>>29)&0xff,(l>>21)&0xff,(l>>13)&0xff,(l>>5)&0xff,(l<<3)&0xff])
	i=0
	while (i<len(dt)):
		h=_sha1_chunk(h,dt[i:i+64])
		i+=64
	dt_h=f"{h[0]:08x}{h[1]:08x}{h[2]:08x}{h[3]:08x}{h[4]:08x}"
	if (os.path.exists(o_fp+"last-build.dt")):
		with open(o_fp+"last-build.dt","r") as f:
			sha1=f.read()
		if (sha1[:40]!=dt_h):
			_print("\x1b[38;2;200;40;20mHash not Matching.\x1b[0m Rebuilding Everything\x1b[38;2;100;100;100m...")
			dl=[]
			for r,ndl,fl in os.walk(o_fp):
				r=r.replace("\\","/").rstrip("/")+"/"
				for d in ndl:
					dl.insert(0,r+d)
				for f in fl:
					os.remove(r+f)
			for k in dl:
				os.rmdir(k)
	_print("Writing New Hash\x1b[38;2;100;100;100m...")
	with open(o_fp+"last-build.dt","w") as f:
		f.write(dt_h)
	_print("Running Recipe 'recipe.hooks.prebuild'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.prebuild") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	l_off=0
	nh_inc=False
	_print("Bundling Program Files\x1b[38;2;100;100;100m...")
	with open(o_fp+m_fp.split("/")[-1]+".cpp","wb") as bf:
		src=b""
		for r,_,fl in os.walk(s_fp):
			for fp in fl:
				if (fp.split(".")[-1].lower()=="ino"):
					_print(f"Found Main Program File '{os.path.join(r,fp)}'\x1b[38;2;100;100;100m...")
					with open(os.path.join(r,fp),"rb") as f:
						dt=f.read().replace(b"\r\n",b"\n")
						if (nh_inc is False):
							for k in ARDUINO_CPP_INCLUDE_FILE_REGEX.findall(str(dt,"utf-8").lower()):
								if (k=="arduino.h"):
									nh_inc=True
									break
							if (nh_inc is False):
								bf.write(b"#include <arduino.h>\n")
								l_off+=1
								nh_inc=True
						src+=dt+b"\n"
						bf.write(bytes(f"#line 1 \"{os.path.join(r,fp).replace(chr(92),chr(92)+chr(92)).replace(chr(34),chr(92)+chr(34))}\"\n","utf-8")+_replace_arduino_include(dt)+b"\n;\n")
						l_off+=(1 if os.path.join(r,fp)==m_fp else 0)
		dl=[(e[0].replace("\\","/"),e[1].replace("\\","/")+("/" if e[1][-1] not in "\\/" else "")) for e in [(s_fp,s_fp)]+[(os.path.join(r,d),r) for r,dl,_ in os.walk(s_fp) for d in dl]+[(e,e) for e in inc_l]]
		l=[e for e in ARDUINO_CPP_INCLUDE_FILE_REGEX.findall(str(src,"utf-8").lower()) if e!="arduino.h"]
		r_dl=[]
		for k in l:
			if (k[-2:]==".h"):
				l.append(k[:-2]+".cpp")
				l.append(k[:-2]+".c")
				l.append(k[:-2]+".s")
				l.append(k.split("/")[-1][:-2]+".cpp")
				l.append(k.split("/")[-1][:-2]+".c")
				l.append(k.split("/")[-1][:-2]+".s")
			for d in dl:
				if (os.path.exists(os.path.join(d[0],k))):
					_print(f"Found Included Program File '{os.path.join(d[0],k)}'\x1b[38;2;100;100;100m...")
					with open(o_fp+"/"+os.path.join(d[0],k)[len(d[1]):].replace("\\","/").replace("/","$"),"wb") as wf,open(os.path.join(d[0],k),"rb") as rf:
						dt=rf.read().replace(b"\r\n",b"\n")
						for e in ARDUINO_CPP_INCLUDE_FILE_REGEX.findall(str(src,"utf-8").lower()):
							if (e!="arduino.h" and e not in l):
								l.append(e)
						wf.write(bytes(f"#line 1 \"{os.path.join(d[0],k).replace(chr(92),chr(92)+chr(92)).replace(chr(34),chr(92)+chr(34))}\"\n","utf-8")+_replace_arduino_include(dt)+b"\n;\n")
					for e in inc_l:
						if (os.path.join(d[0],k).replace("\\","/").startswith(e.replace("\\","/"))):
							if (e not in r_dl):
								r_dl.append(e)
							break
					break
		for k in r_dl:
			inc_l.remove(k)
	inc_l.append(bp["build.core.path"])
	inc_l.append(o_fp)
	if (bp["build.variant.path"]!=""):
		inc_l.append(bp["build.variant.path"])
	_print("Generating Preprocessor Properties\x1b[38;2;100;100;100m...")
	pd={"recipe.preproc.macros":bp["recipe.cpp.o.pattern"].replace("{compiler.cpp.flags}","{compiler.cpp.flags} {preproc.macros.flags}").replace("{object_file}","{preprocessed_file_path}"),**bp,"source_file":o_fp+m_fp.split("/")[-1]+".cpp","preprocessed_file_path":o_fp+m_fp.split("/")[-1].split(".")[0]+".cpp","includes":" ".join([f"\"-I{re.sub('('+chr(92)+r'|/)$','',e)}\"".replace("\\","/") for e in inc_l])}
	cmd=pd["recipe.preproc.macros"]
	while ("{" in cmd):
		cmd=ARDUINO_COMMAND_FORMAT_REGEX.sub(lambda m:(pd[m.group(1)] if m.group(1) in pd else ""),cmd)
	_print("Running Preprocessor\x1b[38;2;100;100;100m...")
	_run_process(cmd.replace("-MMD","")+" -DARDUINO_LIB_DISCOVERY_PHASE")
	os.remove(o_fp+m_fp.split("/")[-1]+".cpp")
	_print("Running Recipe 'recipe.hooks.sketch.prebuild'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.sketch.prebuild") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	_print("Compiling Files\x1b[38;2;100;100;100m...")
	s_of=_compile_arduino_files(bp,o_fp,o_fp,inc_l,False)+(_compile_arduino_files(bp,o_fp+"src",o_fp+"src",inc_l,True) if os.path.exists(o_fp+"src") else [])
	_print("Running Recipe 'recipe.hooks.sketch.postbuild'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.sketch.postbuild") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	_print("Running Recipe 'recipe.hooks.core.prebuild'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.core.prebuild") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	c_inc_l=[bp["build.core.path"]]+([bp["build.variant.path"]] if bp["build.variant.path"]!="" else [])
	_print("Buliding Core\x1b[38;2;100;100;100m...")
	if (not os.path.exists(o_fp+"core")):
		_print("\x1b[38;2;200;40;20mPrebuild Core not Found.\x1b[0m Rebuilding\x1b[38;2;100;100;100m...")
		os.mkdir(o_fp+"core")
		os.mkdir(o_fp+"core/build")
		_print("Compiling Core Variant Files\x1b[38;2;100;100;100m...")
		v_of=(_compile_arduino_files(bp,bp["build.variant.path"],o_fp+"core",c_inc_l,True) if bp["build.variant.path"]!="" else [])
		_print("Compiling Core Files\x1b[38;2;100;100;100m...")
		pr=False
		for c_of in _compile_arduino_files(bp,bp["build.core.path"],o_fp+"core/build",c_inc_l,True):
			if (pr is False):
				_print("Archiving Core Files\x1b[38;2;100;100;100m...")
			pr=True
			_run_process(ARDUINO_COMMAND_FORMAT_REGEX.sub("",bp["recipe.ar.pattern"].replace("{object_file}",c_of)))
	else:
		_print("Collecting Core Variant Files\x1b[38;2;100;100;100m...")
		v_of=[e for e in os.listdir(o_fp+"core/") if e.endswith(".o")]
	_print("Running Recipe 'recipe.hooks.core.postbuild'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.core.postbuild") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	_print("Running Recipe 'recipe.hooks.linking.prelink'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.linking.prelink") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	_print("Linking Files\x1b[38;2;100;100;100m...")
	_run_process(ARDUINO_COMMAND_FORMAT_REGEX.sub("",bp["recipe.c.combine.pattern"].replace("{compiler.warning_flags}",bp.get("compiler.warning_flags","")+(f".{ARDUINO_CUSTOM_WARNING_LEVEL}" if ARDUINO_CUSTOM_WARNING_LEVEL!="" else "")).replace("{object_files}"," ".join([f"\"{e}\"" for e in s_of+v_of]))))
	_print("Running Recipe 'recipe.hooks.linking.postlink'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.linking.postlink") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	_print("Running Recipe 'recipe.hooks.objcopy.preobjcopy'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.objcopy.preobjcopy") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	_print("Running Recipe 'recipe.objcopy'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.objcopy") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	_print("Running Recipe 'recipe.hooks.objcopy.postobjcopy'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.objcopy.postobjcopy") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	_print("Running Recipe 'recipe.hooks.postbuild'\x1b[38;2;100;100;100m...")
	for k,v in bp.items():
		if (k.startswith("recipe.hooks.postbuild") and k.endswith(".pattern") and len(v)>0):
			_run_process(v)
	sz=[0,0]
	if (bp["upload.maximum_size"]!=""):
		_print("Processing Statistics\x1b[38;2;100;100;100m...")
		in_h=kernel32.GetStdHandle(STD_INPUT_HANDLE)
		out_r_h=ctypes.wintypes.HANDLE()
		out_w_h=ctypes.wintypes.HANDLE()
		sa=ctypes.wintypes.SECURITY_ATTRIBUTES()
		sa.nLength=ctypes.sizeof(ctypes.wintypes.SECURITY_ATTRIBUTES())
		sa.lpSecurityDescriptor=None
		sa.bInheritHandle=True
		kernel32.CreatePipe(ctypes.byref(out_r_h),ctypes.byref(out_w_h),ctypes.byref(sa),0)
		tmp_h=ctypes.wintypes.HANDLE()
		kernel32.DuplicateHandle(kernel32.GetCurrentProcess(),in_h,kernel32.GetCurrentProcess(),ctypes.byref(tmp_h),0,True,DUPLICATE_SAME_ACCESS)
		in_h=tmp_h
		kernel32.DuplicateHandle(kernel32.GetCurrentProcess(),out_w_h,kernel32.GetCurrentProcess(),ctypes.byref(tmp_h),0,True,DUPLICATE_SAME_ACCESS)
		out_w_h=tmp_h
		err_h=ctypes.wintypes.HANDLE()
		kernel32.DuplicateHandle(kernel32.GetCurrentProcess(),out_w_h,kernel32.GetCurrentProcess(),ctypes.byref(err_h),0,True,DUPLICATE_SAME_ACCESS)
		si=ctypes.wintypes.STARTUPINFOW()
		si.cb=ctypes.sizeof(ctypes.wintypes.STARTUPINFOW)
		si.lpReserved=None
		si.lpDesktop=None
		si.lpTitle=None
		si.dwFlags=STARTF_USESTDHANDLES
		si.cbReserved2=0
		si.lpReserved2=None
		si.hStdInput=in_h
		si.hStdOutput=out_w_h
		si.hStdError=err_h
		pi=ctypes.wintypes.PROCESS_INFORMATION()
		kernel32.CreateProcessW(None,ARDUINO_COMMAND_FORMAT_REGEX.sub("",bp["recipe.size.pattern"].replace("{compiler.warning_flags}",bp.get("compiler.warning_flags","")+(f".{ARDUINO_CUSTOM_WARNING_LEVEL}" if ARDUINO_CUSTOM_WARNING_LEVEL!="" else ""))),None,None,True,0,None,None,ctypes.byref(si),ctypes.byref(pi))
		kernel32.CloseHandle(pi.hThread)
		kernel32.CloseHandle(in_h)
		kernel32.CloseHandle(out_w_h)
		kernel32.CloseHandle(err_h)
		kernel32.WaitForSingleObject(pi.hProcess,INFINITE)
		o=""
		bf=ctypes.create_string_buffer(FILE_READ_CHUNK_SIZE)
		bf_l=ctypes.wintypes.DWORD()
		while (True):
			kernel32.ReadFile(out_r_h,bf,FILE_READ_CHUNK_SIZE,ctypes.byref(bf_l),None)
			o+=str(bf.raw[:bf_l.value],"utf-8")
			if (bf_l.value!=FILE_READ_CHUNK_SIZE):
				break
		ec=ctypes.wintypes.DWORD()
		kernel32.GetExitCodeProcess(pi.hProcess,ctypes.byref(ec))
		kernel32.CloseHandle(pi.hProcess)
		kernel32.CloseHandle(out_r_h)
		if (ec.value!=0):
			kernel32.ExitProcess(ec)
		for k in re.findall(bp["recipe.size.regex"],o,re.M):
			sz[0]+=int(k)
		for k in re.findall(bp["recipe.size.regex.data"],o,re.M):
			sz[1]+=int(k)
		_print(f"Code: {sz[0]} / {bp['upload.maximum_size']} bytes ({sz[0]*100//int(bp['upload.maximum_size'])}%)")
		if (bp["upload.maximum_data_size"]!=""):
			_print(f"Global Variables: {sz[1]} / {bp['upload.maximum_data_size']} bytes ({sz[1]*100//int(bp['upload.maximum_data_size'])}%)")
		else:
			_print(f"Global Variables: {sz[1]} bytes")
		if (sz[0]>int(bp["upload.maximum_size"])):
			_print(f"\x1b[38;2;200;40;20mCode Too Big",df=True)
			kernel32.ExitProcess(1)
		if (bp["upload.maximum_data_size"]!="" and sz[1]>int(bp["upload.maximum_data_size"])):
			_print(f"\x1b[38;2;200;40;20mProgram Uses Too Much Dynamic Memory",df=True)
			kernel32.ExitProcess(1)
	return sz



def _upload_to_arduino(o_fp,p,fqbn,bb,vu,inc_l):
	fqbn=fqbn.split(":")
	o_fp=os.path.abspath(o_fp).replace("\\","/")
	if (o_fp[-1]!="/"):
		o_fp+="/"
	_print("Searching For Build Directory\x1b[38;2;100;100;100m...")
	if (not os.path.exists(o_fp)):
		_print("\x1b[38;2;200;40;20mProgram Build Directory Not Found.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		kernel32.ExitProcess(1)
	_print("Loading Packages\x1b[38;2;100;100;100m...")
	if (not os.path.exists(__file_base_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/")):
		_print(f"\x1b[38;2;200;40;20mPackage '{fqbn[0]}:{fqbn[1]}' isn't Installed.",df=True)
		kernel32.ExitProcess(1)
	h_fp=os.path.abspath(__file_base_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"+sorted(os.listdir(__file_base_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"),reverse=True)[0])+"/"
	_print(f"Reading File '{h_fp}boards.txt'\x1b[38;2;100;100;100m...")
	with open(h_fp+"boards.txt","r") as hb_f:
		h_pm={}
		for k in hb_f.read().replace("\r\n","\n").split("\n"):
			if (len(k.strip())==0 or k.strip()[0]=="#"):
				continue
			if (k.split(".")[0] not in list(h_pm.keys())):
				h_pm[k.split(".")[0]]={}
			h_pm[k.split(".")[0]][".".join(k.split("=")[0].split(".")[1:])]=k[len(k.split("=")[0])+1:]
	if (fqbn[2] not in list(h_pm.keys())):
		_print(f"\x1b[38;2;200;40;20mInvalid FQBN '{':'.join(fqbn)}'\x1b[38;2;200;40;20m.")
		kernel32.ExitProcess(1)
	h_pm=h_pm[fqbn[2]]
	_print(f"Reading File '{h_fp}platform.txt'\x1b[38;2;100;100;100m...")
	with open(h_fp+"platform.txt","r") as hp_f:
		p_pm={k.split("=")[0]:k[len(k.split("=")[0])+1:] for k in hp_f.read().replace("\r\n","\n").split("\n") if len(k.strip())>0 and k.strip()[0]!="#"}
	_print(f"Generating Upload Properties\x1b[38;2;100;100;100m...")
	up={**p_pm,**h_pm,"serial.port":p,"serial.port.file":p,"runtime.platform.path":h_fp}
	for k,v in list(up.items()):
		if (k.startswith(f"tools.{h_pm[('bootloader.tool' if bb is True else 'upload.tool')]}.")):
			up[k[len(h_pm[("bootloader.tool" if bb is True else "upload.tool")])+7:]]=v
	if (bb is False):
		up["build.path"]=o_fp
		for e in os.listdir(o_fp):
			if (e[-4:]==".hex"):
				up["build.project_name"]=e.split(".")[0]
				break
	for k in "upload,program,erase,bootloader".split(","):
		up[f"{k}.verbose"]=up.get(f"{k}.params.quiet","")
	for k in ("upload","program"):
		up[f"{k}.verify"]=up.get(f"{k}.params.{('no' if vu is False else '')}verify","")
	_print(f"Loading Tools\x1b[38;2;100;100;100m...")
	for v in os.listdir(__file_base_dir__+f"arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb is True else 'upload.tool')]}/"):
		up[f"runtime.tools.{h_pm[('bootloader.tool' if bb is True else 'upload.tool')]}-{v}.path"]=_get_inner_dir(__file_base_dir__+f"arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb is True else 'upload.tool')]}/{v}/")
	up[f"runtime.tools.{h_pm[('bootloader.tool' if bb is True else 'upload.tool')]}.path"]=__file_base_dir__+f"arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb is True else 'upload.tool')]}/{v}/{h_pm[('bootloader.tool' if bb is True else 'upload.tool')]}"
	_print("Expanding Upload Properties\x1b[38;2;100;100;100m...")
	for k,v in up.items():
		while ("{" in v):
			v=ARDUINO_COMMAND_FORMAT_REGEX.sub(lambda m:(up[m.group(1)] if m.group(1) in up else ""),v)
		up[k]=v
	if (bb is False):
		_print("Setting Board in Bootloader Mode\x1b[38;2;100;100;100m...")
		if (bool(up.get("upload.use_1200bps_touch","False")) is True):
			_print("\x1b[38;2;200;40;20m1200Bps Touch not Implemented Yet.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
		if (bool(up.get("upload.wait_for_upload_port","False")) is True):
			_print("Searching For Avaible Boards\x1b[38;2;100;100;100m...")
			b=None
			for usb_b in _list_arduino_boards():
				if (usb_b["fqbn"]==":".join(fqbn)):
					if (usb_b["location"]==p or b is None):
						b=usb_b
			if (b is None):
				_print("\x1b[38;2;200;40;20mNo Boards Found.\x1b[0m Stopping Upload\x1b[38;2;100;100;100m...")
				kernel32.ExitProcess(1)
			up.update({"serial.port":b["location"],"serial.port.file":b["location"]})
		_print(f"Uploading Program to Board on Port '{p}'\x1b[38;2;100;100;100m...")
		_run_process(up["upload.pattern"])
	else:
		_print("Erasing Board\x1b[38;2;100;100;100m...")
		_run_process(up["erase.pattern"])
		_print("Burning Bootloader to Board\x1b[38;2;100;100;100m...")
		_run_process(up["bootloader.pattern"])
	_print("Upload Finished")



def _open_project_file(d,e,*f):
	ok=False
	for fn in f:
		if (os.path.isfile(fn)):
			_run_process(f"\"{EDITOR_FILE_PATH}\" \"{fn}\"")
			ok=True
	if (ok):
		return
	for r,_,fl in os.walk(d):
		r=r.replace("\\","/").rstrip("/")+"/"
		for f in fl:
			if (f.endswith(e)):
				_run_process(f"\"{EDITOR_FILE_PATH}\" \"{r+f}\"")
				return



def _create_project(t,nm,op):
	if (nm is not None):
		t=t.lower()
		if (t not in VALID_PROGRAM_TYPES):
			_print(f"\x1b[38;2;200;40;20mUnknown Project Type '{t}'.",df=True)
			kernel32.ExitProcess(1)
		nm=nm.replace("_"," ").lower().title().replace(" ","_")
		p=PROJECT_DIR+f"{t.title()}-{nm}/"
		cr=False
		if (not os.path.exists(p)):
			cr=True
			os.mkdir(p)
		b_fp=__file_base_dir__+f"templates/{t.lower()}/"
	else:
		p=__file_base_dir__
		b_fp=__file_base_dir__+"templates/python/"
		t="python"
		nm="Boot_Program"
		cr=False
	if (not os.path.exists(p+".gitrepo")):
		for r,dl,fl in os.walk(b_fp):
			r=r.replace("\\","/").rstrip("/")+"/"
			pr=p+r[len(b_fp):].replace("$$$NAME$$$",nm.lower())
			if (cr is False and r!=b_fp):
				break
			for d in dl:
				d=d.replace("$$$NAME$$$",nm.lower())
				if (not os.path.exists(pr+d)):
					os.mkdir(pr+d)
			for f in fl:
				pf=f.replace("$$$NAME$$$",nm.lower())
				if (not os.path.exists(pr+pf)):
					with open(pr+pf,"xb") as wf,open(r+f,"rb") as rf:
						wf.write(rf.read().replace(b"$$$YEAR$$$",bytes(str(int(time.time()//31556926+1970)),"utf-8")).replace(b"$$$PRETTY_TITLE$$$",bytes(f"{t.title()} - {nm.replace('_',' ').title()}","utf-8")).replace(b"$$$NAME$$$",bytes(nm.lower(),"utf-8")).replace(b"$$$UPPERCASE_NAME$$$",bytes(nm.upper(),"utf-8")).replace(b"$$$TITLE_NAME$$$",bytes(nm.replace("_"," ").title(),"utf-8")))
				if (f[0]=="."):
					kernel32.SetFileAttributesW(pr+pf,FILE_ATTRIBUTE_ARCHIVE|FILE_ATTRIBUTE_HIDDEN)
	if (op is True):
		_run_process(f"\"{EDITOR_FILE_PATH}\" --add \"{p}\"")
		if (t=="arduino"):
			_open_project_file(p,"ino",p+"src/main.ino")
		elif (t=="assembly"):
			_open_project_file(p,"asm",p+"src/main.asm")
		elif (t=="c"):
			_open_project_file(p,"c",p+"src/main.c")
		elif (t=="cpp"):
			_open_project_file(p,"cpp",p+"src/main.cpp")
		elif (t=="css"):
			_open_project_file(p,"css",p+"src/index.html",p+"src/style/main.css")
		elif (t=="java"):
			_open_project_file(p,"java",p+f"src/com/krzem/{nm.lower()}/Main.java")
		elif (t=="javascript"):
			_open_project_file(p,"js",p+"src/index.html",p+"src/js/main.js")
		elif (t=="php"):
			_open_project_file(p,"php",p+"src/index.php")
		elif (t=="processing"):
			_open_project_file(p,"pde",p+"src/Main.pde")
		else:
			_open_project_file(p,"py",p+"src/main.py")



class _Serial_UI:
	def __init__(self,sz):
		self._sz=sz
		self._o=[f"\x1b[0m\x1b[48;2;24;24;24m{' '*(self._sz[0]-1)}",f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ╔{'═'*(self._sz[0]-9)}╗   ",*(f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ║{' '*(self._sz[0]-9)}\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m║   ",)*(self._sz[1]-5),f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ╚{'═'*(self._sz[0]-9)}╝   ",f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m{' '*(self._sz[0]-1)}"]
		self._m=0
		self._t=0
		self._inp_bf=""
		self._pl=None
		self._pi=0
		self._p=None
		self._p_s=None
		self._dt=[]
		self._k=None
		self._off=[0,0]
		self._a_s=True
		self._mem=[""]
		self._mem_i=0
		self._b_tm=-1
		self._b=True
		self._nm_d_tm=-1
		self._nm_d=True
		self._cl_cache=[]
		self._dl=[]



	def loop(self):
		while (True):
			self._o=[f"\x1b[0m\x1b[48;2;24;24;24m{' '*(self._sz[0]-1)}",f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ╔{'═'*(self._sz[0]-9)}╗   ",*(f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ║{' '*(self._sz[0]-9)}\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m║   ",)*(self._sz[1]-5),f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ╚{'═'*(self._sz[0]-9)}╝   ",f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m{' '*(self._sz[0]-1)}"]
			ud=False
			if (msvcrt.kbhit()==1):
				k=msvcrt.getch()
				if (k==b"\x03"):
					if (self._m==0):
						break
					elif (self._m==1):
						kernel32.SetCommTimeouts(self._p_s[0],self._p_s[1])
						if (not kernel32.GetOverlappedResult(self._p_s[0],ctypes.byref(self._p_s[2]),ctypes.byref(ctypes.wintypes.DWORD()),False) and kernel32.GetLastError() in (ERROR_IO_PENDING,ERROR_IO_INCOMPLETE)):
							kernel32.CancelIoEx(self._p_s[0],self._p_s[2])
						kernel32.CloseHandle(self._p_s[2].hEvent)
						if (not kernel32.GetOverlappedResult(self._p_s[0],ctypes.byref(self._p_s[3]),ctypes.byref(ctypes.wintypes.DWORD()),False) and kernel32.GetLastError() in (ERROR_IO_PENDING,ERROR_IO_INCOMPLETE)):
							kernel32.CancelIoEx(self._p_s[0],self._p_s[3])
						kernel32.CloseHandle(self._p_s[3].hEvent)
						kernel32.CloseHandle(self._p_s[0])
						self._m=0
						self._t=0
						self._pl=None
						self._pi=0
						self._p=None
						self._p_s=None
						self._inp_bf=""
						self._dt=[]
						self._off=[0,0]
						self._a_s=True
						self._mem=[""]
						self._mem_i=0
						self._b_tm=-1
						self._b=True
						self._nm_d_tm=-1
						self._nm_d=True
						self._cl_cache=[]
						self._dl=[]
				elif (k==b"\xe0"):
					self._k=(k,msvcrt.getch())
				else:
					self._k=(k,b"")
			else:
				self._k=(b"",b"")
			if (self._m==0):
				if (self._k[0]==b"r" or self._pl is None):
					self._pl=_list_arduino_boards()
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"H"):
					self._pi=((self._pi-1)+len(self._pl))%len(self._pl)
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"P"):
					self._pi=(self._pi+1)%len(self._pl)
					ud=True
				elif (self._k[0]==b"\r"):
					if (len(self._pl)>0):
						ud=True
						self._p=self._pl[self._pi]
						h=kernel32.CreateFileW(f"\\\\.\\{self._p['location']}",GENERIC_READ|GENERIC_WRITE,0,None,OPEN_EXISTING,FILE_ATTRIBUTE_NORMAL|FILE_FLAG_OVERLAPPED,0)
						if (h!=INVALID_HANDLE_VALUE):
							kernel32.SetupComm(h,4096,4096)
							o_tm=ctypes.wintypes.COMMTIMEOUTS()
							kernel32.GetCommTimeouts(h,ctypes.byref(o_tm))
							n_tm=ctypes.wintypes.COMMTIMEOUTS()
							n_tm.ReadTotalTimeoutConstant=max(SERIAL_TIMEOUT,1)
							kernel32.SetCommTimeouts(h,ctypes.byref(n_tm))
							kernel32.SetCommMask(h,EV_ERR)
							comDCB=ctypes.wintypes.DCB()
							kernel32.GetCommState(h,ctypes.byref(comDCB))
							comDCB.BaudRate=SERIAL_BAUD
							comDCB.ByteSize=8
							comDCB.Parity=NOPARITY
							comDCB.StopBits=ONESTOPBIT
							comDCB.fBinary=1
							comDCB.fRtsControl=RTS_CONTROL_ENABLE
							comDCB.fOutxCtsFlow=False
							comDCB.fDtrControl=DTR_CONTROL_ENABLE
							comDCB.fOutxDsrFlow=False
							comDCB.fOutX=False
							comDCB.fInX=False
							comDCB.fNull=0
							comDCB.fErrorChar=0
							comDCB.fAbortOnError=0
							comDCB.XonChar=b"\x11"
							comDCB.XoffChar=b"\x13"
							if (not kernel32.SetCommState(h,ctypes.byref(comDCB))):
								kernel32.SetCommTimeouts(h,o_tm)
								kernel32.CloseHandle(h)
							else:
								kernel32.PurgeComm(h,PURGE_TXCLEAR|PURGE_TXABORT|PURGE_RXCLEAR|PURGE_RXABORT)
								self._p_s=(h,o_tm,ctypes.wintypes.OVERLAPPED(),ctypes.wintypes.OVERLAPPED())
								self._p_s[2].hEvent=kernel32.CreateEventW(None,1,0,None)
								self._p_s[3].hEvent=kernel32.CreateEventW(None,0,0,None)
								self._m=1
				tb_h={"name":("Name","#8ae8c6"),"arch":("Arch","#dbdf0c"),"fqbn":("FQBN","#e386d0"),"location":("Location","#59c51e")}
				mx_l=[max([len(tb_h[list(tb_h.keys())[i]][0])]+[len(e[k]) for e in self._pl])+2 for i,k in enumerate(list(tb_h.keys()))]
				off=((self._sz[0]-9-(sum(mx_l)+len(list(tb_h.keys()))+1))//2,3)
				self._set(off[0],off[1],"\x1b[38;2;156;156;156m┌"+"┬".join(["─"*mx_l[i] for i in range(0,len(mx_l))])+"┐")
				self._set(off[0],off[1]+1,"\x1b[38;2;156;156;156m│"+"\x1b[38;2;156;156;156m│".join([f"\x1b[38;2;{min(255,int(tb_h[e][1][1:3],16)+65)};{min(255,int(tb_h[e][1][3:5],16)+65)};{min(255,int(tb_h[e][1][5:7],16)+65)}m"+tb_h[e][0].center(mx_l[i]," ") for i,e in enumerate(list(tb_h.keys()))])+"\x1b[38;2;156;156;156m│")
				self._set(off[0],off[1]+2,"\x1b[38;2;156;156;156m├"+"┼".join(["─"*mx_l[i] for i in range(0,len(mx_l))])+"┤")
				for i,k in enumerate(self._pl):
					self._set(off[0],off[1]+i+3,"\x1b[38;2;156;156;156m│"+"\x1b[38;2;156;156;156m│".join([f"\x1b[38;2;{max(0,int(tb_h[e][1][1:3],16)-(0 if i%2==0 else 65))};{max(0,int(tb_h[e][1][3:5],16)-(0 if i%2==0 else 65))};{max(0,int(tb_h[e][1][5:7],16)-(0 if i%2==0 else 65))}m"+("\x1b[48;2;37;37;37m" if i==self._pi else "")+k[e].center(mx_l[j]," ") for j,e in enumerate(list(tb_h.keys()))])+"\x1b[48;2;24;24;24m\x1b[38;2;156;156;156m│")
				self._set(off[0],off[1]+len(self._pl)+3,"\x1b[38;2;156;156;156m└"+"┴".join(["─"*mx_l[i] for i in range(0,len(mx_l))])+"┘")
			elif (self._m==1):
				n_dt=False
				inp_ch=False
				if (self._k[0]==b"\r"):
					if (len(self._inp_bf)>0):
						dt=bytes(self._inp_bf,"utf-8")
						c=ctypes.wintypes.DWORD()
						if (kernel32.WriteFile(self._p_s[0],dt,len(dt),ctypes.byref(c),self._p_s[3]) or kernel32.GetLastError() in (ERROR_SUCCESS,ERROR_IO_PENDING)):
							kernel32.GetOverlappedResult(self._p_s[0],self._p_s[3],ctypes.byref(c),True)
							if (self._inp_bf in self._mem):
								self._mem.remove(self._inp_bf)
							self._mem=self._mem[:-1]+[self._inp_bf,""]
							self._mem_i=len(self._mem)-1
							self._extend(1,self._inp_bf+"\n")
							self._inp_bf=""
							self._off[1]=0
							n_dt=True
							inp_ch=True
							ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"\x8d"):
					self._a_s=False
					self._off[0]=max(0,self._off[0]-1)
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"\x91"):
					self._off[0]+=1
					ud=True
					if (self._off[0]>=sum([len(e[1])-(1 if None in e else 0) for e in self._dt])):
						self._a_s=True
						self._off[0]=sum([len(e[1])-(1 if None in e else 0) for e in self._dt])
				elif (self._k[0]==b"\xe0" and self._k[1]==b"w"):
					self._a_s=False
					self._off[0]=0
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"u"):
					self._a_s=True
					self._off[0]=sum([len(e[1])-(1 if None in e else 0) for e in self._dt])
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"H"):
					if (self._mem_i!=0):
						inp_ch=True
					self._mem_i=max(0,self._mem_i-1)
					self._inp_bf=self._mem[self._mem_i]
					self._off[1]=len(self._inp_bf)
					inp_ch=True
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"P"):
					if (self._mem_i!=len(self._mem)-1):
						inp_ch=True
					self._mem_i=min(len(self._mem)-1,self._mem_i+1)
					self._inp_bf=self._mem[self._mem_i]
					self._off[1]=len(self._inp_bf)
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"K"):
					if (self._off[1]!=0):
						inp_ch=True
					self._off[1]=max(0,self._off[1]-1)
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"M"):
					if (self._off[1]!=len(self._inp_bf)):
						inp_ch=True
					self._off[1]=min(self._off[1]+1,len(self._inp_bf))
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"G"):
					if (self._off[1]!=0):
						inp_ch=True
					self._off[1]=0
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"O"):
					if (self._off[1]!=len(self._inp_bf)):
						inp_ch=True
					self._off[1]=len(self._inp_bf)
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"S"):
					t=self._inp_bf+""
					self._inp_bf=self._inp_bf[:self._off[1]]+self._inp_bf[self._off[1]+1:]
					if (t!=self._inp_bf):
						inp_ch=True
					ud=True
				elif (self._k[0]==b"\b"):
					t=self._inp_bf
					self._inp_bf=self._inp_bf[:max(self._off[1]-1,0)]+self._inp_bf[self._off[1]:]
					self._off[1]=max(self._off[1]-1,0)
					if (t!=self._inp_bf):
						inp_ch=True
					ud=True
				elif (self._k[0]==b"\x0c"):
					self._dt=[]
					ud=True
				elif (self._k[0]==b"\xe0" and self._k[1]==b"\x92"):# CTRL + Insert
					self._t=1-self._t
					ud=True
				elif (len(self._k[0])==1 and self._k[0][0]>31 and self._k[0][0]<127):
					self._inp_bf=self._inp_bf[:self._off[1]]+repr(self._k[0])[2:-1]+self._inp_bf[self._off[1]:]
					self._off[1]+=len(repr(self._k[0])[2:-1])
					inp_ch=True
					ud=True
				ql=ctypes.wintypes.COMSTAT()
				if (not kernel32.ClearCommError(self._p_s[0],ctypes.byref(ctypes.wintypes.DWORD()),ctypes.byref(ql))):
					ql.cbInQue=0
				if (ql.cbInQue>0):
					kernel32.ResetEvent(self._p_s[2].hEvent)
					bf=ctypes.create_string_buffer(ql.cbInQue)
					bf_l=ctypes.wintypes.DWORD()
					if ((kernel32.ReadFile(self._p_s[0],bf,ql.cbInQue,ctypes.byref(bf_l),ctypes.byref(self._p_s[2])) or kernel32.GetLastError() in (ERROR_SUCCESS,ERROR_IO_PENDING)) and (kernel32.GetOverlappedResult(self._p_s[0],ctypes.byref(self._p_s[2]),ctypes.byref(bf_l),True) or kernel32.GetLastError()==ERROR_OPERATION_ABORTED)):
						self._extend(0,ARDUINO_DATA_LINE_SEPARATOR_REGEX.sub(r"\1",str(bf.raw[:bf_l.value],"utf-8")).replace("\t","    "))
						n_dt=True
						ud=True
				if (self._a_s is True and n_dt is True):
					self._dt=self._dt[-1000:]
					self._off[0]=max(0,sum([len(e[1])-(1 if None in e[1] else 0) for e in self._dt])-(self._sz[1]-9))
					ud=True
				if (inp_ch is False and self._b_tm<time.time()):
					self._b=not self._b
					self._b_tm=time.time()+0.65
					ud=True
				elif (inp_ch is True):
					self._b=True
					self._b_tm=time.time()+0.65
					ud=True
				if (self._nm_d_tm==-1):
					self._nm_d_tm=time.time()+2
				elif (self._nm_d_tm<time.time()):
					self._nm_d=not self._nm_d
					self._nm_d_tm=time.time()+2
					ud=True
				if (self._nm_d is True):
					self._set(4,2,self._p["name"].center(self._sz[0]-9).replace(self._p["name"],f"\x1b[38;2;89;189;240m{self._p['name']}"))
				else:
					self._set(4,2,self._p["fqbn"].center(self._sz[0]-9).replace(self._p["fqbn"],f"\x1b[38;2;255;199;255m{self._p['fqbn']}"))
				self._set(5,2,f"\x1b[38;2;154;255;95m{self._p['location']}")
				self._set(self._sz[0]-13,2,f"\x1b[38;2;{('255;85;95','115;35;60')[self._t]}mTXT \x1b[38;2;{('255;85;95','115;35;60')[1-self._t]}mPLT")
				self._set(4,self._sz[1]-4,"\x1b[38;2;207;207;207m"+"".join([(e if i!=self._off[1] else f"\x1b[{('2' if self._b is False else '')}4m{e}\x1b[24m") for i,e in enumerate(list(self._inp_bf+" "))]))
				if (self._t==0):
					self._set(3,3,f"╠{'═'*(self._sz[0]-9)}╣")
					self._set(3,self._sz[1]-5,f"╠{'═'*(self._sz[0]-9)}╣")
					l=[]
					for k in self._dt:
						for i,e in enumerate(k[1]):
							if (e is not None):
								l.append(((True if i==0 else False),k[0],e))
					for i,k in enumerate(l[self._off[0]:self._off[0]+self._sz[1]-9]):
						if (i==0 or k[0] is True):
							self._set(4,i+4,("\x1b[38;2;255;135;5m","\x1b[38;2;180;230;60m")[k[1]]+f"{'»«'[k[1]]} {k[2]}")
						else:
							self._set(6,i+4,("\x1b[38;2;255;135;5m","\x1b[38;2;180;230;60m")[k[1]]+k[2])
				else:
					l=[]
					for k in self._dt[::-1]:
						if (k[0]!=0 or None not in k[1]):
							continue
						for e in k[1][::-1]:
							if (e is not None and ARDUINO_SERIAL_PLOT_DATA_REGEX.fullmatch(e) is not None):
								l.append([float(se) for se in e.split(",")])
						if (len(l)>=self._sz[0]-11):
							l=l[:self._sz[0]-11]
							break
					if (len(l)>0):
						while (len(self._cl_cache)<max([len(e) for e in l])):
							h=(len(self._cl_cache)*211)%360/30
							self._cl_cache.append(f"\x1b[38;2;{int(192-64*max(min((h)%12-3,9-(h)%12,1),-1))};{int(192-64*max(min((h+8)%12-3,9-(h+8)%12,1),-1))};{int(192-64*max(min((h+4)%12-3,9-(h+4)%12,1),-1))}m")
						r=(min([min(e) for e in l]),max([max(e) for e in l]),self._sz[1]-10,0)
						if (r[0]==r[1]):
							r=(r[0]-1,r[1]+1,r[2],r[3])
						m=[[" ","\x1b[38;2;92;92;92m┤"]+[" " for _ in range(0,self._sz[0]-11)] for _ in range(0,self._sz[1]-9)]
						dt=[[] for _ in range(0,max([len(e)for e in l]))]
						for e in l:
							for j,se in enumerate(e):
								dt[j]=[int((se-r[0])/(r[1]-r[0])*(r[3]-r[2])+r[2])]+dt[j]
						dt=[e for e in dt if len(e)>0]
						if (len(dt)>0):
							if (len(self._dl)<len(dt)):
								self._dl+=list(range(len(self._dl),len(dt)))
							self._set(0,0,repr(self._dl))
							for i in self._dl[::-1]:
								m[dt[i][0]][1]=m[dt[i][0]][1][:-1]+"┼"
								for j in range(len(dt[i])-1,-1,-1):
									v=([dt[i][0]]+dt[i])[j:j+2]
									if (j==len(dt[i])-1):
										m[v[1]][j+2]=self._cl_cache[i]+"╵╴╷"[(0 if v[0]<v[1] else (1 if v[0]==v[1] else 2))]
									else:
										m[v[1]][j+2]=self._cl_cache[i]+"└─┌"[(0 if v[0]<v[1] else (1 if v[0]==v[1] else 2))]
									if (v[0]!=v[1]):
										m[v[0]][j+2]=self._cl_cache[i]+"┐ ┘"[(0 if v[0]<v[1] else (1 if v[0]==v[1] else 2))]
										if (v[0]<v[1]):
											for k in range(v[0]+1,v[1]):
												m[k][j+2]=f"{self._cl_cache[i]}│"
										else:
											for k in range(v[1]+1,v[0]):
												m[k][j+2]=f"{self._cl_cache[i]}│"
							self._set(3,3,f"╠═╤{'═'*(self._sz[0]-11)}╣")
							self._set(3,self._sz[1]-5,f"╠═╧{'═'*(self._sz[0]-11)}╣")
							for i in range(0,len(m)):
								self._set(4,i+4,"".join(m[i]))
					if (len(l)==0):
						self._set(3,3,f"╠{'═'*(self._sz[0]-9)}╣")
						self._set(3,self._sz[1]-5,f"╠{'═'*(self._sz[0]-9)}╣")
						self._set(4,self._sz[1]//2,"\x1b[38;2;115;80;55m"+"[No Data]".center(self._sz[0]-9))
			if (ud is True):
				sys.__stdout__.write("\x1b[0;0H\x1b[2J"+"\n".join(self._o)+"\x1b[0m")
				sys.__stdout__.flush()



	def _set(self,x,y,v):
		i=0
		j=0
		while (i<len(self._o[y])):
			m=REMOVE_COLOR_FORMATTING_REGEX.match(self._o[y][i:])
			if (m is not None):
				i+=len(m.group(0))
				continue
			if (j==x):
				k=i+0
				l=j+0
				em=""
				while (l<len(self._o[y])):
					m=REMOVE_COLOR_FORMATTING_REGEX.match(self._o[y][k:])
					if (m is not None):
						em+=m.group(0)
						k+=len(m.group(0))
						continue
					if (l==j+len(REMOVE_COLOR_FORMATTING_REGEX.sub("",v))):
						break
					em=""
					k+=1
					l+=1
				self._o[y]=self._o[y][:i]+v+em+self._o[y][k:]
				return
			i+=1
			j+=1



	def _extend(self,i,v):
		e=False
		if (v[-1]=="\n"):
			e=True
			v=v[:-1]
		if ("\n" in v):
			for j,k in enumerate(v.split("\n")):
				self._extend(i,k+("\n" if j<len(v.split("\n"))-1 or e is True else ""))
			return
		l=[j for j,e in enumerate(self._dt) if e[0]==i]
		if (len(l)==0 or self._dt[l[-1]][1][-1] is None):
			self._dt.append([i,[""]])
			i=len(self._dt)-1
			j=0
		else:
			i=l[-1]
			j=len(self._dt[i][1])-1
		k=0
		while (True):
			nk=self._sz[0]-12-len(self._dt[i][1][j])
			self._dt[i][1][j]+=v[k:self._sz[0]-12-len(self._dt[i][1][j])]
			if (nk>=len(v)):
				break
			j+=1
			k=nk
			self._dt[i][1].append("")
		if (e is True):
			self._dt[i][1].append(None)
		if (len(self._dt)>128):
			self._dt=self._dt[-128:]



def _u_mcs(fp):
	fp=os.path.abspath(fp).replace("\\","/").rstrip("/")+"/"
	_print(f"Starting Minecraft Server in Folder '{fp}'\x1b[38;2;100;100;100m...")
	if (not os.path.exists(fp)):
		_print("\x1b[38;2;200;40;20mMinecraft Server Folder Missing.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		return
	_print("Downloading Metadata\x1b[38;2;100;100;100m...")
	try:
		for k in requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").json()["versions"]:
			if (k["id"] not in MINECRAFT_SKIP_UPDATE):
				dw=True
				json=requests.get(k["url"]).json()
				if (os.path.exists(fp+"server.jar")):
					dw=False
					_print("Inspecting Current Version\x1b[38;2;100;100;100m...")
					sz=os.stat(fp+"server.jar").st_size
					_print(f"File Size: {sz}, New Size: {json['downloads']['server']['size']}")
					if (sz!=json["downloads"]["server"]["size"]):
						dw=True
					else:
						h=SHA1_START_VALUE.copy()
						hl=0
						h_bf=b""
						j=0
						lp=-1
						with open(fp+"server.jar","rb") as f:
							dt=f.read(FILE_READ_CHUNK_SIZE)
							while (len(dt)>0):
								j+=FILE_READ_CHUNK_SIZE
								if (j>sz):
									j=sz
								p=int(j*100/sz)
								if (p>lp):
									lp=p
									_print(f"\x1b[38;2;100;100;100m{p}% Hashed...")
								hl+=len(dt)
								h_bf+=dt
								i=0
								while (i+64<=len(h_bf)):
									h=_sha1_chunk(h,h_bf[i:i+64])
									i+=64
								h_bf=h_bf[i:]
								dt=f.read(FILE_READ_CHUNK_SIZE)
						h_bf+=b"\x80"+b"\x00"*((56-(hl+1)%64)%64)+bytes([hl>>53,(hl>>45)&0xff,(hl>>37)&0xff,(hl>>29)&0xff,(hl>>21)&0xff,(hl>>13)&0xff,(hl>>5)&0xff,(hl<<3)&0xff])
						i=0
						while (i<len(h_bf)):
							h=_sha1_chunk(h,h_bf[i:i+64])
							i+=64
						_print(f"File Hash: {h[0]:08x}{h[1]:08x}{h[2]:08x}{h[3]:08x}{h[4]:08x}, New Hash: {json['downloads']['server']['sha1']}")
						if (f"{h[0]:08x}{h[1]:08x}{h[2]:08x}{h[3]:08x}{h[4]:08x}"!=json["downloads"]["server"]["sha1"]):
							dw=True
					if (dw is True):
						if (not os.path.exists(fp+"backup")):
							os.mkdir(fp+"backup")
						nm="backup/world-backup_"+json["id"]
						while (os.path.exists(fp+nm+".zip")):
							nm+="_"
						nm+=".zip"
						_print(f"Creating Backup ('{nm}')\x1b[38;2;100;100;100m...")
						with zipfile.ZipFile(fp+nm,"w") as zf:
							for r,dl,fl in os.walk(fp+"world"):
								r=r.replace("\\","/").rstrip("/")+"/"
								nr=r[len(fp+"world/"):]
								for f in fl:
									try:
										with open(r+f,"rb") as rf:
											zf.writestr(nr+f,rf.read())
									except PermissionError:
										_print(f"Skipping File '{r+f}', Permission Error\x1b[38;2;100;100;100m...")
						dw=True
				if (dw is True):
					_print(f"Downloading Server For {json['id']} ('{json['downloads']['server']['url']}')\x1b[38;2;100;100;100m...")
					r=requests.get(json["downloads"]["server"]["url"],stream=True).raw
					with open(fp+"server.jar","wb") as f:
						while (True):
							dt=r.read(FILE_READ_CHUNK_SIZE)
							f.write(dt)
							if (len(dt)<FILE_READ_CHUNK_SIZE):
								break
				break
	except requests.exceptions.ConnectionError:
		_print("\x1b[38;2;200;40;20mNo Internet Connection.\x1b[0m Skipping Update Check\x1b[38;2;100;100;100m...")
	_print("Starting Server\x1b[38;2;100;100;100m...")
	_create_process(f"\"{CMD_FILE_PATH}\" /c \"^\"{__executable__}^\" ^\"{__file__}^\" 7 ^\"{fp}^\"\"")



def _hotkey_handler(c,wp,lp):
	try:
		dt=ctypes.cast(lp,ctypes.POINTER(ctypes.wintypes.KBDLLHOOKSTRUCT)).contents
		if (dt.vkCode!=VK_PACKET and (dt.flags&(LLKHF_INJECTED|LLKHF_ALTDOWN))==0 and (dt.flags&LLKHF_UP)==0):
			if (dt.vkCode==0xa5 and _hotkey_handler._ig_alt):
				_hotkey_handler._ig_alt=False
			else:
				vk=dt.vkCode
				if (dt.scanCode==0x21d and vk==0xa2):
					_hotkey_handler._ig_alt=True
				if (wp in (WM_KEYDOWN,WM_SYSKEYDOWN) and vk in _hotkey_handler._hk and user32.GetAsyncKeyState(VK_CONTROL)!=0 and user32.GetAsyncKeyState(VK_SHIFT)!=0 and user32.GetAsyncKeyState(VK_MENU)!=0):
						_hotkey_handler._hk[vk]()
	except Exception:
		user32.PostMessageW(None,HOTKEY_HANDLER_END_MESSAGE,0,0)
	return user32.CallNextHookEx(None,c,wp,lp)



def _screen_blocker_keyboard_handler(c,wp,lp):
	dt=ctypes.cast(lp,ctypes.POINTER(ctypes.wintypes.KBDLLHOOKSTRUCT)).contents
	if (dt.vkCode==0x1b):
		user32.PostMessageW(None,HOTKEY_HANDLER_END_MESSAGE,0,0)
	else:
		return -1
	return user32.CallNextHookEx(None,c,wp,lp)



def _screen_blocker_wnd_proc(hwnd,msg,wp,lp):
	if (msg==WM_KILLFOCUS):
		user32.SetFocus(hwnd)
		return 0
	return user32.DefWindowProcW(hwnd,msg,wp,lp)



def _check_close(t):
	if (user32.MessageBoxW(None,"Close?","Close",MB_YESNO|MB_ICONQUESTION|MB_DEFBUTTON2|MB_SYSTEMMODAL)==IDYES):
		th=ctypes.wintypes.HANDLE()
		tkp=ctypes.wintypes.TOKEN_PRIVILEGES()
		advapi32.OpenProcessToken(kernel32.GetCurrentProcess(),TOKEN_ADJUST_PRIVILEGES|TOKEN_QUERY,ctypes.byref(th))
		advapi32.LookupPrivilegeValueW(None,SE_SHUTDOWN_NAME,ctypes.byref(tkp.Privileges[0].Luid))
		tkp.PrivilegeCount=1
		tkp.Privileges[0].Attributes=SE_PRIVILEGE_ENABLED
		advapi32.AdjustTokenPrivileges(th,False,ctypes.byref(tkp),0,None,None)
		if (t==0):
			user32.ExitWindowsEx(EWX_LOGOFF,SHTDN_REASON_MAJOR_OTHER|SHTDN_REASON_MINOR_OTHER|SHTDN_REASON_FLAG_PLANNED)
		else:
			user32.ExitWindowsEx(EWX_FORCE|EWX_FORCEIFHUNG|EWX_POWEROFF|EWX_SHUTDOWN,SHTDN_REASON_MAJOR_OTHER|SHTDN_REASON_MINOR_OTHER|SHTDN_REASON_FLAG_PLANNED)



kernel32.SetConsoleMode(kernel32.GetStdHandle(STD_OUTPUT_HANDLE),ctypes.wintypes.DWORD(7))
kernel32.SetConsoleTitleW("")
hwnd=kernel32.GetConsoleWindow()
user32.SendMessageW(hwnd,WM_SETICON,ICON_SMALL,user32.LoadImageW(0,__file_base_dir__+CUSTOM_ICON_FILE_PATH,IMAGE_ICON,16,16,LR_LOADFROMFILE))
user32.SendMessageW(hwnd,WM_SETICON,ICON_BIG,user32.LoadImageW(0,__file_base_dir__+CUSTOM_ICON_FILE_PATH,IMAGE_ICON,32,32,LR_LOADFROMFILE))
if (len(GITHUB_TOKEN)!=40):
	_print("\x1b[38;2;200;40;20mInvalid Github Token.\x1b[0m Project Push will Fail\x1b[38;2;100;100;100m...")
if (len(sys.argv)==1):
	if (sys.executable.replace("\\","/")!=__headless_executable__):
		_create_process(f"\"{__headless_executable__}\" \"{__file__}\"")
	else:
		move_to_desktop.switch_to_desktop(0)
		_create_process(f"\"{__executable__}\" \"{__file__}\" 7")
		for k in os.listdir(PROJECT_DIR):
			_create_project(k.split("-")[0],k[len(k.split("-")[0])+1:],False)
		_create_process(f"\"{CMD_FILE_PATH}\" /c \"^\"{__executable__}^\" ^\"{__file__}^\" 4\"")
		_hotkey_handler._hk={}
		_hotkey_handler._ig_alt=False
		kb_cb=ctypes.wintypes.LowLevelKeyboardProc(_hotkey_handler)
		hk=user32.SetWindowsHookExW(WH_KEYBOARD_LL,kb_cb,kernel32.GetModuleHandleW(None),ctypes.wintypes.DWORD(0))
		_hotkey_handler._hk[0x23]=lambda:_check_close(1)
		_hotkey_handler._hk[0x24]=lambda:_check_close(0)
		_hotkey_handler._hk[0x31]=lambda:_create_process(f"\"{__headless_executable__}\" \"{__file__}\" 8 0")
		_hotkey_handler._hk[0x32]=lambda:_create_process(f"\"{__headless_executable__}\" \"{__file__}\" 8 1")
		_hotkey_handler._hk[0x33]=lambda:_create_process(f"\"{__headless_executable__}\" \"{__file__}\" 8 2")
		_hotkey_handler._hk[0x49]=lambda:_create_process(f"\"{__executable__}\" \"{__file__}\" 7")
		_hotkey_handler._hk[0x51]=lambda:_create_process(f"\"{__executable__}\" \"{__file__}\" 1")
		_hotkey_handler._hk[0x52]=lambda:_create_process(f"\"{__headless_executable__}\" \"{__file__}\" 0")
		_hotkey_handler._hk[0x57]=lambda:shell32.ShellExecuteW(None,"open",ROOT_FILE_PATH,None,None,SW_SHOWMAXIMIZED)
		msg=ctypes.wintypes.MSG()
		while (True):
			e=user32.GetMessageW(ctypes.byref(msg),None,0,0)
			if (e==-1):
				break
			if (e!=0):
				if (msg.message==HOTKEY_HANDLER_END_MESSAGE):
					break
				user32.TranslateMessage(ctypes.byref(msg))
				user32.DispatchMessageW(ctypes.byref(msg))
		user32.UnhookWindowsHookEx(hk)
else:
	v=int(sys.argv[1])
	if (v==0):
		mh=kernel32.GetModuleHandleW(None)
		wc=ctypes.wintypes.WNDCLASSEXW()
		wc.cbSize=ctypes.sizeof(ctypes.wintypes.WNDCLASSEXW)
		wc.style=0
		wc.lpfnWndProc=ctypes.wintypes.WNDPROC(_screen_blocker_wnd_proc)
		wc.cbClsExtra=0
		wc.cbWndExtra=0
		wc.hInstance=mh
		wc.hIcon=None
		wc.hCursor=None
		wc.hbrBackground=gdi32.CreateSolidBrush(0x00000000)
		wc.lpszMenuName=None
		wc.lpszClassName="screen_blocker_window_class"
		wc.hIconSm=None
		user32.RegisterClassExW(ctypes.byref(wc))
		shcore.SetProcessDpiAwareness(PROCESS_PER_MONITOR_DPI_AWARE)
		hwnd=user32.CreateWindowExW(WS_EX_TOPMOST,"screen_blocker_window_class","Screen Blocker",WS_VISIBLE,0,0,100,100,None,None,mh,None)
		user32.SetFocus(hwnd)
		user32.SetWindowLongPtrW(hwnd,GWL_STYLE,WS_VISIBLE)
		user32.SetWindowLongPtrW(hwnd,GWL_EXSTYLE,WS_EX_TOPMOST)
		mi=ctypes.wintypes.MONITORINFO()
		mi.cbSize=ctypes.sizeof(ctypes.wintypes.MONITORINFO)
		user32.GetMonitorInfoW(user32.MonitorFromWindow(hwnd,MONITOR_DEFAULTTONEAREST),ctypes.byref(mi))
		user32.SetWindowPos(hwnd,HWND_TOP,mi.rcMonitor.left,mi.rcMonitor.top,mi.rcMonitor.right-mi.rcMonitor.left,mi.rcMonitor.bottom-mi.rcMonitor.top,SWP_SHOWWINDOW)
		c_func=ctypes.wintypes.LowLevelKeyboardProc(_screen_blocker_keyboard_handler)
		hk=user32.SetWindowsHookExW(WH_KEYBOARD_LL,c_func,mh,ctypes.wintypes.DWORD(0))
		user32.ShowCursor(0)
		msg=ctypes.wintypes.MSG()
		while (True):
			e=user32.GetMessageW(ctypes.byref(msg),None,0,0)
			if (e==-1):
				break
			if (e!=0):
				if (msg.message==HOTKEY_HANDLER_END_MESSAGE):
					break
				user32.TranslateMessage(ctypes.byref(msg))
				user32.DispatchMessageW(ctypes.byref(msg))
		user32.DestroyWindow(hwnd)
		user32.UnhookWindowsHookEx(hk)
		user32.UnregisterClassW("screen_blocker_window_class",mh)
	elif (v==1):
		user32.SetFocus(hwnd)
		ho=kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
		kernel32.SetConsoleMode(kernel32.GetStdHandle(STD_INPUT_HANDLE),ctypes.wintypes.DWORD(0x80))
		kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
		nci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		nci.dwSize=ci.dwSize
		nci.bVisible=0
		kernel32.SetConsoleCursorInfo(ho,ctypes.byref(nci))
		bf=""
		u=True
		ll=0
		while (True):
			if (msvcrt.kbhit()==1):
				k=msvcrt.getch()
				if (k==b"\xe0"):
					msvcrt.getch()
				elif (k==b"\x03"):
					break
				elif (k==b"\x08"):
					bf=bf[:-1]
					u=True
				elif (k==b"\r" or k==b"\n"):
					if (bf=="blender"):
						_create_process(BLENDER_FILE_PATH)
						break
					elif (bf=="chrome"):
						_create_process(CHROME_FILE_PATH)
						break
					elif (bf=="gimp"):
						_create_process(GIMP_FILE_PATH)
						break
					elif (bf=="minecraft"):
						_create_process(MINECRAFT_LAUNCHER_FILE_PATH)
						break
					elif (bf=="open"):
						_create_process(f"\"{__executable__}\" \"{__file__}\" 2")
						break
					elif (bf=="serial"):
						_create_process(f"\"{__executable__}\" \"{__file__}\" 3")
						break
					elif (bf=="stats"):
						_create_process(f"\"{CMD_FILE_PATH}\" /c \"^\"{__executable__}^\" ^\"{__file__}^\" 6\"")
						break
					elif (bf=="sublime"):
						_create_process(EDITOR_FILE_PATH)
						break
					elif (bf=="" or bf=="exit"):
						break
					bf=""
					u=True
				elif (ord(k)>31 and ord(k)<127):
					bf+=str(k,"utf-8")
					u=True
			if (u is True):
				u=False
				ln=len(REMOVE_COLOR_FORMATTING_REGEX.sub("",bf).replace("\n"," "*(sbi.dwMaximumWindowSize.X+1)))+2
				sys.__stdout__.write(f"\x1b[0;0H> {bf+(' '*(ll-ln) if ll>ln else '')}\x1b[0m")
				sys.__stdout__.flush()
				ll=ln
			time.sleep(1/CONSOLE_APP_FRAME_RATE)
	elif (v==2):
		user32.SetFocus(hwnd)
		ho=kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
		kernel32.SetConsoleMode(kernel32.GetStdHandle(STD_INPUT_HANDLE),ctypes.wintypes.DWORD(0x80))
		kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		nci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		nci.dwSize=ci.dwSize
		nci.bVisible=0
		kernel32.SetConsoleCursorInfo(ho,ctypes.byref(nci))
		rl=[e.split("-")[:2] for e in os.listdir(PROJECT_DIR)]
		tl=["Boot"]
		for k in rl:
			if (k[0] not in tl):
				tl.append(k[0])
		l={"boot":[""]}
		for k in rl:
			if (k[0].lower() not in list(l.keys())):
				l[k[0].lower()]=[]
			l[k[0].lower()].append(k[1].replace("_"," ").title().replace(" ","_"))
		bf=["",""]
		ll=0
		pr=["",""]
		pri=-1
		pri_s=""
		u=True
		bfi=0
		cr=False
		while (True):
			if (msvcrt.kbhit()==1):
				k=msvcrt.getch()
				if (k==b"\xe0"):
					msvcrt.getch()
				if (cr is True):
					if (k in b"yY"):
						_create_project(bf[0],bf[1],True)
						break
					cr=False
					u=True
				elif (k in b"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"):
					bf[bfi]+=str(k,"utf-8")
					pri=-1
					pri_s=""
					u=True
				elif (k==b"-"):
					bfi=1-bfi
					pri=-1
					pri_s=""
					u=True
				elif (k==b"\t"):
					if (bf[0].lower()!="boot" and (len(pr[bfi])>0 or pri!=-1) and len((l.get(bf[0].lower(),[]) if bfi==1 else list(l.keys())))>0):
						al=([e for e in (l.get(bf[0].lower(),[]) if bfi==1 else list(l.keys())) if e.lower().startswith(pri_s)] if pri_s!="" else (l.get(bf[0].lower(),[]) if bfi==1 else list(l.keys())))
						if (len(al)>0):
							if (pri==-1):
								pri_s=bf[bfi].lower()
								bf[bfi]=(bf[bfi]+pr[bfi]).replace("_"," ").title().replace(" ","_")
								pr=0
							else:
								bf[bfi]=al[pri].replace("_"," ").title().replace(" ","_")
							pri=(pri+1)%len(al)
							u=True
				elif (k==b"\x08"):
					if (len(bf[bfi])>0):
						bf[bfi]=bf[bfi][:-1]
						if (bfi==0):
							bf[1]=""
						pri=-1
						pri_s=""
						u=True
				elif (k==b"\r" or k==b"\n"):
					if (bf[0].lower()=="boot"):
						_create_project(__file_base_dir__,None,True)
						break
					if (bf[0].lower() in list(l.keys()) and len(bf[1])>0):
						e=False
						for k in l.get(bf[0].lower(),[]):
							if (k.lower()==bf[1].lower()):
								_create_project(bf[0],bf[1],True)
								e=True
								break
						if (e is True):
							break
						cr=True
						u=True
				elif (k==b"\x03"):
					break
			if (u is True):
				pr=["",""]
				if (len(bf[0])>0):
					for k in tl:
						if (k.lower().startswith(bf[0].lower())):
							pr[0]=k[len(bf[0]):]
							break
				else:
					pr=rl[0][:]
				if (len(bf[1])>0):
					for k in l.get(bf[0].lower(),[]):
						if (k.lower().startswith(bf[1].lower())):
							pr[1]=k[len(bf[1]):]
							break
				elif (len(bf[0])>0 and bf[0].lower() in l):
					pr[1]=l[bf[0].lower()][0]
				o=f"\x1b[38;2;98;145;22mProject\x1b[38;2;59;59;59m: \x1b[38;2;255;255;255m{bf[0]}\x1b[38;2;139;139;139m{pr[0]}\x1b[38;2;59;59;59m-\x1b[38;2;255;255;255m{bf[1]}\x1b[38;2;139;139;139m{pr[1]}"+(f"\n\x1b[38;2;50;155;204mCreate Project?" if cr is True else "")
				ln=len(REMOVE_COLOR_FORMATTING_REGEX.sub("",o).replace("\n"," "*(sbi.dwMaximumWindowSize.X+1)))
				sys.__stdout__.write(f"\x1b[0;0H{o+(' '*(ll-ln) if ll>ln else '')}\x1b[0m")
				sys.__stdout__.flush()
				ll=ln
				u=False
			time.sleep(1/CONSOLE_APP_FRAME_RATE)
	elif (v==3):
		user32.SetFocus(hwnd)
		_init_arduino_cache()
		kernel32.SetConsoleMode(kernel32.GetStdHandle(STD_INPUT_HANDLE),ctypes.wintypes.DWORD(0x80))
		ho=kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
		kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		ui=_Serial_UI((sbi.dwMaximumWindowSize.X+1,sbi.dwMaximumWindowSize.Y+1))
		kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
		kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(sbi.dwMaximumWindowSize.X,sbi.dwMaximumWindowSize.Y))
		kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
		kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
		nci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		nci.dwSize=ci.dwSize
		nci.bVisible=0
		kernel32.SetConsoleCursorInfo(ho,ctypes.byref(nci))
		ui.loop()
	elif (v==4):
		user32.SetFocus(hwnd)
		if (len(sys.argv)==2):
			move_to_desktop.move_to_desktop(hwnd,2)
			if (os.getenv("DISABLE_BULK_PROJECT_PUSH") is not None):
				_print("\x1b[38;2;200;40;20mProject Push Diabled.")
			else:
				_push_all_github_projects()
		else:
			if (sys.argv[2]=="*"):
				if (os.getenv("DISABLE_BULK_PROJECT_PUSH") is not None):
					_print("\x1b[38;2;200;40;20mProject Push Diabled.")
				else:
					_push_all_github_projects(f=True)
			else:
				sys.argv[2]=sys.argv[2].replace("\\","/")
				_push_single_project(sys.argv[2],(GITHUB_INVALID_NAME_CHARACTER_REGEX.sub("",sys.argv[2].lower().replace(PROJECT_DIR.lower(),"").split("/")[0]) if sys.argv[2].lower().startswith(PROJECT_DIR.lower()) else "Boot_Program"))
		input("\x1b[38;2;50;50;50m<ENTER>\x1b[0m")
	elif (v==5):
		_init_arduino_cache()
		if (len(sys.argv)<3):
			_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			kernel32.ExitProcess(1)
		elif (sys.argv[2]=="list"):
			if (len(sys.argv)>3):
				_print("\x1b[38;2;200;40;20mToo many Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				kernel32.ExitProcess(1)
			bl=_list_arduino_boards()
			mx_l=[max([(4,4,4,8)[i]]+[len(b[k]) for b in bl])+2 for i,k in enumerate(("name","fqbn","arch","location"))]
			o=f"┌{'─'*mx_l[0]}┬{'─'*mx_l[1]}┬{'─'*mx_l[2]}┬{'─'*mx_l[3]}┐\n│{'Name'.center(mx_l[0])}│{'FQBN'.center(mx_l[1])}│{'Arch'.center(mx_l[2])}│{'Location'.center(mx_l[3])}│\n├{'─'*mx_l[0]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[1]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[2]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[3]}┤"
			for k in bl:
				o+=f"\n│{k['name'].center(mx_l[0])}│{k['fqbn'].center(mx_l[1])}│{k['arch'].center(mx_l[2])}│{k['location'].center(mx_l[3])}│"
			sys.__stdout__.write(o+f"\n└{'─'*mx_l[0]}┴{'─'*mx_l[1]}┴{'─'*mx_l[2]}┴{'─'*mx_l[3]}┘")
			sys.__stdout__.flush()
		elif (sys.argv[2]=="install"):
			if (len(sys.argv)<4):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				kernel32.ExitProcess(1)
			for k in sys.argv[3:]:
				if (k=="--force"):
					continue
				k=k.split(":")
				if (len(k)>3):
					_print(f"\x1b[38;2;200;40;20mInvalid Package Name '{':'.join(k)}'\x1b[38;2;200;40;20m.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
				if (len(k)==1):
					_install_arduino_package(k[0],force=(True if "--force" in sys.argv[3:] else False))
				else:
					_install_arduino_package({"pkg":k[0],"arch":k[1],"ver":(None if len(k)==2 else k[2])},force=(True if "--force" in sys.argv[3:] else False))
		elif (sys.argv[2]=="compile"):
			if (len(sys.argv)<6):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				kernel32.ExitProcess(1)
			_compile_arduino_prog(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6:])
		elif (sys.argv[2]=="upload"):
			if (len(sys.argv)<6):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				kernel32.ExitProcess(1)
			_upload_to_arduino(sys.argv[3],sys.argv[4],sys.argv[5],(True if "--burn-bootloader" in sys.argv[6:] else False),(True if "--verify" in sys.argv[6:] else False),[e for e in sys.argv[6:] if e not in ["--burn-bootloader","--verify"]])
		else:
			_print(f"\x1b[38;2;200;40;20mUnknown Switch '{sys.argv[2]}'.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			kernel32.ExitProcess(1)
	elif (v==6):
		user32.SetFocus(hwnd)
		ll=None
		hdt=None
		db=None
		l_id_m={}
		if (not os.path.exists(__file_base_dir__+REPO_STATS_LANGUAGE_LIST_FILE)):
			ll={}
			for k,v in yaml.safe_load(requests.get("https://raw.githubusercontent.com/github/linguist/master/lib/linguist/languages.yml",headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).content).items():
				if (v["type"]=="nil"):
					continue
				l_id_m[k]=len(ll)
				ll[k]=[tuple(([e.lower() for e in v["extensions"]] if "extensions" in v else [])),(REPO_STATS_DEFAULT_COLOR if "color" not in v else (int(v["color"][1:3],16),int(v["color"][3:5],16),int(v["color"][5:7],16))),REPO_STATS_LANGUAGE_TYPE.index(v["type"])]
			with open(__file_base_dir__+REPO_STATS_LANGUAGE_LIST_FILE,"wb") as f:
				f.write(bytearray([len(ll)&0xff,len(ll)>>8]))
				for k,v in ll.items():
					if (len(k)>63):
						input("\x1b[38;2;200;40;20mLanguage Name Length Overflow")
						kernel32.ExitProcess(1)
					f.write(bytearray([len(k)|(v[2]<<6),len(v[0]),v[1][0],v[1][1],v[1][2]])+bytes(k,"utf-8"))
					for e in v[0]:
						f.write(bytearray([len(e)])+bytes(e,"utf-8"))
		else:
			with open(__file_base_dir__+REPO_STATS_LANGUAGE_LIST_FILE,"rb") as f:
				ll={}
				bf=f.read(2)
				i=(bf[0])|(bf[1]<<8)
				for j in range(0,i):
					kl,el,r,g,b=f.read(5)
					k=str(f.read(kl&63),"utf-8")
					e=[]
					for _ in range(0,el):
						e.append(str(f.read(f.read(1)[0]),"utf-8"))
					l_id_m[k]=j
					ll[k]=(tuple(e),(r,g,b),kl>>6)
		if (not os.path.exists(__file_base_dir__+REPO_STATS_LANGUAGE_HEURISTIC_FILE)):
			hdt=[]
			_hdt=yaml.safe_load(requests.get("https://raw.githubusercontent.com/github/linguist/master/lib/linguist/heuristics.yml",headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).content)
			for k in _hdt["disambiguations"]:
				rl=[]
				for e in k["rules"]:
					pl=[]
					if ("and" in e):
						pl=e["and"]
					elif ("pattern" in e):
						pl.append({"pattern":e["pattern"]})
					elif ("negative_pattern" in e):
						pl.append({"negative_pattern":e["negative_pattern"]})
					elif ("named_pattern" in e):
						pl.append({"named_pattern":e["named_pattern"]})
					if (len(pl)==0):
						rl.append((e["language"],None))
					else:
						npl=[]
						for se in pl:
							pm=True
							if ("named_pattern" in se):
								se=_hdt["named_patterns"][se["named_pattern"]]
							elif ("negative_pattern" in se):
								se=se["negative_pattern"]
								pm=False
							else:
								se=se["pattern"]
							if (type(se)==str):
								se=[se]
							npl.extend([(sse,pm) for sse in se])
						rl.append((e["language"],npl))
				hdt.append((tuple(k["extensions"]),rl))
			with open(__file_base_dir__+REPO_STATS_LANGUAGE_HEURISTIC_FILE,"wb") as f:
				f.write(bytearray([len(hdt)]))
				for k in hdt:
					f.write(bytearray([len(k[0]),len(k[1])]))
					for e in k[0]:
						f.write(bytearray([len(e)])+bytes(e,"utf-8"))
					for e in k[1]:
						if (type(e[0])==str):
							f.write(bytearray([len(e[0]),(len(e[1]) if e[1] is not None else 0)])+bytes(e[0],"utf-8"))
						else:
							f.write(bytearray([len(e[0])|128,(len(e[1]) if e[1] is not None else 0)]))
							for v in e[0]:
								f.write(bytearray([len(v)])+bytes(v,"utf-8"))
						if (e[1] is not None):
							for i,v in enumerate(e[1]):
								if (len(v[0])>32767):
									input("\x1b[38;2;200;40;20mLanguage File Pattern Length Overflow")
									kernel32.ExitProcess(1)
								f.write(bytearray([len(v[0])&0xff,(len(v[0])>>8)|(0 if v[1] else 128)])+bytes(v[0],"utf-8"))
								e[1][i]=(regex.compile(v[0],regex.M|regex.V1),v[1])
		else:
			with open(__file_base_dir__+REPO_STATS_LANGUAGE_HEURISTIC_FILE,"rb") as f:
				hdt=[]
				i=f.read(1)[0]
				while (i):
					i-=1
					el,dtl=f.read(2)
					e=[]
					for _ in range(0,el):
						e.append(str(f.read(f.read(1)[0]),"utf-8"))
					dt=[]
					for _ in range(0,dtl):
						nml,pll=f.read(2)
						nm=None
						if (nml&128):
							nm=[]
							for _ in range(0,nml&127):
								nm.append(str(f.read(f.read(1)[0]),"utf-8"))
							nm=tuple(nm)
						else:
							nm=str(f.read(nml),"utf-8")
						if (pll==0):
							dt.append((nm,None))
						else:
							pl=[]
							for _ in range(0,pll):
								bf=f.read(2)
								l=(bf[0])|(bf[1]<<8)
								pl.append((regex.compile(str(f.read(l&32767),"utf-8"),regex.M|regex.V1),(False if l&32768 else True)))
							dt.append((nm,tuple(pl)))
					hdt.append((tuple(e),tuple(dt)))
		if (not os.path.exists(__file_base_dir__+REPO_STATS_LANGUAGE_DATABASE_FILE)):
			t=requests.get("https://api.github.com/repos/github/linguist/branches/master",headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).json()["commit"]["commit"]["tree"]["sha"]
			db={"tokens_total":0,"languages_total":0,"tokens":{},"language_tokens":{},"languages":{},"filenames":{}}
			for e in requests.get(f"https://api.github.com/repos/github/linguist/git/trees/{t}").json()["tree"]:
				if (e["path"]=="samples"):
					t=requests.get(f"https://api.github.com/repos/github/linguist/git/trees/{e['sha']}?recursive=1").json()
					if (t["truncated"] is True):
						input("\x1b[38;2;200;40;20mSamples Tree Truncated")
						kernel32.ExitProcess(1)
					for k in t["tree"]:
						if (k["type"]!="blob"):
							continue
						nm=k["path"].split("/")[0]
						if (nm not in l_id_m):
							continue
						_print(f"Downloading: {k['path']}",df=True)
						tl=_tokenize_file(requests.get(k["url"],headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).content.decode("utf-8",errors="replace"))
						if (len(tl)==0):
							continue
						db["languages_total"]+=1
						if (nm not in db["tokens"]):
							db["tokens"][nm]={}
							db["language_tokens"][nm]=1
							db["languages"][nm]=1
							db["filenames"][nm]=[k["path"].split("/")[-1]]
						else:
							db["language_tokens"][nm]+=1
							db["languages"][nm]+=1
							db["filenames"][nm].append(k["path"].split("/")[-1])
						for t in tl:
							if (t not in db["tokens"][nm]):
								db["tokens"][nm][t]=1
							else:
								db["tokens"][nm][t]+=1
							db["tokens_total"]+=1
					break
			with open(__file_base_dir__+REPO_STATS_LANGUAGE_DATABASE_FILE,"wb") as f:
				f.write(bytearray([db["tokens_total"]&0xff,(db["tokens_total"]>>8)&0xff,(db["tokens_total"]>>16)&0xff,db["tokens_total"]>>24,db["languages_total"]&0xff,db["languages_total"]>>8,len(db["tokens"])&0xff,len(db["tokens"])>>8]))
				for k,v in db["filenames"].items():
					f.write(bytearray([len(k),len(v),db["languages"][k],db["language_tokens"][k],len(db["tokens"][k])&0xff,len(db["tokens"][k])>>8])+bytes(k,"utf-8"))
					for e in v:
						ee=bytes(e,"utf-8")
						f.write(bytearray([len(ee)])+ee)
					for ek,ev in db["tokens"][k].items():
						eek=bytes(ek,"utf-8")
						f.write(bytearray([len(eek),ev&0xff,ev>>8])+eek)
		else:
			with open(__file_base_dir__+REPO_STATS_LANGUAGE_DATABASE_FILE,"rb") as f:
				bf=f.read(8)
				db={"filenames":{},"language_tokens":{},"languages":{},"tokens":{},"tokens_total":(bf[0])|(bf[1]<<8)|(bf[2]<<16)|(bf[3]<<24),"languages_total":(bf[4])|(bf[5]<<8)}
				i=(bf[6])|(bf[7]<<8)
				while (i):
					i-=1
					kl,fnm_l,lc,ltc,tl,tl2=f.read(6)
					tl|=tl2<<8
					k=str(f.read(kl),"utf-8")
					db["languages"][k]=lc
					db["language_tokens"][k]=ltc
					fnm=[]
					for _ in range(0,fnm_l):
						fnm.append(str(f.read(f.read(1)[0]),"utf-8"))
					db["filenames"][k]=tuple(fnm)
					t={}
					for _ in range(0,tl):
						ln,v,v2=f.read(3)
						v|=v2<<8
						t[str(f.read(ln),"utf-8")]=v
					db["tokens"][k]=t
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		ho=kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
		kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		el={}
		zt=math.log(1/db["languages_total"])
		if (len(sys.argv)==2):
			for fp in os.listdir(PROJECT_DIR):
				_project_stats(PROJECT_DIR+fp+"/",ll,hdt,db,el,zt)
			_project_stats(__file_base_dir__,ll,hdt,db,el,zt)
		else:
			_project_stats(sys.argv[2].replace("\\","/").rstrip("/")+"/",ll,hdt,db,el,zt)
		ud=False
		f=True
		ln_f=False
		o=[]
		vs=0
		kernel32.SetConsoleMode(kernel32.GetStdHandle(STD_INPUT_HANDLE),ctypes.wintypes.DWORD(0x80))
		kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
		kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(sbi.srWindow.Right+1,sbi.srWindow.Bottom+1))
		kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
		kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		ci.bVisible=0
		kernel32.SetConsoleCursorInfo(ho,ctypes.byref(ci))
		while (True):
			if (msvcrt.kbhit()==1):
				c=(msvcrt.getch(),None)
				if (c[0]==b"\xe0"):
					c=(c[0],msvcrt.getch())
				if (c[0]==b"\x03"):
					break
				elif (c[0]==b"t"):
					f=not f
					o.clear()
				elif (c[0]==b"l"):
					ln_f=not ln_f
					o.clear()
				elif (c[0]==b"\xe0" and c[1]==b"H" and vs>0):
					vs-=1
					ud=True
				elif (c[0]==b"\xe0" and c[1]==b"P"):
					vs+=1
					ud=True
			if (len(o)==0):
				pl={}
				pll={}
				pt=0
				pkl=0
				for k,v in list(el.items()):
					if (f is True and ll[k][2]!=REPO_STATS_LANGUAGE_TYPE.index("programming") and ll[k][2]!=REPO_STATS_LANGUAGE_TYPE.index("markup")):
						continue
					pl[k]=v[0]
					pll[k]=v[1]
					pt+=v[0]
					pkl=max(pkl,len(k))
				if (len(pl)!=0):
					ud=True
					pl={k:(v,v*10000//pt/100) for k,v in sorted(pl.items(),key=lambda e:-e[1])}
					pvl=max([len(str(int(e[1]))) for e in pl.values()])
					pvll=max([len(str(e)) for e in pll.values()])
					ptvl=max([len(str(e[0])) for e in pl.values()])
					o.append(f"\x1b[48;2;18;18;18m{' '*sbi.dwMaximumWindowSize.X}")
					o.append(f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ╔{'═'*(sbi.dwMaximumWindowSize.X-8)}╗   ")
					o.append("\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ║ ")
					np=0
					ln=sbi.dwMaximumWindowSize.X-10
					mv=0
					si=None
					for k,v in pl.items():
						if (mv==0):
							mv=v[0]
						bw=int(v[0]*(sbi.dwMaximumWindowSize.X-10)*2/pt)/2-np/2
						if (bw<0):
							bw=0
						o[2]+=(f"\x1b[48;2;{ll[k][1][0]};{ll[k][1][1]};{ll[k][1][2]}m▌\x1b[0m" if np!=0 else "")+f"\x1b[38;2;{ll[k][1][0]};{ll[k][1][1]};{ll[k][1][2]}m"
						if (si is None):
							si=len(o[1])-1
						o[2]+="█"*int(bw)
						ln-=int(bw)+np
						np=int((bw-int(bw))*2)
						if (bw==0):
							break
					if (ln!=0 or np!=0):
						ln-=np
						if (ln<0):
							o[2]=o[2][:si]+o[2][si-ln:]
						o[2]+="\x1b[48;2;18;18;18m"+("▌" if np!=0 else "")+" "*ln
					o[2]+="\x1b[48;2;18;18;18m \x1b[38;2;52;52;52m║   "
					o.append(f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ╠{'═'*(sbi.dwMaximumWindowSize.X-8)}╣   ")
					if (ln_f is False):
						bs=int((sbi.dwMaximumWindowSize.X-pkl-pvl-ptvl-22)*pt/mv)*2/pt
						for k,v in pl.items():
							bw=round(v[0]*bs)/2
							cl=f"\x1b[38;2;{ll[k][1][0]};{ll[k][1][1]};{ll[k][1][2]}m"
							o.append(f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ║ {cl}{k.ljust(pkl,' ')} \x1b[38;2;40;40;40m({cl}{str(int(v[1])).rjust(pvl,' ')}.{str(v[1]).split('.')[1].ljust(2,'0')}%\x1b[38;2;40;40;40m, {cl}{str(v[0]).rjust(ptvl,' ')}\x1b[38;2;40;40;40m) » {cl}"+"█"*int(bw)+f"{' ▌'[int((bw-int(bw))*2)]}{' '*(sbi.dwMaximumWindowSize.X-pkl-pvl-ptvl-int(bw)-22)}\x1b[38;2;52;52;52m║   ")
					else:
						bs=int((sbi.dwMaximumWindowSize.X-pkl-pvl-pvll-ptvl-24)*pt/mv)*2/pt
						for k,v in pl.items():
							bw=round(v[0]*bs)/2
							cl=f"\x1b[38;2;{ll[k][1][0]};{ll[k][1][1]};{ll[k][1][2]}m"
							o.append(f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ║ {cl}{k.ljust(pkl,' ')} \x1b[38;2;40;40;40m({cl}{str(int(v[1])).rjust(pvl,' ')}.{str(v[1]).split('.')[1].ljust(2,'0')}%\x1b[38;2;40;40;40m, {cl}{str(v[0]).rjust(ptvl,' ')}\x1b[38;2;40;40;40m, {cl}{str(pll[k]).rjust(pvll,' ')}\x1b[38;2;40;40;40m) » {cl}"+"█"*int(bw)+f"{' ▌'[int((bw-int(bw))*2)]}{' '*(sbi.dwMaximumWindowSize.X-pkl-pvl-pvll-ptvl-int(bw)-24)}\x1b[38;2;52;52;52m║   ")
					o.append(f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ╚{'═'*(sbi.dwMaximumWindowSize.X-8)}╝   ")
					o.append(f"\x1b[48;2;18;18;18m{' '*sbi.dwMaximumWindowSize.X}")
					while (len(o)<sbi.srWindow.Bottom+1):
						o.append(" "*sbi.dwMaximumWindowSize.X)
			vs=min(vs,max(len(o)-sbi.srWindow.Bottom-1,0))
			if (ud is True):
				ud=False
				sys.__stdout__.write("\x1b[0;0H\x1b[2J"+"\n".join(o[vs:vs+sbi.srWindow.Bottom+1])+"\x1b[0m")
				sys.__stdout__.flush()
			time.sleep(1/CONSOLE_APP_FRAME_RATE)
	elif (v==7):
		move_to_desktop.move_to_desktop(hwnd,2)
		if (len(sys.argv)==2):
			_u_mcs(__file_base_dir__+"mc_server")
		else:
			si=ctypes.wintypes.STARTUPINFOW()
			si.cb=ctypes.sizeof(ctypes.wintypes.STARTUPINFOW)
			si.lpReserved=None
			si.lpDesktop=None
			si.lpTitle=None
			si.dwFlags=0
			si.cbReserved2=0
			si.lpReserved2=None
			pi=ctypes.wintypes.PROCESS_INFORMATION()
			kernel32.CreateProcessW(None,f"\"{MINECRAFT_JAVA_RUNTIME_FILE_PATH}\" -Xms{MINECRAFT_JAVA_RUNTIME_MEMORY} -Xmx{MINECRAFT_JAVA_RUNTIME_MEMORY} -jar \"{sys.argv[2].replace(chr(92),'/').rstrip('/')+'/server.jar'}\" --nogui",None,None,False,0,None,sys.argv[2].replace("\\","/").rstrip("/")+"/",ctypes.byref(si),ctypes.byref(pi))
			kernel32.CloseHandle(pi.hProcess)
			kernel32.CloseHandle(pi.hThread)
	elif (v==8):
		move_to_desktop.switch_to_desktop(int(sys.argv[2]))

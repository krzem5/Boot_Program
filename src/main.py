import atexit
import ctypes
import ctypes.wintypes
import datetime
import fnmatch
import hashlib
import json
import math
import msvcrt
import os
import re
import regex
import requests
import socket
import subprocess
import sys
import tarfile
import threading
import time
import tkinter
import traceback
import yaml
import zipfile



__file__=os.path.abspath(__file__).replace("\\","/")
__file_dir__=__file__[:-len(__file__.split("/")[-1])-4].strip("/")+"/"
if (not os.path.exists(__file_dir__+"data")):
	os.mkdir(__file_dir__+"data")



ARDUINO_CACHE={}
ARDUINO_COMMAND_FORMAT_REGEX=re.compile(r"\{.+?\}")
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
CMD_FILE_PATH="cmd.exe"
CONSOLE_APP_FRAME_RATE=60
CUSTOM_ICON_FILE_PATH="rsrc/icon.ico"
GITHUB_API_QUOTA=5000
GITHUB_CREATED_PROJECT_LIST_FILE_PATH="data/github-created.dt"
GITHUB_EMPTY_FILE_HASH="e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"
GITHUB_HEADERS="application/vnd.github.v3+json,application/vnd.github.mercy-preview+json"
GITHUB_INVALID_NAME_CHARACTER_REGEX=re.compile(r"[^A-Za-z0-9_\.\-]")
GITHUB_MAX_FILE_SIZE=52428800
GITHUB_PUSHED_PROJECT_LIST_FILE_PATH="data/github.dt"
with open(__file_dir__+"data/secret.dt","r") as f:
	GITHUB_TOKEN=f.read().strip()
GITHUB_USERNAME="Krzem5"
GITIGNORE_FILE_PATH_REGEX=re.compile(r"[\\/]([!# ])")
JAVA_RUNTIME_FILE_PATH="java.exe"
JAVA_RUNTIME_MEMORY="8G"
MINECRAFT_SKIP_UPDATE=["1.16.5-rc1","1.16.5","21w06a","21w07a","21w08a","21w08b","21w10a","21w11a","21w13a","21w14a"]
MOVE_TO_DESKTOP_DLL_PATH="lib/move_to_desktop.dll"
PRINT_ADD_COLOR_REGEX=re.compile(r"'[^']*'|-?[0-9]+(?:\.[0-9]+)?(?:%|\b)|[0123456789abcdefABCDEF]+\b")
PROJECT_DIR="D:/K/Coding/"
REMOVE_COLOR_FORMATTING_REGEX=re.compile(r"\x1b\[[^m]*m")
REPO_STATS_COMMON_REGEX=re.compile(r";|\{|\}|\(|\)|\[|\]|[\w\.\@\#\/\*]+|\<\<?|\+|\-|\*|\/|%|&&?|\|\|?")
REPO_STATS_DEFAULT_COLOR=(240,240,240)
REPO_STATS_IGNORE_REGEX=re.compile(r"""[ \t]*(\/\/|--|\#|%|\").*?$|/\*(?:.)*?\*/|<!--(?:.)*?-->|\{-(?:.)*?-\}|\(\*(?:.)*?\*\)|(?P<ml_c>[\'\"]|\'{3}|\"{3})(?:\\[\'\"]|.)*?(?P=ml_c)|(0x[0-9a-fA-F]([0-9a-fA-F]|\.)*|[0-9]([0-9]|\.)*)([uU][lL]{0,2}|([eE][-+][0-9]*)?[fFlL]*)""",re.M|re.S)
REPO_STATS_LOG_ZERO_TOKENS=None
REPO_STATS_MAX_READ=65536
REPO_STATS_MAX_TOKEN_LEN=32
REPO_STATS_SHEBANG_REGEX=re.compile(r"#!\s*?([^ \t\v\n\r]*?)(?:$|[ \t]+(.*?)$|[ \t\v\n\r])",re.M|re.S)
REPO_STATS_TAG_ATTR_REGEX=re.compile(r"""([\w\$\.]+)(?:\s*=?(?:[\w\$\.]+(?:\s|$)|\"(?:\\\"|.)*?\"))?""",re.M|re.S)
REPO_STATS_TAG_REGEX=re.compile(r"<\s*\??\s*([\w\$\.]+)(.*?)\??\s*>")
REPO_STATS_XML_REGEX=re.compile(r"<\?xml version=")
ROOT_FILE_PATH="D:/K/"
SERIAL_BAUD=9600
SERIAL_TIMEOUT=5000
SERIAL_VALID_DEVICE_NAME_REGEX=re.compile(r"VID_([0-9a-f]{4})\+PID_([0-9a-f]{4})",re.I)
SERIAL_VALID_DEVICE_NAME_USB_REGEX=re.compile(r"VID_([0-9a-f]{4})&PID_([0-9a-f]{4})",re.I)
STDOUT_LOCK=threading.Lock()
TEMP_DIR=os.path.abspath((os.getenv("TEMP") if os.getenv("TEMP") else os.getenv("TMP"))).replace("\\","/").strip("/")+"/"
VALID_PROGRAM_TYPES=[k.lower() for k in os.listdir(__file_dir__+"templates")]
VK_KEYS={"cancel":0x03,"backspace":0x08,"tab":0x09,"clear":0x0c,"enter":0x0d,"shift":0x10,"ctrl":0x11,"alt":0x12,"pause":0x13,"capslock":0x14,"esc":0x1b,"spacebar":0x20,"pageup":0x21,"pagedown":0x22,"end":0x23,"home":0x24,"left":0x25,"up":0x26,"right":0x27,"down":0x28,"select":0x29,"print":0x2a,"execute":0x2b,"printscreen":0x2c,"insert":0x2d,"delete":0x2e,"help":0x2f,"0":0x30,"1":0x31,"2":0x32,"3":0x33,"4":0x34,"5":0x35,"6":0x36,"7":0x37,"8":0x38,"9":0x39,"a":0x41,"b":0x42,"c":0x43,"d":0x44,"e":0x45,"f":0x46,"g":0x47,"h":0x48,"i":0x49,"j":0x4a,"k":0x4b,"l":0x4c,"m":0x4d,"n":0x4e,"o":0x4f,"p":0x50,"q":0x51,"r":0x52,"s":0x53,"t":0x54,"u":0x55,"v":0x56,"w":0x57,"x":0x58,"y":0x59,"z":0x5a,"leftwindows":0xffff,"rightwindows":0xffff,"apps":0x5d,"sleep":0x5f,"*":0x6a,"+":0x6b,"separator":0x6c,"-":0x6d,"decimal":0x6e,"/":0x6f,"f1":0x70,"f2":0x71,"f3":0x72,"f4":0x73,"f5":0x74,"f6":0x75,"f7":0x76,"f8":0x77,"f9":0x78,"f10":0x79,"f11":0x7a,"f12":0x7b,"f13":0x7c,"f14":0x7d,"f15":0x7e,"f16":0x7f,"f17":0x80,"f18":0x81,"f19":0x82,"f20":0x83,"f21":0x84,"f22":0x85,"f23":0x86,"f24":0x87,"numlock":0x90,"scrolllock":0x91,"leftshift":0x10,"rightshift":0x10,"leftctrl":0x11,"rightctrl":0x11,"leftmenu":0x12,"rightmenu":0x12,"volumemute":0xad,"volumedown":0xae,"volumeup":0xaf,";":0xba,",":0xbc,".":0xbe,"`":0xc0,"[":0xdb,"\\":0xdc,"]":0xdd,"'":0xde,"windows":0xffff}
VK_SAME_KEYS={0x5b:0xffff,0x5c:0xffff,0xa0:0x10,0xa2:0x11,0xa4:0x12,0xa5:0x12}



DICS_FLAG_GLOBAL=1
DIGCF_PRESENT=2
DIREG_DEV=1
DTR_CONTROL_ENABLE=1
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
ICON_BIG=1
ICON_SMALL=0
IDYES=6
IMAGE_ICON=1
INVALID_HANDLE_VALUE=0xffffffffffffffff
KEY_READ=0x20019
LLKHF_ALTDOWN=0x20
LLKHF_INJECTED=0x10
LR_LOADFROMFILE=0x10
MB_DEFBUTTON2=0x100
MB_ICONQUESTION=0x20
MB_SYSTEMMODAL=0x1000
MB_YESNO=0x4
NOPARITY=0
ONESTOPBIT=0
OPEN_EXISTING=3
PM_REMOVE=1
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
SW_SHOWMAXIMIZED=3
TOKEN_ADJUST_PRIVILEGES=0x20
TOKEN_QUERY=0x8
VK_PACKET=0xe7
WH_KEYBOARD_LL=13
WM_KEYDOWN=0x100
WM_SETICON=0x80
WM_SYSKEYDOWN=0x104



ctypes.wintypes.HDEVINFO=ctypes.c_void_p
ctypes.wintypes.LRESULT=ctypes.c_int
ctypes.wintypes.PCWSTR=ctypes.c_wchar_p
ctypes.wintypes.ULONG_PTR=ctypes.POINTER(ctypes.wintypes.DWORD)
ctypes.wintypes.CHAR_INFO_CHAR=type("CHAR_INFO_CHAR",(ctypes.Union,),{"_fields_":[("UnicodeChar",ctypes.wintypes.WCHAR),("AsciiChar",ctypes.wintypes.CHAR)]})
ctypes.wintypes.CHAR_INFO=type("CHAR_INFO",(ctypes.Structure,),{"_fields_":[("Char",ctypes.wintypes.CHAR_INFO_CHAR),("Attributes",ctypes.wintypes.WORD)],"_anonymous_":("Char",)})
ctypes.wintypes.COMMTIMEOUTS=type("COMMTIMEOUTS",(ctypes.Structure,),{"_fields_":[("ReadIntervalTimeout",ctypes.wintypes.DWORD),("ReadTotalTimeoutMultiplier",ctypes.wintypes.DWORD),("ReadTotalTimeoutConstant",ctypes.wintypes.DWORD),("WriteTotalTimeoutMultiplier",ctypes.wintypes.DWORD),("WriteTotalTimeoutConstant",ctypes.wintypes.DWORD)]})
ctypes.wintypes.COMSTAT=type("COMSTAT",(ctypes.Structure,),{"_fields_":[("fCtsHold",ctypes.wintypes.DWORD,1),("fDsrHold",ctypes.wintypes.DWORD,1),("fRlsdHold",ctypes.wintypes.DWORD,1),("fXoffHold",ctypes.wintypes.DWORD,1),("fXoffSent",ctypes.wintypes.DWORD,1),("fEof",ctypes.wintypes.DWORD,1),("fTxim",ctypes.wintypes.DWORD,1),("fReserved",ctypes.wintypes.DWORD,25),("cbInQue",ctypes.wintypes.DWORD),("cbOutQue",ctypes.wintypes.DWORD)]})
ctypes.wintypes.CONSOLE_CURSOR_INFO=type("CONSOLE_CURSOR_INFO",(ctypes.Structure,),{"_fields_":[("dwSize",ctypes.wintypes.DWORD),("bVisible",ctypes.wintypes.BOOL)]})
ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO=type("CONSOLE_SCREEN_BUFFER_INFO",(ctypes.Structure,),{"_fields_":[("dwSize",ctypes.wintypes._COORD),("dwCursorPosition",ctypes.wintypes._COORD),("wAttributes",ctypes.wintypes.WORD),("srWindow",ctypes.wintypes.SMALL_RECT),("dwMaximumWindowSize",ctypes.wintypes._COORD)]})
ctypes.wintypes.DCB=type("DCB",(ctypes.Structure,),{"_fields_":[("DCBlength",ctypes.wintypes.DWORD),("BaudRate",ctypes.wintypes.DWORD),("fBinary",ctypes.wintypes.DWORD,1),("fParity",ctypes.wintypes.DWORD,1),("fOutxCtsFlow",ctypes.wintypes.DWORD,1),("fOutxDsrFlow",ctypes.wintypes.DWORD,1),("fDtrControl",ctypes.wintypes.DWORD,2),("fDsrSensitivity",ctypes.wintypes.DWORD,1),("fTXContinueOnXoff",ctypes.wintypes.DWORD,1),("fOutX",ctypes.wintypes.DWORD,1),("fInX",ctypes.wintypes.DWORD,1),("fErrorChar",ctypes.wintypes.DWORD,1),("fNull",ctypes.wintypes.DWORD,1),("fRtsControl",ctypes.wintypes.DWORD,2),("fAbortOnError",ctypes.wintypes.DWORD,1),("fDummy2",ctypes.wintypes.DWORD,17),("wReserved",ctypes.wintypes.WORD),("XonLim",ctypes.wintypes.WORD),("XoffLim",ctypes.wintypes.WORD),("ByteSize",ctypes.wintypes.BYTE),("Parity",ctypes.wintypes.BYTE),("StopBits",ctypes.wintypes.BYTE),("XonChar",ctypes.c_char),("XoffChar",ctypes.c_char),("ErrorChar",ctypes.c_char),("EofChar",ctypes.c_char),("EvtChar",ctypes.c_char),("wReserved1",ctypes.wintypes.WORD)]})
ctypes.wintypes.GUID=type("GUID",(ctypes.Structure,),{"_fields_":[("Data1",ctypes.wintypes.DWORD),("Data2",ctypes.wintypes.WORD),("Data3",ctypes.wintypes.WORD),("Data4",ctypes.wintypes.BYTE*8)]})
ctypes.wintypes.KBDLLHOOKSTRUCT=type("KBDLLHOOKSTRUCT",(ctypes.Structure,),{"_fields_":[("vk_code",ctypes.wintypes.DWORD),("scan_code",ctypes.wintypes.DWORD),("flags",ctypes.wintypes.DWORD),("time",ctypes.c_int),("dwExtraInfo",ctypes.wintypes.ULONG_PTR)]})
ctypes.wintypes.LUID=type("LUID_",(ctypes.Structure,),{"_fields_":[("LowPart",ctypes.wintypes.DWORD),("HighPart",ctypes.wintypes.LONG)]})
ctypes.wintypes.LUID_AND_ATTRIBUTES=type("LUID_AND_ATTRIBUTES",(ctypes.Structure,),{"_fields_":[("Luid",ctypes.wintypes.LUID),("Attributes",ctypes.wintypes.DWORD)]})
ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME=type("OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME",(ctypes.Structure,),{"_fields_":[("Offset",ctypes.wintypes.DWORD),("OffsetHigh",ctypes.wintypes.DWORD)]})
ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME=type("OVERLAPPED_DUMMYUNIONNAME",(ctypes.Union,),{"_fields_":[("_0",ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME_DUMMYSTRUCTNAME),("Pointer",ctypes.wintypes.LPVOID)],"_anonymous_":["_0"]})
ctypes.wintypes.OVERLAPPED=type("OVERLAPPED",(ctypes.Structure,),{"_fields_":[("Internal",ctypes.wintypes.ULONG_PTR),("InternalHigh",ctypes.wintypes.ULONG_PTR),("_0",ctypes.wintypes.OVERLAPPED_DUMMYUNIONNAME),("hEvent",ctypes.wintypes.HANDLE)],"_anonymous_":["_0"]})
ctypes.wintypes.SP_DEVINFO_DATA=type("SP_DEVINFO_DATA",(ctypes.Structure,),{"_fields_":[("cbSize",ctypes.wintypes.DWORD),("ClassGuid",ctypes.wintypes.GUID),("DevInst",ctypes.wintypes.DWORD),("Reserved",ctypes.wintypes.ULONG_PTR)]})
ctypes.wintypes.TOKEN_PRIVILEGES=type("TOKEN_PRIVILEGES",(ctypes.Structure,),{"_fields_":[("PrivilegeCount",ctypes.wintypes.DWORD),("Privileges",ctypes.wintypes.LUID_AND_ATTRIBUTES*1)]})
ctypes.wintypes.LowLevelKeyboardProc=ctypes.WINFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
ctypes.wintypes.LPCOMMTIMEOUTS=ctypes.POINTER(ctypes.wintypes.COMMTIMEOUTS)
ctypes.wintypes.LPCOMSTAT=ctypes.POINTER(ctypes.wintypes.COMSTAT)
ctypes.wintypes.LPDCB=ctypes.POINTER(ctypes.wintypes.DCB)
ctypes.wintypes.LPOVERLAPPED=ctypes.POINTER(ctypes.wintypes.OVERLAPPED)
ctypes.wintypes.LPSECURITY_ATTRIBUTES=ctypes.c_void_p
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



advapi32=ctypes.windll.advapi32
kernel32=ctypes.windll.kernel32
move_to_desktop=ctypes.windll.LoadLibrary(__file_dir__+MOVE_TO_DESKTOP_DLL_PATH)
setupapi=ctypes.windll.setupapi
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
kernel32.GetConsoleMode.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDWORD)
kernel32.GetConsoleMode.restype=ctypes.wintypes.BOOL
kernel32.GetConsoleScreenBufferInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PCONSOLE_SCREEN_BUFFER_INFO)
kernel32.GetConsoleScreenBufferInfo.restype=ctypes.wintypes.BOOL
kernel32.GetConsoleWindow.argtypes=tuple()
kernel32.GetConsoleWindow.restype=ctypes.wintypes.HWND
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
shell32.ShellExecuteW.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.INT)
shell32.ShellExecuteW.restype=ctypes.wintypes.HINSTANCE
user32.CallNextHookEx.argtypes=(ctypes.wintypes.PHHOOK,ctypes.c_int,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
user32.CallNextHookEx.restype=ctypes.wintypes.LRESULT
user32.DispatchMessageW.argtypes=(ctypes.wintypes.LPMSG,)
user32.DispatchMessageW.restype=ctypes.wintypes.LRESULT
user32.ExitWindowsEx.argtypes=(ctypes.wintypes.UINT,ctypes.wintypes.DWORD)
user32.ExitWindowsEx.restype=ctypes.wintypes.BOOL
user32.GetAsyncKeyState.artypes=(ctypes.c_int,)
user32.GetAsyncKeyState.restype=ctypes.wintypes.SHORT
user32.LoadImageW.argtypes=(ctypes.wintypes.HINSTANCE,ctypes.wintypes.LPCWSTR,ctypes.c_uint,ctypes.c_int,ctypes.c_int,ctypes.c_uint)
user32.LoadImageW.restype=ctypes.wintypes.HANDLE
user32.MessageBoxW.argtypes=(ctypes.wintypes.HWND,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.c_uint)
user32.MessageBoxW.restype=ctypes.c_int
user32.PeekMessageW.argtypes=(ctypes.wintypes.LPMSG,ctypes.wintypes.HWND,ctypes.c_uint,ctypes.c_uint,ctypes.c_uint)
user32.PeekMessageW.restype=ctypes.wintypes.BOOL
user32.SendMessageW.argtypes=(ctypes.wintypes.HWND,ctypes.c_uint,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
user32.SendMessageW.restype=ctypes.wintypes.LRESULT
user32.SetWindowsHookExW.argtypes=(ctypes.c_int,ctypes.wintypes.LowLevelKeyboardProc,ctypes.wintypes.HINSTANCE,ctypes.wintypes.DWORD)
user32.SetWindowsHookExW.restype=ctypes.wintypes.HHOOK
user32.ShowCursor.argtypes=(ctypes.wintypes.BOOL,)
user32.ShowCursor.restype=ctypes.c_int
user32.TranslateMessage.argtypes=(ctypes.wintypes.LPMSG,)
user32.TranslateMessage.restype=ctypes.wintypes.BOOL
user32.UnhookWindowsHookEx.argtypes=(ctypes.wintypes.HHOOK,)
user32.UnhookWindowsHookEx.restype=ctypes.wintypes.BOOL



def _print(*a,end="\n"):
	global STDOUT_LOCK
	def _r_color_f(m):
		if (m.group(0)[0]=="'"):
			return f"\x1b[38;2;91;216;38m{m.group(0)}\x1b[0m"
		elif (m.group(0)[0] in "-0123456789" and (m.end(0)==1 or m.group(0)[1:].isnumeric())):
			return f"\x1b[38;2;48;109;206m{m.group(0)}\x1b[0m"
		elif (m.group(0)[0] in "-0123456789" and m.group(0)[-1]=="%"):
			return f"\x1b[38;2;245;103;245m{m.group(0)}\x1b[0m"
		else:
			return f"\x1b[38;2;227;204;59m{m.group(0)}\x1b[0m"
	a=" ".join([str(e) for e in a])
	if (not hasattr(threading.current_thread(),"_df") or not threading.current_thread()._df):
		i=0
		while (i<len(a)):
			m=REMOVE_COLOR_FORMATTING_REGEX.match(a[i:])
			if (m!=None):
				i+=len(m.group(0))
			if (a[i] in "'-" or i==0 or a[i-1] not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"):
				m=PRINT_ADD_COLOR_REGEX.match(a[i:])
				if (m!=None):
					o=_r_color_f(m)
					a=a[:i]+o+a[i+len(m[0]):]
					i+=len(o)-1
			i+=1
	t=(datetime.datetime.now().strftime((f"\x1b[38;2;50;50;50m[%H:%M:%S]\x1b[0m [{threading.current_thread()._nm}] " if not hasattr(threading.current_thread(),"_dpt") or threading.current_thread()._dpt==False else f"\x1b[38;2;50;50;50m[%H:%M:%S]\x1b[0m ")) if not hasattr(threading.current_thread(),"_dph") or threading.current_thread()._dph==False else "")
	STDOUT_LOCK.acquire()
	sys.__stdout__.write(t+a.replace("\n","\n"+" "*len(REMOVE_COLOR_FORMATTING_REGEX.sub(r"",t)))+"\x1b[0m"+end)
	STDOUT_LOCK.release()



def _match_gitignore_path(gdt,fp):
	ig=False
	for p in gdt:
		if ((ig==False or p[0]==True)):
			fnm=os.path.normpath(fp).replace(os.sep,"/").split("/")
			if (len(fnm)<len(p[1].split("/"))):
				continue
			if (len(p[1].split("/")[0])==0):
				ok=True
				for sr,sfnm in zip(p[1].split("/"),fnm):
					if (fnmatch.fnmatch(sfnm,sr)==False):
						ok=False
						break
				if (ok==False):
					continue
			else:
				ok=False
				for i in range(0,len(fnm)-len(p[1].split("/"))+1):
					for sr,sfnm in zip(p[1].split("/"),fnm[i:]):
						if (fnmatch.fnmatch(sfnm,sr)==False):
							break
					else:
						ok=True
						break
				if (ok==False):
					continue
			if (p[0]==True):
				continue
			ig=True
	if (ig==True):
		return True
	return False



def _is_binary(fp):
	with open(fp,"rb") as f:
		dt=f.read(4096)
	if (len(dt)==0):
		return False
	r1=len(dt.translate(None,b"\b\t\n\f\r !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"))/len(dt)
	r2=len(dt.translate(None,bytes(range(127,256))))/len(dt)
	if (r1>0.90 and r2>0.9):
		return True
	enc_u=True
	try:
		dt.decode(encoding="utf-8")
	except UnicodeDecodeError:
		enc_u=False
	if ((r1>0.3 and r2<0.05) or (r1>0.8 and r2>0.8)):
		return (False if enc_u==True else True)
	else:
		return (True if enc_u==False and (b"\x00" in dt or b"\xff" in dt) else False)



def _github_api_request(m,**kw):
	kw["headers"]={**kw.get("headers",{}),"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Update API"}
	r=getattr(requests,m)(**kw)
	if ("X-RateLimit-Remaining" in r.headers.keys() and r.headers["X-RateLimit-Remaining"]=="0"):
		print(r.headers)
		sys.exit(1)
	time.sleep(3600/GITHUB_API_QUOTA)
	if (type(r.json())==dict and "message" in r.json().keys() and r.json()["message"]=="Server Error"):
		print(r.json())
		return None
	return r.json()



def _get_project_tree(r_nm,sha,p):
	_print(f"\x1b[38;2;100;100;100mReading Tree \x1b[38;2;65;118;46m'{p}'\x1b[38;2;100;100;100m...")
	r=_github_api_request("get",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{r_nm}/git/trees/{sha}",data=json.dumps({"recursive":"false"}))
	o={}
	for e in r["tree"]:
		if (e["type"]=="tree"):
			o.update(_get_project_tree(r_nm,e["sha"],p+"/"+e["path"]))
		elif ((p+"/"+e["path"]).replace("./","")!="_"):
			o[(p+"/"+e["path"]).replace("./","")]={"sz":e["size"],"sha":e["sha"]}
	return o



def _push_single_project(p,b_nm):
	b_nm=b_nm.split("-")[0].title()+("" if b_nm.count("-")==0 else "-"+b_nm.split("-")[1].replace("_"," ").title().replace(" ","_"))
	nm=GITHUB_INVALID_NAME_CHARACTER_REGEX.sub(r"",b_nm)
	with open(__file_dir__+GITHUB_CREATED_PROJECT_LIST_FILE_PATH,"r") as f:
		gr_dt=f.read().strip().replace("\r","").split("\n")
	if (nm not in gr_dt):
		_print(f"\x1b[38;2;100;100;100mCreating Project \x1b[38;2;65;118;46m'{nm}'\x1b[38;2;100;100;100m...")
		try:
			_github_api_request("post",url="https://api.github.com/user/repos",data=json.dumps({"name":nm,"description":nm.replace("-"," - ")}))
		except requests.exceptions.ConnectionError:
			_print("\x1b[38;2;200;40;20mNo Internet Connection.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			return False
	_print(f"\x1b[38;2;100;100;100mParsing Github Ignore File\x1b[38;2;100;100;100m...")
	with open(os.path.join(p,".gitignore"),"r") as f:
		gdt=[]
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
						gdt+=[[iv,ln.replace("**/","")]]
					gdt+=[[iv,ln]]
	_print(f"\x1b[38;2;100;100;100mFetching Tree Data\x1b[38;2;100;100;100m...")
	msg=datetime.datetime.now().strftime("Push Update %m/%d/%Y, %H:%M:%S")
	br=_github_api_request("get",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/branches")
	br=[e["name"] for e in br]
	br=("main" if "main" in br else ("master" if "master" in br else ("main" if len(br)==0 else br[0])))
	_print(f"\x1b[38;2;100;100;100mCommiting to Branch \x1b[38;2;65;118;46m'{br}'\x1b[38;2;100;100;100m with Message \x1b[38;2;65;118;46m'{msg}'\x1b[38;2;100;100;100m...")
	try:
		bt_sha=_github_api_request("get",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/git/ref/heads/{br}")["object"]["sha"]
	except KeyError:
		_github_api_request("put",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/contents/_",data=json.dumps({"message":msg,"content":""}))
		bt_sha=_github_api_request("get",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/git/ref/heads/{br}")["object"]["sha"]
	r_t=_get_project_tree(nm,bt_sha,".")
	_print(f"\x1b[38;2;100;100;100mCreating Commit\x1b[38;2;100;100;100m...")
	bl=[]
	cnt=[0,0,0,0]
	p=os.path.abspath(p).replace("\\","/").strip("/")+"/"
	for r,_,fl in os.walk(p):
		r=r.replace("\\","/").strip("/")+"/"
		for f in fl:
			fp=(r+f)[len(p):]
			if (_match_gitignore_path(gdt,fp)==True):
				cnt[2]+=1
				_print(f"\x1b[38;2;190;0;220m! {b_nm}/{fp}\x1b[0m")
				continue
			if (fp in list(r_t.keys())):
				if (_is_binary(r+f)==False):
					try:
						with open(r+f,"r",encoding="cp1252") as rf:
							dt=rf.read().replace("\r\n","\n")
							if (len(dt)==r_t[fp]["sz"] and hashlib.sha1(f"blob {len(dt)}\x00{dt}".encode("cp1252")).hexdigest()==r_t[fp]["sha"]):
								cnt[1]+=1
								bl+=[[fp,None]]
								_print(f"\x1b[38;2;230;210;40m? {b_nm}/{fp}\x1b[0m")
								continue
					except UnicodeDecodeError:
						if (os.stat(r+f).st_size==r_t[fp]["sz"]):
							with open(r+f,"rb") as rf:
								if (hashlib.sha1(f"blob {os.stat(r+f).st_size}\x00".encode("cp1252")+rf.read()).hexdigest()==r_t[fp]["sha"]):
									cnt[1]+=1
									bl+=[[fp,None]]
									_print(f"\x1b[38;2;230;210;40m? {b_nm}/{fp}\x1b[0m")
									continue
				elif (os.stat(r+f).st_size==r_t[fp]["sz"]):
					with open(r+f,"rb") as rf:
						if (hashlib.sha1(f"blob {os.stat(r+f).st_size}\x00".encode("cp1252")+rf.read()).hexdigest()==r_t[fp]["sha"]):
							cnt[1]+=1
							bl+=[[fp,None]]
							_print(f"\x1b[38;2;230;210;40m? {b_nm}/{fp}\x1b[0m")
							continue
			cnt[0]+=1
			_print(f"\x1b[38;2;70;210;70m+ {b_nm}/{fp}\x1b[0m")
			dt=f"File too Large (size = {os.stat(os.path.join(r,f)).st_size} b)"
			b_sha=False
			if (os.stat(r+f).st_size<=50*1024*1024):
				b64=True
				if (_is_binary(r+f)==False):
					try:
						with open(r+f,"r",encoding="utf-8") as rbf:
							dt=rbf.read().replace("\r\n","\n")
						b64=False
					except UnicodeDecodeError:
						pass
				if (b64==True):
					if (len(dt)*4//3>GITHUB_MAX_FILE_SIZE):
						b_sha=False
						dt="File too Large (size = %d b)"%(len(dt))
					else:
						b_sha=True
						with open(os.path.join(r,f),"rb") as rbf:
							dt=""
							i=0
							b_dt=rbf.read()
							while (i<len(b_dt)-2):
								dt+=BASE64_ALPHABET[b_dt[i]>>2]+BASE64_ALPHABET[((b_dt[i]<<4)&0x3f)|(b_dt[i+1]>>4)]+BASE64_ALPHABET[((b_dt[i+1]<<2)&0x3f)|(b_dt[i+2]>>6)]+BASE64_ALPHABET[b_dt[i+2]&0x3f]
								i+=3
							if (i==len(b_dt)-2):
								dt+=BASE64_ALPHABET[b_dt[i]>>2]+BASE64_ALPHABET[((b_dt[i]<<4)&0x3f)|(b_dt[i+1]>>4)]+BASE64_ALPHABET[(b_dt[i+1]<<2)&0x3f]+"="
							elif (i==len(b_dt)-1):
								dt+=BASE64_ALPHABET[b_dt[i]>>2]+BASE64_ALPHABET[(b_dt[i]<<4)&0x3f]+"=="
							b=_github_api_request("post",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/git/blobs",data=json.dumps({"content":dt,"encoding":"base64"}))
							if (b is None):
								b_sha=False
								dt="Github Server Error"
							else:
								dt=b["sha"]
			bl+=[[fp,({"path":fp,"mode":"100644","type":"blob","content":dt} if b_sha==False else {"path":fp,"mode":"100644","type":"blob","sha":dt})]]
	for fp in r_t.keys():
		rm=True
		for e in bl:
			if (e[0]!=None and e[0]==fp):
				rm=False
				break
		if (rm==True):
			_print(f"\x1b[38;2;210;40;40m- {b_nm}/{fp}\x1b[0m")
			cnt[3]+=1
			bl+=[[None,{"path":fp,"mode":"100644","type":"blob","sha":None}]]
	if (any([(True if b[1]!=None else False) for b in bl]) and (cnt[0]>0 or cnt[3]>0)):
		_print(f"\x1b[38;2;100;100;100mUploading Changes\x1b[38;2;100;100;100m...")
		_github_api_request("patch",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/git/refs/heads/{br}",data=json.dumps({"sha":_github_api_request("post",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/git/commits",data=json.dumps({"message":msg,"tree":_github_api_request("post",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/git/trees",data=json.dumps({"base_tree":bt_sha,"tree":[b[1] for b in bl if b[1]!=None]}))["sha"],"parents":[bt_sha]}))["sha"],"force":True}))
	if (nm not in gr_dt):
		_github_api_request("delete",url=f"https://api.github.com/repos/{GITHUB_USERNAME}/{nm}/contents/_",data=json.dumps({"message":msg,"sha":GITHUB_EMPTY_FILE_HASH}))
		with open(__file_dir__+GITHUB_CREATED_PROJECT_LIST_FILE_PATH,"w") as f:
			f.write("\n".join(gr_dt)+f"\n{nm}")
	_print(f"\x1b[38;2;40;210;190m{b_nm} => \x1b[38;2;70;210;70m+{cnt[0]}\x1b[38;2;40;210;190m, \x1b[38;2;230;210;40m?{cnt[1]}\x1b[38;2;40;210;190m, \x1b[38;2;190;0;220m!{cnt[2]}\x1b[38;2;40;210;190m, \x1b[38;2;210;40;40m-{cnt[3]}\x1b[0m")
	return True



def _push_all_github_projects(r=False,fr=False):
	if (r==False):
		_print(f"Starting Global Github Project Push\x1b[38;2;100;100;100m...")
	threading.current_thread()._df=True
	tm=int(time.time()//604800)
	t=[0,0]
	with open(__file_dir__+GITHUB_PUSHED_PROJECT_LIST_FILE_PATH,"r") as f:
		b_dt=f.read().replace("\r\n","\n").split("\n")
	with open(__file_dir__+GITHUB_PUSHED_PROJECT_LIST_FILE_PATH,"w") as f:
		if (len(b_dt[0])==0 or int(b_dt[0])<tm):
			b_dt=[None]
		f.write(str(tm)+"\n")
		f.flush()
		for p in sorted(os.listdir(PROJECT_DIR)):
			if (fr==False and p in b_dt[1:]):
				t[1]+=1
				f.write(p+"\n")
				f.flush()
				continue
			t[0]+=1
			if (_push_single_project(PROJECT_DIR+p,p)==False):
				return
			f.write(p+"\n")
			f.flush()
		if (fr==False and "Boot_Program" in b_dt[1:]):
			t[1]+=1
			f.write("Boot_Program\n")
			f.flush()
		else:
			t[0]+=1
			if (_push_single_project(__file_dir__,"Boot_Program")==False):
				return
			f.write("Boot_Program\n")
			f.flush()
	threading.current_thread()._df=False
	if (r==False):
		_print(f"Finished Github Project Push Check, {t[0]} Projects Updated, {t[1]} Skipped.")



def _tokenize_file(dt,el=None):
	o=[]
	i=0
	sl=True
	ig=0
	t=min(REPO_STATS_MAX_READ,len(dt))
	while (i<t):
		if (el!=None and el["__e__"]==1):
			return []
		sl=(True if i==0 or dt[i-1] in "\r\n" else False)
		if (sl==True):
			m=REPO_STATS_SHEBANG_REGEX.match(dt[i:])
			if (m!=None):
				i+=m.end(0)
				if (m.group(1).split("/")[-1]=="env"):
					o+="~~SHEBANG"+m.group(2)
				else:
					o+="~~SHEBANG"+m.group(1).split("/")[-1]
				continue
		m=REPO_STATS_IGNORE_REGEX.match(dt[i:])
		if (m!=None):
			ig+=m.end(0)
			if (ig/t>0.25):
				return []
			i+=m.end(0)
			continue
		m=REPO_STATS_TAG_REGEX.match(dt[i:])
		if (m!=None):
			i+=m.end(0)
			o+=["<"+m.group(1)+">"]
			if (len(m.group(2))>0):
				o+=REPO_STATS_TAG_ATTR_REGEX.findall(m.group(2).strip())
			continue
		m=REPO_STATS_COMMON_REGEX.match(dt[i:])
		if (m!=None):
			i+=m.end(0)
			if (m.end(0)<=REPO_STATS_MAX_TOKEN_LEN):
				o+=[m.group(0)]
			continue
		i+=1
	return o



def _project_stats_detect_file(r,fn,ll,hdt,db):
	if (os.stat(r+fn).st_size==0 or _is_binary(r+fn)==True):
		return None
	o=list(ll.keys())
	c=[]
	for k in db["languages"]:
		if (fn in db["filenames"][k]):
			c.append(k)
	if (el["__e__"]==1):
		return None
	if (len(c)>0):
		o=c[:]
	if (len(o)==1):
		return o[0]
	ex="."+fn.split(".")[-1].lower()
	c.clear()
	for k in o:
		if (ex in ll[k][0]):
			c.append(k)
	if (el["__e__"]==1):
		return None
	if (len(c)>0):
		o=c[:]
	if (len(o)==1):
		return o[0]
	dt=None
	try:
		with open(r+fn,"rb") as f:
			dt=f.read().decode("utf-8",errors="replace")
	except PermissionError:
		return None
	if (REPO_STATS_XML_REGEX.search("\n".join(dt.split("\n")[:2]))!=None):
		return "XML"
	if (el["__e__"]==1):
		return None
	c.clear()
	for k in hdt:
		if (ex in k[0]):
			for e in k[1]:
				if (e[1] is None):
					c.append(e[0])
					break
				f=True
				for p in e[1]:
					if ((p[0].match(dt)!=None)!=p[1]):
						f=False
						break
				if (f==False):
					continue
				c.append(e[0])
				break
			break
	if (el["__e__"]==1):
		return None
	if (len(c)>0):
		o=c[:]
	if (len(o)==1):
		return o[0]
	if (len(o)==0):
		return None
	tl=_tokenize_file(dt,el)
	if (el["__e__"]==1):
		return None
	if (len(tl)==0):
		return None
	tc={}
	for t in tl:
		if (t not in tc):
			tc[t]=1
		else:
			tc[t]+=1
	p=[]
	for l in o:
		if (l not in db["languages"]):
			continue
		lp=math.log(db["languages"][l]/db["languages_total"])
		for k,v in tc.items():
			lp+=v*(math.log(db["tokens"][l][k]/db["language_tokens"][l]) if k in db["tokens"][l] else REPO_STATS_LOG_ZERO_TOKENS)
		p+=[(l,lp)]
	return sorted(p,key=lambda e:-e[1])[0][0]



def _project_stats(p_fp,ll,hdt,db,el):
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
						gdt+=[[iv,ln.replace("**/","")]]
					gdt+=[[iv,ln]]
	if (el["__e__"]==1):
		return
	for r,_,fl in os.walk(p_fp):
		r=r.replace("\\","/").strip("/")+"/"
		if (el["__ig__"]==True and r[len(p_fp):].strip("/")[:4]=="docs"):
			continue
		if (el["__e__"]==1):
			return
		if ("/build" not in r.lower()):
			for f in fl:
				if (el["__e__"]==1):
					return
				el["__cf__"]=r+f
				if (el["__ig__"]==True and _match_gitignore_path(gdt,r[len(p_fp):]+f)==True):
					continue
				l=_project_stats_detect_file(r,f,ll,hdt,db)
				if (el["__e__"]==1):
					return
				if (l is None):
					continue
				if (l not in el):
					el[l]=0
				sz=os.stat(r+f).st_size
				el[l]+=sz
				el["__tcnt__"]+=sz



def _read_project_stats(fp,ll,hdt,db,el):
	if (fp is None):
		for fp in os.listdir(PROJECT_DIR):
			_project_stats(PROJECT_DIR+fp+"/",ll,hdt,db,el)
			if (el["__e__"]==1):
				break
		_project_stats(__file_dir__,ll,hdt,db,el)
	else:
		_project_stats(fp,ll,hdt,db,el)
	el["__cf__"]=None
	el["__e__"]=2



def _arduino_clone_file(url,fp,sz):
	sz=int(sz)
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((url.split("/")[2],80))
	s.send(bytes(f"GET /{'/'.join(url.split('/')[3:])} HTTP/1.1\r\nHost: {url.split('/')[2]}\r\n\r\n","utf-8"))
	bf=b""
	while (not bf.endswith(b"\r\n\r\n")):
		bf+=s.recv(1)
	t=0
	at=0
	threading.current_thread()._df=True
	_print(f"{fp.split('/')[-1]} [....................] 0/{sz} 0%",end="")
	with open(fp,"wb") as f:
		while (t<sz):
			dt=s.recv(1024)
			if (len(dt)==0):
				break
			f.write(dt)
			at+=len(dt)
			if (at>sz):
				sz=at
			t=min(t+len(dt),sz)
			p=int(t/sz*20)
			_print(f"\x1b[0G\x1b[2K{fp.split('/')[-1]} [{'='*(p-1)}{('>' if p>0 and p<20 else '')}{'.'*(20-p)}] {t}/{sz} {float(t*10000//sz)/100}%",end="")
	_print("\n",end="")
	s.close()
	threading.current_thread()._df=False



def _init_arduino_cache():
	_print("Initialising Arduino Data Cache\x1b[38;2;100;100;100m...")
	if (not os.path.exists(__file_dir__+"arduino")):
		os.mkdir(__file_dir__+"arduino")
	if (not os.path.exists(__file_dir__+f"arduino/cache")):
		os.mkdir(__file_dir__+f"arduino/cache")
	if (not os.path.exists(__file_dir__+f"arduino/cache/index")):
		with open(__file_dir__+f"arduino/cache/index","w"):
			pass
	else:
		with open(__file_dir__+f"arduino/cache/index","r") as f:
			for k in f.read().replace("\r","").split("\n"):
				if (len(k)>0):
					ARDUINO_CACHE[k.split(":")[0]]=float(k.split(":")[1])
	u=False
	_print("Reading Cache Index\x1b[38;2;100;100;100m...")
	for k in list(ARDUINO_CACHE.keys()):
		if (ARDUINO_CACHE[k]<time.time() or not os.path.exists(__file_dir__+f"arduino/cache/{k}")):
			if (os.path.exists(__file_dir__+f"arduino/cache/{k}")):
				os.remove(__file_dir__+f"arduino/cache/{k}")
			del ARDUINO_CACHE[k]
			u=True
	_print("Removing Old Cache\x1b[38;2;100;100;100m...")
	for k in os.listdir(__file_dir__+f"arduino/cache/"):
		if (k=="index" or k in list(ARDUINO_CACHE.keys())):
			continue
		os.remove(__file_dir__+f"arduino/cache/{k}")
	if (u==True):
		with open(__file_dir__+f"arduino/cache/index","w") as f:
			f.write("\n".join([f"{e[0]}:{e[1]}" for e in ARDUINO_CACHE.items()]))



def _get_arduino_cache(k):
	t=ARDUINO_CACHE.get(k,0)
	if (t==0):
		return None
	with open(__file_dir__+f"arduino/cache/{k}","rb") as f:
		return f.read()



def _set_arduino_cache(k,v,t=2592000):
	ARDUINO_CACHE[k]=time.time()+t
	with open(__file_dir__+f"arduino/cache/index","w") as f:
		f.write("\n".join([f"{e[0]}:{e[1]}" for e in ARDUINO_CACHE.items()]))
	with open(__file_dir__+f"arduino/cache/{k}","wb") as f:
		f.write(v)



def _list_arduino_boards(p=True):
	if (p==True):
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
			m=(SERIAL_VALID_DEVICE_NAME_USB_REGEX if hw_id.value[:3]=="USB" else SERIAL_VALID_DEVICE_NAME_REGEX).search(hw_id.value)
			if (m is not None):
				r=_get_arduino_cache(f"vid_pid-0x{hex(int(m.group(1),16))[2:].rjust(4,'0')}-0x{hex(int(m.group(2),16))[2:].rjust(4,'0')}.json")
				if (r is None):
					r=requests.get(f"https://builder.arduino.cc/v3/boards/byVidPid/0x{hex(int(m.group(1),16))[2:].rjust(4,'0')}/0x{hex(int(m.group(2),16))[2:].rjust(4,'0')}",headers={"Content-Type":"application/json"}).text
					_set_arduino_cache(f"vid_pid-0x{hex(int(m.group(1),16))[2:].rjust(4,'0')}-0x{hex(int(m.group(2),16))[2:].rjust(4,'0')}.json",bytes(r,"utf-8"))
				if (len(r)==0):
					continue
				r=json.loads(r)
				o+=[{"arch":r["architecture"],"fqbn":r["fqbn"],"name":r["name"],"location":nm.value.replace("\\","/").split("/")[-1]}]
			else:
				continue
		setupapi.SetupDiDestroyDeviceInfoList(di_g)
	return o



def _install_arduino_package(b,force=False):
	if (type(b)==str):
		_print(f"Searching For Package '{b}'\x1b[38;2;100;100;100m...")
		i_pkg=[]
		if (os.path.exists(__file_dir__+f"arduino/packages/index")):
			with open(__file_dir__+f"arduino/packages/index","r") as f:
				i_pkg=f.read().replace("\r\n","\n").split("\n")
		_print(f"Querying 'https://api.github.com/repos/arduino/{b}/releases/latest' for Package Metadata\x1b[38;2;100;100;100m...")
		dt=requests.get(f"https://api.github.com/repos/arduino/{b}/releases/latest").json()
		if (force==False and f"arduino-{b}-{dt['tag_name']}" in i_pkg):
			_print(f"\x1b[38;2;200;40;20mPackage 'arduino:{b}:{dt['tag_name']}' already Installed.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			return
		_print(f"Searching for '{ARDUINO_OS_TYPE}' Release\x1b[38;2;100;100;100m...")
		for k in dt["assets"]:
			if (k["name"].startswith(b+"-") and (k["name"].endswith(".zip") or k["name"].endswith(".tar.bz2")) and "mingw32" in re.sub(r"(\.zip|\.tar\.bz2)$","",k["name"][len(b)+1:])):
				_print(f"Found Release '{k['name']}'.\nCloning to File '{TEMP_DIR}{k['name']}' ...")
				_arduino_clone_file(k["browser_download_url"],f"{TEMP_DIR}{k['name']}",k["size"])
				with open(f"{TEMP_DIR}{k['name']}","wb") as f:
					f.write(requests.get(k["browser_download_url"]).content)
				if (k["name"].endswith(".tar.bz2")):
					_print("Using Extractor 'tar/r:bz2'\x1b[38;2;100;100;100m...")
					_print("Extracting Files\x1b[38;2;100;100;100m...")
					with tarfile.open(f"{TEMP_DIR}{k['name']}","r:bz2") as tf:
						tf.extractall(__file_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}")
						off=len(__file_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}/")
						_print("Copying Extracted Files\x1b[38;2;100;100;100m...")
						for r,_,fl in os.walk(__file_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}"):
							for f in fl:
								fp=os.path.join(r,f)
								os.makedirs(os.path.dirname(__file_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}"),exist_ok=True)
								try:
									with open(fp,"rb") as rf,open(__file_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}","wb") as wf:
										wf.write(rf.read())
								except Exception as e:
									traceback.print_exception(None,e,e.__traceback__)
									_print(f"\x1b[38;2;200;40;20mError while Copying File '{fp}' to '{__file_dir__}arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
						rm_fp=__file_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}"
						dl=[rm_fp]
						for r,ndl,fl in os.walk(rm_fp):
							r=r.replace("\\","/").strip("/")+"/"
							for d in ndl:
								dl.insert(0,r+d)
							for f in fl:
								os.remove(r+f)
						for k in dl:
							os.rmdir(k)
				elif (k["name"].endswith(".zip")):
					_print("Using Extractor 'zip'\x1b[38;2;100;100;100m...")
					_print("Extracting Files\x1b[38;2;100;100;100m...")
					with zipfile.ZipFile(f"{TEMP_DIR}{k['name']}","r") as zf:
						zf.extractall(__file_dir__+f"arduino/packages/arduino/tools/{b}/{dt['tag_name']}")
				else:
					_print(f"\x1b[38;2;200;40;20mUnknown File Extractor for File Extensions '{k['name'][len(k['name'].split('.')[0]):]}'.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
					raise RuntimeError(f"Unknown File Extension '{k['name'][len(k['name'].split('.')[0]):]}'.")
				_print("Removing Archive\x1b[38;2;100;100;100m...")
				os.remove(f"{TEMP_DIR}{k['name']}")
		_print("Indexing Package\x1b[38;2;100;100;100m...")
		with open(__file_dir__+f"arduino/packages/index","a") as f:
			f.write(f"arduino-{b}-{dt['tag_name']}\n")
		return
	_print(f"Searching For Package '{b['pkg']}:{b['arch']}{(':'+b['ver'] if b['ver']!=None else '')}'...\nReading Package Index Cache\x1b[38;2;100;100;100m...")
	dt=_get_arduino_cache("package_index.json")
	if (dt is None):
		_print("\x1b[38;2;200;40;20mPackage Index Cache not Found.\x1b[0m Downloaing It\x1b[38;2;100;100;100m...")
		dt=requests.get("https://downloads.arduino.cc/packages/package_index.json",headers={"Content-Type":"application/json"}).text
		_set_arduino_cache("package_index.json",bytes(dt,"utf-8"))
	p={e["name"]:e for e in json.loads(dt)["packages"]}
	dl=[b]
	o=[]
	while (len(dl)>0):
		d,dl=dl[0],dl[1:]
		_print(f"Searching For Package '{d['pkg']}:{(d['name'] if 'name' in list(d.keys()) else d['arch'])}{(':'+d['ver'] if d['ver']!=None else '')}'\x1b[38;2;100;100;100m...")
		l=[]
		for k in p[d["pkg"]]["platforms"]:
			if (("arch" in list(d.keys()) and k["architecture"]==d["arch"]) or ("arch" not in list(d.keys()) and k["name"]==d["name"])):
				l+=[(k["version"],k,False)]
		for k in p[d["pkg"]]["tools"]:
			if (("name" in list(d.keys()) and k["name"]==d["name"])):
				l+=[(k["version"],k,True)]
		e=(sorted(l,key=lambda e:e[0],reverse=True)[0] if d["ver"] is None else [e for e in l if e[0]==d["ver"]][0])
		if (e[2]==False):
			o+=[(d["pkg"],(d["arch"] if "arch" in list(d.keys()) else d["name"]),e[1]["version"],e[1]["url"],e[1]["archiveFileName"],"hardware",int(e[1]["size"]))]
			if (len(e[1]["toolsDependencies"])>0):
				_print(f"Found Dependencies: ('{(chr(39)+', '+chr(39)).join([k['packager']+':'+k['name']+':'+k['version'] for k in e[1]['toolsDependencies']])}')")
			dl+=[{"pkg":k["packager"],"name":k["name"],"ver":k["version"]} for k in e[1]["toolsDependencies"]]
		else:
			o+=[(d["pkg"],(d["arch"] if "arch" in list(d.keys()) else d["name"]),e[1]["version"],k["url"],k["archiveFileName"],"tools",k["size"]) for k in e[1]["systems"] if k["host"]==ARDUINO_HOST_SYSTEM]
	if (not os.path.exists(__file_dir__+f"arduino/packages")):
		os.mkdir(__file_dir__+f"arduino/packages")
	i_pkg=[]
	if (os.path.exists(__file_dir__+f"arduino/packages/index")):
		with open(__file_dir__+f"arduino/packages/index","r") as f:
			i_pkg=f.read().replace("\r\n","\n").split("\n")
	else:
		with open(__file_dir__+f"arduino/packages/index","w"):
			pass
	for k in o:
		if (force==False and f"{k[0]}-{k[1]}-{k[2]}" in i_pkg):
			_print(f"\x1b[38;2;200;40;20mPackage '{k[0]}:{k[1]}:{k[2]}' already Installed.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
			continue
		if (not os.path.exists(__file_dir__+f"arduino/packages/{k[0]}")):
			os.mkdir(__file_dir__+f"arduino/packages/{k[0]}")
		if (not os.path.exists(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}")):
			os.mkdir(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}")
		if (not os.path.exists(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}")):
			os.mkdir(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}")
		if (not os.path.exists(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")):
			os.mkdir(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
		_print(f"Cloning to File '{TEMP_DIR}{k[4]}' ...")
		_arduino_clone_file(k[3],TEMP_DIR+"/"+k[4],k[6])
		if (k[4].endswith(".tar.bz2")):
			_print("Using Extractor 'tar/r:bz2'\x1b[38;2;100;100;100m...")
			_print("Extracting Files\x1b[38;2;100;100;100m...")
			with tarfile.open(TEMP_DIR+"/"+k[4],"r:bz2") as tf:
				tf.extractall(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
				off=len(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}/")
				_print("Copying Extracted Files\x1b[38;2;100;100;100m...")
				for r,_,fl in os.walk(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}"):
					for f in fl:
						fp=os.path.join(r,f)
						os.makedirs(os.path.dirname(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}"),exist_ok=True)
						try:
							with open(fp,"rb") as rf,open(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}","wb") as wf:
								wf.write(rf.read())
						except Exception as e:
							traceback.print_exception(None,e,e.__traceback__)
							_print(f"\x1b[38;2;200;40;20mError while Copying File '{fp}' to '{__file_dir__}arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
				rm_fp=__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}"
				dl=[rm_fp]
				for r,ndl,fl in os.walk(rm_fp):
					r=r.replace("\\","/").strip("/")+"/"
					for d in ndl:
						dl.insert(0,r+d)
					for f in fl:
						os.remove(r+f)
				for k in dl:
					os.rmdir(k)
		elif (k[4].endswith(".zip")):
			_print("Using Extractor 'zip'\x1b[38;2;100;100;100m...")
			_print("Extracting Files\x1b[38;2;100;100;100m...")
			with zipfile.ZipFile(TEMP_DIR+"/"+k[4],"r") as zf:
				zf.extractall(__file_dir__+f"arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
		_print("Removing Archive\x1b[38;2;100;100;100m...")
		os.remove(TEMP_DIR+"/"+k[4])
		_print("Indexing Package\x1b[38;2;100;100;100m...")
		with open(__file_dir__+f"arduino/packages/index","a") as f:
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



def _split_cmd(cmd):
	o=[""]
	i=0
	while (i<len(cmd)):
		if (cmd[i] in " \t\n\r\v\f"):
			if (len(o[-1])>0):
				o+=[""]
			i+=1
			continue
		elif (cmd[i] in "'\""):
			if (len(o[-1])>0):
				o+=[""]
			i+=1
			while (cmd[i] not in "'\""):
				o[-1]+=cmd[i]
				i+=1
		else:
			o[-1]+=cmd[i]
		i+=1
	if (len(o[-1])==0):
		o=o[:-1]
	return o



def _expand_arduino_cmd(d,s):
	while (True):
		ns=s+""
		for k,v in d.items():
			ns=ns.replace("{"+k+"}",v)
		if (ns==s):
			return s
		s=ns



def _run_arduino_recipe(bp,pfx,sfx):
	for k in bp.keys():
		if (k.startswith(pfx) and k.endswith(sfx) and len(bp[k])>0):
			cmd=_split_cmd(ARDUINO_COMMAND_FORMAT_REGEX.sub("",_expand_arduino_cmd(bp,bp[k])))
			p=subprocess.run(cmd)
			if (p.returncode!=0):
				sys.exit(p.returncode)



def _compile_arduino_files(b,i_fp,o_fp,inc_l,rc):
	l=[[],[],[]]
	for r,_,fl in os.walk(i_fp):
		for f in fl:
			if (f.lower().endswith(".s")):
				l[0]+=[os.path.join(r,f)]
			elif (f.lower().endswith(".c")):
				l[1]+=[os.path.join(r,f)]
			elif (f.lower().endswith(".cpp")):
				l[2]+=[os.path.join(r,f)]
		if (rc==False):
			break
	o=[]
	for i in range(0,3):
		for f in l[i]:
			c_bp={**bp,"compiler.warning_flags":bp.get("compiler.warning_flags","")+("."+ARDUINO_CUSTOM_WARNING_LEVEL if ARDUINO_CUSTOM_WARNING_LEVEL!="" else ""),"includes":" ".join([f"\"-I{re.sub('('+chr(92)+r'|/)$','',e)}\"" for e in inc_l]),"source_file":f,"object_file":o_fp+f[len(i_fp):]+".o"}
			if (not os.path.exists(o_fp+"/".join(f[len(i_fp):].split("/")[:-1]))):
				os.makedirs(o_fp+"/".join(f[len(i_fp):].split("/")[:-1]))
			p=subprocess.run(_split_cmd(ARDUINO_COMMAND_FORMAT_REGEX.sub("",_expand_arduino_cmd(c_bp,c_bp[("recipe.S.o.pattern","recipe.c.o.pattern","recipe.cpp.o.pattern")[i]]))))
			if (p.returncode!=0):
				sys.exit(p.returncode)
			o+=[o_fp+f[len(i_fp):]+".o"]
	return o



def _compile_arduino_prog(s_fp,o_fp,fqbn,inc_l):
	fqbn=fqbn.split(":")
	s_fp=os.path.abspath(s_fp).replace("\\","/")
	if (s_fp[-1]!="/"):
		s_fp+="/"
	o_fp=os.path.abspath(o_fp).replace("\\","/")
	if (o_fp[-1]!="/"):
		o_fp+="/"
	if (not os.path.exists(s_fp)):
		raise RuntimeError(f"Sketch {s_fp} doesn't Exist.")
	if (not os.path.isdir(s_fp)):
		raise RuntimeError("Sketch Path must Be a Directory.")
	b_fp=f"{TEMP_DIR}arduino-build-{hashlib.new('md5',bytes(s_fp,'utf-8')).hexdigest()}/"
	_print(f"Compiling Sketch '{s_fp}' to Directory '{b_fp}' with Architecture '{':'.join(fqbn)}'\x1b[38;2;100;100;100m...")
	if (not os.path.exists(b_fp)):
		os.mkdir(b_fp)
	m_fp=f"{s_fp}main.ino"
	_print("Searching For Main File\x1b[38;2;100;100;100m...")
	if (os.path.exists(m_fp)==False or os.path.isdir(m_fp)==True):
		raise RuntimeError("Sketch doesn't Contain a Main Program")
	_print("Loading Packages\x1b[38;2;100;100;100m...")
	if (not os.path.exists(__file_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/")):
		raise RuntimeError(f"Package '{fqbn[0]}:{fqbn[1]}' isn't Installed.")
	h_fp=os.path.abspath(__file_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"+sorted(os.listdir(__file_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"),reverse=True)[0])+"/"
	_print(f"Reading '{h_fp}boards.txt'\x1b[38;2;100;100;100m...")
	with open(f"{h_fp}boards.txt","r") as hb_f:
		h_pm={}
		for k in hb_f.read().replace("\r\n","\n").split("\n"):
			if (len(k.strip())==0 or k.strip()[0]=="#"):
				continue
			if (k.split(".")[0] not in list(h_pm.keys())):
				h_pm[k.split(".")[0]]={}
			h_pm[k.split(".")[0]][".".join(k.split("=")[0].split(".")[1:])]=k[len(k.split("=")[0])+1:]
	if (fqbn[2] not in list(h_pm.keys())):
		raise RuntimeError(f"Invalid FQBN '{':'.join(fqbn)}'.")
	_print(f"Reading '{h_fp}platform.txt'\x1b[38;2;100;100;100m...")
	with open(f"{h_fp}platform.txt","r") as hp_f:
		p_pm={k.split("=")[0]:k[len(k.split("=")[0])+1:] for k in hp_f.read().replace("\r\n","\n").split("\n") if len(k.strip())>0 and k.strip()[0]!="#"}
	_print(f"Creating Build Properties\x1b[38;2;100;100;100m...")
	bp={"software":"ARDUINO",**p_pm,**h_pm[fqbn[2]],"build.path":ARDUINO_DIRECTORY_PATH_REGEX.sub("",b_fp),"build.project_name":m_fp.split("/")[-1],"build.arch":fqbn[1].upper()}
	bp.update({"build.core.path":f"{h_fp}cores/{bp['build.core']}","build.system.path":f"{h_fp}system","runtime.platform.path":ARDUINO_DIRECTORY_PATH_REGEX.sub("",h_fp),"runtime.hardware.path":ARDUINO_DIRECTORY_PATH_REGEX.sub("",os.path.abspath(__file_dir__+f"arduino/packages/{fqbn[0]}/hardware/")),"runtime.ide.version":"10607","runtime.ide.path":__file_dir__+"","build.fqbn":":".join(fqbn),"ide_version":"ide_version","runtime.os":ARDUINO_OS_TYPE,"build.variant.path":("" if bp["build.variant"]=="" else f"{h_fp}variants/{bp['build.variant']}"),"build.source.path":ARDUINO_DIRECTORY_PATH_REGEX.sub("",s_fp),"extra.time.utc":str(int(time.time())),"extra.time.local":str(datetime.datetime.now(datetime.timezone.utc).timestamp()),"extra.time.zone":"0","extra.time.dst":"0"})
	if (ARDUINO_OPTIMIZE_FOR_DEBUG==True):
		if ("compiler.optimization_flags.debug" in list(bp.keys())):
			bp["compiler.optimization_flags"]=bp["compiler.optimization_flags.debug"]
	else:
		if ("compiler.optimization_flags.release" in list(bp.keys())):
			bp["compiler.optimization_flags"]=bp["compiler.optimization_flags.release"]
	_print("Loading Tools\x1b[38;2;100;100;100m...")
	for pkg in os.listdir(__file_dir__+f"arduino/packages/"):
		if (os.path.exists(__file_dir__+f"arduino/packages/{pkg}/tools/")):
			for t in os.listdir(__file_dir__+f"arduino/packages/{pkg}/tools/"):
				for v in os.listdir(__file_dir__+f"arduino/packages/{pkg}/tools/{t}/"):
					bp[f"runtime.tools.{t}-{v}.path"]=_get_inner_dir(__file_dir__+f"arduino/packages/{pkg}/tools/{t}/{v}/")
				bp[f"runtime.tools.{t}.path"]=_get_inner_dir(__file_dir__+f"arduino/packages/{pkg}/tools/{t}/{v}/")
	_print("Comparing Old Build Properties\x1b[38;2;100;100;100m...")
	if (os.path.exists(f"{b_fp}build-properties.md5")):
		with open(f"{b_fp}build-properties.md5","r") as f:
			md5=f.read()
		if (md5[:32]!=hashlib.new("md5",bytes([(k,v) for k,v in bp.items() if not k.startswith("extra.time")].__repr__(),"utf-8")).hexdigest()):
			_print("\x1b[38;2;200;40;20mHash not Matching.\x1b[0m Rebuilding Everything\x1b[38;2;100;100;100m...")
			dl=[]
			for r,ndl,fl in os.walk(b_fp):
				r=r.replace("\\","/").strip("/")+"/"
				for d in ndl:
					dl.insert(0,r+d)
				for f in fl:
					os.remove(r+f)
			for k in dl:
				os.rmdir(k)
	_print("Writing New Hash\x1b[38;2;100;100;100m...")
	with open(f"{b_fp}build-properties.md5","w") as f:
		f.write(hashlib.new("md5",bytes([(k,v) for k,v in bp.items() if not k.startswith("extra.time")].__repr__(),"utf-8")).hexdigest())
	_print("Running Recipe 'recipe.hooks.prebuild'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.prebuild",".pattern")
	l_off=0
	nh_inc=False
	_print("Bundling Sketch Files\x1b[38;2;100;100;100m...")
	with open(b_fp+m_fp.split("/")[-1]+".cpp","wb") as bf:
		src=b""
		for r,_,fl in os.walk(s_fp):
			for fp in fl:
				if (fp.split(".")[-1].lower()=="ino"):
					_print(f"Found Main Sketch File '{os.path.join(r,fp)}'\x1b[38;2;100;100;100m...")
					with open(os.path.join(r,fp),"rb") as f:
						dt=f.read().replace(b"\r\n",b"\n")
						if (nh_inc==False):
							for k in ARDUINO_CPP_INCLUDE_FILE_REGEX.findall(str(dt,"utf-8").lower()):
								if (k=="arduino.h"):
									nh_inc=True
									break
							if (nh_inc==False):
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
				l+=[k[:-2]+".cpp",k[:-2]+".c",k[:-2]+".s",k.split("/")[-1][:-2]+".cpp",k.split("/")[-1][:-2]+".c",k.split("/")[-1][:-2]+".s"]
			for d in dl:
				if (os.path.exists(os.path.join(d[0],k))):
					_print(f"Found Included Sketch File '{os.path.join(d[0],k)}'\x1b[38;2;100;100;100m...")
					with open(b_fp+"/"+os.path.join(d[0],k)[len(d[1]):].replace("\\","/").replace("/","$"),"wb") as wf,open(os.path.join(d[0],k),"rb") as rf:
						dt=rf.read().replace(b"\r\n",b"\n")
						l+=[e for e in ARDUINO_CPP_INCLUDE_FILE_REGEX.findall(str(src,"utf-8").lower()) if e!="arduino.h" and e not in l]
						wf.write(bytes(f"#line 1 \"{os.path.join(d[0],k).replace(chr(92),chr(92)+chr(92)).replace(chr(34),chr(92)+chr(34))}\"\n","utf-8")+_replace_arduino_include(dt)+b"\n;\n")
					for e in inc_l:
						if (os.path.join(d[0],k).replace("\\","/").startswith(e.replace("\\","/"))):
							if (e not in r_dl):
								r_dl+=[e]
							break
					break
		for k in r_dl:
			inc_l.remove(k)
	inc_l+=[bp["build.core.path"],b_fp]
	if (bp["build.variant.path"]!=""):
		inc_l+=[bp["build.variant.path"]]
	_print("Generating Preprocessor Properties\x1b[38;2;100;100;100m...")
	pd={**bp,"source_file":b_fp+m_fp.split("/")[-1]+".cpp","preprocessed_file_path":b_fp+m_fp.split("/")[-1].split(".")[0]+".cpp","includes":" ".join([f"\"-I{re.sub('('+chr(92)+r'|/)$','',e)}\"".replace("\\","/") for e in inc_l])}
	if ("recipe.preproc.macros" not in list(pd.keys())):
		pd["recipe.preproc.macros"]=pd["recipe.cpp.o.pattern"].replace("{compiler.cpp.flags}","{compiler.cpp.flags} {preproc.macros.flags}").replace("{object_file}","{preprocessed_file_path}")
	_print("Running Preprocessor\x1b[38;2;100;100;100m...")
	p=subprocess.run([e for e in _split_cmd(ARDUINO_COMMAND_FORMAT_REGEX.sub("",_expand_arduino_cmd(pd,pd["recipe.preproc.macros"]))) if e!="-MMD"]+["-DARDUINO_LIB_DISCOVERY_PHASE"])
	if (p.returncode!=0):
		sys.exit(p.returncode)
	os.remove(b_fp+m_fp.split("/")[-1]+".cpp")
	_print("Running Recipe 'recipe.hooks.sketch.prebuild'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.sketch.prebuild",".pattern")
	_print("Compiling Files\x1b[38;2;100;100;100m...")
	s_of=_compile_arduino_files(bp,b_fp,b_fp,inc_l,False)+(_compile_arduino_files(bp,f"{b_fp}src/",f"{b_fp}src/",inc_l,True) if os.path.exists(f"{b_fp}src/") else [])
	_print("Running Recipe 'recipe.hooks.sketch.postbuild'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.sketch.postbuild",".pattern")
	_print("Running Recipe 'recipe.hooks.core.prebuild'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.core.prebuild",".pattern")
	c_inc_l=[bp["build.core.path"]]+([bp["build.variant.path"]] if bp["build.variant.path"]!="" else [])
	_print("Buliding Core\x1b[38;2;100;100;100m...")
	if (not os.path.exists(f"{b_fp}core/")):
		_print("\x1b[38;2;200;40;20mPrebuild Core not Found.\x1b[0m Rebuilding\x1b[38;2;100;100;100m...")
		os.mkdir(f"{b_fp}core/")
		_print("Compiling Core Variant Files\x1b[38;2;100;100;100m...")
		v_of=(_compile_arduino_files(bp,bp["build.variant.path"],f"{b_fp}core",c_inc_l,True) if bp["build.variant.path"]!="" else [])
		_print("Compiling Core Files\x1b[38;2;100;100;100m...")
		pr=False
		for c_of in _compile_arduino_files(bp,bp["build.core.path"],f"{b_fp}core",c_inc_l,True):
			if (pr==False):
				_print("Archiving Core Files\x1b[38;2;100;100;100m...")
			pr=True
			p=subprocess.run(_split_cmd(ARDUINO_COMMAND_FORMAT_REGEX.sub("",_expand_arduino_cmd({**bp,"archive_file":"core.a","archive_file_path":f"{b_fp}core/core.a","object_file":c_of},bp["recipe.ar.pattern"]))))
			if (p.returncode!=0):
				sys.exit(p.returncode)
			os.remove(c_of)
			os.remove(c_of[:-2]+".d")
	else:
		_print("Collecting Core Variant Files\x1b[38;2;100;100;100m...")
		v_of=[e for e in os.listdir(f"{b_fp}core/") if e.endswith(".o")]
	_print("Running Recipe 'recipe.hooks.core.postbuild'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.core.postbuild",".pattern")
	_print("Running Recipe 'recipe.hooks.linking.prelink'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.linking.prelink",".pattern")
	_print("Linking Files\x1b[38;2;100;100;100m...")
	p=subprocess.run(_split_cmd(ARDUINO_COMMAND_FORMAT_REGEX.sub("",_expand_arduino_cmd({**bp,"compiler.warning_flags":bp.get("compiler.warning_flags","")+(f".{ARDUINO_CUSTOM_WARNING_LEVEL}" if ARDUINO_CUSTOM_WARNING_LEVEL!="" else ""),"archive_file":"core/core.a","archive_file_path":f"{b_fp}core/core.a","object_files":" ".join([f"\"{e}\"" for e in s_of+v_of])},bp["recipe.c.combine.pattern"]))))
	if (p.returncode!=0):
		sys.exit(p.returncode)
	_print("Running Recipe 'recipe.hooks.linking.postlink'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.linking.postlink",".pattern")
	_print("Running Recipe 'recipe.hooks.objcopy.preobjcopy'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.objcopy.preobjcopy",".pattern")
	_print("Running Recipe 'recipe.objcopy.'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.objcopy.",".pattern")
	_print("Running Recipe 'recipe.hooks.objcopy.postobjcopy'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.objcopy.postobjcopy",".pattern")
	_print("Running Recipe 'recipe.hooks.postbuild'\x1b[38;2;100;100;100m...")
	_run_arduino_recipe(bp,"recipe.hooks.postbuild",".pattern")
	sz=[0,0]
	if (bp["upload.maximum_size"]!=""):
		_print("Processing Statistics\x1b[38;2;100;100;100m...")
		p=subprocess.run(_split_cmd(_expand_arduino_cmd({**bp,"compiler.warning_flags":bp.get("compiler.warning_flags","")+(f".{ARDUINO_CUSTOM_WARNING_LEVEL}" if ARDUINO_CUSTOM_WARNING_LEVEL!="" else "")},bp["recipe.size.pattern"])),stdout=subprocess.PIPE)
		if (p.returncode!=0):
			sys.exit(p.returncode)
		o=str(p.stdout,"utf-8")
		for k in re.findall(bp["recipe.size.regex"],o,re.M):
			sz[0]+=int(k)
		for k in re.findall(bp["recipe.size.regex.data"],o,re.M):
			sz[1]+=int(k)
		if (sz[0]>int(bp["upload.maximum_size"])):
			print(f"\x1b[38;2;200;40;20mSketch Uses {sz[0]} bytes out of {int(bp['upload.maximum_size'])} bytes of storage space.")
			sys.exit(1)
		if (bp["upload.maximum_data_size"]!="" and sz[1]>int(bp["upload.maximum_data_size"])):
			print(f"\x1b[38;2;200;40;20mSketch Uses {sz[0]} bytes out of {int(bp['upload.maximum_size'])} bytes of Dynamic Memory.")
			sys.exit(1)
		_print(f"Sketch uses {sz[0]} bytes ({sz[0]*100//int(bp['upload.maximum_size'])}%) of program storage space. Maximum is {bp['upload.maximum_size']} bytes.")
		if (bp["upload.maximum_data_size"]!=""):
			_print(f"Global variables use {sz[1]} bytes ({sz[1]*100//int(bp['upload.maximum_data_size'])}%) of dynamic memory, leaving {int(bp['upload.maximum_data_size'])-sz[1]} bytes for local variables. Maximum is {bp['upload.maximum_data_size']} bytes.")
		else:
			_print(f"Global variables use {sz[1]} bytes of dynamic memory.")
	if (os.path.exists(o_fp)):
		dl=[]
		for r,ndl,fl in os.walk(o_fp):
			r=r.replace("\\","/").strip("/")+"/"
			for d in ndl:
				dl.insert(0,r+d)
			for f in fl:
				os.remove(r+f)
		for k in dl:
			os.rmdir(k)
	else:
		os.mkdir(o_fp)
	for k in os.listdir(b_fp):
		if (k==f"{m_fp[len(s_fp):]}.hex"):
			with open(f"{o_fp}{m_fp[len(s_fp):].split('.')[0]}.hex","wb") as wf,open(f"{b_fp}{k}","rb") as rf:
				wf.write(rf.read())
		if (k not in ["core","build-properties.md5"]):
			os.remove(f"{b_fp}{k}")
	return sz



def _upload_to_arduino(b_fp,p,fqbn,bb,vu,inc_l):
	fqbn=fqbn.split(":")
	b_fp=os.path.abspath(b_fp).replace("\\","/")
	if (b_fp[-1]!="/"):
		b_fp+="/"
	_print("Searching For Build Directory\x1b[38;2;100;100;100m...")
	if (not os.path.exists(b_fp)):
		_print("\x1b[38;2;200;40;20mSketch Build Directory Not Found.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		return
	_print("Loading Packages\x1b[38;2;100;100;100m...")
	if (not os.path.exists(__file_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/")):
		raise RuntimeError(f"Package '{fqbn[0]}:{fqbn[1]}' isn't Installed.")
	h_fp=os.path.abspath(__file_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"+sorted(os.listdir(__file_dir__+f"arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"),reverse=True)[0])+"/"
	_print(f"Reading File '{h_fp}boards.txt'\x1b[38;2;100;100;100m...")
	with open(f"{h_fp}boards.txt","r") as hb_f:
		h_pm={}
		for k in hb_f.read().replace("\r\n","\n").split("\n"):
			if (len(k.strip())==0 or k.strip()[0]=="#"):
				continue
			if (k.split(".")[0] not in list(h_pm.keys())):
				h_pm[k.split(".")[0]]={}
			h_pm[k.split(".")[0]][".".join(k.split("=")[0].split(".")[1:])]=k[len(k.split("=")[0])+1:]
	if (fqbn[2] not in list(h_pm.keys())):
		raise RuntimeError(f"Invalid FQBN '{':'.join(fqbn)}'.")
	h_pm=h_pm[fqbn[2]]
	_print(f"Reading File '{h_fp}platform.txt'\x1b[38;2;100;100;100m...")
	with open(f"{h_fp}platform.txt","r") as hp_f:
		p_pm={k.split("=")[0]:k[len(k.split("=")[0])+1:] for k in hp_f.read().replace("\r\n","\n").split("\n") if len(k.strip())>0 and k.strip()[0]!="#"}
	_print(f"Generating Upload Properties\x1b[38;2;100;100;100m...")
	up={**p_pm,**h_pm,"serial.port":p,"serial.port.file":p,"runtime.platform.path":h_fp}
	up.update({k[len(h_pm[("bootloader.tool" if bb==True else "upload.tool")])+7:]:v for k,v in up.items() if k.startswith(f"tools.{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}.")})
	for k in "upload,program,erase,bootloader".split(","):
		up[f"{k}.verbose"]=up.get(f"{k}.params.quiet","")
	for k in ("upload","program"):
		up[f"{k}.verify"]=up.get(f"{k}.params.{('no' if vu==False else '')}verify","")
	_print(f"Loading Tools\x1b[38;2;100;100;100m...")
	for v in os.listdir(__file_dir__+f"arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}/"):
		up[f"runtime.tools.{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}-{v}.path"]=_get_inner_dir(__file_dir__+f"arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}/{v}/")
	up[f"runtime.tools.{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}.path"]=__file_dir__+f"arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}/{v}/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}"
	if (bb==False):
		up.update({"build.path":b_fp,"build.project_name":[e.split(".")[0] for e in os.listdir(b_fp) if e[-4:]==".hex"][0]})
		_print("Setting Board in Bootloader Mode\x1b[38;2;100;100;100m...")
		if (bool(up.get("upload.use_1200bps_touch","False"))==True):
			_print("\x1b[38;2;200;40;20m1200Bps Touch not Implemented Yet.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
		if (bool(up.get("upload.wait_for_upload_port","False"))==True):
			_print("Searching For Avaible Boards\x1b[38;2;100;100;100m...")
			b=None
			for usb_b in _list_arduino_boards():
				if (usb_b["fqbn"]==":".join(fqbn)):
					if (usb_b["location"]==p or b is None):
						b=usb_b
			if (b is None):
				_print("\x1b[38;2;200;40;20mNo Boards Found.\x1b[0m Stopping Upload\x1b[38;2;100;100;100m...")
				sys.exit(1)
			up.update({"serial.port":b["location"],"serial.port.file":b["location"]})
		_print(f"Uploading Program to Board on Port '{p}'\x1b[38;2;100;100;100m...")
		p=subprocess.run(_split_cmd(ARDUINO_COMMAND_FORMAT_REGEX.sub("",_expand_arduino_cmd(up,up["upload.pattern"]))))
		if (p.returncode!=0):
			sys.exit(p.returncode)
	else:
		_print("Erasing Board\x1b[38;2;100;100;100m...")
		p=subprocess.run(_split_cmd(ARDUINO_COMMAND_FORMAT_REGEX.sub("",_expand_arduino_cmd(up,up["erase.pattern"]))))
		if (p.returncode!=0):
			sys.exit(p.returncode)
		_print("Burning Bootloader to Board\x1b[38;2;100;100;100m...")
		p=subprocess.run(_split_cmd(ARDUINO_COMMAND_FORMAT_REGEX.sub("",_expand_arduino_cmd(up,up["bootloader.pattern"]))))
		if (p.returncode!=0):
			sys.exit(p.returncode)
	_print("Upload Finished.")



def _open_project_file(p,d,e,*f):
	op=False
	for fn in f:
		if (os.path.isfile(fn)):
			subprocess.run([p,fn])
			op=True
	if (op==False):
		for r,_,fl in os.walk(d):
			r=r.replace("\\","/").strip("/")+"/"
			for f in fl:
				if (f.endswith(e)):
					subprocess.run([p,r+f])
					return



def _create_project(t,nm,op):
	t=t.lower()
	if (t not in VALID_PROGRAM_TYPES):
		raise RuntimeError(f"Unknown Type '{t}'")
	nm=nm.replace("_"," ").lower().title().replace(" ","_")
	p=PROJECT_DIR+f"{t.title()}-{nm}/"
	fel=[]
	for r,_,fl in os.walk(p):
		for f in fl:
			fel+=[os.path.join(r,f).split(".")[-1]]
	cr=False
	if (not os.path.exists(p)):
		cr=True
		os.mkdir(p)
	cr=True
	b_fp=__file_dir__+f"templates/{t.lower()}/"
	for r,dl,fl in os.walk(b_fp):
		r=r.replace("\\","/").strip("/")+"/"
		pr=p+r[len(b_fp):].replace("$$$NAME$$$",nm.lower())
		if (cr==False and r!=b_fp):
			break
		for d in dl:
			d=d.replace("$$$NAME$$$",nm.lower())
			if (not os.path.exists(pr+d)):
				os.mkdir(pr+d)
		for f in fl:
			pf=f.replace("$$$NAME$$$",nm.lower())
			if (not os.path.exists(pr+pf)):
				with open(pr+pf,"xb") as wf,open(r+f,"rb") as rf:
					wf.write(rf.read().replace(b"$$$YEAR$$$",bytes(str(datetime.datetime.now().year),"utf-8")).replace(b"$$$PRETTY_TITLE$$$",bytes(f"{t.title()} - {nm.replace('_',' ').title()}","utf-8")).replace(b"$$$NAME$$$",bytes(nm.lower(),"utf-8")).replace(b"$$$UPPERCASE_NAME$$$",bytes(nm.upper(),"utf-8")).replace(b"$$$TITLE_NAME$$$",bytes(nm.replace("_"," ").title(),"utf-8")))
			if (f[0]=="."):
				kernel32.SetFileAttributesW(pr+pf,FILE_ATTRIBUTE_ARCHIVE|FILE_ATTRIBUTE_HIDDEN)
	if (op==True):
		p=PROJECT_DIR+t.title()+"-"+nm+"/"
		subprocess.run(["C:/Program Files/Sublime Text 3/sublime_text.exe","--add",p])
		if (t=="arduino"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"ino",p+"src/main.ino")
		elif (t=="assembly"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"asm",p+"src/main.asm")
		elif (t=="c"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"c",p+"src/main.c")
		elif (t=="cpp"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"cpp",p+"src/main.cpp")
		elif (t=="css"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"css",p+"src/index.html",p+"src/style/main.css")
		elif (t=="java"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"java",p+f"src/com/krzem/{nm.lower()}/Main.java")
		elif (t=="javascript"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"js",p+"src/index.html",p+"src/js/main.js")
		elif (t=="php"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"php",p+"src/index.php")
		elif (t=="processing"):
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"pde",p+"src/Main.pde")
		else:
			_open_project_file("C:/Program Files/Sublime Text 3/sublime_text.exe",p,"py",p+"src/main.py")



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
			if (msvcrt.kbhit()==True):
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
				self._draw_table({"name":("Name","#8ae8c6"),"arch":("Arch","#dbdf0c"),"fqbn":("FQBN","#e386d0"),"location":("Location","#59c51e")},self._pl,s=self._pi)
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
				if (self._a_s==True and n_dt==True):
					self._dt=self._dt[-1000:]
					self._off[0]=max(0,sum([len(e[1])-(1 if None in e[1] else 0) for e in self._dt])-(self._sz[1]-9))
					ud=True
				if (inp_ch==False and self._b_tm<time.time()):
					self._b=not self._b
					self._b_tm=time.time()+0.65
					ud=True
				elif (inp_ch==True):
					self._b=True
					self._b_tm=time.time()+0.65
					ud=True
				if (self._nm_d_tm==-1):
					self._nm_d_tm=time.time()+2
				elif (self._nm_d_tm<time.time()):
					self._nm_d=not self._nm_d
					self._nm_d_tm=time.time()+2
					ud=True
				if (self._nm_d==True):
					self._set(4,2,self._p["name"].center(self._sz[0]-9).replace(self._p["name"],f"\x1b[38;2;89;189;240m{self._p['name']}"))
				else:
					self._set(4,2,self._p["fqbn"].center(self._sz[0]-9).replace(self._p["fqbn"],f"\x1b[38;2;255;199;255m{self._p['fqbn']}"))
				self._set(5,2,f"\x1b[38;2;154;255;95m{self._p['location']}")
				self._set(self._sz[0]-13,2,f"\x1b[38;2;{('255;85;95','115;35;60')[self._t]}mTXT \x1b[38;2;{('255;85;95','115;35;60')[1-self._t]}mPLT")
				self._set(4,self._sz[1]-4,"\x1b[38;2;207;207;207m"+"".join([(e if i!=self._off[1] else f"\x1b[{('2' if self._b==False else '')}4m{e}\x1b[24m") for i,e in enumerate(list(self._inp_bf+" "))]))
				if (self._t==0):
					self._set(3,3,f"╠{'═'*(self._sz[0]-9)}╣")
					self._set(3,self._sz[1]-5,f"╠{'═'*(self._sz[0]-9)}╣")
					l=[]
					for k in self._dt:
						l+=[((True if i==0 else False),k[0],e) for i,e in enumerate(k[1]) if e!=None]
					for i,k in enumerate(l[self._off[0]:self._off[0]+self._sz[1]-9]):
						if (i==0 or k[0]==True):
							self._set(4,i+4,("\x1b[38;2;255;135;5m","\x1b[38;2;180;230;60m")[k[1]]+f"{'»«'[k[1]]} {k[2]}")
						else:
							self._set(6,i+4,("\x1b[38;2;255;135;5m","\x1b[38;2;180;230;60m")[k[1]]+k[2])
				else:
					l=[]
					for k in self._dt[::-1]:
						if (k[0]!=0 or None not in k[1]):
							continue
						l+=[[float(se) for se in e.split(",")] for e in k[1][::-1] if e!=None and ARDUINO_SERIAL_PLOT_DATA_REGEX.fullmatch(e)!=None]
						if (len(l)>=self._sz[0]-11):
							l=l[:self._sz[0]-11]
							break
					if (len(l)>0):
						while (len(self._cl_cache)<max([len(e) for e in l])):
							h=(len(self._cl_cache)*211)%360/30
							self._cl_cache+=[f"\x1b[38;2;{int(192-64*max(min((h)%12-3,9-(h)%12,1),-1))};{int(192-64*max(min((h+8)%12-3,9-(h+8)%12,1),-1))};{int(192-64*max(min((h+4)%12-3,9-(h+4)%12,1),-1))}m"]
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
			if (ud==True):
				sys.__stdout__.write("\x1b[0;0H\x1b[2J"+"\n".join(self._o)+"\x1b[0m")



	def _draw_table(self,nm,d,s=-1):
		mx_l=[max([len(nm[list(nm.keys())[i]][0])]+[len(e[k]) for e in d])+2 for i,k in enumerate(list(nm.keys()))]
		off=((self._sz[0]-9-(sum(mx_l)+len(list(nm.keys()))+1))//2,3)
		self._set(off[0],off[1],"\x1b[38;2;156;156;156m┌"+"┬".join(["─"*mx_l[i] for i in range(0,len(mx_l))])+"┐")
		self._set(off[0],off[1]+1,"\x1b[38;2;156;156;156m│"+"\x1b[38;2;156;156;156m│".join([f"\x1b[38;2;{min(255,int(nm[e][1][1:3],16)+65)};{min(255,int(nm[e][1][3:5],16)+65)};{min(255,int(nm[e][1][5:7],16)+65)}m"+nm[e][0].center(mx_l[i]," ") for i,e in enumerate(list(nm.keys()))])+"\x1b[38;2;156;156;156m│")
		self._set(off[0],off[1]+2,"\x1b[38;2;156;156;156m├"+"┼".join(["─"*mx_l[i] for i in range(0,len(mx_l))])+"┤")
		for i,k in enumerate(d):
			self._set(off[0],off[1]+i+3,"\x1b[38;2;156;156;156m│"+"\x1b[38;2;156;156;156m│".join([f"\x1b[38;2;{max(0,int(nm[e][1][1:3],16)-(0 if i%2==0 else 65))};{max(0,int(nm[e][1][3:5],16)-(0 if i%2==0 else 65))};{max(0,int(nm[e][1][5:7],16)-(0 if i%2==0 else 65))}m"+("\x1b[48;2;37;37;37m" if i==s else "")+k[e].center(mx_l[j]," ") for j,e in enumerate(list(nm.keys()))])+"\x1b[48;2;24;24;24m\x1b[38;2;156;156;156m│")
		self._set(off[0],off[1]+len(d)+3,"\x1b[38;2;156;156;156m└"+"┴".join(["─"*mx_l[i] for i in range(0,len(mx_l))])+"┘")



	def _set(self,x,y,v):
		i=0
		j=0
		while (i<len(self._o[y])):
			m=REMOVE_COLOR_FORMATTING_REGEX.match(self._o[y][i:])
			if (m!=None):
				i+=len(m.group(0))
				continue
			if (j==x):
				k=i+0
				l=j+0
				em=""
				while (l<len(self._o[y])):
					m=REMOVE_COLOR_FORMATTING_REGEX.match(self._o[y][k:])
					if (m!=None):
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
				self._extend(i,k+("\n" if j<len(v.split("\n"))-1 or e==True else ""))
			return
		l=[j for j,e in enumerate(self._dt) if e[0]==i]
		if (len(l)==0 or self._dt[l[-1]][1][-1] is None):
			self._dt+=[[i,[""]]]
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
			self._dt[i][1]+=[""]
		if (e==True):
			self._dt[i][1]+=[None]
		if (len(self._dt)>128):
			self._dt=self._dt[-128:]



def _u_mcs(fp):
	fp=os.path.abspath(fp).replace("\\","/").strip("/")+"/"
	_print(f"Starting Minecraft Server in Folder '{fp}'\x1b[38;2;100;100;100m...")
	if (not os.path.exists(fp)):
		_print("\x1b[38;2;200;40;20mMinecraft Server Folder Missing.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		return
	_print("Downloading Metadata\x1b[38;2;100;100;100m...")
	try:
		json=requests.get([e for e in requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").json()["versions"] if e["id"] not in MINECRAFT_SKIP_UPDATE][0]["url"]).json()
		dw=True
		if (os.path.exists(fp+"server.jar")):
			dw=False
			_print("Inspecting Current Version\x1b[38;2;100;100;100m...")
			h=hashlib.sha1()
			with open(f"{fp}/server.jar","rb") as f:
				fb=f.read(2**16)
				while (len(fb)>0):
					h.update(fb)
					fb=f.read(2**16)
			_print(f"File Hash: {h.hexdigest()}, New Hash: {json['downloads']['server']['sha1']}")
			if (h.hexdigest()!=json["downloads"]["server"]["sha1"]):
				_print(f"Creating Backup\x1b[38;2;100;100;100m...")
				if (not os.path.exists(f"{fp}/world-backup_{json['id']}")):
					os.mkdir(f"{fp}/world-backup_{json['id']}")
				for r,dl,fl in os.walk(f"{fp}/world"):
					nr=f"{fp}/world-backup_{json['id']}"+r[len(f"{fp}/world"):]
					for d in dl:
						if (not os.path.exists(os.path.join(nr,d))):
							os.mkdir(os.path.join(nr,d))
					for f in fl:
						if (not os.path.exists(os.path.join(nr,f))):
							try:
								with open(os.path.join(r,f),"rb") as rf,open(os.path.join(nr,f),"wb") as wf:
									wf.write(rf.read())
							except PermissionError:
								if (os.path.exists(os.path.join(nr,f))):
									os.remove(os.path.join(nr,f))
				dw=True
		if (dw==True):
			_print(f"Downloading Server For {json['id']} ('{json['downloads']['server']['url']}')\x1b[38;2;100;100;100m...")
			r=requests.get(json["downloads"]["server"]["url"],stream=True).raw
			with open(f"{fp}/server.jar","wb") as f:
				while (True):
					dt=r.read(4096)
					f.write(dt)
					if (len(dt)<4096):
						break
	except requests.exceptions.ConnectionError:
		_print("\x1b[38;2;200;40;20mNo Internet Connection.\x1b[0m Skipping Update Check\x1b[38;2;100;100;100m...")
	_print("Starting Server\x1b[38;2;100;100;100m...")
	subprocess.Popen([CMD_FILE_PATH,"/c",sys.executable,__file__,"7",fp],creationflags=subprocess.CREATE_NEW_CONSOLE)



def _hotkey_handler_thr(vk,wp):
	if (vk in VK_SAME_KEYS):
		vk=VK_SAME_KEYS[vk]
	if (wp in (WM_KEYDOWN,WM_SYSKEYDOWN) and vk in _hotkey_handler._hk and user32.GetAsyncKeyState(VK_KEYS["ctrl"])!=0 and user32.GetAsyncKeyState(VK_KEYS["shift"])!=0 and user32.GetAsyncKeyState(VK_KEYS["alt"])!=0):
			_hotkey_handler._hk[vk]()



def _hotkey_handler(c,wp,lp):
	try:
		dt=ctypes.cast(lp,ctypes.POINTER(ctypes.wintypes.KBDLLHOOKSTRUCT)).contents
		if (dt.vk_code!=VK_PACKET and dt.flags&(LLKHF_INJECTED|LLKHF_ALTDOWN)!=LLKHF_INJECTED|LLKHF_ALTDOWN):
			if (dt.vk_code==0xa5 and _hotkey_handler._ig_alt):
				_hotkey_handler._ig_alt=False
			else:
				if (dt.scan_code==0x21d and dt.vk_code==0xa2):
					_hotkey_handler._ig_alt=True
				thr=threading.Thread(target=_hotkey_handler_thr,args=(dt.vk_code,wp))
				thr.daemon=True
				thr.start()
	except KeyboardInterrupt:
		_hotkey_handler._end=True
	except Exception as e:
		traceback.print_exception(None,e,e.__traceback__)
	return user32.CallNextHookEx(None,c,wp,lp)



def _handle_blocker_kb(c,wp,lp):
	try:
		dt=ctypes.cast(lp,ctypes.POINTER(ctypes.wintypes.KBDLLHOOKSTRUCT)).contents
		if (dt.vk_code==0x1b):
			_handle_blocker_kb._r.destroy()
		else:
			return -1
	except Exception as e:
		traceback.print_exception(None,e,e.__traceback__)
	return user32.CallNextHookEx(None,c,wp,lp)



def _blocker_msg_loop(r):
	if (user32.PeekMessageW(ctypes.byref(_blocker_msg_loop._msg),None,0,0,PM_REMOVE)!=0):
		user32.TranslateMessage(ctypes.byref(_blocker_msg_loop._msg))
		user32.DispatchMessageW(ctypes.byref(_blocker_msg_loop._msg))
	r.after(1000//60,_blocker_msg_loop,r)



def _check_close(t):
	if (user32.MessageBoxW(None,"Close?","Close",MB_YESNO|MB_ICONQUESTION|MB_DEFBUTTON2|MB_SYSTEMMODAL)==IDYES):
		hToken=ctypes.wintypes.HANDLE()
		tkp=ctypes.wintypes.TOKEN_PRIVILEGES()
		advapi32.OpenProcessToken(kernel32.GetCurrentProcess(),TOKEN_ADJUST_PRIVILEGES|TOKEN_QUERY,ctypes.byref(hToken))
		advapi32.LookupPrivilegeValueW(None,SE_SHUTDOWN_NAME,ctypes.byref(tkp.Privileges[0].Luid))
		tkp.PrivilegeCount=1
		tkp.Privileges[0].Attributes=SE_PRIVILEGE_ENABLED
		advapi32.AdjustTokenPrivileges(hToken,False,ctypes.byref(tkp),0,None,None)
		if (t==0):
			user32.ExitWindowsEx(EWX_LOGOFF,SHTDN_REASON_MAJOR_OTHER|SHTDN_REASON_MINOR_OTHER|SHTDN_REASON_FLAG_PLANNED)
		else:
			user32.ExitWindowsEx(EWX_FORCE|EWX_FORCEIFHUNG|EWX_POWEROFF|EWX_SHUTDOWN,SHTDN_REASON_MAJOR_OTHER|SHTDN_REASON_MINOR_OTHER|SHTDN_REASON_FLAG_PLANNED)



def _register_hk(e,cb):
	if (e not in VK_KEYS):
		raise RuntimeError(f"Unknown Key '{e}'!")
	_hotkey_handler._hk[VK_KEYS[e]]=cb



kernel32.SetConsoleMode(kernel32.GetStdHandle(-11),ctypes.wintypes.DWORD(7))
kernel32.SetConsoleTitleW("")
hwnd=kernel32.GetConsoleWindow()
user32.SendMessageW(hwnd,WM_SETICON,ICON_SMALL,user32.LoadImageW(0,__file_dir__+CUSTOM_ICON_FILE_PATH,IMAGE_ICON,16,16,LR_LOADFROMFILE))
user32.SendMessageW(hwnd,WM_SETICON,ICON_BIG,user32.LoadImageW(0,__file_dir__+CUSTOM_ICON_FILE_PATH,IMAGE_ICON,32,32,LR_LOADFROMFILE))
if (len(sys.argv)==1):
	ho=kernel32.GetStdHandle(-11)
	csbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
	kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(csbi))
	fc=ctypes.wintypes.CHAR_INFO()
	fc.Char.UnicodeChar=" "
	fc.Attributes=csbi.wAttributes
	csbi.dwCursorPosition.X=0
	csbi.dwCursorPosition.Y=0
	kernel32.ScrollConsoleScreenBufferW(ho,ctypes.byref(ctypes.wintypes.SMALL_RECT(0,0,csbi.dwSize.X,csbi.dwSize.Y)),0,ctypes.wintypes._COORD(0,-csbi.dwSize.Y),ctypes.byref(fc))
	kernel32.SetConsoleCursorPosition(ho,csbi.dwCursorPosition)
	threading.current_thread()._nm="__main__"
	_print("Starting Boot Sequence\x1b[38;2;100;100;100m...")
	move_to_desktop.move_to_desktop(hwnd,2)
	move_to_desktop.switch_to_desktop(0)
	_print("Registering Hotkey Handler\x1b[38;2;100;100;100m...")
	_hotkey_handler._hk={}
	_hotkey_handler._ig_alt=False
	_hotkey_handler._end=False
	kb_cb=ctypes.wintypes.LowLevelKeyboardProc(_hotkey_handler)
	user32.SetWindowsHookExW(WH_KEYBOARD_LL,kb_cb,kernel32.GetModuleHandleW(None),ctypes.wintypes.DWORD(0))
	atexit.register(user32.UnhookWindowsHookEx,kb_cb)
	_print("Registering Hotkey\x1b[38;2;100;100;100m...")
	_register_hk("a",lambda:shell32.ShellExecuteW(None,"open",ROOT_FILE_PATH,None,None,SW_SHOWMAXIMIZED))
	_register_hk("q",lambda:subprocess.Popen([sys.executable,__file__,"1"],creationflags=subprocess.CREATE_NEW_CONSOLE))
	_register_hk("r",lambda:subprocess.Popen([sys.executable,__file__,"0"],creationflags=subprocess.CREATE_NEW_CONSOLE))
	_register_hk("i",lambda:subprocess.Popen([sys.executable,__file__,"7"],creationflags=subprocess.CREATE_NEW_CONSOLE))
	_register_hk("home",lambda:_check_close(0))
	_register_hk("end",lambda:_check_close(1))
	_print("Starting Minecraft Server\x1b[38;2;100;100;100m...")
	thr=threading.Thread(target=_u_mcs,args=(__file_dir__+"mc_server",),name="minecraft_server_updater")
	thr._nm="minecraft_server_updater"
	thr.daemon=True
	thr.start()
	_print("Upgrading All Projects\x1b[38;2;100;100;100m...")
	for k in os.listdir("D:/K/Coding"):
		_create_project(k.split("-")[0],k[len(k.split("-")[0])+1:],False)
	_print("Starting Github Project Push Check\x1b[38;2;100;100;100m...")
	thr=threading.Thread(target=_push_all_github_projects,name="github_project_push")
	thr._nm="github_project_push"
	thr.daemon=True
	thr.start()
	_print("Starting Message Loop\x1b[38;2;100;100;100m...")
	msg=ctypes.wintypes.MSG()
	while (not _hotkey_handler._end):
		if (user32.PeekMessageW(ctypes.byref(msg),None,0,0,PM_REMOVE)!=0):
			user32.TranslateMessage(ctypes.byref(msg))
			user32.DispatchMessageW(ctypes.byref(msg))
else:
	v=int(sys.argv[1])
	if (v==0):
		r=tkinter.Tk()
		r.bind("<FocusOut>",lambda _:r.focus_force())
		r.attributes("-fullscreen",True)
		r.attributes("-topmost",True)
		r.configure(background="#000000")
		r.resizable(False,False)
		r.overrideredirect(True)
		r.focus_force()
		r.update_idletasks()
		_handle_blocker_kb._r=r
		_blocker_msg_loop._msg=ctypes.wintypes.MSG()
		kb_cb=ctypes.wintypes.LowLevelKeyboardProc(_handle_blocker_kb)
		user32.SetWindowsHookExW(WH_KEYBOARD_LL,kb_cb,kernel32.GetModuleHandleW(None),ctypes.wintypes.DWORD(0))
		atexit.register(user32.UnhookWindowsHookEx,kb_cb)
		user32.ShowCursor(0)
		r.after(0,_blocker_msg_loop,r)
		r.mainloop()
	elif (v==1):
		ho=kernel32.GetStdHandle(-11)
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		try:
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
				if (msvcrt.kbhit()==True):
					k=msvcrt.getch()
					if (k==b"\xe0"):
						msvcrt.getch()
					elif (k==b"\x03"):
						break
					elif (k==b"\x08"):
						bf=bf[:-1]
						u=True
					elif (k==b"\r" or k==b"\n"):
						if (bf=="chrome"):
							subprocess.Popen("C:/Program Files/Google/Chrome Dev/Application/chrome.exe",creationflags=subprocess.CREATE_NEW_CONSOLE)
							break
						elif (bf=="sublime"):
							subprocess.Popen("C:/Program Files/Sublime Text 3/sublime_text.exe",creationflags=subprocess.CREATE_NEW_CONSOLE)
							break
						elif (bf=="minecraft"):
							subprocess.Popen("C:/Program Files (x86)/Minecraft Launcher/MinecraftLauncher.exe",creationflags=subprocess.CREATE_NEW_CONSOLE)
							break
						elif (bf=="vm"):
							subprocess.Popen("C:/Program Files/Oracle/VirtualBox/VirtualBox.exe",creationflags=subprocess.CREATE_NEW_CONSOLE)
							break
						elif (bf=="blender"):
							subprocess.Popen("C:/Program Files/Blender Foundation/Blender/blender.exe",creationflags=subprocess.CREATE_NEW_CONSOLE)
							break
						elif (bf=="work"):
							subprocess.Popen([sys.executable,__file__,"2"],creationflags=subprocess.CREATE_NEW_CONSOLE)
							break
						elif (bf=="serial"):
							subprocess.Popen([sys.executable,__file__,"3"],creationflags=subprocess.CREATE_NEW_CONSOLE)
							break
						elif (bf=="stats"):
							subprocess.Popen([sys.executable,__file__,"6"],creationflags=subprocess.CREATE_NEW_CONSOLE)
							break
						elif (bf=="" or bf=="exit"):
							break
						bf=""
						u=True
					elif (ord(k)>31 and ord(k)<127):
						bf+=str(k,"utf-8")
						u=True
				if (u==True):
					u=False
					ln=len(REMOVE_COLOR_FORMATTING_REGEX.sub("",bf).replace("\n"," "*(sbi.dwMaximumWindowSize.X+1)))+2
					sys.__stdout__.write(f"\x1b[0;0H> {bf+(' '*(ll-ln) if ll>ln else '')}\x1b[0m")
					sys.__stdout__.flush()
					ll=ln
				time.sleep(1/CONSOLE_APP_FRAME_RATE)
		except Exception as e:
			traceback.print_exception(None,e,e.__traceback__)
	elif (v==2):
		ho=kernel32.GetStdHandle(-11)
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		try:
			nci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
			nci.dwSize=ci.dwSize
			nci.bVisible=0
			kernel32.SetConsoleCursorInfo(ho,ctypes.byref(nci))
			rl=[e.split("-")[:2] for e in os.listdir("D:/K/Coding")]
			tl=[]
			for k in rl:
				if (k[0] not in tl):
					tl+=[k[0]]
			l={}
			for k in rl:
				if (k[0].lower() not in list(l.keys())):
					l[k[0].lower()]=[]
				l[k[0].lower()]+=[k[1].replace("_"," ").title().replace(" ","_")]
			bf=["",""]
			ll=0
			pr=["",""]
			pri=-1
			pri_s=""
			u=True
			bfi=0
			cr=False
			while (True):
				if (msvcrt.kbhit()==True):
					k=msvcrt.getch()
					if (k==b"\xe0"):
						msvcrt.getch()
					if (cr==True):
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
						if ((len(pr[bfi])>0 or pri!=-1) and len((l.get(bf[0].lower(),[]) if bfi==1 else list(l.keys())))>0):
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
						if (bf[0].lower() in list(l.keys()) and len(bf[1])>0):
							e=False
							for k in l.get(bf[0].lower(),[]):
								if (k.lower()==bf[1].lower()):
									_create_project(bf[0],bf[1],True)
									e=True
									break
							if (e==True):
								break
							cr=True
							u=True
					elif (k==b"\x03"):
						break
				if (u==True):
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
					elif (len(bf[0])>0):
						for k in list(l.keys()):
							if (k.lower()==bf[0].lower()):
								pr[1]=l[k][0]
								break
					o=f"\x1b[38;2;98;145;22mProject\x1b[38;2;59;59;59m: \x1b[38;2;255;255;255m{bf[0]}\x1b[38;2;139;139;139m{pr[0]}\x1b[38;2;59;59;59m-\x1b[38;2;255;255;255m{bf[1]}\x1b[38;2;139;139;139m{pr[1]}"+(f"\n\x1b[38;2;50;155;204mCreate Project?" if cr==True else "")
					ln=len(REMOVE_COLOR_FORMATTING_REGEX.sub("",o).replace("\n"," "*(sbi.dwMaximumWindowSize.X+1)))
					sys.__stdout__.write(f"\x1b[0;0H{o+(' '*(ll-ln) if ll>ln else '')}\x1b[0m")
					sys.__stdout__.flush()
					ll=ln
					u=False
				time.sleep(1/CONSOLE_APP_FRAME_RATE)
		except Exception as e:
			traceback.print_exception(None,e,e.__traceback__)
			while (True):
				pass
	elif (v==3):
		threading.current_thread()._dpt=True
		_init_arduino_cache()
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		ho=kernel32.GetStdHandle(-11)
		kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		ui=_Serial_UI((sbi.dwMaximumWindowSize.X+1,sbi.dwMaximumWindowSize.Y+1))
		try:
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
		except Exception as e:
			traceback.print_exception(None,e,e.__traceback__)
	elif (v==4):
		if (len(sys.argv)==2):
			threading.current_thread()._nm="github_project_push_remote"
			threading.current_thread()._dpt=True
			_push_all_github_projects(r=True)
		else:
			if (sys.argv[2]=="*"):
				threading.current_thread()._nm="github_project_push_all"
				threading.current_thread()._dpt=True
				_push_all_github_projects(r=True,fr=True)
			else:
				threading.current_thread()._nm="github_project_push_single"
				threading.current_thread()._dpt=True
				sys.argv[2]=sys.argv[2].replace("\\","/")
				threading.current_thread()._df=True
				_push_single_project(sys.argv[2],(GITHUB_INVALID_NAME_CHARACTER_REGEX.sub("",sys.argv[2].lower().replace(PROJECT_DIR.lower(),"").split("/")[0]) if sys.argv[2].lower().startswith(PROJECT_DIR.lower()) else "Boot_Program"))
				input("\x1b[38;2;50;50;50m<ENTER>\x1b[0m")
	elif (v==5):
		threading.current_thread()._nm="arduino_runner"
		threading.current_thread()._dpt=True
		_init_arduino_cache()
		if (len(sys.argv)<3):
			_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			sys.exit(1)
		elif (sys.argv[2]=="list"):
			if (len(sys.argv)>3):
				_print("\x1b[38;2;200;40;20mToo many Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			bl=_list_arduino_boards()
			mx_l=[max([(4,4,4,8)[i]]+[len(b[k]) for b in bl])+2 for i,k in enumerate(("name","fqbn","arch","location"))]
			threading.current_thread()._df=True
			threading.current_thread()._dph=True
			o=f"┌{'─'*mx_l[0]}┬{'─'*mx_l[1]}┬{'─'*mx_l[2]}┬{'─'*mx_l[3]}┐\n│{'Name'.center(mx_l[0])}│{'FQBN'.center(mx_l[1])}│{'Arch'.center(mx_l[2])}│{'Location'.center(mx_l[3])}│\n├{'─'*mx_l[0]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[1]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[2]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[3]}┤"
			for k in bl:
				o+=f"\n│{k['name'].center(mx_l[0])}│{k['fqbn'].center(mx_l[1])}│{k['arch'].center(mx_l[2])}│{k['location'].center(mx_l[3])}│"
			o+=f"\n└{'─'*mx_l[0]}┴{'─'*mx_l[1]}┴{'─'*mx_l[2]}┴{'─'*mx_l[3]}┘"
			_print(o)
		elif (sys.argv[2]=="install"):
			threading.current_thread()._dph=True
			if (len(sys.argv)<4):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			for k in sys.argv[3:]:
				if (k=="--force"):
					continue
				k=k.split(":")
				if (len(k)>3):
					_print(f"\x1b[38;2;200;40;20mInvalid Package Name '{':'.join(k)}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
				if (len(k)==1):
					_install_arduino_package(k[0],force=(True if "--force" in sys.argv[3:] else False))
				else:
					_install_arduino_package({"pkg":k[0],"arch":k[1],"ver":(None if len(k)==2 else k[2])},force=(True if "--force" in sys.argv[3:] else False))
		elif (sys.argv[2]=="compile"):
			if (len(sys.argv)<6):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			_compile_arduino_prog(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6:])
		elif (sys.argv[2]=="upload"):
			if (len(sys.argv)<6):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			_upload_to_arduino(sys.argv[3],sys.argv[4],sys.argv[5],(True if "--burn-bootloader" in sys.argv[6:] else False),(True if "--verify" in sys.argv[6:] else False),[e for e in sys.argv[6:] if e not in ["--burn-bootloader","--verify"]])
		else:
			_print(f"\x1b[38;2;200;40;20mUnknown Switch '{sys.argv[2]}'.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			sys.exit(1)
	elif (v==6):
		ll=None
		hdt=None
		db=None
		if (not os.path.exists(__file_dir__+"data/git-languages.json") or not os.path.exists(__file_dir__+"data/git-languages-h.json") or not os.path.exists(__file_dir__+"data/git-languages-db.json")):
			ll={}
			l_id_m={}
			for k,v in yaml.safe_load(requests.get("https://api.github.com/repos/github/linguist/contents/lib/linguist/languages.yml",headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).content,Loader=yaml.safe_loader).items():
				l_id_m[k]=len(ll)
				ll[k]=[([e.lower() for e in v["extensions"]] if "extensions" in v else []),(f"#{hex(REPO_STATS_DEFAULT_COLOR[0])[2:].rjust(2,'0')}{hex(REPO_STATS_DEFAULT_COLOR[1])[2:].rjust(2,'0')}{hex(REPO_STATS_DEFAULT_COLOR[2])[2:].rjust(2,'0')}" if "color" not in v else v["color"]),v["type"]]
			with open(__file_dir__+"data/git-languages.json","w") as f:
				f.write(json.dumps(ll,separators=(",",":"),indent=None))
			hdt=[]
			_hdt=yaml.safe_load(requests.get("https://api.github.com/repos/github/linguist/contents/lib/linguist/heuristics.yml",headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).content,Loader=yaml.safe_loader)
			for k in _hdt["disambiguations"]:
				rl=[]
				for e in k["rules"]:
					pl=[]
					if ("and" in e):
						pl=e["and"]
					elif ("pattern" in e):
						pl+=[{"pattern":e["pattern"]}]
					elif ("negative_pattern" in e):
						pl+=[{"negative_pattern":e["negative_pattern"]}]
					elif ("named_pattern" in e):
						pl+=[{"named_pattern":e["named_pattern"]}]
					if (len(pl)==0):
						rl+=[(e["language"],None)]
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
							npl+=[(sse,pm) for sse in se]
						rl+=[(e["language"],npl)]
				hdt+=[(k["extensions"],rl)]
			with open(__file_dir__+"data/git-languages-h.json","w") as f:
				f.write(json.dumps(hdt,separators=(",",":"),indent=None))
			t=requests.get("https://api.github.com/repos/github/linguist/branches/master",headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).json()["commit"]["commit"]["tree"]["sha"]
			db={"tokens_total":0,"languages_total":0,"tokens":{},"language_tokens":{},"languages":{},"filenames":{}}
			for e in requests.get(f"https://api.github.com/repos/github/linguist/git/trees/{t}").json()["tree"]:
				if (e["path"]=="samples"):
					t=requests.get(f"https://api.github.com/repos/github/linguist/git/trees/{e['sha']}?recursive=1").json()
					if (t["truncated"]==True):
						raise RuntimeError("Samples Tree Truncated")
					for k in t["tree"]:
						if (k["type"]!="blob"):
							continue
						nm=k["path"].split("/")[0]
						if (nm not in l_id_m):
							continue
						print(f"Downloading: {k['path']}")
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
							db["filenames"][nm]+=[k["path"].split("/")[-1]]
						for t in tl:
							if (t not in db["tokens"][nm]):
								db["tokens"][nm][t]=1
							else:
								db["tokens"][nm][t]+=1
							db["tokens_total"]+=1
					break
			with open(__file_dir__+"data/git-languages-db.json","w") as f:
				f.write(json.dumps(db,indent=4).replace("    ","\t"))
		else:
			with open(__file_dir__+"data/git-languages.json","r") as f:
				ll=json.loads(f.read(),strict=False)
			with open(__file_dir__+"data/git-languages-h.json","r") as f:
				hdt=json.loads(f.read(),strict=False)
				for i,k in enumerate(hdt):
					hdt[i]=(k[0],tuple((e[0],(tuple((regex.compile(sk,regex.M|regex.V1),sv) for sk,sv in e[1]) if e[1]!=None else None)) for e in k[1]))
			with open(__file_dir__+"data/git-languages-db.json","r") as f:
				db=json.loads(f.read(),strict=False)
		REPO_STATS_LOG_ZERO_TOKENS=math.log(1/db["languages_total"])
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		ho=kernel32.GetStdHandle(-11)
		kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		kernel32.SetConsoleMode(kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
		kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(sbi.srWindow.Right+1,sbi.srWindow.Bottom+1))
		kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
		kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
		nci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		nci.dwSize=ci.dwSize
		nci.bVisible=0
		kernel32.SetConsoleCursorInfo(ho,ctypes.byref(nci))
		el={"__tcnt__":0,"__e__":False,"__cf__":None,"__ig__":True}
		thr=threading.Thread(target=_read_project_stats,args=((None if len(sys.argv)==2 else sys.argv[2]),ll,hdt,db,el))
		thr.daemon=True
		thr.start()
		elc=0
		elcf=None
		elcf_sz=0
		ud=False
		f=True
		o0=[]
		o1=[]
		vs=0
		while (True):
			if (msvcrt.kbhit()==True):
				c=(msvcrt.getch(),None)
				if (c[0]==b"\xe0"):
					c=(c[0],msvcrt.getch())
				if (c[0]==b"\x03"):
					break
				elif (c[0]==b"t"):
					f=not f
					elc=-1
				elif (c[0]==b"a"):
					if (el["__e__"]==0):
						el["__e__"]=1
					thr=None
				elif (c[0]==b"\xe0" and c[1]==b"H" and vs>0):
					vs-=1
					ud=True
				elif (c[0]==b"\xe0" and c[1]==b"P"):
					vs+=1
					ud=True
			if (thr is None and el["__e__"]==2):
				el={"__tcnt__":0,"__e__":0,"__cf__":None,"__ig__":not el["__ig__"]}
				thr=threading.Thread(target=_read_project_stats,args=((None if len(sys.argv)==2 else sys.argv[2]),ll,hdt,db,el))
				thr.daemon=True
				thr.start()
			if (elc!=el["__tcnt__"]):
				elc=el["__tcnt__"]
				pl={}
				pt=0
				pkl=0
				for k,v in list(el.items()):
					if (k[:2]=="__" or (f==True and ll[k][2] not in ["programming","markup"])):
						continue
					pl[k]=v
					pt+=v
					pkl=max(pkl,len(k))
				if (len(pl)!=0):
					ud=True
					pl={k:(v,v*10000//pt/100) for k,v in sorted(pl.items(),key=lambda e:-e[1])}
					pvl=max([len(str(int(e[1]))) for e in pl.values()])
					ptvl=max([len(str(e[0])) for e in pl.values()])
					o0=[f"\x1b[48;2;18;18;18m{' '*sbi.dwMaximumWindowSize.X}",f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ╔{'═'*(sbi.dwMaximumWindowSize.X-8)}╗   ","\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ║ "]
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
						o0[2]+=(f"\x1b[48;2;{int(ll[k][1][1:3],16)};{int(ll[k][1][3:5],16)};{int(ll[k][1][5:7],16)}m▌\x1b[0m" if np!=0 else "")+f"\x1b[38;2;{int(ll[k][1][1:3],16)};{int(ll[k][1][3:5],16)};{int(ll[k][1][5:7],16)}m"
						if (si is None):
							si=len(o0[1])-1
						o0[2]+="█"*int(bw)
						ln-=int(bw)+np
						np=int((bw-int(bw))*2)
						if (bw==0):
							break
					if (ln!=0 or np!=0):
						ln-=np
						if (ln<0):
							o0[2]=o0[2][:si]+o0[2][si-ln:]
						if (ln<-1):
							print(ln)
							while (True):
								pass
						o0[2]+="\x1b[48;2;18;18;18m"+("▌" if np!=0 else "")+" "*ln
					o0[2]+="\x1b[48;2;18;18;18m \x1b[38;2;52;52;52m║   "
					o0+=[f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ╠{'═'*(sbi.dwMaximumWindowSize.X-8)}╣   "]
					bs=int((sbi.dwMaximumWindowSize.X-pkl-pvl-ptvl-22)*pt/mv)*2/pt
					for k,v in pl.items():
						bw=round(v[0]*bs)/2
						cl=f"\x1b[38;2;{int(ll[k][1][1:3],16)};{int(ll[k][1][3:5],16)};{int(ll[k][1][5:7],16)}m"
						o0+=[f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ║ {cl}{k.ljust(pkl,' ')} \x1b[38;2;40;40;40m({cl}{str(int(v[1])).rjust(pvl,' ')}.{str(v[1]).split('.')[1].ljust(2,'0')}%\x1b[38;2;40;40;40m, {cl}{str(v[0]).rjust(ptvl,' ')}\x1b[38;2;40;40;40m) » {cl}"+"█"*int(bw)+f"{' ▌'[int((bw-int(bw))*2)]}{' '*(sbi.dwMaximumWindowSize.X-pkl-pvl-ptvl-int(bw)-22)}\x1b[38;2;52;52;52m║   "]
					o0+=[f"\x1b[48;2;18;18;18m\x1b[38;2;52;52;52m   ╚{'═'*(sbi.dwMaximumWindowSize.X-8)}╝   "]
					elcf=-1
					elcf_sz=max(len(pl)+6,sbi.srWindow.Bottom+1)-len(pl)-5
			if (el["__cf__"]!=elcf):
				elcf=el["__cf__"]
				ud=True
				lc=(math.ceil(len(elcf)/sbi.dwMaximumWindowSize.X) if elcf!=None else 0)
				o1=[" "*sbi.dwMaximumWindowSize.X for i in range(0,max(elcf_sz,lc))]
				if (elcf!=None):
					for i in range(0,lc):
						o1[-lc+i]="\x1b[38;2;200;200;200m"+elcf[i*sbi.dwMaximumWindowSize.X:(i+1)*sbi.dwMaximumWindowSize.X]+(" "*(sbi.dwMaximumWindowSize.X-len(elcf)%sbi.dwMaximumWindowSize.X) if i==lc-1 else "")
			vs=min(vs,max(len(o0)+len(o1)-sbi.srWindow.Bottom-1,0))
			if (ud==True):
				ud=False
				sys.__stdout__.write("\x1b[0;0H\x1b[2J"+"\n".join((o0+o1)[vs:vs+sbi.srWindow.Bottom+1])+"\x1b[0m")
			time.sleep(1/CONSOLE_APP_FRAME_RATE)
	elif (v==7):
		if (len(sys.argv)==2):
			threading.current_thread()._nm="minecraft_server_updater"
			_u_mcs(__file_dir__+"mc_server")
		else:
			threading.current_thread()._dpt=True
			move_to_desktop.move_to_desktop(kernel32.GetConsoleWindow(),2)
			subprocess.run([JAVA_RUNTIME_FILE_PATH,"-Xms"+JAVA_RUNTIME_MEMORY,"-Xmx"+JAVA_RUNTIME_MEMORY,"-jar",sys.argv[2]+"/server.jar","--nogui"],cwd=sys.argv[2])
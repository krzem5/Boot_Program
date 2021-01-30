import atexit
import base64
import ctypes
import datetime
import fnmatch
import hashlib
import io
import json
import math
import msvcrt
import os
import random
import re
import regex
import requests
import serial
import socket
import subprocess
import sys
import tarfile
import tempfile
import threading
import time
import tkinter
import traceback
import urllib
import urllib.parse
import urllib.request
import yaml
import zipfile



os.system("title  ")
with open("D:\\boot\\secret.dt","r") as f:
	f=f.read()



global CMD_L,STDOUT_LOCK,R_STD_BUFFER
GITHUB_HEADERS="application/vnd.github.VERSION.raw,application/vnd.github.v3+json,application/vnd.github.mercy-preview+json"
SERIAL_BAUD=9600
R_STD_BUFFER={"_s":None,"bf":[],"_e":False}
STDOUT_LOCK=False
CMD_L={}
GIT_CLONE_REGEX=re.compile(r"^([A-Za-z0-9]+@|http(|s)\:\/\/)([A-Za-z0-9.]+(:\d+)?)(?::|\/)([\d\/\w.-]+?)\.git$")
URL_REGEX=re.compile(r"^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\xffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$",re.I|re.S)
GITHUB_TOKEN,CONTACT_EMAIL=f.replace("\r","").split("\n")[:2]
MINECRAFT_SKIP_UPDATE=["1.16.5-rc1","1.16.5"]
ARDUINO_HOST_SYSTEM="i686-mingw32"
ARDUINO_OS_TYPE="windows"
ARDUINO_MAIN_SKETCH_FILE_EXTENSIONS=[".ino",".pde"]
ARDUINO_ADDITIONAL_SKETCH_FILE_EXTENSIONS=[".c",".cpp",".h",".hh",".hpp",".s"]
ARDUINO_OPTIMIZE_FOR_DEBUG=False
ARDUINO_PREPROCESSOR_BUILD_PROPERTIES={"tools.arduino-preprocessor.path":"{runtime.tools.arduino-preprocessor.path}","tools.arduino-preprocessor.cmd.path":"{path}/arduino-preprocessor","tools.arduino-preprocessor.pattern":"\"{cmd.path}\" \"{source_file}\" \"{codecomplete}\" -- -std=gnu++11","preproc.macros.flags":"-w -x c++ -E -CC"}
ARDUINO_CUSTOM_WARNING_LEVEL=""
REPO_STATS_MAX_READ=65536
REPO_STATS_IGNORE_REGEX=re.compile(r"""(?://|#|%).*?$|/\*(?:.)*?\*/|<!--(?:.)*?-->|\{-(?:.)*?-\}|\(\*(?:.)*?\*\)|(?P<ml_c>[\'\"]|\'{3}|\"{3})(?:\\[\'\"]|.)*?(?P=ml_c)|0[bB][0-1]+|0[oO][0-7]+|0[xX][0-9a-f]+|(?:[0-9]+(?:\.[0-9]+)?|\.[0-9]+)(?:[eE][\+\-]?[0-9]+)?""",re.M|re.S)
REPO_STATS_IGNORE_REGEX=re.compile(r"""[ \t]*(\/\/|--|\#|%|\").*?$|/\*(?:.)*?\*/|<!--(?:.)*?-->|\{-(?:.)*?-\}|\(\*(?:.)*?\*\)|(?P<ml_c>[\'\"]|\'{3}|\"{3})(?:\\[\'\"]|.)*?(?P=ml_c)|(0x[0-9a-fA-F]([0-9a-fA-F]|\.)*|[0-9]([0-9]|\.)*)([uU][lL]{0,2}|([eE][-+][0-9]*)?[fFlL]*)""",re.M|re.S)
REPO_STATS_SHEBANG_REGEX=re.compile(r"#!\s*?([^ \t\v\n\r]*?)(?:$|[ \t]+(.*?)$|[ \t\v\n\r])",re.M|re.S)
REPO_STATS_TAG_REGEX=re.compile(r"<\s*\??\s*([\w\$\.]+)(.*?)\??\s*>")
REPO_STATS_TAG_ATTR_REGEX=re.compile(r"""([\w\$\.]+)(?:\s*=?(?:[\w\$\.]+(?:\s|$)|\"(?:\\\"|.)*?\"))?""",re.M|re.S)
REPO_STATS_COMMON_REGEX=re.compile(r";|\{|\}|\(|\)|\[|\]|[\w\.\@\#\/\*]+|\<\<?|\+|\-|\*|\/|%|&&?|\|\|?")
REPO_STATS_XML_REGEX=re.compile(r"<\?xml version=")
REPO_STATS_MAX_TOKEN_LEN=32
REPO_STATS_LOG_ZERO_TOKENS=None
REPO_STATS_BAR_WIDTH=60
REPO_STATS_DEFAULT_COLOR=(240,240,240)
VK_KEYS={"cancel":0x03,"backspace":0x08,"tab":0x09,"clear":0x0c,"enter":0x0d,"shift":0x10,"ctrl":0x11,"alt":0x12,"pause":0x13,"capslock":0x14,"esc":0x1b,"spacebar":0x20,"pageup":0x21,"pagedown":0x22,"end":0x23,"home":0x24,"left":0x25,"up":0x26,"right":0x27,"down":0x28,"select":0x29,"print":0x2a,"execute":0x2b,"printscreen":0x2c,"insert":0x2d,"delete":0x2e,"help":0x2f,"0":0x30,"1":0x31,"2":0x32,"3":0x33,"4":0x34,"5":0x35,"6":0x36,"7":0x37,"8":0x38,"9":0x39,"a":0x41,"b":0x42,"c":0x43,"d":0x44,"e":0x45,"f":0x46,"g":0x47,"h":0x48,"i":0x49,"j":0x4a,"k":0x4b,"l":0x4c,"m":0x4d,"n":0x4e,"o":0x4f,"p":0x50,"q":0x51,"r":0x52,"s":0x53,"t":0x54,"u":0x55,"v":0x56,"w":0x57,"x":0x58,"y":0x59,"z":0x5a,"leftwindows":0xffff,"rightwindows":0xffff,"apps":0x5d,"sleep":0x5f,"0":0x60,"1":0x61,"2":0x62,"3":0x63,"4":0x64,"5":0x65,"6":0x66,"7":0x67,"8":0x68,"9":0x69,"*":0x6a,"+":0x6b,"separator":0x6c,"-":0x6d,"decimal":0x6e,"/":0x6f,"f1":0x70,"f2":0x71,"f3":0x72,"f4":0x73,"f5":0x74,"f6":0x75,"f7":0x76,"f8":0x77,"f9":0x78,"f10":0x79,"f11":0x7a,"f12":0x7b,"f13":0x7c,"f14":0x7d,"f15":0x7e,"f16":0x7f,"f17":0x80,"f18":0x81,"f19":0x82,"f20":0x83,"f21":0x84,"f22":0x85,"f23":0x86,"f24":0x87,"numlock":0x90,"scrolllock":0x91,"leftshift":0x10,"rightshift":0x10,"leftctrl":0x11,"rightctrl":0x11,"leftmenu":0x12,"rightmenu":0x12,"volumemute":0xad,"volumedown":0xae,"volumeup":0xaf,";":0xba,"+":0xbb,",":0xbc,"-":0xbd,".":0xbe,"/":0xbf,"`":0xc0,"[":0xdb,"\\":0xdc,"]":0xdd,"'":0xde,"windows":0xffff}
VK_SAME_KEYS={0x5b:0xffff,0x5c:0xffff,0xa0:0x10,0xa1:0x10,0xa2:0x11,0xa2:0x11,0xa4:0x12,0xa5:0x12}
for k,v in VK_KEYS.items():
	if (v in VK_SAME_KEYS):
		VK_KEYS[k]=VK_SAME_KEYS[v]



DICS_FLAG_GLOBAL=1
DIGCF_PRESENT=2
DIREG_DEV=1
KEY_READ=131097
LLKHF_ALTDOWN=32
LLKHF_INJECTED=16
PM_REMOVE=1
SPDRP_HARDWAREID=1
VK_PACKET=231
WH_KEYBOARD_LL=13
WM_KEYDOWN=256
WM_SYSKEYDOWN=260



ctypes.wintypes.ULONG_PTR=ctypes.POINTER(ctypes.wintypes.DWORD)
ctypes.wintypes.LRESULT=ctypes.c_int
ctypes.wintypes.HDEVINFO=ctypes.c_void_p
ctypes.wintypes.PCWSTR=ctypes.c_wchar_p
ctypes.wintypes.LowLevelKeyboardProc=ctypes.WINFUNCTYPE(ctypes.c_int,ctypes.c_int,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
ctypes.wintypes.PSMALL_RECT=ctypes.POINTER(ctypes.wintypes.SMALL_RECT)
ctypes.wintypes.PHHOOK=ctypes.POINTER(ctypes.wintypes.HHOOK)
ctypes.wintypes.CONSOLE_CURSOR_INFO=type("CONSOLE_CURSOR_INFO",(ctypes.Structure,),{"_fields_":[("dwSize",ctypes.wintypes.DWORD),("bVisible",ctypes.wintypes.BOOL)]})
ctypes.wintypes.PCONSOLE_CURSOR_INFO=ctypes.POINTER(ctypes.wintypes.CONSOLE_CURSOR_INFO)
ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO=type("CONSOLE_SCREEN_BUFFER_INFO",(ctypes.Structure,),{"_fields_":[("dwSize",ctypes.wintypes._COORD),("dwCursorPosition",ctypes.wintypes._COORD),("wAttributes",ctypes.wintypes.WORD),("srWindow",ctypes.wintypes.SMALL_RECT),("dwMaximumWindowSize",ctypes.wintypes._COORD)]})
ctypes.wintypes.PCONSOLE_SCREEN_BUFFER_INFO=ctypes.POINTER(ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO)
ctypes.wintypes.KBDLLHOOKSTRUCT=type("KBDLLHOOKSTRUCT",(ctypes.Structure,),{"_fields_":[("vk_code",ctypes.wintypes.DWORD),("scan_code",ctypes.wintypes.DWORD),("flags",ctypes.wintypes.DWORD),("time",ctypes.c_int),("dwExtraInfo",ctypes.wintypes.ULONG_PTR)]})
ctypes.wintypes.GUID=type("GUID",(ctypes.Structure,),{"_fields_":[("Data1",ctypes.wintypes.DWORD),("Data2",ctypes.wintypes.WORD),("Data3",ctypes.wintypes.WORD),("Data4",ctypes.wintypes.BYTE*8)]})
ctypes.wintypes.PGUID=ctypes.POINTER(ctypes.wintypes.GUID)
ctypes.wintypes.SP_DEVINFO_DATA=type("SP_DEVINFO_DATA",(ctypes.Structure,),{"_fields_":[("cbSize",ctypes.wintypes.DWORD),("ClassGuid",ctypes.wintypes.GUID),("DevInst",ctypes.wintypes.DWORD),("Reserved",ctypes.wintypes.ULONG_PTR)]})
ctypes.wintypes.PSP_DEVINFO_DATA=ctypes.POINTER(ctypes.wintypes.SP_DEVINFO_DATA)
ctypes.windll.advapi32.RegCloseKey.argtypes=(ctypes.wintypes.HKEY,)
ctypes.windll.advapi32.RegCloseKey.restype=ctypes.wintypes.LONG
ctypes.windll.advapi32.RegQueryValueExW.argtypes=(ctypes.wintypes.HKEY,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPDWORD,ctypes.wintypes.LPDWORD,ctypes.c_void_p,ctypes.wintypes.LPDWORD)
ctypes.windll.advapi32.RegQueryValueExW.restype=ctypes.wintypes.LONG
ctypes.windll.kernel32.FillConsoleOutputAttribute.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.WORD,ctypes.wintypes.DWORD,ctypes.wintypes._COORD,ctypes.wintypes.LPDWORD)
ctypes.windll.kernel32.FillConsoleOutputAttribute.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.FillConsoleOutputCharacterA.argtypes=(ctypes.wintypes.HANDLE,ctypes.c_char,ctypes.wintypes.DWORD,ctypes.wintypes._COORD,ctypes.wintypes.LPDWORD)
ctypes.windll.kernel32.FillConsoleOutputCharacterA.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.GetConsoleCursorInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PCONSOLE_CURSOR_INFO)
ctypes.windll.kernel32.GetConsoleCursorInfo.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.GetConsoleMode.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.LPDWORD)
ctypes.windll.kernel32.GetConsoleMode.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.GetConsoleScreenBufferInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PCONSOLE_SCREEN_BUFFER_INFO)
ctypes.windll.kernel32.GetConsoleScreenBufferInfo.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.GetModuleHandleW.argtypes=(ctypes.wintypes.LPCWSTR,)
ctypes.windll.kernel32.GetModuleHandleW.restype=ctypes.wintypes.HMODULE
ctypes.windll.kernel32.GetStdHandle.argtypes=(ctypes.wintypes.DWORD,)
ctypes.windll.kernel32.GetStdHandle.restype=ctypes.wintypes.HANDLE
ctypes.windll.kernel32.SetConsoleCursorInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.PCONSOLE_CURSOR_INFO)
ctypes.windll.kernel32.SetConsoleCursorInfo.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetConsoleCursorPosition.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes._COORD)
ctypes.windll.kernel32.SetConsoleCursorPosition.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetConsoleMode.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.DWORD)
ctypes.windll.kernel32.SetConsoleMode.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetConsoleScreenBufferSize.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes._COORD)
ctypes.windll.kernel32.SetConsoleScreenBufferSize.restype=ctypes.wintypes.BOOL
ctypes.windll.kernel32.SetConsoleWindowInfo.argtypes=(ctypes.wintypes.HANDLE,ctypes.wintypes.BOOL,ctypes.wintypes.PSMALL_RECT)
ctypes.windll.kernel32.SetConsoleWindowInfo.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiClassGuidsFromNameW.argtypes=(ctypes.wintypes.PCWSTR,ctypes.wintypes.PGUID,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD)
ctypes.windll.setupapi.SetupDiClassGuidsFromNameW.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiDestroyDeviceInfoList.argtypes=(ctypes.wintypes.HDEVINFO,)
ctypes.windll.setupapi.SetupDiDestroyDeviceInfoList.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiEnumDeviceInfo.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.DWORD,ctypes.wintypes.PSP_DEVINFO_DATA)
ctypes.windll.setupapi.SetupDiEnumDeviceInfo.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiGetClassDevsW.argtypes=(ctypes.wintypes.PGUID,ctypes.wintypes.PCWSTR,ctypes.wintypes.HWND,ctypes.wintypes.DWORD)
ctypes.windll.setupapi.SetupDiGetClassDevsW.restype=ctypes.wintypes.HDEVINFO
ctypes.windll.setupapi.SetupDiGetDeviceRegistryPropertyW.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.PSP_DEVINFO_DATA,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD,ctypes.c_void_p,ctypes.wintypes.DWORD,ctypes.wintypes.PDWORD)
ctypes.windll.setupapi.SetupDiGetDeviceRegistryPropertyW.restype=ctypes.wintypes.BOOL
ctypes.windll.setupapi.SetupDiOpenDevRegKey.argtypes=(ctypes.wintypes.HDEVINFO,ctypes.wintypes.PSP_DEVINFO_DATA,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD,ctypes.wintypes.DWORD)
ctypes.windll.setupapi.SetupDiOpenDevRegKey.restype=ctypes.wintypes.HKEY
ctypes.windll.user32.CallNextHookEx.argtypes=(ctypes.wintypes.PHHOOK,ctypes.c_int,ctypes.wintypes.WPARAM,ctypes.wintypes.LPARAM)
ctypes.windll.user32.CallNextHookEx.restype=ctypes.wintypes.LRESULT
ctypes.windll.user32.DispatchMessageW.argtypes=(ctypes.wintypes.LPMSG,)
ctypes.windll.user32.DispatchMessageW.restype=ctypes.wintypes.LRESULT
ctypes.windll.user32.PeekMessageW.argtypes=(ctypes.wintypes.LPMSG,ctypes.wintypes.HWND,ctypes.c_uint,ctypes.c_uint,ctypes.c_uint)
ctypes.windll.user32.PeekMessageW.restype=ctypes.wintypes.BOOL
ctypes.windll.user32.SetWindowsHookExW.argtypes=(ctypes.c_int,ctypes.wintypes.LowLevelKeyboardProc,ctypes.wintypes.HINSTANCE,ctypes.wintypes.DWORD)
ctypes.windll.user32.SetWindowsHookExW.restype=ctypes.wintypes.HHOOK
ctypes.windll.user32.ShowCursor.argtypes=(ctypes.wintypes.BOOL,)
ctypes.windll.user32.ShowCursor.restype=ctypes.c_int
ctypes.windll.user32.TranslateMessage.argtypes=(ctypes.wintypes.LPMSG,)
ctypes.windll.user32.TranslateMessage.restype=ctypes.wintypes.BOOL
ctypes.windll.user32.UnhookWindowsHookEx.argtypes=(ctypes.wintypes.HHOOK,)
ctypes.windll.user32.UnhookWindowsHookEx.restype=ctypes.wintypes.BOOL



def _set_print(*a):
	if (len(a)==1):
		threading.current_thread()._b_nm=t._b_nm
		threading.current_thread()._nm=t._nm
	else:
		threading.current_thread()._b_nm=a[0]
		threading.current_thread()._nm=a[1]



def _print(*a,end="\n"):
	global CMD_L,STDOUT_LOCK,R_STD_BUFFER
	def _r_color_f(m):
		if (m.group(0)[0]=="'"):
			return f"\x1b[38;2;91;216;38m{m.group(0)}\x1b[0m"
		elif (m.group(0)[0] in "-0123456789" and m.group(0)[-1]!="%"):
			return f"\x1b[38;2;48;109;206m{m.group(0)}\x1b[0m"
		elif (m.group(0)[0] in "-0123456789" and m.group(0)[-1]=="%"):
			return f"\x1b[38;2;245;103;245m{m.group(0)}\x1b[0m"
		m=m.group(0)[1:-1]
		o=""
		i=0
		while (i<len(m)):
			while (m[i]==" "):
				o+=" "
				i+=1
			o+="\x1b[38;2;214;206;42m"+m[i:].split("=")[0]+"\x1b[38;2;32;162;132m="
			i+=len(m[i:].split("=")[0])+1
			while (m[i]==" "):
				o+=" "
				i+=1
			if (m[i]=="'"):
				o+="\x1b[38;2;91;216;38m'"
				i+=1
				s=False
				while (s==False or m[i-1]!="'"):
					o+=m[i]
					i+=1
					s=True
			elif (m[i:].startswith("False")):
				o+="\x1b[38;2;239;128;15mFalse"
				i+=5
			elif (m[i:][:4] in "True,None".split(",")):
				o+=f"\x1b[38;2;239;128;15m{m[i:][:4]}"
				i+=4
			else:
				o+="\x1b[38;2;48;109;206m"
				while (m[i] in "0123456789.-"):
					o+=m[i]
					i+=1
			if (i>=len(m)):
				break
			while (m[i]==" "):
				o+=" "
				i+=1
			if (m[i]==","):
				o+="\x1b[38;2;32;162;132m,"
				i+=1
		return "\x1b[38;2;186;39;130m("+o+"\x1b[38;2;186;39;130m)\x1b[0m"
	def _r_std_thr():
		global R_STD_BUFFER
		while (R_STD_BUFFER["_e"]==False):
			if (len(R_STD_BUFFER["bf"])>0):
				_,R_STD_BUFFER["bf"]=R_STD_BUFFER["_s"].sendall(base64.b64encode(R_STD_BUFFER["bf"][0])+b"\n"),R_STD_BUFFER["bf"][1:]
	a=" ".join([str(e) for e in a])
	if (not hasattr(threading.current_thread(),"_df") or threading.current_thread()._df==False):
		i=0
		while (i<len(a)):
			_im=re.match(r"\x1b\[[^m]+m",a[i:])
			if (_im!=None):
				i+=len(_im.group(0))
			m=re.match(r"\(( *[A-Za-z0-9_]+ *= *(?:False|True|None|-?[0-9]+(?:\.[0-9]+)?%?|'[^']*'),?)+ *\)|'[^']*'|-?[0-9]+(?:\.[0-9]+)?%|-?[0-9]+(?:\.[0-9]+)?\b",a[i:])
			if (m!=None):
				o=_r_color_f(m)
				a=a[:i]+o+a[i+len(m[0]):]
				i+=len(o)-1
			i+=1
	if (hasattr(threading.current_thread(),"_r") and threading.current_thread()._r>=1):
		if (R_STD_BUFFER["_s"]==None):
			R_STD_BUFFER["_s"]=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			R_STD_BUFFER["_s"].connect(("127.0.0.1",8022))
			thr=threading.Thread(target=_r_std_thr,args=(),kwargs={})
			thr.daemon=True
			thr.start()
			atexit.register(lambda:(R_STD_BUFFER.__setitem__("_e",True),[R_STD_BUFFER["_s"].sendall(base64.b64encode(e)+b"\n") for e in R_STD_BUFFER["bf"]]))
		R_STD_BUFFER["bf"]+=[bytes(f"{threading.current_thread()._b_nm}\x00{threading.current_thread()._nm}\x00{a}","utf-8")]
		if (threading.current_thread()._r>=2):
			return
	if (not hasattr(threading.current_thread(),"_dp") or threading.current_thread()._dp==False):
		t=(datetime.datetime.now().strftime("\x1b[38;2;50;50;50m[%H:%M:%S]\x1b[0m ") if not hasattr(threading.current_thread(),"_dph") or threading.current_thread()._dph==False else "")
		if (threading.current_thread()._nm not in CMD_L[threading.current_thread()._b_nm].keys()):
			CMD_L[threading.current_thread()._b_nm][threading.current_thread()._nm]=b""
		CMD_L[threading.current_thread()._b_nm][threading.current_thread()._nm]+=bytes(t+a.replace("\n","\n"+" "*len(re.sub(r"\x1b\[[^m]+m","",t)))+end,"utf-8")
	t=(datetime.datetime.now().strftime((f"\x1b[38;2;50;50;50m[%H:%M:%S]\x1b[0m [{threading.current_thread()._b_nm}/{threading.current_thread()._nm}] " if not hasattr(threading.current_thread(),"_dpt") or threading.current_thread()._dpt==False else f"\x1b[38;2;50;50;50m[%H:%M:%S]\x1b[0m ")) if not hasattr(threading.current_thread(),"_dph") or threading.current_thread()._dph==False else "")
	while (STDOUT_LOCK==True):
		pass
	STDOUT_LOCK=True
	sys.__stdout__.write(t+a.replace("\n","\n"+" "*len(re.sub(r"\x1b\[[^m]+m","",t)))+"\x1b[0m"+end)
	STDOUT_LOCK=False



def _start_thr(f,b_nm,nm,*a,**kw):
	def _wr(f,a,kw):
		global CMD_L
		if (b_nm not in CMD_L.keys()):
			CMD_L[b_nm]={nm:b""}
		if (nm not in CMD_L[b_nm].keys()):
			CMD_L[b_nm][nm]=b""
		try:
			f(*a,**kw)
		except Exception as e:
			f=io.StringIO()
			traceback.print_exception(None,e,e.__traceback__,file=f)
			CMD_L[threading.current_thread()._b_nm][threading.current_thread()._nm]+=bytes("\x1b[38;2;200;40;20m"+f.getvalue(),"utf-8")
			print(f.getvalue(),file=sys.__stdout__,end="")
	thr=threading.Thread(target=_wr,args=(f,a,kw),kwargs={},name=f"{b_nm} => {nm} Thread")
	thr._b_nm=b_nm
	thr._nm=nm
	thr.daemon=True
	thr.start()
	return thr



def _open_app(p,file=False):
	if (file==True):
		os.startfile(p)
	else:
		subprocess.Popen(p,creationflags=subprocess.CREATE_NEW_CONSOLE)



def _gitigonre_match(gdt,fp):
	def _pattern(p,fp):
		fnm=os.path.normpath(fp).replace(os.sep,"/").split("/")
		if (len(fnm)<len(p[1].split("/"))):
			return False
		if (len(p[1].split("/")[0])==0):
			for sr,sfnm in zip(p[1].split("/"),fnm):
				if (fnmatch.fnmatch(sfnm,sr)==False):
					return False
			return True
		else:
			for i in range(0,len(fnm)-len(p[1].split("/"))+1):
				for sr,sfnm in zip(p[1].split("/"),fnm[i:]):
					if (fnmatch.fnmatch(sfnm,sr)==False):
						break
				else:
					return True
			return False
	ig=False
	for p in gdt:
		if ((ig==False or p[0]==True) and _pattern(p,fp)==True):
			if (p[0]==True):
				return False
			ig=True
	if (ig==True):
		return True
	return False



def _is_bin(fp):
	with open(fp,"rb") as f:
		dt=f.read(4096)
	if (len(dt)==0):
		return False
	r1=len(dt.translate(None,b"\t\r\n\f\b"+bytes(range(32,127))))/len(dt)
	r2=len(dt.translate(None,bytes(range(127,256))))/len(dt)
	if (r1>0.90 and r2>0.9):
		return True
	enc_u=False
	try:
		dt.decode(encoding="utf-8")
		enc_u=True
	except:
		pass
	if ((r1>0.3 and r2<0.05) or (r1>0.8 and r2>0.8)):
		return (False if enc_u==True else True)
	else:
		return (True if enc_u==False and (b"\x00" in dt or b"\xff" in dt) else False)



def _update_repo(p,b_nm):
	def _request(m="get",**kw):
		kw["headers"]={**kw.get("headers",{}),"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Update API"}
		r=getattr(requests,m)(**kw)
		if ("X-RateLimit-Remaining" in r.headers.keys() and r.headers["X-RateLimit-Remaining"]=="0"):
			print(r.headers)
			sys.exit(1)
		time.sleep(0.72)
		if (type(r.json())==dict and "message" in r.json().keys() and r.json()["message"]=="Server Error"):
			print(r.json())
			return None
		return r.json()
	def _get_tree(r_nm,sha):
		def _rec_get(r_nm,sha,p):
			r=_request("get",url=f"https://api.github.com/repos/Krzem5/{r_nm}/git/trees/{sha}",data=json.dumps({"recursive":"false"}))
			o={}
			for e in r["tree"]:
				if (e["type"]=="tree"):
					o.update(_rec_get(r_nm,e["sha"],p+"/"+e["path"]))
				elif ((p+"/"+e["path"]).replace("./","")!="_"):
					o[(p+"/"+e["path"]).replace("./","")]={"sz":e["size"],"sha":e["sha"]}
			return o
		return _rec_get(r_nm,sha,".")
	def _match_f(fp,dt):
		if (_is_bin(fp)==False):
			try:
				with open(fp,"r",encoding="cp1252") as f:
					f=f.read().replace("\r\n","\n")
					if (len(f)!=dt["sz"]):
						return False
					return (True if hashlib.sha1(f"blob {len(f)}\x00{f}".encode("cp1252")).hexdigest()==dt["sha"] else False)
			except:
				if (os.stat(fp).st_size!=dt["sz"]):
					return False
				with open(fp,"rb") as f:
					return (True if hashlib.sha1(f"blob {os.stat(fp).st_size}\x00".encode("cp1252")+f.read()).hexdigest()==dt["sha"] else False)
		else:
			if (os.stat(fp).st_size!=dt["sz"]):
				return False
			with open(fp,"rb") as f:
				return (True if hashlib.sha1(f"blob {os.stat(fp).st_size}\x00".encode("cp1252")+f.read()).hexdigest()==dt["sha"] else False)
	b_nm=b_nm.split("-")[0].title()+("" if b_nm.count("-")==0 else "-"+b_nm.split("-")[1].replace("_"," ").title().replace(" ","_"))
	nm=re.sub(r"[^A-Za-z0-9_\.\-]",r"",b_nm)
	with open("D:\\boot\\github-created.dt","r") as f:
		gr_dt=f.read().strip().replace("\r","").split("\n")
	if (nm not in gr_dt):
		try:
			_request("post",url="https://api.github.com/user/repos",data=json.dumps({"name":nm,"description":nm.replace("-"," - ")}))
		except requests.exceptions.ConnectionError:
			_print("\x1b[38;2;200;40;20mNo Internet Connection.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			return False
	with open(os.path.join(p,".gitignore"),"r") as f:
		gdt=[]
		for ln in f.read().replace("\r","").split("\n"):
			if (ln.endswith("\n")):
				ln=ln[:-1]
			ln=ln.lstrip()
			if (not ln.startswith("#")):
				iv=False
				if (ln.startswith("!")):
					ln=ln[1:]
					iv=True
				while (ln.endswith(" ") and ln[-2:]!="\\ "):
					ln=ln[:-1]
				ln=re.sub(r"\\([!# ])",r"\1",ln)
				if (len(ln)>0):
					if ("**/" in ln):
						gdt+=[[iv,ln.replace("**/","")]]
					gdt+=[[iv,ln]]
	msg=datetime.datetime.now().strftime("Push Update %m/%d/%Y, %H:%M:%S")
	br=_request("get",url=f"https://api.github.com/repos/Krzem5/{nm}/branches")
	if ("message" in br):
		return True
	br=[e["name"] for e in br]
	br=("main" if "main" in br else ("master" if "master" in br else ("main" if len(br)==0 else br[0])))
	try:
		bt_sha=_request("get",url=f"https://api.github.com/repos/Krzem5/{nm}/git/ref/heads/{br}")["object"]["sha"]
	except KeyError:
		_request("put",url=f"https://api.github.com/repos/Krzem5/{nm}/contents/_",data=json.dumps({"message":msg,"content":""}))
		bt_sha=_request("get",url=f"https://api.github.com/repos/Krzem5/{nm}/git/ref/heads/{br}")["object"]["sha"]
	r_t=_get_tree(nm,bt_sha)
	bl=[]
	cnt=[0,0,0,0]
	for r,_,fl in os.walk(p):
		for f in fl:
			fp=os.path.join(r,f).replace(p,"")[(1 if not p.endswith("\\") else 0):].replace("\\","/")
			if (_gitigonre_match(gdt,fp)==True):
				cnt[2]+=1
				_print(f"\x1b[38;2;190;0;220m! {b_nm}/{fp}\x1b[0m")
				continue
			if (fp in list(r_t.keys()) and _match_f(os.path.join(r,f),r_t[fp])==True):
				cnt[1]+=1
				bl+=[[fp,None]]
				_print(f"\x1b[38;2;230;210;40m? {b_nm}/{fp}\x1b[0m")
				continue
			cnt[0]+=1
			_print(f"\x1b[38;2;70;210;70m+ {b_nm}/{fp}\x1b[0m")
			dt=f"File too Large (size = {os.stat(os.path.join(r,f)).st_size} b)"
			b_sha=False
			if (os.stat(os.path.join(r,f)).st_size<=50*1024*1024):
				b64=True
				if (_is_bin(os.path.join(r,f))==False):
					try:
						with open(os.path.join(r,f),"r",encoding="utf-8") as rbf:
							dt=rbf.read().replace("\r\n","\n")
						b64=False
					except:
						pass
				if (b64==True):
					b_sha=True
					with open(os.path.join(r,f),"rb") as rbf:
						dt=str(base64.b64encode(rbf.read()),"utf-8")
					if (len(dt)>50*1024*1024):
						b_sha=False
						dt="File too Large (size = %d b)"%(len(dt))
					else:
						b=_request("post",url=f"https://api.github.com/repos/Krzem5/{nm}/git/blobs",data=json.dumps({"content":dt,"encoding":"base64"}))
						if (b==None):
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
		_request("patch",url=f"https://api.github.com/repos/Krzem5/{nm}/git/refs/heads/{br}",data=json.dumps({"sha":_request("post",url=f"https://api.github.com/repos/Krzem5/{nm}/git/commits",data=json.dumps({"message":msg,"tree":_request("post",url=f"https://api.github.com/repos/Krzem5/{nm}/git/trees",data=json.dumps({"base_tree":bt_sha,"tree":[b[1] for b in bl if b[1]!=None]}))["sha"],"parents":[bt_sha]}))["sha"],"force":True}))
	if (nm not in gr_dt):
		_request("delete",url=f"https://api.github.com/repos/Krzem5/{nm}/contents/_",data=json.dumps({"message":msg,"sha":"e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"}))
		with open("D:\\boot\\github-created.dt","w") as f:
			f.write("\n".join(gr_dt)+f"\n{nm}")
	_print(f"\x1b[38;2;40;210;190m{b_nm} => \x1b[38;2;70;210;70m+{cnt[0]}\x1b[38;2;40;210;190m, \x1b[38;2;230;210;40m?{cnt[1]}\x1b[38;2;40;210;190m, \x1b[38;2;190;0;220m!{cnt[2]}\x1b[38;2;40;210;190m, \x1b[38;2;210;40;40m-{cnt[3]}\x1b[0m")
	return True



def _git_project_push(r=False,fr=False):
	_print(f"Starting Github Project Push Check\x1b[38;2;100;100;100m...")
	if (r==True):
		threading.current_thread()._dp=True
		threading.current_thread()._r=1
	threading.current_thread()._df=True
	tm=int(time.time()//604800)
	t=[0,0]
	with open("./github.dt","r") as f:
		b_dt=f.read().replace("\r","").split("\n")
	with open("./github.dt","w") as f:
		if (len(b_dt[0])==0 or int(b_dt[0])<tm):
			b_dt=[None]
		f.write(str(tm)+"\n")
		f.flush()
		for p in sorted(os.listdir("D:\\K\\Coding")):
			if (fr==False and p in b_dt[1:]):
				t[1]+=1
				f.write(p+"\n")
				f.flush()
				continue
			t[0]+=1
			if (_update_repo(f"D:\\K\\Coding\\{p}",p)==False):
				return
			f.write(p+"\n")
			f.flush()
		if (fr==False and "Boot_Program" in b_dt[1:]):
			t[1]+=1
			f.write("Boot_Program\n")
			f.flush()
		else:
			t[0]+=1
			if (_update_repo("D:\\boot\\","Boot_Program")==False):
				return
			f.write("Boot_Program\n")
			f.flush()
	threading.current_thread()._df=False
	_print(f"Finished Github Project Push Check, {t[0]} Projects Updated, {t[1]} Skipped.")



def _repo_file_tokenize(dt,el=None):
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



def _repo_stats_detect_file(r,fn,ll,hdt,db):
	if (os.stat(os.path.join(r,fn)).st_size==0 or _is_bin(os.path.join(r,fn))==True or fn=="LICENSE"):
		return None
	o=list(ll.keys())
	c=[]
	for k in db["languages"]:
		if (fn in db["filenames"][k]):
			c.append(k)
	if (el["__e__"]==1):
		return
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
		return
	if (len(c)>0):
		o=c[:]
	if (len(o)==1):
		return o[0]
	dt=None
	try:
		with open(os.path.join(r,fn),"rb") as f:
			dt=f.read().decode("utf-8",errors="replace")
	except PermissionError:
		return None
	if (REPO_STATS_XML_REGEX.search("\n".join(dt.split("\n")[:2]))!=None):
		return "XML"
	if (el["__e__"]==1):
		return
	c.clear()
	for k in hdt:
		if (ex in k[0]):
			for e in k[1]:
				if (e[1]==None):
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
		return
	if (len(c)>0):
		o=c[:]
	if (len(o)==1):
		return o[0]
	if (len(o)==0):
		return None
	tl=_repo_file_tokenize(dt,el)
	if (el["__e__"]==1):
		return
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



def _repo_stats(fp,ll,hdt,db,el):
	gdt=[]
	with open(os.path.join(fp,".gitignore"),"r") as f:
		for ln in f.read().replace("\r","").split("\n"):
			if (ln.endswith("\n")):
				ln=ln[:-1]
			ln=ln.lstrip()
			if (not ln.startswith("#")):
				iv=False
				if (ln.startswith("!")):
					ln=ln[1:]
					iv=True
				while (ln.endswith(" ") and ln[-2:]!="\\ "):
					ln=ln[:-1]
				ln=re.sub(r"\\([!# ])",r"\1",ln)
				if (len(ln)>0):
					if ("**/" in ln):
						gdt+=[[iv,ln.replace("**/","")]]
					gdt+=[[iv,ln]]
	if (el["__e__"]==1):
		return
	for r,_,fl in os.walk(fp):
		if (el["__e__"]==1):
			return
		if ("\\build" not in r.lower()):
			for f in fl:
				if (el["__e__"]==1):
					return
				el["__cf__"]=os.path.join(r,f)
				if (el["__ig__"]==True and _gitigonre_match(gdt,os.path.join(r,f)[len(fp):])==True):
					continue
				l=_repo_stats_detect_file(r,f,ll,hdt,db)
				if (el["__e__"]==1):
					return
				if (l==None):
					continue
				if (l not in el):
					el[l]=0
				el[l]+=os.stat(os.path.join(r,f)).st_size
				el["__tcnt__"]+=os.stat(os.path.join(r,f)).st_size



def _read_repo_stats(fp,ll,hdt,db,el):
	if (fp==None):
		for fp in os.listdir("D:\\K\\Coding\\"):
			_repo_stats(f"D:\\K\\Coding\\{fp}\\",ll,hdt,db,el)
			if (el["__e__"]==1):
				break
		_repo_stats("D:\\boot\\",ll,hdt,db,el)
	else:
		_repo_stats(fp,ll,hdt,db,el)
	el["__cf__"]=None
	el["__e__"]=2



def _arduino_clone_f(url,fp,sz):
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



def _rm_dir(fp):
	for r,_,fl in os.walk(fp):
		for f in fl:
			os.remove(os.path.join(r,f))
	os.rmdir(fp)



class _Arduino_Cache:
	def init():
		_print("Initialising Cache\x1b[38;2;100;100;100m...")
		if (not os.path.exists(f"D:/boot/arduino/cache")):
			os.mkdir(f"D:/boot/arduino/cache")
		if (not os.path.exists(f"D:/boot/arduino/cache/index")):
			with open(f"D:/boot/arduino/cache/index","w"):
				_Arduino_Cache._dt={}
		else:
			with open(f"D:/boot/arduino/cache/index","r") as f:
				_Arduino_Cache._dt={k.split(":")[0]:float(k.split(":")[1]) for k in f.read().replace("\r","").split("\n") if len(k)>0}
		u=False
		_print("Reading Cache Index\x1b[38;2;100;100;100m...")
		for k in list(_Arduino_Cache._dt.keys()):
			if (_Arduino_Cache._dt[k]<time.time() or not os.path.exists(f"D:/boot/arduino/cache/{k}")):
				if (os.path.exists(f"D:/boot/arduino/cache/{k}")):
					os.remove(f"D:/boot/arduino/cache/{k}")
				del _Arduino_Cache._dt[k]
				u=True
		_print("Removing Old Cache\x1b[38;2;100;100;100m...")
		for k in os.listdir(f"D:/boot/arduino/cache/"):
			if (k=="index" or k in list(_Arduino_Cache._dt.keys())):
				continue
			os.remove(f"D:/boot/arduino/cache/{k}")
		if (u==True):
			with open(f"D:/boot/arduino/cache/index","w") as f:
				f.write("\n".join([f"{e[0]}:{e[1]}" for e in _Arduino_Cache._dt.items()]))



	@staticmethod
	def get(k):
		t=_Arduino_Cache._dt.get(k,0)
		if (t==0):
			return None
		with open(f"D:/boot/arduino/cache/{k}","rb") as f:
			return f.read()



	@staticmethod
	def set(k,v,t=2592000):
		_Arduino_Cache._dt[k]=time.time()+t
		with open(f"D:/boot/arduino/cache/index","w") as f:
			f.write("\n".join([f"{e[0]}:{e[1]}" for e in _Arduino_Cache._dt.items()]))
		with open(f"D:/boot/arduino/cache/{k}","wb") as f:
			f.write(v)



def _l_ard_boards(p=True):
	if (p==True):
		_print("Listing Arduino Boards Attached to the System\x1b[38;2;100;100;100m...")
	pg=(ctypes.wintypes.GUID*8)()
	pg_l=ctypes.wintypes.DWORD()
	ctypes.windll.setupapi.SetupDiClassGuidsFromNameW("Ports",pg,ctypes.sizeof(pg),ctypes.byref(pg_l))
	mg=(ctypes.wintypes.GUID*8)()
	mg_l=ctypes.wintypes.DWORD()
	ctypes.windll.setupapi.SetupDiClassGuidsFromNameW("Modem",mg,ctypes.sizeof(mg),ctypes.byref(mg_l))
	o=[]
	for k in (pg[:pg_l.value]+mg[:mg_l.value]):
		di_g=ctypes.windll.setupapi.SetupDiGetClassDevsW(ctypes.byref(k),None,0,DIGCF_PRESENT)
		di=ctypes.wintypes.SP_DEVINFO_DATA()
		di.cbSize=ctypes.sizeof(di)
		i=0
		while (ctypes.windll.setupapi.SetupDiEnumDeviceInfo(di_g,i,ctypes.byref(di))!=0):
			i+=1
			hkey=ctypes.windll.setupapi.SetupDiOpenDevRegKey(di_g,ctypes.byref(di),DICS_FLAG_GLOBAL,0,DIREG_DEV,KEY_READ)
			nm=ctypes.create_unicode_buffer(256)
			ctypes.windll.advapi32.RegQueryValueExW(hkey,"PortName",None,None,ctypes.byref(nm),ctypes.byref(ctypes.wintypes.ULONG(ctypes.sizeof(nm))))
			ctypes.windll.advapi32.RegCloseKey(hkey)
			if (nm.value[:3]=="LPT"):
				continue
			hw_id=ctypes.create_unicode_buffer(250)
			ctypes.windll.setupapi.SetupDiGetDeviceRegistryPropertyW(di_g,ctypes.byref(di),SPDRP_HARDWAREID,None,ctypes.byref(hw_id),ctypes.sizeof(hw_id)-1,None)
			m=re.search((r"VID_([0-9a-f]{4})&PID_([0-9a-f]{4})" if hw_id.value[:3]=="USB" else r"VID_([0-9a-f]{4})\+PID_([0-9a-f]{4})"),hw_id.value,re.I)
			if (m is not None):
				r=_Arduino_Cache.get(f"vid_pid-0x{hex(int(m.group(1),16))[2:].rjust(4,'0')}-0x{hex(int(m.group(2),16))[2:].rjust(4,'0')}.json")
				if (r==None):
					r=requests.get(f"https://builder.arduino.cc/v3/boards/byVidPid/0x{hex(int(m.group(1),16))[2:].rjust(4,'0')}/0x{hex(int(m.group(2),16))[2:].rjust(4,'0')}",headers={"Content-Type":"application/json"}).text
					_Arduino_Cache.set(f"vid_pid-0x{hex(int(m.group(1),16))[2:].rjust(4,'0')}-0x{hex(int(m.group(2),16))[2:].rjust(4,'0')}.json",bytes(r,"utf-8"))
				if (len(r)==0):
					continue
				r=json.loads(r)
				o+=[{"arch":r["architecture"],"fqbn":r["fqbn"],"name":r["name"],"location":nm.value.replace("\\","/").split("/")[-1]}]
			else:
				continue
		ctypes.windll.setupapi.SetupDiDestroyDeviceInfoList(di_g)
	return o



def _install_ard_pkg(b,force=False):
	if (type(b)==str):
		_print(f"Searching For Package '{b}'\x1b[38;2;100;100;100m...")
		i_pkg=[]
		if (os.path.exists(f"D:/boot/arduino/packages/index")):
			with open(f"D:/boot/arduino/packages/index","r") as f:
				i_pkg=f.read().replace("\r","").split("\n")
		_print(f"Querying 'https://api.github.com/repos/arduino/{b}/releases/latest' for Package Metadata\x1b[38;2;100;100;100m...")
		dt=requests.get(f"https://api.github.com/repos/arduino/{b}/releases/latest").json()
		if (force==False and f"arduino-{b}-{dt['tag_name']}" in i_pkg):
			_print(f"\x1b[38;2;200;40;20mPackage 'arduino:{b}:{dt['tag_name']}' already Installed.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			return
		_print(f"Searching for '{ARDUINO_OS_TYPE}' Release\x1b[38;2;100;100;100m...")
		for k in dt["assets"]:
			if (k["name"].startswith(b+"-") and (k["name"].endswith(".zip") or k["name"].endswith(".tar.bz2")) and "mingw32" in re.sub(r"(\.zip|\.tar\.bz2)$","",k["name"][len(b)+1:])):
				_print(f"Found Release '{k['name']}'.\nCloning to File '{tempfile.gettempdir()}/{k['name']}' ...")
				_arduino_clone_f(k["browser_download_url"],f"{tempfile.gettempdir()}/{k['name']}",k["size"])
				with open(f"{tempfile.gettempdir()}/{k['name']}","wb") as f:
					f.write(requests.get(k["browser_download_url"]).content)
				if (k["name"].endswith(".tar.bz2")):
					_print("Using Extractor 'tar/r:bz2'\x1b[38;2;100;100;100m...")
					_print("Extracting Files\x1b[38;2;100;100;100m...")
					with tarfile.open(f"{tempfile.gettempdir()}/{k['name']}","r:bz2") as tf:
						tf.extractall(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}")
						off=len(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}/")
						_print("Copying Extracted Files\x1b[38;2;100;100;100m...")
						for r,_,fl in os.walk(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}"):
							for f in fl:
								fp=os.path.join(r,f)
								os.makedirs(os.path.dirname(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}"),exist_ok=True)
								try:
									with open(fp,"rb") as rf,open(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}","wb") as wf:
										wf.write(rf.read())
								except Exception as e:
									traceback.print_exception(None,e,e.__traceback__)
									_print(f"\x1b[38;2;200;40;20mError while Copying File '{fp}' to 'D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
						_rm_dir(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}")
				elif (k["name"].endswith(".zip")):
					_print("Using Extractor 'zip'\x1b[38;2;100;100;100m...")
					_print("Extracting Files\x1b[38;2;100;100;100m...")
					with zipfile.ZipFile(f"{tempfile.gettempdir()}/{k['name']}","r") as zf:
						zf.extractall(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}")
				else:
					_print(f"\x1b[38;2;200;40;20mUnknown File Extractor for File Extensions '{k['name'][len(k['name'].split('.')[0]):]}'.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
					raise RuntimeError(f"Unknown File Extension '{k['name'][len(k['name'].split('.')[0]):]}'.")
				_print("Removing Archive\x1b[38;2;100;100;100m...")
				os.remove(f"{tempfile.gettempdir()}/{k['name']}")
		_print("Indexing Package\x1b[38;2;100;100;100m...")
		with open(f"D:/boot/arduino/packages/index","a") as f:
			f.write(f"arduino-{b}-{dt['tag_name']}\n")
		return
	_print(f"Searching For Package '{b['pkg']}:{b['arch']}{(':'+b['ver'] if b['ver']!=None else '')}'...")
	_print("Reading Package Index Cache\x1b[38;2;100;100;100m...")
	dt=_Arduino_Cache.get("package_index.json")
	if (dt==None):
		_print("\x1b[38;2;200;40;20mPackage Index Cache not Found.\x1b[0m Downloaing It\x1b[38;2;100;100;100m...")
		dt=requests.get("https://downloads.arduino.cc/packages/package_index.json",headers={"Content-Type":"application/json"}).text
		_Arduino_Cache.set("package_index.json",bytes(dt,"utf-8"))
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
		e=(sorted(l,key=lambda e:e[0],reverse=True)[0] if d["ver"]==None else [e for e in l if e[0]==d["ver"]][0])
		if (e[2]==False):
			o+=[(d["pkg"],(d["arch"] if "arch" in list(d.keys()) else d["name"]),e[1]["version"],e[1]["url"],e[1]["archiveFileName"],"hardware",int(e[1]["size"]))]
			if (len(e[1]["toolsDependencies"])>0):
				_print(f"Found Dependencies: ('{(chr(39)+', '+chr(39)).join([k['packager']+':'+k['name']+':'+k['version'] for k in e[1]['toolsDependencies']])}')")
			dl+=[{"pkg":k["packager"],"name":k["name"],"ver":k["version"]} for k in e[1]["toolsDependencies"]]
		else:
			o+=[(d["pkg"],(d["arch"] if "arch" in list(d.keys()) else d["name"]),e[1]["version"],k["url"],k["archiveFileName"],"tools",k["size"]) for k in e[1]["systems"] if k["host"]==ARDUINO_HOST_SYSTEM]
	if (not os.path.exists(f"D:/boot/arduino/packages")):
		os.mkdir(f"D:/boot/arduino/packages")
	i_pkg=[]
	if (os.path.exists(f"D:/boot/arduino/packages/index")):
		with open(f"D:/boot/arduino/packages/index","r") as f:
			i_pkg=f.read().replace("\r","").split("\n")
	else:
		with open(f"D:/boot/arduino/packages/index","w"):
			pass
	for k in o:
		if (force==False and f"{k[0]}-{k[1]}-{k[2]}" in i_pkg):
			_print(f"\x1b[38;2;200;40;20mPackage '{k[0]}:{k[1]}:{k[2]}' already Installed.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
			continue
		if (not os.path.exists(f"D:/boot/arduino/packages/{k[0]}")):
			os.mkdir(f"D:/boot/arduino/packages/{k[0]}")
		if (not os.path.exists(f"D:/boot/arduino/packages/{k[0]}/{k[5]}")):
			os.mkdir(f"D:/boot/arduino/packages/{k[0]}/{k[5]}")
		if (not os.path.exists(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}")):
			os.mkdir(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}")
		if (not os.path.exists(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")):
			os.mkdir(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
		_print(f"Cloning to File '{tempfile.gettempdir()}/{k[4]}' ...")
		_arduino_clone_f(k[3],tempfile.gettempdir()+"/"+k[4],k[6])
		if (k[4].endswith(".tar.bz2")):
			_print("Using Extractor 'tar/r:bz2'\x1b[38;2;100;100;100m...")
			_print("Extracting Files\x1b[38;2;100;100;100m...")
			with tarfile.open(tempfile.gettempdir()+"/"+k[4],"r:bz2") as tf:
				tf.extractall(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
				off=len(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}/")
				_print("Copying Extracted Files\x1b[38;2;100;100;100m...")
				for r,_,fl in os.walk(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}"):
					for f in fl:
						fp=os.path.join(r,f)
						os.makedirs(os.path.dirname(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}"),exist_ok=True)
						try:
							with open(fp,"rb") as rf,open(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}","wb") as wf:
								wf.write(rf.read())
						except Exception as e:
							traceback.print_exception(None,e,e.__traceback__)
							_print(f"\x1b[38;2;200;40;20mError while Copying File '{fp}' to 'D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
				_rm_dir(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}")
		elif (k[4].endswith(".zip")):
			_print("Using Extractor 'zip'\x1b[38;2;100;100;100m...")
			_print("Extracting Files\x1b[38;2;100;100;100m...")
			with zipfile.ZipFile(tempfile.gettempdir()+"/"+k[4],"r") as zf:
				zf.extractall(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")
		_print("Removing Archive\x1b[38;2;100;100;100m...")
		os.remove(tempfile.gettempdir()+"/"+k[4])
		_print("Indexing Package\x1b[38;2;100;100;100m...")
		with open(f"D:/boot/arduino/packages/index","a") as f:
			f.write(f"{k[0]}-{k[1]}-{k[2]}\n")



def _split(cmd):
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



def _compile_ard_prog(s_fp,o_fp,fqbn,inc_l):
	def _run_cmd(*a,**kw):
		o=subprocess.run(*a,**kw)
		if (o.returncode!=0):
			sys.exit(o.returncode)
		return o
	def _step_dir(fp):
		return fp+os.listdir(fp)[0]+"/"
	def _quote_fp(fp):
		return fp.replace("\\","\\\\").replace("\"","\\\"")
	def _expand_in_string(d,s):
		while (True):
			ns=s+""
			for k,v in d.items():
				ns=ns.replace(f"{{{k}}}",v)
			if (ns==s):
				return s
			s=ns
	def _prepare_cmd(cmd):
		return [e for e in _split(cmd) if len(e)>0]
	def _run_recipe(bp,pfx,sfx):
		l=[]
		for k in bp.keys():
			if (k.startswith(pfx) and k.endswith(sfx) and len(bp[k])>0):
				cmd=_prepare_cmd(re.sub(r"\{.+?\}","",_expand_in_string(bp,bp[k])))
				_run_cmd(cmd)
	def _compile_files(b,i_fp,o_fp,inc_l,rc):
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
				_run_cmd(_prepare_cmd(re.sub(r"\{.+?\}","",_expand_in_string(c_bp,c_bp[("recipe.S.o.pattern","recipe.c.o.pattern","recipe.cpp.o.pattern")[i]]))))
				o+=[o_fp+f[len(i_fp):]+".o"]
		return o
	def _replace_inc(dt):
		i=0
		while (i<len(dt)):
			m=re.search(br"""^\s*#\s*include\s*(<[^>]+>|"[^"]+")""",dt[i:],re.M)
			if (m==None):
				return dt
			dt=dt[:i+m.start(0)]+b"#include <"+m.group(1)[1:-1].replace(b"\\",b"/").replace(b"/",b"$")+b">"+dt[i+m.end(0)-1:]
			i+=m.end(0)
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
	b_fp=f"{tempfile.gettempdir()}/arduino-build-{hashlib.new('md5',bytes(s_fp,'utf-8')).hexdigest()}/"
	_print(f"Compiling Sketch '{s_fp}' to Directory '{b_fp}' with Architecture '{':'.join(fqbn)}'\x1b[38;2;100;100;100m...")
	if (not os.path.exists(b_fp)):
		os.mkdir(b_fp)
	m_fp=None
	_print("Searching For Main File\x1b[38;2;100;100;100m...")
	for k in ARDUINO_MAIN_SKETCH_FILE_EXTENSIONS:
		if (os.path.exists(f"{s_fp}main{k}")==True and os.path.isdir(f"{s_fp}main{k}")==False):
			if (m_fp!=None):
				raise RuntimeError("Sketch Contains Multiple Main Programs.")
			m_fp=f"{s_fp}main{k}"
	if (m_fp==None):
		raise RuntimeError("Sketch doesn't Contain a Main Program.")
	_print("Loading Packages\x1b[38;2;100;100;100m...")
	if (not os.path.exists(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/")):
		raise RuntimeError(f"Package '{fqbn[0]}:{fqbn[1]}' isn't Installed.")
	h_fp=os.path.abspath(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"+sorted(os.listdir(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"),reverse=True)[0])+"/"
	_print(f"Reading '{h_fp}boards.txt'\x1b[38;2;100;100;100m...")
	with open(f"{h_fp}boards.txt","r") as hb_f:
		h_pm={}
		for k in hb_f.read().replace("\r","").split("\n"):
			if (len(k.strip())==0 or k.strip()[0]=="#"):
				continue
			if (k.split(".")[0] not in list(h_pm.keys())):
				h_pm[k.split(".")[0]]={}
			h_pm[k.split(".")[0]][".".join(k.split("=")[0].split(".")[1:])]=k[len(k.split("=")[0])+1:]
	if (fqbn[2] not in list(h_pm.keys())):
		raise RuntimeError(f"Invalid FQBN '{':'.join(fqbn)}'.")
	_print(f"Reading '{h_fp}platform.txt'\x1b[38;2;100;100;100m...")
	with open(f"{h_fp}platform.txt","r") as hp_f:
		p_pm={k.split("=")[0]:k[len(k.split("=")[0])+1:] for k in hp_f.read().replace("\r","").split("\n") if len(k.strip())>0 and k.strip()[0]!="#"}
	_print(f"Creating Build Properties\x1b[38;2;100;100;100m...")
	bp={"software":"ARDUINO",**p_pm,**h_pm[fqbn[2]],"build.path":re.sub(r"/$","",b_fp),"build.project_name":m_fp.split("/")[-1],"build.arch":fqbn[1].upper()}
	bp.update({"build.core.path":f"{h_fp}cores/{bp['build.core']}","build.system.path":f"{h_fp}system","runtime.platform.path":re.sub(r"/$","",h_fp),"runtime.hardware.path":re.sub(r"/$","",os.path.abspath(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/")),"runtime.ide.version":"10607","runtime.ide.path":"D:/boot/","build.fqbn":":".join(fqbn),"ide_version":"ide_version","runtime.os":ARDUINO_OS_TYPE,"build.variant.path":("" if bp["build.variant"]=="" else f"{h_fp}variants/{bp['build.variant']}"),"build.source.path":re.sub(r"/$","",s_fp),"extra.time.utc":str(int(time.time())),"extra.time.local":str(datetime.datetime.now(datetime.timezone.utc).timestamp()),"extra.time.zone":"0","extra.time.dst":"0"})
	if (ARDUINO_OPTIMIZE_FOR_DEBUG==True):
		if ("compiler.optimization_flags.debug" in list(bp.keys())):
			bp["compiler.optimization_flags"]=bp["compiler.optimization_flags.debug"]
	else:
		if ("compiler.optimization_flags.release" in list(bp.keys())):
			bp["compiler.optimization_flags"]=bp["compiler.optimization_flags.release"]
	_print("Loading Tools\x1b[38;2;100;100;100m...")
	for pkg in os.listdir(f"D:/boot/arduino/packages/"):
		if (os.path.exists(f"D:/boot/arduino/packages/{pkg}/tools/")):
			for t in os.listdir(f"D:/boot/arduino/packages/{pkg}/tools/"):
				for v in os.listdir(f"D:/boot/arduino/packages/{pkg}/tools/{t}/"):
					bp[f"runtime.tools.{t}-{v}.path"]=_step_dir(f"D:/boot/arduino/packages/{pkg}/tools/{t}/{v}/")
				bp[f"runtime.tools.{t}.path"]=_step_dir(f"D:/boot/arduino/packages/{pkg}/tools/{t}/{v}/")
	_print("Comparing Old Build Properties\x1b[38;2;100;100;100m...")
	if (os.path.exists(f"{b_fp}build-properties.md5")):
		with open(f"{b_fp}build-properties.md5","r") as f:
			md5=f.read()
		if (md5[:32]!=hashlib.new("md5",bytes([(k,v) for k,v in bp.items() if not k.startswith("extra.time")].__repr__(),"utf-8")).hexdigest()):
			_print("\x1b[38;2;200;40;20mHash not Matching.\x1b[0m Rebuilding Everything\x1b[38;2;100;100;100m...")
			_rm_dir(b_fp)
			os.mkdir(b_fp)
	_print("Writing New Hash\x1b[38;2;100;100;100m...")
	with open(f"{b_fp}build-properties.md5","w") as f:
		f.write(hashlib.new("md5",bytes([(k,v) for k,v in bp.items() if not k.startswith("extra.time")].__repr__(),"utf-8")).hexdigest())
	_print("Running Recipe 'recipe.hooks.prebuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.prebuild",".pattern")
	l_off=0
	nh_inc=False
	_print("Bundling Sketch Files\x1b[38;2;100;100;100m...")
	with open(b_fp+m_fp.split("/")[-1]+".cpp","wb") as bf:
		src=b""
		for r,_,fl in os.walk(s_fp):
			for fp in fl:
				if ("."+fp.split(".")[-1].lower() in ARDUINO_MAIN_SKETCH_FILE_EXTENSIONS):
					_print(f"Found Main Sketch File '{os.path.join(r,fp)}'\x1b[38;2;100;100;100m...")
					with open(os.path.join(r,fp),"rb") as f:
						dt=f.read().replace(b"\r\n",b"\n")
						if (nh_inc==False and re.search(br"""(?m)^\s*#\s*include\s*[<\"]Arduino\.h[>\"]""",dt)==None):
							bf.write(b"#include <arduino.h>\n")
							l_off+=1
						nh_inc=True
						src+=dt+b"\n"
						bf.write(bytes(f"#line 1 \"{_quote_fp(os.path.join(r,fp))}\"\n","utf-8")+_replace_inc(dt)+b"\n;\n")
						l_off+=(1 if os.path.join(r,fp)==m_fp else 0)
		dl=[(e[0].replace("\\","/"),e[1].replace("\\","/")+("/" if e[1][-1] not in "\\/" else "")) for e in [(s_fp,s_fp)]+[(os.path.join(r,d),r) for r,dl,_ in os.walk(s_fp) for d in dl]+[(e,e) for e in inc_l]]
		l=[e for e in re.findall(r"(?m)^\s*#\s*include\s*[<\"]([^>\"]+)[>\"]",str(src,"utf-8").lower()) if e!="arduino.h"]
		r_dl=[]
		for k in l:
			if (k[-2:]==".h"):
				l+=[k[:-2]+".cpp",k[:-2]+".c",k[:-2]+".s",k.split("/")[-1][:-2]+".cpp",k.split("/")[-1][:-2]+".c",k.split("/")[-1][:-2]+".s"]
			for d in dl:
				if (os.path.exists(os.path.join(d[0],k))):
					_print(f"Found Included Sketch File '{os.path.join(d[0],k)}'\x1b[38;2;100;100;100m...")
					with open(b_fp+"/"+os.path.join(d[0],k)[len(d[1]):].replace("\\","/").replace("/","$"),"wb") as wf,open(os.path.join(d[0],k),"rb") as rf:
						dt=rf.read().replace(b"\r\n",b"\n")
						l+=[e for e in re.findall(r"^\s*#\s*include\s*[<\"]([^>\"]+)[>\"]",str(dt,"utf-8").lower(),re.M) if e!="arduino.h" and e not in l]
						wf.write(bytes(f"#line 1 \"{_quote_fp(os.path.join(d[0],k))}\"\n","utf-8")+_replace_inc(dt)+b"\n;\n")
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
	_run_cmd([e for e in _prepare_cmd(re.sub(r"\{.+?\}","",_expand_in_string(pd,pd["recipe.preproc.macros"]))) if e!="-MMD"]+["-DARDUINO_LIB_DISCOVERY_PHASE"])
	os.remove(b_fp+m_fp.split("/")[-1]+".cpp")
	_print("Running Recipe 'recipe.hooks.sketch.prebuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.sketch.prebuild",".pattern")
	_print("Compiling Files\x1b[38;2;100;100;100m...")
	s_of=_compile_files(bp,b_fp,b_fp,inc_l,False)+(_compile_files(bp,f"{b_fp}src/",f"{b_fp}src/",inc_l,True) if os.path.exists(f"{b_fp}src/") else [])
	_print("Running Recipe 'recipe.hooks.sketch.postbuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.sketch.postbuild",".pattern")
	_print("Running Recipe 'recipe.hooks.core.prebuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.core.prebuild",".pattern")
	c_inc_l=[bp["build.core.path"]]+([bp["build.variant.path"]] if bp["build.variant.path"]!="" else [])
	_print("Buliding Core\x1b[38;2;100;100;100m...")
	if (not os.path.exists(f"{b_fp}core/")):
		_print("\x1b[38;2;200;40;20mPrebuild Core not Found.\x1b[0m Rebuilding\x1b[38;2;100;100;100m...")
		os.mkdir(f"{b_fp}core/")
		_print("Compiling Core Variant Files\x1b[38;2;100;100;100m...")
		v_of=(_compile_files(bp,bp["build.variant.path"],f"{b_fp}core",c_inc_l,True) if bp["build.variant.path"]!="" else [])
		_print("Compiling Core Files\x1b[38;2;100;100;100m...")
		pr=False
		for c_of in _compile_files(bp,bp["build.core.path"],f"{b_fp}core",c_inc_l,True):
			if (pr==False):
				_print("Archiving Core Files\x1b[38;2;100;100;100m...")
			pr=True
			_run_cmd(_prepare_cmd(re.sub(r"\{.+?\}","",_expand_in_string({**bp,"archive_file":"core.a","archive_file_path":f"{b_fp}core/core.a","object_file":c_of},bp["recipe.ar.pattern"]))))
			os.remove(c_of)
			os.remove(c_of[:-2]+".d")
	else:
		_print("Collecting Core Variant Files\x1b[38;2;100;100;100m...")
		v_of=[e for e in os.listdir(f"{b_fp}core/") if e.endswith(".o")]
	_print("Running Recipe 'recipe.hooks.core.postbuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.core.postbuild",".pattern")
	_print("Running Recipe 'recipe.hooks.linking.prelink'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.linking.prelink",".pattern")
	_print("Linking Files\x1b[38;2;100;100;100m...")
	_run_cmd(_prepare_cmd(re.sub(r"\{.+?\}","",_expand_in_string({**bp,"compiler.warning_flags":bp.get("compiler.warning_flags","")+(f".{ARDUINO_CUSTOM_WARNING_LEVEL}" if ARDUINO_CUSTOM_WARNING_LEVEL!="" else ""),"archive_file":"core/core.a","archive_file_path":f"{b_fp}core/core.a","object_files":" ".join([f"\"{e}\"" for e in s_of+v_of])},bp["recipe.c.combine.pattern"]))))
	_print("Running Recipe 'recipe.hooks.linking.postlink'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.linking.postlink",".pattern")
	_print("Running Recipe 'recipe.hooks.objcopy.preobjcopy'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.objcopy.preobjcopy",".pattern")
	_print("Running Recipe 'recipe.objcopy.'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.objcopy.",".pattern")
	_print("Running Recipe 'recipe.hooks.objcopy.postobjcopy'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.objcopy.postobjcopy",".pattern")
	_print("Running Recipe 'recipe.hooks.postbuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.postbuild",".pattern")
	sz=[0,0]
	if (bp["upload.maximum_size"]!=""):
		_print("Processing Statistics\x1b[38;2;100;100;100m...")
		sz_bp={**bp,"compiler.warning_flags":bp.get("compiler.warning_flags","")+(f".{ARDUINO_CUSTOM_WARNING_LEVEL}" if ARDUINO_CUSTOM_WARNING_LEVEL!="" else "")}
		out=str(_run_cmd(_prepare_cmd(_expand_in_string({**bp,"compiler.warning_flags":bp.get("compiler.warning_flags","")+(f".{ARDUINO_CUSTOM_WARNING_LEVEL}" if ARDUINO_CUSTOM_WARNING_LEVEL!="" else "")},bp["recipe.size.pattern"])),stdout=subprocess.PIPE).stdout,"utf-8")
		for i,r in enumerate(("recipe.size.regex","recipe.size.regex.data")):
			for k in re.findall(r"(?m)"+bp[r],out):
				sz[i]+=int(k)
		if (sz[0]>int(bp["upload.maximum_size"])):
			raise RuntimeError(f"Sketch Uses {sz[0]} bytes out of {int(bp['upload.maximum_size'])} bytes of storage space.")
		if (bp["upload.maximum_data_size"]!="" and sz[1]>int(bp["upload.maximum_data_size"])):
			raise RuntimeError(f"Sketch Uses {sz[0]} bytes out of {int(bp['upload.maximum_size'])} bytes of Dynamic Memory.")
		_print(f"Sketch uses {sz[0]} bytes ({sz[0]*100//int(bp['upload.maximum_size'])}%) of program storage space. Maximum is {bp['upload.maximum_size']} bytes.")
		if (bp["upload.maximum_data_size"]!=""):
			_print(f"Global variables use {sz[1]} bytes ({sz[1]*100//int(bp['upload.maximum_data_size'])}%) of dynamic memory, leaving {int(bp['upload.maximum_data_size'])-sz[1]} bytes for local variables. Maximum is {bp['upload.maximum_data_size']} bytes.")
		else:
			_print(f"Global variables use {sz[1]} bytes of dynamic memory.")
	if (os.path.exists(o_fp)):
		_rm_dir(o_fp)
	os.mkdir(o_fp)
	for k in os.listdir(b_fp):
		if (k==f"{m_fp[len(s_fp):]}.hex"):
			with open(f"{o_fp}{m_fp[len(s_fp):].split('.')[0]}.hex","wb") as wf,open(f"{b_fp}{k}","rb") as rf:
				wf.write(rf.read())
		if (k not in ["core","build-properties.md5"]):
			os.remove(f"{b_fp}{k}")
	return sz



def _upload_to_ard(b_fp,p,fqbn,bb,vu,inc_l):
	def _run_cmd(*a,**kw):
		o=subprocess.run(*a,**kw)
		if (o.returncode!=0):
			sys.exit(o.returncode)
		return o
	def _step_dir(fp):
		return fp+os.listdir(fp)[0]+"/"
	def _expand_in_string(d,s):
		while (True):
			ns=s+""
			for k,v in d.items():
				ns=ns.replace(f"{{{k}}}",v)
			if (ns==s):
				return s
			s=ns
	fqbn=fqbn.split(":")
	b_fp=os.path.abspath(b_fp).replace("\\","/")
	if (b_fp[-1]!="/"):
		b_fp+="/"
	_print("Searching For Build Directory\x1b[38;2;100;100;100m...")
	if (not os.path.exists(b_fp)):
		_print("\x1b[38;2;200;40;20mSketch Build Directory Not Found.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		return
	_print("Loading Packages\x1b[38;2;100;100;100m...")
	if (not os.path.exists(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/")):
		raise RuntimeError(f"Package '{fqbn[0]}:{fqbn[1]}' isn't Installed.")
	h_fp=os.path.abspath(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"+sorted(os.listdir(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"),reverse=True)[0])+"/"
	_print(f"Reading File '{h_fp}boards.txt'\x1b[38;2;100;100;100m...")
	with open(f"{h_fp}boards.txt","r") as hb_f:
		h_pm={}
		for k in hb_f.read().replace("\r","").split("\n"):
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
		p_pm={k.split("=")[0]:k[len(k.split("=")[0])+1:] for k in hp_f.read().replace("\r","").split("\n") if len(k.strip())>0 and k.strip()[0]!="#"}
	_print(f"Generating Upload Properties\x1b[38;2;100;100;100m...")
	up={**p_pm,**h_pm,"serial.port":p,"serial.port.file":p,"runtime.platform.path":h_fp}
	up.update({k[len(h_pm[("bootloader.tool" if bb==True else "upload.tool")])+7:]:v for k,v in up.items() if k.startswith(f"tools.{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}.")})
	for k in "upload,program,erase,bootloader".split(","):
		up[f"{k}.verbose"]=up.get(f"{k}.params.quiet","")
	for k in ("upload","program"):
		up[f"{k}.verify"]=up.get(f"{k}.params.{('no' if vu==False else '')}verify","")
	_print(f"Loading Tools\x1b[38;2;100;100;100m...")
	for v in os.listdir(f"D:/boot/arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}/"):
		up[f"runtime.tools.{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}-{v}.path"]=_step_dir(f"D:/boot/arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}/{v}/")
	up[f"runtime.tools.{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}.path"]=f"D:/boot/arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}/{v}/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}"
	if (bb==False):
		up.update({"build.path":b_fp,"build.project_name":[e.split(".")[0] for e in os.listdir(b_fp) if e[-4:]==".hex"][0]})
		_print("Setting Board in Bootloader Mode\x1b[38;2;100;100;100m...")
		if (bool(up.get("upload.use_1200bps_touch","False"))==True):
			_print("\x1b[38;2;200;40;20m1200Bps Touch not Implemented Yet.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
		if (bool(up.get("upload.wait_for_upload_port","False"))==True):
			_print("Searching For Avaible Boards\x1b[38;2;100;100;100m...")
			b=None
			for usb_b in _l_ard_boards():
				if (usb_b["fqbn"]==":".join(fqbn)):
					if (usb_b["location"]==p or b==None):
						b=usb_b
			if (b==None):
				_print("\x1b[38;2;200;40;20mNo Boards Found.\x1b[0m Stopping Upload\x1b[38;2;100;100;100m...")
				sys.exit(1)
			time.sleep(0.5)
			p=b["location"]
			up.update({"serial.port":p,"serial.port.file":p})
		_print(f"Uploading Program to Board on Port '{p}'\x1b[38;2;100;100;100m...")
		_run_cmd([e for e in _split(re.sub(r"\{.+?\}","",_expand_in_string(up,up["upload.pattern"]))) if len(e)>0])
	else:
		_print("Erasing Board\x1b[38;2;100;100;100m...")
		_run_cmd([e for e in _split(re.sub(r"\{.+?\}","",_expand_in_string(up,up["erase.pattern"]))) if len(e)>0])
		_print("Burning Bootloader to Board\x1b[38;2;100;100;100m...")
		_run_cmd([e for e in _split(re.sub(r"\{.+?\}","",_expand_in_string(up,up["bootloader.pattern"]))) if len(e)>0])
	_print("Upload Finished.")



def _rec_rm_pycache(bd):
	_print(f"Deleting PyCache For Folder '{bd}'\x1b[38;2;100;100;100m...")
	for sd in os.scandir(bd):
		if (sd.is_dir()==False or "\\Python38" in sd.path or "\\Python37" in sd.path or "\\Windows" in sd.path):
			continue
		if ("__pycache__" in sd.path):
			_rm_dir(sd.path)
		try:
			_rec_rm_pycache(sd.path)
		except:
			continue



def _save_f(fn,txt):
	p=""
	i=0
	for ps in fn.split("\\")[:-1]:
		p+=ps+"\\"
		if (i<2):
			i+=1
			continue
		if (not os.path.exists(p)):
			os.mkdir(p)
		i+=1
	with open(fn,"w") as f:
		f.write(txt)



def _open_prog_w(p):
	def _open_prog_w_f(p,p2,e,*f):
		op=False
		for fn in f:
			if (os.path.isfile(fn)):
				subprocess.Popen([p,fn])
				op=True
		if (op==False):
			for r,_,fl in os.walk(p2):
				for fn in fl:
					if (fn.endswith(e)):
						subprocess.Popen([p,os.path.join(r,fn)])
						return
	t=p.split("-")[0].lower()
	_print(f"Opening Project: (name='{p[len(t)+1:]}', type='{t}', path='D:\\K\\Coding\\{p}\\')\x1b[38;2;100;100;100m...")
	p=f"D:\\K\\Coding\\{p}\\"
	subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
	if (t=="arduino"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"ino",f"{p}src/main.ino")
	if (t=="assembly"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"ino",f"{p}src/main.asm")
	elif (t=="c"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"c",f"{p}src/main.c")
	elif (t=="cpp"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"cpp",f"{p}src/main.cpp")
	elif (t=="css"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"css",f"{p}src/index.html",f"{p}src/style.css")
	elif (t=="java"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"java",f"{p}src/com/krzem/{p.split('-')[1].lower().replace(' ','_')}\\Main.java")
	elif (t=="javascript"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"js",f"{p}src/index.html",f"{p}src/main.js")
	elif (t=="php"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"php",f"{p}src/index.php")
	elif (t=="processing"):
		os.system(f"start /min cmd /c \"{p}main/main.pde\"")
	elif (t=="python"):
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"py",f"{p}src/main.py")
	else:
		_print("\x1b[38;2;200;40;20mUnknown type.\x1b[0m Defaulting to Editor\x1b[38;2;100;100;100m...")



def _create_prog(type_,name,op=True,pr=True):
	if (pr==True):
		_print(f"Creating Project: (type='{type_}', name='{name}', open_on_creation={op})")
	type_=type_.lower()
	if (type_ not in "arduino,assembly,c,cpp,css,java,js,javascript,php,processing,python".split(",")):
		_print(f"Unknown Prog Type: {type_}")
		return
	if (type_=="js"):
		type_="javascript"
	name=name.replace("_"," ").lower().title().replace(" ","_")
	p="D:\\K\\Coding\\"+type_.title()+"-"+name+"\\"
	fel=[]
	for r,_,fl in os.walk(p):
		for f in fl:
			fel+=[os.path.join(r,f).split(".")[-1]]
	if (not os.path.exists(p)):
		os.mkdir(p)
	if (not os.path.exists(f"{p}src")):
		os.mkdir(f"{p}src")
	if (not os.path.exists(f"{p}.gitignore")):
		with open(f"{p}.gitignore","x") as f:
			f.write("build\n")
		os.system(f"cd /d {p}&&attrib +h .gitignore")
	if (not os.path.exists(f"{p}LICENSE.txt")):
		with open(f"{p}LICENSE.txt","x") as f:
			f.write(f"""Copyright (c) {datetime.datetime.now().year} Krzem\n\nPermission is hereby granted, free of charge, to any person obtaining a\ncopy of this software and associated documentation files (the\n"Software"), to deal in the Software without restriction, including without\nlimitation the rights to use, copy, modify, merge, publish, distribute,\nsublicense, and/or sell copies of the Software, and to permit persons\nto whom the Software is furnished to do so, subject to the following\nconditions:\n\nThe above copyright notice and this permission notice shall be included\nin all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY\nKIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE\nWARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR\nPURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\nTHE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,\nDAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF\nCONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN\nCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS\nIN THE SOFTWARE.\n""")
	if (not os.path.exists(f"{p}README.md")):
		with open(f"{p}README.md","x") as f:
			f.write(f"""# {type_.title()} - {name.replace('_',' ').title()}\n(This is an auto - generated file.)\n""")
	if (type_=="arduino"):
		if (not os.path.exists(f"{p}src/main.ino") and "ino" not in fel):
			with open(f"{p}src/main.ino","x") as f:
				f.write("#include <arduino.h>\n\n\n\nvoid setup(){\n\t\n}\n\n\n\nvoid loop(){\n\t\n}\n")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\npython D:\\boot\\boot.py 5 compile ./src ./build arduino:avr:uno&&python D:\\boot\\boot.py 5 upload ./build COM3 arduino:avr:uno\n")
	elif (type_=="assembly"):
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\n")
	elif (type_=="c"):
		if (not os.path.exists(f"{p}src/main.c") and "c" not in fel):
			if (not os.path.exists(f"{p}src/{name.lower()}")):
				os.mkdir(f"{p}src/{name.lower()}")
			if (not os.path.exists(f"{p}src/include")):
				os.mkdir(f"{p}src/include")
			with open(f"{p}src/main.c","x") as f:
				f.write("int main(int argc,const char** argv){\n\t(void)argc;\n\t(void)argv;\n\treturn 0;\n}")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\nset _INCLUDE=%INCLUDE%\nset INCLUDE=../src/include;%INCLUDE%\nif exist build rmdir /s /q build\nmkdir build\ncd build\nif %1.==. goto dbg\nif %1==-r (\n\tcl /c /permissive- /GS /W3 /Zc:wchar_t /Gm- /sdl /Zc:inline /fp:precise /D \"NDEBUG\"  /D \"_WINDOWS\" /D \"_UNICODE\" /D \"UNICODE\" /errorReport:none /WX /Zc:forScope /Gd /Oi /FC /EHsc /nologo /diagnostics:column /GL /Gy /Zi /O2 /Oi /MD ../src/main.c ../src/{name.lower()}/*.c&&link *.obj /OUT:{name.lower()}.exe /DYNAMICBASE \"kernel32.lib\" \"user32.lib\" \"gdi32.lib\" \"winspool.lib\" \"comdlg32.lib\" \"advapi32.lib\" \"shell32.lib\" \"ole32.lib\" \"oleaut32.lib\" \"uuid.lib\" \"odbc32.lib\" \"odbccp32.lib\" /MACHINE:X64 /SUBSYSTEM:CONSOLE /ERRORREPORT:none /NOLOGO /TLBID:1 /WX /LTCG /OPT:REF /INCREMENTAL:NO /OPT:ICF&&goto run\n\tgoto end\n)\n:dbg\ncl /c /permissive- /GS /W3 /Zc:wchar_t /Gm- /sdl /Zc:inline /fp:precise /D \"_DEBUG\"  /D \"_WINDOWS\" /D \"_UNICODE\" /D \"UNICODE\" /errorReport:none /WX /Zc:forScope /Gd /Oi /FC /EHsc /nologo /diagnostics:column /ZI /Od /RTC1 /MDd ../src/main.c ../src/{name.lower()}/*.c&&link *.obj /OUT:{name.lower()}.exe /DYNAMICBASE \"kernel32.lib\" \"user32.lib\" \"gdi32.lib\" \"winspool.lib\" \"comdlg32.lib\" \"advapi32.lib\" \"shell32.lib\" \"ole32.lib\" \"oleaut32.lib\" \"uuid.lib\" \"odbc32.lib\" \"odbccp32.lib\" /MACHINE:X64 /SUBSYSTEM:CONSOLE /ERRORREPORT:none /NOLOGO /TLBID:1 /WX /DEBUG /INCREMENTAL&&goto run\ngoto end\n:run\ndel *.obj\ndel *.pdb\ndel *.exp\ndel *.ilk\ndel *.idb\ncls\n{name.lower()}.exe\n:end\ncd ..\nset INCLUDE=%_INCLUDE%")
	elif (type_=="cpp"):
		if (not os.path.exists(f"{p}src/main.cpp") and "cpp" not in fel):
			with open(f"{p}src/main.cpp","x") as f:
				f.write("int main(int argc,const char** argv){\n\t(void)argc;\n\t(void)argv;\n\treturn 0;\n}")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\ndel *.obj&&del {name.lower()}.exe&&cl /EHsc *.cpp /link /OUT:{name.lower()}.exe&&del *.obj&&cls&&{name.lower()}.exe\n")
	elif (type_=="css"):
		if (not os.path.exists(f"{p}src/index.html") and "html" not in fel):
			with open(f"{p}src/index.html","x") as f:
				f.write(f"<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{name.replace('_',' ')}</title>\n\t\t<link href=\"css/style.css\" rel=\"stylesheet\" type=\"text/css\">\n\t</head>\n\t<body>\n\t</body>\n</html>")
		if (not os.path.exists(f"{p}src/css/style.css") and "css" not in fel):
			if (not os.path.exists(f"{p}src/css")):
				os.mkdir(f"{p}src/css")
			with open(f"{p}src/css/style.css","x") as f:
				f.write("body {\n\twidth: 100%;\n\theight: 100%\n}\nbody, body * {\n\tmargin: 0;\n\tpadding: 0;\n}")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/Google/Chrome Dev/Application/chrome.exe\" http://localhost:8020/{p}")
	elif (type_=="java"):
		if (not os.path.exists(f"{p}src/com/krzem/{name.lower()}/Main.java") and "java" not in fel):
			if (not os.path.exists(f"{p}src/com/")):
				os.mkdir(f"{p}src/com/")
			if (not os.path.exists(f"{p}src/com/krzem/")):
				os.mkdir(f"{p}src/com/krzem/")
			if (not os.path.exists(f"{p}src/com/krzem/{name.lower()}/")):
				os.mkdir(f"{p}src/com/krzem/{name.lower()}/")
			with open(f"{p}src/com/krzem/{name.lower()}/Main.java","x") as f:
				f.write("package com.krzem."+name.lower()+";\n\n\n\npublic class Main{\n\tpublic static void main(String[] args){\n\t\tnew Main();\n\t}\n\n\n\n\tpublic Main(){\n\t\t\n\t}\n}")
		if (not os.path.exists(f"{p}/manifest.mf")):
			with open(p+"manifest.mf","x") as f:
				f.write(f"Manifest-Version: 1.0\nCreated-By: Krzem\nMain-Class: com.krzem.{name.lower().replace(' ','_')}.Main\n")
		if (not os.path.exists(f"{p}build.bat")):
			with open(p+"build.bat","x") as f:
				f.write(f"@echo off\ncls\nif exist build rmdir /s /q build\nmkdir build\ncd src\njavac -d ../build com/krzem/{name.lower().replace(' ','_')}/Main.java&&jar cvmf ../manifest.mf ../build/{name.lower().replace(' ','_')}.jar\n -C ../build *&&goto run\ncd ..\ngoto end\n:run\ncd ..\npushd \"build\"\nfor /D %%D in (\"*\") do (\n\trd /S /Q \"%%~D\"\n)\nfor %%F in (\"*\") do (\n\tif /I not \"%%~nxF\"==\"{name.lower().replace(' ','_')}.jar\" del \"%%~F\"\n)\npopd\njava -jar build/{name.lower().replace(' ','_')}.jar\n:end\n")
	elif (type_=="javascript"):
		if (not os.path.exists(f"{p}src/index.html") and "html" not in fel):
			with open(f"{p}src/index.html","x") as f:
				f.write(f"<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{name.replace('_',' ')}</title>\n\t\t<script type=\"text/javascript\" src=\"js/main.js\"></script>\n\t</head>\n\t<body>\n\t</body>\n</html>")
		if (not os.path.exists(f"{p}src/js/main.js") and "js" not in fel):
			if (not os.path.exists(f"{p}src/js/")):
				os.mkdir(f"{p}src/js/")
			with open(f"{p}src/js/main.js","x") as f:
				f.write("function init(){\n\t\n}\ndocument.addEventListener(\"DOMContentLoaded\",init,false)")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/Google/Chrome Dev/Application/chrome.exe\" http://localhost:8020/{p}")
	elif (type_=="php"):
		if (not os.path.exists(f"{p}src/index.php") and "php" not in fel):
			with open(f"{p}src/index.php","x") as f:
				f.write("<?php\n\n?>")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/Google/Chrome Dev/Application/chrome.exe\" http://localhost:8020/{p}src/index.php")
	elif (type_=="processing"):
		if (not os.path.exists(f"{p}main/")):
			os.mkdir(f"{p}main/")
		if (not os.path.exists(f"{p}main/main.pde")):
			with open(f"{p}main/main.pde","x") as f:
				f.write("void setup(){\n\t\n}\n\nvoid draw(){\n\t\n}")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\nstart /min cmd /c \"{p}main/main.pde\"")
	elif (type_=="python"):
		if (not os.path.exists(f"{p}src/main.py") and "py" not in fel):
			with open(f"{p}src/main.py","x") as f:
				f.write("")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\npython src/main.py")
		if (not os.path.exists(f"{p}build.bat")):
			with open(f"{p}build.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/Google/Chrome Dev/Application/chrome.exe\" http://localhost:8020/{p}")
	if (op==True):
		_open_prog_w(type_.title()+"-"+name)



def _start_s():
	def _r_std_h(cs):
		threading.current_thread()._df=True
		bf=b""
		e=False
		while (e==False):
			try:
				bf+=cs.recv(1024)
			except ConnectionResetError:
				e=True
			if (b"\n" in bf):
				dt,bf=base64.b64decode(bf.split(b"\n")[0]),b"\n".join(bf.split(b"\n")[1:])
				threading.current_thread()._b_nm,threading.current_thread()._nm=str(dt,"utf-8").split("\x00")[:2]
				_print(str(dt[len(b" ".join(dt.split(b"\x00")[:2]))+1:],"utf-8"))
	_print("Starting Remote Std Listener on Port '127.0.0.1:8022'\x1b[38;2;100;100;100m...")
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind(("127.0.0.1",8022))
	s.listen(5)
	while (True):
		threading.Thread(target=_r_std_h,args=(s.accept()[0],),kwargs={}).start()
	s.close()



def _u_mcs(fp):
	_print(f"Starting Minecraft Server in Folder '{fp}'\x1b[38;2;100;100;100m...")
	if (not os.path.exists(fp)):
		_print("\x1b[38;2;200;40;20mMinecraft Server Folder Missing.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		return
	_print("Downloading Metadata\x1b[38;2;100;100;100m...")
	json=requests.get([e for e in requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").json()["versions"] if e["id"] not in MINECRAFT_SKIP_UPDATE][0]["url"]).json()
	if (os.path.exists(f"{fp}\\server.jar")):
		_print("Inspecting Current Version\x1b[38;2;100;100;100m...")
		h=hashlib.sha1()
		with open(f"{fp}\\server.jar","rb") as f:
			fb=f.read(2**16)
			while (len(fb)>0):
				h.update(fb)
				fb=f.read(2**16)
		_print(f"File Hash: {h.hexdigest()}, New Hash: {json['downloads']['server']['sha1']}")
		if (h.hexdigest()!=json["downloads"]["server"]["sha1"]):
			_print(f"Creating Backup\x1b[38;2;100;100;100m...")
			if (not os.path.exists(f"{fp}\\world-backup_{json['id']}")):
				os.mkdir(f"{fp}\\world-backup_{json['id']}")
			for r,dl,fl in os.walk(f"{fp}\\world"):
				nr=f"{fp}\\world-backup_{json['id']}"+r[len(f"{fp}\\world"):]
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
							pass
			_print(f"Downloading Server For {json['id']}\x1b[38;2;100;100;100m...")
			urllib.request.urlretrieve(json["downloads"]["server"]["url"],f"{fp}\\server.jar")
	else:
		urllib.request.urlretrieve(json["downloads"]["server"]["url"],f"{fp}\\server.jar")
	_print("Starting Server\x1b[38;2;100;100;100m...")
	p=subprocess.Popen(["vdesk","on:3","noswitch:true","run:cmd","/c","java -Xms4G -Xmx4G -jar server.jar --nogui"],cwd=fp,creationflags=subprocess.CREATE_NEW_CONSOLE)



def _hotkey_handler(c,wp,lp):
	try:
		dt=ctypes.cast(lp,ctypes.POINTER(ctypes.wintypes.KBDLLHOOKSTRUCT)).contents
		if (dt.vk_code!=VK_PACKET and dt.flags&(LLKHF_INJECTED|LLKHF_ALTDOWN)!=LLKHF_INJECTED|LLKHF_ALTDOWN):
			if (dt.vk_code==0xa5 and _hotkey_handler._ig_alt):
				_hotkey_handler._ig_alt=False
			else:
				if (dt.scan_code==0x21d and dt.vk_code==0xa2):
					_hotkey_handler._ig_alt=True
				if (dt.vk_code in VK_SAME_KEYS):
					dt.vk_code=VK_SAME_KEYS[dt.vk_code]
				if (dt.vk_code in VK_KEYS.values()):
					_hotkey_handler._kb[dt.vk_code]=(wp in (WM_KEYDOWN,WM_SYSKEYDOWN))
					if (_hotkey_handler._kb[dt.vk_code]):
						for k,v in _hotkey_handler._hk:
							if (dt.vk_code in k):
								for e in k:
									if (not _hotkey_handler._kb[e]):
										v=None
										break
								if (v is not None):
									v()
									return -1
	except Exception as e:
		traceback.print_exception(None,e,e.__traceback__)
	return ctypes.windll.user32.CallNextHookEx(None,c,wp,lp)



def _register_hk(hk,cb):
	o=[]
	for e in hk.lower().split("+"):
		if (e not in VK_KEYS):
			raise RuntimeError(f"Unknown Key '{e}'!")
		o+=[VK_KEYS[e]]
	_hotkey_handler._hk+=[(tuple(o),cb)]



def _end(a):
	subprocess.run(["C:\\Windows\\System32\\shutdown.exe"]+a+["/f"])



ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),ctypes.wintypes.DWORD(7))
if (len(sys.argv)==1):
	os.system("cls")
	ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),ctypes.wintypes.DWORD(7))
	CMD_L["__core__"]={"__main__":b""}
	threading.current_thread()._b_nm="__core__"
	threading.current_thread()._nm="__main__"
	_print("Starting Boot Sequence\x1b[38;2;100;100;100m...")
	_print("Registering Hotkey Handler\x1b[38;2;100;100;100m...")
	_hotkey_handler._hk=[]
	_hotkey_handler._kb={e:False for e in VK_KEYS.values()}
	_hotkey_handler._ig_alt=False
	kb_cb=ctypes.wintypes.LowLevelKeyboardProc(_hotkey_handler)
	ctypes.windll.user32.SetWindowsHookExW(WH_KEYBOARD_LL,kb_cb,ctypes.windll.kernel32.GetModuleHandleW(None),ctypes.wintypes.DWORD(0))
	atexit.register(ctypes.windll.user32.UnhookWindowsHookEx,kb_cb)
	_print("Registering Hotkey\x1b[38;2;100;100;100m...")
	_register_hk("ctrl+alt+shift+e",lambda:_open_app("C:\\Windows\\System32\\control.exe"))
	_register_hk("ctrl+alt+shift+c",lambda:_open_app(["python","D:\\boot\\boot.py","0"]))
	_register_hk("ctrl+alt+shift+q",lambda:_open_app(["python","D:\\boot\\boot.py","1"]))
	_register_hk("ctrl+alt+shift+a",lambda:_open_app("D:\\K",file=True))
	_register_hk("ctrl+alt+shift+r",lambda:_open_app(["pythonw","D:\\boot\\boot.py","0"]))
	_register_hk("ctrl+alt+shift+home",lambda:_end(["/l"]))
	_register_hk("ctrl+alt+shift+end",lambda:_end(["/s","/t","0"]))
	_register_hk("ctrl+alt+shift+w",lambda:_open_app("D:\\boot",file=True))
	_register_hk("ctrl+alt+shift+d",lambda:_open_app("C:\\Windows\\System32\\Taskmgr.exe"))
	_register_hk("ctrl+alt+shift+v",lambda:_open_app(["python","D:\\boot\\boot.py","2"]))
	_print("Starting Minecraft Server\x1b[38;2;100;100;100m...")
	_start_thr(_u_mcs,"__core__","minecraft_server_updater","D:\\boot\\mcs")
	_print("Registering All Projects\x1b[38;2;100;100;100m...")
	for k in os.listdir("D:\\K\\Coding"):
		_create_prog(k.split("-")[0],k[len(k.split("-")[0])+1:],op=False,pr=False)
	_print("Starting Github Project Push Check\x1b[38;2;100;100;100m...")
	_start_thr(_git_project_push,"__core__","github_project_push")
	_print("Startint Remote Std Listener\x1b[38;2;100;100;100m...")
	_start_thr(_start_s,"__core__","remote_std_server")
	_print("Starting Infinite Loop\x1b[38;2;100;100;100m...")
	try:
		msg=ctypes.wintypes.LPMSG()
		while (True):
			if (ctypes.windll.user32.PeekMessageW(msg,None,0,0,PM_REMOVE)!=0):
				ctypes.windll.user32.TranslateMessage(msg)
				ctypes.windll.user32.DispatchMessageW(msg)
	except:
		pass
	os.system(f"taskkill /pid {os.getpid()} /f")
else:
	v=int(sys.argv[1])
	if (v==0):
		def _handle(c,wp,lp):
			try:
				dt=ctypes.cast(lp,ctypes.POINTER(ctypes.wintypes.KBDLLHOOKSTRUCT)).contents
				if (dt.vk_code==0x1b):
					_handle._r.destroy()
				else:
					return -1
			except Exception as e:
				traceback.print_exception(None,e,e.__traceback__)
			return ctypes.windll.user32.CallNextHookEx(None,c,wp,lp)
		def _loop(r):
			if (ctypes.windll.user32.PeekMessageW(_loop._msg,None,0,0,PM_REMOVE)!=0):
				ctypes.windll.user32.TranslateMessage(_loop._msg)
				ctypes.windll.user32.DispatchMessageW(_loop._msg)
			r.after(1000//60,_loop,r)
		r=tkinter.Tk()
		r.bind("<FocusOut>",lambda _:r.focus_force())
		r.attributes("-fullscreen",True)
		r.attributes("-topmost",True)
		r.configure(background="#000000")
		r.resizable(False,False)
		r.overrideredirect(True)
		r.focus_force()
		r.update_idletasks()
		_handle._ig_alt=False
		_handle._r=r
		_loop._msg=ctypes.wintypes.LPMSG()
		kb_cb=ctypes.wintypes.LowLevelKeyboardProc(_handle)
		ctypes.windll.user32.SetWindowsHookExW(WH_KEYBOARD_LL,kb_cb,ctypes.windll.kernel32.GetModuleHandleW(None),ctypes.wintypes.DWORD(0))
		atexit.register(ctypes.windll.user32.UnhookWindowsHookEx,kb_cb)
		ctypes.windll.user32.ShowCursor(0)
		r.after(0,_loop,r)
		r.mainloop()
	elif (v==1):
		while (True):
			p=input("> ").lower().strip()
			if (p=="list"):
				os.system("cls")
				_print("list, chrome, python, python37, processing, sublime, minecraft, vm, github, blender, print, serial, stats, cad, <any file path>, <git clone url>, <any url>")
				continue
			elif (p=="chrome"):
				_open_app("C:\\Program Files\\Google\\Chrome Dev\\Application\\chrome.exe")
			elif (p=="python"):
				_open_app(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python38\\python.exe")
			elif (p=="python37"):
				_open_app(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python37\\python.exe")
			elif (p=="processing"):
				_open_app("C:\\Program Files\\Processing\\processing.exe")
			elif (p=="sublime"):
				_open_app("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
			elif (p=="minecraft"):
				_open_app("C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe")
			elif (p=="vm"):
				_open_app("C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe")
			elif (p=="github"):
				_open_app("C:\\Users\\aleks\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
			elif (p=="blender"):
				_open_app("C:\\Program Files\\Blender Foundation\\Blender\\blender.exe")
			elif (p=="work"):
				_open_app(["python","D:\\boot\\boot.py","2"])
			elif (p=="serial"):
				_open_app(["python","D:\\boot\\boot.py","3"])
			elif (p=="stats"):
				_open_app(["python","D:\\boot\\boot.py","6"])
			elif (p=="docs"):
				_open_app(["C:\\Program Files\\Google\\Chrome Dev\\Application\\chrome_proxy.exe","--profile-directory=Default","--app-id=ahiigpfcghkbjfcibpojancebdfjmoop"])
			elif (p=="cad"):
				_open_app("C:\\Program Files\\CAD\\FreeCAD 0.18\\bin\\FreeCAD.exe")
			elif (os.path.exists(p)):
				_open_app(p,file=True)
			elif (GIT_CLONE_REGEX.match(p)!=None):
				os.system(f"cd /d D:\\K\\Downloads\\&&git clone {p}")
				_open_app("D:\\K\\Downloads\\"+p.split(".git")[0].split("/")[-1],file=True)
			elif (URL_REGEX.match(p)!=None):
				_open_app(["C:\\Program Files\\Google\\Chrome Dev\\Application\\chrome.exe",p])
			elif (p=="" or p=="exit"):
				break
			else:
				os.system("cls")
				continue
			break
	elif (v==2):
		threading.current_thread()._b_nm="__core__"
		threading.current_thread()._nm="work_terminal"
		threading.current_thread()._r=2
		inp_cm=ctypes.wintypes.DWORD(0)
		ctypes.windll.kernel32.GetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),ctypes.byref(inp_cm))
		out_cm=ctypes.wintypes.DWORD(0)
		ho=ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.GetConsoleMode(ho,ctypes.byref(out_cm))
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		ctypes.windll.kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		ctypes.windll.kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		try:
			ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
			nci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
			nci.dwSize=ci.dwSize
			nci.bVisible=0
			ctypes.windll.kernel32.SetConsoleCursorInfo(ho,ctypes.byref(nci))
			rl=[e.split("-")[:2] for e in os.listdir("D:\\K\\Coding")]
			tl=[]
			for k in rl:
				if (k[0] not in tl):
					tl+=[k[0]]
			l={}
			for k in rl:
				if (k[0].lower() not in list(l.keys())):
					l[k[0].lower()]=[]
				l[k[0].lower()]+=[k[1].replace("_"," ").title().replace(" ","_")]
			w=sbi.dwMaximumWindowSize.X+1
			h=sbi.dwMaximumWindowSize.Y
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
							_create_prog(bf[0],bf[1])
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
					elif (k==b"\r"):
						if (bf[0].lower() in list(l.keys())):
							e=False
							for k in l.get(bf[0].lower(),[]):
								if (k.lower()==bf[1].lower()):
									_open_prog_w(f"{bf[0].title()}-{bf[1].replace('_',' ').title().replace(' ','_')}")
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
					ln=len(re.sub(r"\x1b\[[^m]*m","",o).replace("\n"," "*(sbi.dwMaximumWindowSize.X+1)))
					sys.__stdout__.write(f"\x1b[0;0H{o+(' '*(ll-ln) if ll>ln else '')}\x1b[0m")
					sys.__stdout__.flush()
					ll=ln
					u=False
				time.sleep(0.01)
			ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
		except Exception as e:
			traceback.print_exception(None,e,e.__traceback__)
			while (True):
				pass
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),inp_cm)
		ctypes.windll.kernel32.SetConsoleMode(ho,out_cm)
		ctypes.windll.kernel32.SetConsoleCursorInfo(ho,ctypes.byref(ci))
		ctypes.windll.kernel32.SetConsoleScreenBufferSize(ho,sbi.dwSize)
		ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
	elif (v==3):
		class _UI:
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
				def _cmp(a,b):
					return (0 if a==b else (-1 if a<b else 1))
				while (True):
					self._o=[f"\x1b[0m\x1b[48;2;24;24;24m{' '*(self._sz[0]-1)}",f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ╔{'═'*(self._sz[0]-9)}╗   ",*(f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ║{' '*(self._sz[0]-9)}\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m║   ",)*(self._sz[1]-5),f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ╚{'═'*(self._sz[0]-9)}╝   ",f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m{' '*(self._sz[0]-1)}"]
					ud=False
					if (msvcrt.kbhit()==True):
						k=msvcrt.getch()
						if (k==b"\x03"):
							if (self._m==0):
								break
							elif (self._m==1):
								self._p_s.close()
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
						if (self._k[0]==b"r" or self._pl==None):
							self._pl=_l_ard_boards()
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
								self._p_s=serial.Serial(self._p["location"],SERIAL_BAUD,timeout=5)
								while (self._p_s.is_open==False):
									time.sleep(1e-4)
								self._m=1
						self._draw_table({"name":("Name","#8ae8c6"),"arch":("Arch","#dbdf0c"),"fqbn":("FQBN","#e386d0"),"location":("Location","#59c51e")},self._pl,s=self._pi)
					elif (self._m==1):
						n_dt=False
						inp_ch=False
						if (self._k[0]==b"\r"):
							if (self._inp_bf in self._mem):
								self._mem.remove(self._inp_bf)
							self._mem=self._mem[:-1]+[self._inp_bf,""]
							self._mem_i=len(self._mem)-1
							self._extend(1,self._inp_bf+"\n")
							self._p_s.write(bytes(self._inp_bf,"utf-8"))
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
						if (self._p_s.in_waiting>0):
							self._extend(0,re.sub(r"\r(\n|$)",r"\1",str(self._p_s.read(self._p_s.in_waiting),"utf-8")).replace("\t","    "))
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
								l+=[[float(se) for se in e.split(",")] for e in k[1][::-1] if e!=None and re.fullmatch(r"^(?:-?[0-9]+(?:\.[0-9]+)?(?:,|$))+(?<!,)$",e)!=None]
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
												m[v[1]][j+2]=self._cl_cache[i]+"╵╴╷"[_cmp(v[0],v[1])+1]
											else:
												m[v[1]][j+2]=self._cl_cache[i]+"└─┌"[_cmp(v[0],v[1])+1]
											if (v[0]!=v[1]):
												m[v[0]][j+2]=self._cl_cache[i]+"┐ ┘"[_cmp(v[0],v[1])+1]
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
				mw=self._sz[0]-11
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
					m=re.match(r"\x1b\[[^m]*m",self._o[y][i:])
					if (m!=None):
						i+=len(m.group(0))
						continue
					if (j==x):
						k=i+0
						l=j+0
						em=""
						while (l<len(self._o[y])):
							m=re.match(r"\x1b\[[^m]*m",self._o[y][k:])
							if (m!=None):
								em+=m.group(0)
								k+=len(m.group(0))
								continue
							if (l==j+len(re.sub(r"\x1b\[[^m]*m","",v))):
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
				if (len(l)==0 or self._dt[l[-1]][1][-1]==None):
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
		threading.current_thread()._b_nm="__core__"
		threading.current_thread()._nm="arduino_serial_terminal"
		threading.current_thread()._r=2
		_Arduino_Cache.init()
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		ho=ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		ctypes.windll.kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		PATCH_HEIGHT=11
		ui=_UI((sbi.dwMaximumWindowSize.X+1,sbi.dwMaximumWindowSize.Y-PATCH_HEIGHT))
		try:
			ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
			ctypes.windll.kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(sbi.dwMaximumWindowSize.X,sbi.dwMaximumWindowSize.Y-PATCH_HEIGHT-1))
			ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
			ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
			nci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
			nci.dwSize=ci.dwSize
			nci.bVisible=0
			ctypes.windll.kernel32.SetConsoleCursorInfo(ho,ctypes.byref(nci))
			ui.loop()
		except Exception as e:
			traceback.print_exception(None,e,e.__traceback__)
			while (True):
				pass
	elif (v==4):
		if (len(sys.argv)==2):
			threading.current_thread()._b_nm="__core__"
			threading.current_thread()._nm="github_project_push_remote"
			threading.current_thread()._dpt=True
			threading.current_thread()._r=2
			_git_project_push(r=True)
		else:
			if (sys.argv[2]=="*"):
				threading.current_thread()._b_nm="__core__"
				threading.current_thread()._nm="github_project_push_all"
				threading.current_thread()._dpt=True
				threading.current_thread()._r=2
				_git_project_push(r=True,fr=True)
			else:
				threading.current_thread()._b_nm="__core__"
				threading.current_thread()._nm="github_project_push_single"
				threading.current_thread()._dpt=True
				threading.current_thread()._r=2
				nm=(re.sub(r"[^A-Za-z0-9_.-]","",sys.argv[2].replace("D:\\K\\Coding\\","").split("\\")[0]) if sys.argv[2].lower().startswith("d:\\k") else "Boot_Program")
				dc=("None" if sys.argv[2].lower().startswith("d:\\k") else "'Boot Program'")
				_print(f"Pushing Project to Github: (path='{sys.argv[2]}', name='{nm}', desc={dc})")
				threading.current_thread()._dp=True
				threading.current_thread()._df=True
				threading.current_thread()._r=1
				_update_repo(sys.argv[2],(re.sub(r"[^A-Za-z0-9_.-]","",sys.argv[2].lower().replace("d:\\k\\coding\\","").split("\\")[0]) if sys.argv[2].lower().startswith("d:\\k") else "Boot_Program"))
				input("\x1b[38;2;50;50;50m<ENTER>\x1b[0m")
	elif (v==5):
		threading.current_thread()._b_nm="__core__"
		threading.current_thread()._nm="arduino_runner"
		threading.current_thread()._dpt=True
		threading.current_thread()._dp=True
		threading.current_thread()._r=1
		if (not os.path.exists(f"D:/boot/arduino")):
			os.mkdir(f"D:/boot/arduino")
		_Arduino_Cache.init()
		if (len(sys.argv)<3):
			_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			sys.exit(1)
		elif (sys.argv[2]=="list"):
			if (len(sys.argv)>3):
				_print("\x1b[38;2;200;40;20mToo many Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			bl=_l_ard_boards()
			mx_l=[max([(4,4,4,8)[i]]+[len(b[k]) for b in bl])+2 for i,k in enumerate(("name","fqbn","arch","location"))]
			threading.current_thread()._df=True
			threading.current_thread()._dph=True
			o=f"┌{'─'*mx_l[0]}┬{'─'*mx_l[1]}┬{'─'*mx_l[2]}┬{'─'*mx_l[3]}┐\n│{'Name'.center(mx_l[0])}│{'FQBN'.center(mx_l[1])}│{'Arch'.center(mx_l[2])}│{'Location'.center(mx_l[3])}│\n├{'─'*mx_l[0]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[1]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[2]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[3]}┤"
			for k in bl:
				o+=f"\n│{k['name'].center(mx_l[0])}│{k['fqbn'].center(mx_l[1])}│{k['arch'].center(mx_l[2])}│{k['location'].center(mx_l[3])}│"
			o+=f"\n└{'─'*mx_l[0]}┴{'─'*mx_l[1]}┴{'─'*mx_l[2]}┴{'─'*mx_l[3]}┘"
			_print(o)
		elif (sys.argv[2]=="install"):
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
					_install_ard_pkg(k[0],force=(True if "--force" in sys.argv[3:] else False))
				else:
					_install_ard_pkg({"pkg":k[0],"arch":k[1],"ver":(None if len(k)==2 else k[2])},force=(True if "--force" in sys.argv[3:] else False))
		elif (sys.argv[2]=="compile"):
			if (len(sys.argv)<6):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			_compile_ard_prog(sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6:])
		elif (sys.argv[2]=="upload"):
			if (len(sys.argv)<6):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			_upload_to_ard(sys.argv[3],sys.argv[4],sys.argv[5],(True if "--burn-bootloader" in sys.argv[6:] else False),(True if "--verify" in sys.argv[6:] else False),[e for e in sys.argv[6:] if e not in ["--burn-bootloader","--verify"]])
		else:
			_print(f"\x1b[38;2;200;40;20mUnknown Switch '{sys.argv[2]}'.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			sys.exit(1)
	elif (v==6):
		ll=None
		hdt=None
		db=None
		if (not os.path.exists("D:\\boot\\git-languages.json") or not os.path.exists("D:\\boot\\git-languages-h.json") or not os.path.exists("D:\\boot\\git-languages-db.json")):
			ll={}
			l_id_m={}
			for k,v in yaml.load(requests.get("https://api.github.com/repos/github/linguist/contents/lib/linguist/languages.yml",headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).content,Loader=yaml.Loader).items():
				l_id_m[k]=len(ll)
				ll[k]=[([e.lower() for e in v["extensions"]] if "extensions" in v else []),(f"#{hex(REPO_STATS_DEFAULT_COLOR[0])[2:].rjust(2,'0')}{hex(REPO_STATS_DEFAULT_COLOR[1])[2:].rjust(2,'0')}{hex(REPO_STATS_DEFAULT_COLOR[2])[2:].rjust(2,'0')}" if "color" not in v else v["color"]),v["type"]]
			with open("D:\\boot\\git-languages.json","w") as f:
				f.write(json.dumps(ll,separators=(",",":"),indent=None))
			hdt=[]
			_hdt=yaml.load(requests.get("https://api.github.com/repos/github/linguist/contents/lib/linguist/heuristics.yml",headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).content,Loader=yaml.Loader)
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
			with open("D:\\boot\\git-languages-h.json","w") as f:
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
						print(k["path"])
						tl=_repo_file_tokenize(requests.get(k["url"],headers={"Authorization":f"token {GITHUB_TOKEN}","Accept":GITHUB_HEADERS,"User-Agent":"Language Stats API"}).content.decode("utf-8",errors="replace"))
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
			with open("D:\\boot\\git-languages-db.json","w") as f:
				f.write(json.dumps(db,indent=4).replace("    ","\t"))
		else:
			with open("D:\\boot\\git-languages.json","r") as f:
				ll=json.loads(f.read(),strict=False)
			with open("D:\\boot\\git-languages-h.json","r") as f:
				hdt=json.loads(f.read(),strict=False)
				for i,k in enumerate(hdt):
					hdt[i]=(k[0],tuple((e[0],(tuple((regex.compile(sk,regex.M|regex.V1),sv) for sk,sv in e[1]) if e[1]!=None else None)) for e in k[1]))
			with open("D:\\boot\\git-languages-db.json","r") as f:
				db=json.loads(f.read(),strict=False)
		REPO_STATS_LOG_ZERO_TOKENS=math.log(1/db["languages_total"])
		sbi=ctypes.wintypes.CONSOLE_SCREEN_BUFFER_INFO()
		ho=ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ho,ctypes.byref(sbi))
		ci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		ctypes.windll.kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
		ctypes.windll.kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(sbi.srWindow.Right+1,sbi.srWindow.Bottom+1))
		ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(sbi.srWindow))
		ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sbi.dwSize.X*sbi.dwSize.Y,ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
		ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
		nci=ctypes.wintypes.CONSOLE_CURSOR_INFO()
		nci.dwSize=ci.dwSize
		nci.bVisible=0
		ctypes.windll.kernel32.SetConsoleCursorInfo(ho,ctypes.byref(nci))
		el={"__tcnt__":0,"__e__":False,"__cf__":None,"__ig__":True}
		thr=threading.Thread(target=_read_repo_stats,args=((None if len(sys.argv)==2 else sys.argv[2]),ll,hdt,db,el))
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
			if (thr==None and el["__e__"]==2):
				el={"__tcnt__":0,"__e__":0,"__cf__":None,"__ig__":not el["__ig__"]}
				thr=threading.Thread(target=_read_repo_stats,args=((None if len(sys.argv)==2 else sys.argv[2]),ll,hdt,db,el))
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
					po=False
					ln=sbi.dwMaximumWindowSize.X-10
					mv=0
					si=None
					for k,v in pl.items():
						if (mv==0):
							mv=v[0]
						bw=round(v[0]*(sbi.dwMaximumWindowSize.X-10)*2/pt)/2-np/2
						if (bw<0):
							bw=0
						o0[2]+=(f"\x1b[48;2;{int(ll[k][1][1:3],16)};{int(ll[k][1][3:5],16)};{int(ll[k][1][5:7],16)}m▌\x1b[0m" if np!=0 else "")+f"\x1b[38;2;{int(ll[k][1][1:3],16)};{int(ll[k][1][3:5],16)};{int(ll[k][1][5:7],16)}m"
						if (si==None):
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
			time.sleep(0.01)

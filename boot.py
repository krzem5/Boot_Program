from SimpleWebSocketServer import SimpleWebSocketServer,WebSocket
import keyboard
import socket
import subprocess
import os
import ctypes
import sys
import json
import glob
import ntpath
import threading
import cv2
import zipfile
import time
import shutil
import re
import urllib
import urllib.request
import urllib.parse
import clipboard
import traceback
import struct
import base64
import requests
import fnmatch
import datetime
import io
import random
import hashlib
import chardet
import serial
import serial.tools.list_ports
import shlex
import tempfile
import atexit
import msvcrt
import signal



os.system("title  ")
with open("D:\\boot\\secret.dt","r") as f:
	f=f.read()



global BLK_PID,KB_PID,WORKSPACE_PHP_PID,SWAP_DATA,CMD_L,STDOUT_LOCK,NETWORK,SERIAL_L,R_STD_BUFFER
GITHUB_HEADERS="application/vnd.github.v3+json,application/vnd.github.mercy-preview+json"
MIME_TYPES={"aac":"audio/aac","abw":"application/x-abiword","arc":"application/x-freearc","avi":"video/x-msvideo","azw":"application/vnd.amazon.ebook","bin":"application/octet-stream","bmp":"image/bmp","bz":"application/x-bzip","bz2":"application/x-bzip2","csh":"application/x-csh","css":"text/css","csv":"text/csv","doc":"application/msword","docx":"application/vnd.openxmlformats-officedocument.wordprocessingml.document","eot":"application/vnd.ms-fontobject","epub":"application/epub+zip","gz":"application/gzip","gif":"image/gif","htm":"text/html","html":"text/html","ico":"image/vnd.microsoft.icon","ics":"text/calendar","jar":"application/java-archive","jpeg":"image/jpeg","jpg":"image/jpeg","js":"text/javascript","json":"application/json","jsonld":"application/ld+json","mid":"audio/midi","midi":"audio/x-midi","mjs":"text/javascript","mp3":"audio/mpeg","mpeg":"video/mpeg","mpkg":"application/vnd.apple.installer+xml","odp":"application/vnd.oasis.opendocument.presentation","ods":"application/vnd.oasis.opendocument.spreadsheet","odt":"application/vnd.oasis.opendocument.text","oga":"audio/ogg","ogv":"video/ogg","ogx":"application/ogg","opus":"audio/opus","otf":"font/otf","png":"image/png","pdf":"application/pdf","php":"application/x-httpd-php","ppt":"application/vnd.ms-powerpoint","pptx":"application/vnd.openxmlformats-officedocument.presentationml.presentation","rar":"application/vnd.rar","rtf":"application/rtf","sh":"application/x-sh","svg":"image/svg+xml","swf":"application/x-shockwave-flash","tar":"application/x-tar","tif":"image/tiff","tiff":"image/tiff","ts":"video/mp2t","ttf":"font/ttf","txt":"text/plain","vsd":"application/vnd.visio","wav":"audio/wav","weba":"audio/webm","webm":"video/webm","webp":"image/webp","woff":"font/woff","woff2":"font/woff2","xhtml":"application/xhtml+xml","xls":"application/vnd.ms-excel","xlsx":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet","xml":"application/xml","xul":"application/vnd.mozilla.xul+xml","zip":"application/zip","3gp":"video/3gpp","3g2":"video/3gpp2","7z":"application/x-7z-compressed"}
SERIAL_BAUD=9600
R_STD_BUFFER={"_s":None,"bf":[]}
SERIAL_L={}
NETWORK=False
STDOUT_LOCK=False
CMD_L={}
KB_PID=-1
BLK_PID=-1
WORKSPACE_PHP_SERVER_PORT=random.randint(9001,49151)
WORKSPACE_WORKSPACE_PHP_PID=""
GIT_CLONE_REGEX=re.compile(r"^([A-Za-z0-9]+@|http(|s)\:\/\/)([A-Za-z0-9.]+(:\d+)?)(?::|\/)([\d\/\w.-]+?)\.git$")
URL_REGEX=re.compile(r"^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\xffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$",re.I|re.S)
GITHUB_TOKEN,CONTACT_EMAIL=f.replace("\r","").split("\n")[:2]
ARDUINO_HOST_SYSTEM="i686-mingw32"
ARDUINO_OS_TYPE="windows"
ARDUINO_MAIN_SKETCH_FILE_EXTENSIONS=[".ino",".pde"]
ARDUINO_ADDITIONAL_SKETCH_FILE_EXTENSIONS=[".c",".cpp",".h",".hh",".hpp",".s"]
ARDUINO_OPTIMIZE_FOR_DEBUG=False
ARDUINO_PREPROCESSOR_BUILD_PROPERTIES={"tools.arduino-preprocessor.path":"{runtime.tools.arduino-preprocessor.path}","tools.arduino-preprocessor.cmd.path":"{path}/arduino-preprocessor","tools.arduino-preprocessor.pattern":"\"{cmd.path}\" \"{source_file}\" \"{codecomplete}\" -- -std=gnu++11","preproc.macros.flags":"-w -x c++ -E -CC"}
ARDUINO_CUSTOM_WARNING_LEVEL=""



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
				print(m[i:])
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
		while (True):
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
		R_STD_BUFFER["bf"]+=[bytes(f"{threading.current_thread()._b_nm}\x00{threading.current_thread()._nm}\x00{a}","utf-8")]
		if (threading.current_thread()._r>=2):
			return
	if (not hasattr(threading.current_thread(),"_dp") or threading.current_thread()._dp==False):
		t=datetime.datetime.now().strftime("\x1b[38;2;50;50;50m[%H:%M:%S]\x1b[0m ")
		if (threading.current_thread()._nm not in CMD_L[threading.current_thread()._b_nm]["l"].keys()):
			CMD_L[threading.current_thread()._b_nm]["l"][threading.current_thread()._nm]=b""
		CMD_L[threading.current_thread()._b_nm]["l"][threading.current_thread()._nm]+=bytes(t+a.replace("\n","\n"+" "*len(re.sub(r"\x1b\[[^m]+m","",t)))+end,"utf-8")
	t=datetime.datetime.now().strftime((f"\x1b[38;2;50;50;50m[%H:%M:%S]\x1b[0m [{threading.current_thread()._b_nm}/{threading.current_thread()._nm}] " if not hasattr(threading.current_thread(),"_dpt") or threading.current_thread()._dpt==False else f"\x1b[38;2;50;50;50m[%H:%M:%S]\x1b[0m "))
	while (STDOUT_LOCK==True):
		pass
	STDOUT_LOCK=True
	sys.__stdout__.write(t+a.replace("\n","\n"+" "*len(re.sub(r"\x1b\[[^m]+m","",t)))+"\x1b[0m"+end)
	STDOUT_LOCK=False



def _start_thr(f,b_nm,nm,*a,**kw):
	def _wr(f,a,kw):
		global CMD_L
		if (b_nm not in CMD_L.keys()):
			CMD_L[b_nm]={"_end":lambda:None,"h":type("VoidHandle",(object,),{"stdin":io.StringIO}),"l":{nm:b""}}
		if (nm not in CMD_L[b_nm]["l"].keys()):
			CMD_L[b_nm]["l"][nm]=b""
		try:
			f(*a,**kw)
		except Exception as e:
			f=io.StringIO()
			traceback.print_exception(None,e,e.__traceback__,file=f)
			CMD_L[threading.current_thread()._b_nm]["l"][threading.current_thread()._nm]+=bytes("\x1b[38;2;200;40;20m"+f.getvalue(),"utf-8")
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



def _r_cmd(nm,e,h):
	global CMD_L
	def _h_s(nm,s_nm):
		global CMD_L
		while (True):
			CMD_L[nm]["l"]["__main__"]+=getattr(CMD_L[nm]["h"],"std"+s_nm).read1(1024).replace(b"\r\n",b"\n")
			time.sleep(1e-6)
	CMD_L[nm]={"_end":e,"h":h,"l":{"__main__":b""}}
	_start_thr(_h_s,nm,"_stdout_redirect",nm,"out")
	_start_thr(_h_s,nm,"_stderr_redirect",nm,"err")



def _start_ser(p):
	global SERIAL_L
	def _a_cs(ss,p):
		SERIAL_L[p]["port"]=ss.getsockname()
		_print(f"Starting Forward Socket Client Listener on Port '{ss.getsockname()[0]}:{ss.getsockname()[1]}'\x1b[38;2;100;100;100m...")
		while (SERIAL_L[p]["cnt"]>0):
			SERIAL_L[p]["_cs"]+=[ss.accept()[0]]
	def _w_thr(s):
		_print(f"Starting Writer Listener\x1b[38;2;100;100;100m...")
		while (SERIAL_L[p]["cnt"]>0):
			if (len(SERIAL_L[p]["in"])>0):
				_,SERIAL_L[p]["in"]=s.write(bytes(SERIAL_L[p]["in"][0],"utf-8")),SERIAL_L[p]["in"][1:]
			time.sleep(1e4)
	def _s_w_thr(s):
		_print(f"Starting Socket Writer Listener\x1b[38;2;100;100;100m...")
		while (SERIAL_L[p]["cnt"]>0):
			for cs in SERIAL_L[p]["_cs"]:
				dt=cs.recv(4096)
				if (len(dt)>0):
					print(str(dt))
			time.sleep(1e4)
	def _close_s(s,ss):
		s.close()
		ss.close()
	_print(f"Starting Serial Connection to Port '{p}'\x1b[38;2;100;100;100m...")
	try:
		s=serial.Serial(p,SERIAL_BAUD,timeout=5)
		while (s.is_open==False):
			time.sleep(1e-4)
		s.timeout=0
		_print(f"Creating Forwarding Socket\x1b[38;2;100;100;100m...")
		ss=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		ss.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		ss.bind(("127.0.0.1",0))
		ss.listen(5)
		_start_thr(_a_cs,"__core__",threading.current_thread()._nm+"_client_listener",ss,p)
		_print(f"Registering AtExit\x1b[38;2;100;100;100m...")
		atexit.register(_close_s,s,ss)
		bf=b""
		_start_thr(_w_thr,"__core__",threading.current_thread()._nm+"_writer",s)
		_start_thr(_s_w_thr,"__core__",threading.current_thread()._nm+"_socket_writer",s)
		_print(f"Starting Read Loop\x1b[38;2;100;100;100m...")
		while (SERIAL_L[p]["cnt"]>0):
			while (s.in_waiting==0 and SERIAL_L[p]["cnt"]>0):
				time.sleep(1e-4)
			bf+=s.read(s.in_waiting)
			mn_s=-1
			for cs in SERIAL_L[p]["_cs"][:]:
				mn_s=(cs.send(bf) if mn_s==-1 else min(mn_s,cs.send(bf)))
			bf=bf[mn_s:]
	except Exception as e:
		traceback.print_exception(None,e,e.__traceback__)
	_print(f"Closing Serial\x1b[38;2;100;100;100m...")
	del SERIAL_L[p]
	s.close()
	_print(f"Closing Socket\x1b[38;2;100;100;100m...")
	ss.close()
	_print(f"Unregistering AtExit\x1b[38;2;100;100;100m...")
	atexit.unregister(_close_s)



def _update_repo(p,b_nm,msg):
	def _gitigonre_match(gdt,fp):
		def _pattern(p,fp):
			fnm=ntpath.normpath(fp).replace(os.sep,"/").split("/")
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
	def _is_b(fp):
		with open(fp,"rb") as f:
			dt=f.read(4096)
		if (len(dt)==0):
			return False
		r1=len(dt.translate(None,b"\t\r\n\f\b"+bytes(range(32,127))))/len(dt)
		r2=len(dt.translate(None,bytes(range(127,256))))/len(dt)
		if (r1>0.90 and r2>0.9):
			return True
		enc=chardet.detect(dt)
		enc_u=False
		if (enc["confidence"]>0.9 and enc["encoding"]!="ascii"):
			try:
				dt.decode(encoding=enc["encoding"])
				enc_u=True
			except:
				pass
		if ((r1>0.3 and r2<0.05) or (r1>0.8 and r2>0.8)):
			return (False if enc_u==True else True)
		else:
			return (True if enc_u==False and (b"\x00" in dt or b"\xff" in dt) else False)
	def _match_f(fp,dt):
		if (_is_b(fp)==False):
			try:
				with open(fp,"r",encoding="utf-8") as f:
					f=f.read().replace("\r\n","\n")
					if (len(f)!=dt["sz"]):
						return False
					return (True if hashlib.sha1(f"blob {len(f)}\x00{f}".encode("utf-8")).hexdigest()==dt["sha"] else False)
			except:
				if (os.stat(fp).st_size!=dt["sz"]):
					return False
				with open(fp,"rb") as f:
					return (True if hashlib.sha1(f"blob {os.stat(fp).st_size}\x00".encode("utf-8")+f.read()).hexdigest()==dt["sha"] else False)
		else:
			if (os.stat(fp).st_size!=dt["sz"]):
				return False
			with open(fp,"rb") as f:
				return (True if hashlib.sha1(f"blob {os.stat(fp).st_size}\x00".encode("utf-8")+f.read()).hexdigest()==dt["sha"] else False)
	cfg={"name":re.sub(r"[^A-Za-z0-9_\.\-]",r"",b_nm),"desc":re.sub(r"[^A-Za-z0-9_\.\-]",r"",b_nm),"public":True,"homepage":"","license":"mit","file.readme":".\\README.md","file.gitignore":".\\.gitignore","config.has_issues":True,"config.has_projects":True,"config.has_wiki":True,"config.allow_squash_merge":True,"config.allow_merge_commit":True,"config.allow_rebase_merge":True,"config.delete_branch_on_merge":False}
	cfg_k=list(cfg.keys())
	if (ntpath.exists(f"{p}\\.gitconfig")):
		with open(f"{p}\\.gitconfig","r") as f:
			cfg.update({l.split("=")[0]:l[len(l.split("=")[0])+1:] for l in f.read().replace("\r","").split("\n") if len(l)>0 and "=" in l and l.strip()[0]!="#"})
		os.remove(f"{p}\\.gitconfig")
	for k in list(cfg.keys()):
		if (k not in cfg_k):
			del cfg[k]
	for k in "public,config.has_issues,config.has_projects,config.has_wiki,config.allow_squash_merge,config.allow_rebase_merge,config.allow_merge_commit,config.delete_branch_on_merge".split(","):
		cfg[k]=(True if str(cfg[k]) in ("True","true") else False)
	cfg["homepage"]=(cfg["homepage"] if len(cfg["homepage"])>0 and re.fullmatch(URL_REGEX,cfg["homepage"])!=None else "")
	with open(f"{p}\\.gitconfig","w") as f:
		f.write(f"### Github File Push Config\n\nname={cfg['name']}\ndesc={cfg['desc']}\npublic={str(cfg['public']).lower()}\nhomepage={cfg['homepage']}\nlicense={cfg['license']}\n\nfile.readme={cfg['file.readme']}\nfile.gitignore={cfg['file.gitignore']}\n\nconfig.has_issues={str(cfg['config.has_issues']).lower()}\nconfig.has_projects={str(cfg['config.has_projects']).lower()}\nconfig.has_wiki={str(cfg['config.has_wiki']).lower()}\nconfig.allow_squash_merge={str(cfg['config.allow_squash_merge']).lower()}\nconfig.allow_merge_commit={str(cfg['config.allow_merge_commit']).lower()}\nconfig.allow_rebase_merge={str(cfg['config.allow_rebase_merge']).lower()}\nconfig.delete_branch_on_merge={str(cfg['config.delete_branch_on_merge']).lower()}\n")
	os.system(f"cd /d {p}&&attrib +h .gitconfig&&cd /d D:\\boot")
	try:
		_request("post",url="https://api.github.com/user/repos",data=json.dumps({"name":cfg["name"],"description":cfg["desc"],"private":not cfg["public"],**({"homepage":cfg["homepage"]} if len(cfg["homepage"])>0 else {})},**{k[7:]:v for k,v in cfg.items() if k[:7]==".config"}))
	except requests.exceptions.ConnectionError:
		_print("\x1b[38;2;200;40;20mNo Internet Connection.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		return
	with open(ntpath.join(p,cfg["file.gitignore"]),"r") as f:
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
	br=[e["name"] for e in _request("get",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/branches")]
	br=("main" if "main" in br else ("master" if "master" in br else ("main" if len(br)==0 else br[0])))
	try:
		bt_sha=_request("get",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/git/ref/heads/{br}")["object"]["sha"]
	except KeyError:
		_request("put",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/contents/_",data=json.dumps({"message":msg,"content":""}))
		bt_sha=_request("get",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/git/ref/heads/{br}")["object"]["sha"]
		_request("delete",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/contents/_",data=json.dumps({"message":msg,"sha":"e69de29bb2d1d6434b8b29ae775ad8c2e48c5391"}))
	r_t=_get_tree(cfg["name"],bt_sha)
	bl=[]
	cnt=[0,0,0,0]
	for r,_,fl in os.walk(p):
		for f in fl:
			fp=ntpath.join(r,f).replace(p,"")[(1 if not p.endswith("\\") else 0):].replace("\\","/")
			if (_gitigonre_match(gdt,fp)==True):
				cnt[2]+=1
				_print(f"\x1b[38;2;190;0;220m! {b_nm}/{fp}\x1b[0m")
				continue
			if (fp in list(r_t.keys()) and _match_f(ntpath.join(r,f),r_t[fp])==True):
				cnt[1]+=1
				bl+=[[fp,None]]
				_print(f"\x1b[38;2;230;210;40m? {b_nm}/{fp}\x1b[0m")
				continue
			cnt[0]+=1
			_print(f"\x1b[38;2;70;210;70m+ {b_nm}/{fp}\x1b[0m")
			dt=f"File too Large (size = {os.stat(ntpath.join(r,f)).st_size} b)"
			b_sha=False
			if (os.stat(ntpath.join(r,f)).st_size<=50*1024*1024):
				b64=True
				if (_is_b(ntpath.join(r,f))==False):
					try:
						with open(ntpath.join(r,f),"r") as rbf:
							dt=rbf.read().replace("\r\n","\n")
						b64=False
					except:
						pass
				if (b64==True):
					b_sha=True
					with open(ntpath.join(r,f),"rb") as rbf:
						dt=str(base64.b64encode(rbf.read()),"utf-8")
					if (len(dt)>50*1024*1024):
						b_sha=False
						dt="File too Large (size = %d b)"%(len(dt))
					else:
						b=_request("post",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/git/blobs",data=json.dumps({"content":dt,"encoding":"base64"}))
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
		_request("patch",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/git/refs/heads/{br}",data=json.dumps({"sha":_request("post",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/git/commits",data=json.dumps({"message":msg,"tree":_request("post",url=f"https://api.github.com/repos/Krzem5/{cfg['name']}/git/trees",data=json.dumps({"base_tree":bt_sha,"tree":[b[1] for b in bl if b[1]!=None]}))["sha"],"parents":[bt_sha]}))["sha"],"force":True}))
	_print(f"\x1b[38;2;40;210;190m{b_nm} => \x1b[38;2;70;210;70m+{cnt[0]}\x1b[38;2;40;210;190m, \x1b[38;2;230;210;40m?{cnt[1]}\x1b[38;2;40;210;190m, \x1b[38;2;190;0;220m!{cnt[2]}\x1b[38;2;40;210;190m, \x1b[38;2;210;40;40m-{cnt[3]}\x1b[0m")



def _git_project_push(r=False,fr=False):
	global NETWORK
	msg=datetime.datetime.now().strftime("Push Update %m/%d/%Y, %H:%M:%S")
	_print(f"Starting Github Project Push Check with Commit Message '{msg}'\x1b[38;2;100;100;100m...")
	if (NETWORK==False):
		_print("\x1b[38;2;200;40;20mNo Internet Connection.\x1b[0m Waiting\x1b[38;2;100;100;100m...")
		while (NETWORK==False):
			time.sleep(1e-6)
		_print("Internet Connection Found\x1b[38;2;100;100;100m...")
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
			_update_repo(f"D:\\K\\Coding\\{p}",p,msg)
			f.write(p+"\n")
			f.flush()
		if (fr==False and "Boot_Program" in b_dt[1:]):
			t[1]+=1
			f.write("Boot_Program\n")
			f.flush()
		else:
			t[0]+=1
			_update_repo("D:\\boot\\","Boot_Program",msg)
			f.write("Boot_Program\n")
			f.flush()
	threading.current_thread()._df=False
	_print(f"Finished Github Project Push Check, {t[0]} Projects Updated, {t[1]} Skipped.")



def _arduino_clone_f(url,fp,sz):
	sz=int(sz)
	s=socket.socket(socket.ARDUINO_AF_INET,socket.ARDUINO_SOCK_STREAM)
	s.connect((url.split("/")[2],80))
	s.send(bytes(f"GET /{'/'.join(url.split('/')[3:])} HTTP/1.1\r\nHost: {url.split('/')[2]}\r\n\r\n","utf-8"))
	bf=b""
	while (not bf.endswith(b"\r\n\r\n")):
		bf+=s.recv(1)
	t=0
	at=0
	_print(f"{fp.split('/')[-1]} [....................] 0/{sz} 0%",end="")
	mx_ll=len(f"{fp.split('/')[-1]} [....................] 0/{sz} 0%")
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
			_print("\b"*mx_ll+f"{fp.split('/')[-1]} [{'='*(p-1)}{('>' if p>0 and p<20 else '')}{'.'*(20-p)}] {t}/{sz} {float(t*10000//sz)/100}%"+" "*(max(0,mx_ll-len(f"{fp.split('/')[-1]} [{'='*(p-1)}{('>' if p>0 and p<20 else '')}{'.'*(20-p)}] {t}/{sz} {float(t*10000//sz)/100}%"))),end="")
			mx_ll=max(mx_ll,len(f"{fp.split('/')[-1]} [{'='*(p-1)}{('>' if p>0 and p<20 else '')}{'.'*(20-p)}] {t}/{sz} {float(t*10000//sz)/100}%"))
	_print("\n",end="")
	s.close()



class _Arduino_Cache:
	def init():
		_print("Initialising Cache\x1b[38;2;100;100;100m...")
		if (not ntpath.exists(f"D:/boot/arduino/cache")):
			os.mkdir(f"D:/boot/arduino/cache")
		if (not ntpath.exists(f"D:/boot/arduino/cache/index")):
			with open(f"D:/boot/arduino/cache/index","w"):
				_Arduino_Cache._dt={}
		else:
			with open(f"D:/boot/arduino/cache/index","r") as f:
				_Arduino_Cache._dt={k.split(":")[0]:float(k.split(":")[1]) for k in f.read().replace("\r","").split("\n") if len(k)>0}
		u=False
		_print("Reading Cache Index\x1b[38;2;100;100;100m...")
		for k in list(_Arduino_Cache._dt.keys()):
			if (_Arduino_Cache._dt[k]<time.time() or not ntpath.exists(f"D:/boot/arduino/cache/{k}")):
				if (ntpath.exists(f"D:/boot/arduino/cache/{k}")):
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
	o=[]
	pl=list(serial.tools.list_ports.comports())
	for p in pl:
		r=_Arduino_Cache.get(f"vid_pid-0x{hex(p.vid)[2:].rjust(4,'0')}-0x{hex(p.pid)[2:].rjust(4,'0')}.json")
		if (r==None):
			r=requests.get(f"https://builder.arduino.cc/v3/boards/byVidPid/0x{hex(p.vid)[2:].rjust(4,'0')}/0x{hex(p.pid)[2:].rjust(4,'0')}",headers={"Content-Type":"application/json"}).text
			_Arduino_Cache.set(f"vid_pid-0x{hex(p.vid)[2:].rjust(4,'0')}-0x{hex(p.pid)[2:].rjust(4,'0')}.json",bytes(r,"utf-8"))
		if (len(r)==0):
			continue
		r=json.loads(r)
		o+=[{"arch":r["architecture"],"fqbn":r["fqbn"],"name":r["name"],"location":(p.name if p.name!=None else p.device)}]
	return o



def _install_ard_pkg(b,force=False):
	if (type(b)==str):
		_print(f"Searching For Package '{b}'\x1b[38;2;100;100;100m...")
		i_pkg=[]
		if (ntpath.exists(f"D:/boot/arduino/packages/index")):
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
						for fp in glob.iglob(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}/**/*.*",recursive=True):
							os.makedirs(ntpath.dirname(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}"),exist_ok=True)
							try:
								with open(fp,"rb") as rf,open(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}","wb") as wf:
									wf.write(rf.read())
							except:
								_print(f"\x1b[38;2;200;40;20mError while Copying File '{fp}' to 'D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{fp[off:]}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
						shutil.rmtree(f"D:/boot/arduino/packages/arduino/tools/{b}/{dt['tag_name']}/{b}",ignore_errors=True)
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
	if (not ntpath.exists(f"D:/boot//arduino/packages")):
		os.mkdir(f"D:/boot/arduino/packages")
	i_pkg=[]
	if (ntpath.exists(f"D:/boot/arduino/packages/index")):
		with open(f"D:/boot/arduino/packages/index","r") as f:
			i_pkg=f.read().replace("\r","").split("\n")
	else:
		with open(f"D:/boot/arduino/packages/index","w"):
			pass
	for k in o:
		if (force==False and f"{k[0]}-{k[1]}-{k[2]}" in i_pkg):
			_print(f"\x1b[38;2;200;40;20mPackage '{k[0]}:{k[1]}:{k[2]}' already Installed.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
			continue
		if (not ntpath.exists(f"D:/boot/arduino/packages/{k[0]}")):
			os.mkdir(f"D:/boot/arduino/packages/{k[0]}")
		if (not ntpath.exists(f"D:/boot/arduino/packages/{k[0]}/{k[5]}")):
			os.mkdir(f"D:/boot/arduino/packages/{k[0]}/{k[5]}")
		if (not ntpath.exists(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}")):
			os.mkdir(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}")
		if (not ntpath.exists(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}")):
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
				for fp in glob.iglob(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}/**/*.*",recursive=True):
					os.makedirs(ntpath.dirname(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}"),exist_ok=True)
					try:
						with open(fp,"rb") as rf,open(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}","wb") as wf:
							wf.write(rf.read())
					except:
						_print(f"\x1b[38;2;200;40;20mError while Copying File '{fp}' to 'D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{fp[off:]}'.\x1b[0m Skipping\x1b[38;2;100;100;100m...")
				shutil.rmtree(f"D:/boot/arduino/packages/{k[0]}/{k[5]}/{k[1]}/{k[2]}/{k[1]}",ignore_errors=True)
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



def _compile_ard_prog(s_fp,fqbn,inc_l):
	def _run_cmd(*a,**kw):
		o=subprocess.run(*a,**kw)
		if (o.returncode!=0):
			sys.exit(o.returncode)
		return o
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
		return [e for e in shlex.split(cmd) if len(e)>0]
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
					l[0]+=[ntpath.join(r,f)]
				elif (f.lower().endswith(".c")):
					l[1]+=[ntpath.join(r,f)]
				elif (f.lower().endswith(".cpp")):
					l[2]+=[ntpath.join(r,f)]
			if (rc==False):
				break
		o=[]
		for i in range(0,3):
			for f in l[i]:
				c_bp={**bp,"compiler.warning_flags":bp.get("compiler.warning_flags","")+("."+ARDUINO_CUSTOM_WARNING_LEVEL if ARDUINO_CUSTOM_WARNING_LEVEL!="" else ""),"includes":" ".join([f"\"-I{re.sub('('+chr(92)+r'|/)$','',e)}\"" for e in inc_l]),"source_file":f,"object_file":o_fp+f[len(i_fp):]+".o"}
				if (not ntpath.exists(o_fp+"/".join(f[len(i_fp):].split("/")[:-1]))):
					os.makedirs(o_fp+"/".join(f[len(i_fp):].split("/")[:-1]))
				_run_cmd(_prepare_cmd(re.sub(r"\{.+?\}","",_expand_in_string(c_bp,c_bp[("recipe.S.o.pattern","recipe.c.o.pattern","recipe.cpp.o.pattern")[i]]))))
				o+=[o_fp+f[len(i_fp):]+".o"]
		return o
	s_fp=ntpath.abspath(s_fp).replace("\\","/")
	fqbn=fqbn.split(":")
	if (not ntpath.exists(s_fp)):
		raise RuntimeError(f"Sketch {s_fp} doesn't Exist.")
	if (not ntpath.isdir(s_fp)):
		raise RuntimeError("Sketch Path must Be a Directory.")
	s_fp=s_fp.replace("\\","/")
	if (s_fp[-1]!="/"):
		s_fp+="/"
	b_fp=f"{tempfile.gettempdir()}/arduino-build-{hashlib.new('md5',bytes(s_fp,'utf-8')).hexdigest()}/"
	_print(f"Compiling Sketch '{s_fp}' to Directory '{b_fp}' with Architecture '{':'.join(fqbn)}'\x1b[38;2;100;100;100m...")
	if (not ntpath.exists(b_fp)):
		os.mkdir(b_fp)
	m_fp=None
	_print("Searching For Main File\x1b[38;2;100;100;100m...")
	for k in ARDUINO_MAIN_SKETCH_FILE_EXTENSIONS:
		if (ntpath.exists(f"{s_fp}index{k}")==True and ntpath.isdir(f"{s_fp}index{k}")==False):
			if (m_fp!=None):
				raise RuntimeError("Sketch Contains Multiple Main Programs.")
			m_fp=f"{s_fp}index{k}"
	if (m_fp==None):
		raise RuntimeError("Sketch doesn't Contain a Main Program.")
	_print("Loading Packages\x1b[38;2;100;100;100m...")
	if (not ntpath.exists(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/")):
		raise RuntimeError(f"Package '{fqbn[0]}:{fqbn[1]}' isn't Installed.")
	h_fp=ntpath.abspath(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"+sorted(os.listdir(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"),reverse=True)[0])+"/"
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
	bp={**ARDUINO_PREPROCESSOR_BUILD_PROPERTIES,"software":"ARDUINO",**p_pm,**h_pm[fqbn[2]],"build.path":re.sub(r"/$","",b_fp),"build.project_name":m_fp.split("/")[-1],"build.arch":fqbn[1].upper()}
	bp.update({"build.core.path":f"{h_fp}cores/{bp['build.core']}","build.system.path":f"{h_fp}system","runtime.platform.path":re.sub(r"/$","",h_fp),"runtime.hardware.path":re.sub(r"/$","",ntpath.abspath(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/")),"runtime.ide.version":"10607","runtime.ide.path":"D:/boot/","build.fqbn":":".join(fqbn),"ide_version":"ide_version","runtime.os":ARDUINO_OS_TYPE,"build.variant.path":("" if bp["build.variant"]=="" else f"{h_fp}variants/{bp['build.variant']}"),"build.source.path":re.sub(r"/$","",s_fp),"extra.time.utc":str(int(time.time())),"extra.time.local":str(datetime.datetime.now(datetime.timezone.utc).timestamp()),"extra.time.zone":"0","extra.time.dst":"0"})
	if (ARDUINO_OPTIMIZE_FOR_DEBUG==True):
		if ("compiler.optimization_flags.debug" in list(bp.keys())):
			bp["compiler.optimization_flags"]=bp["compiler.optimization_flags.debug"]
	else:
		if ("compiler.optimization_flags.release" in list(bp.keys())):
			bp["compiler.optimization_flags"]=bp["compiler.optimization_flags.release"]
	_print("Loading Tools\x1b[38;2;100;100;100m...")
	for pkg in os.listdir(f"D:/boot/arduino/packages/"):
		if (ntpath.exists(f"D:/boot/arduino/packages/{pkg}/tools/")):
			for t in os.listdir(f"D:/boot/arduino/packages/{pkg}/tools/"):
				for v in os.listdir(f"D:/boot/arduino/packages/{pkg}/tools/{t}/"):
					bp[f"runtime.tools.{t}-{v}.path"]=f"D:/boot/arduino/packages/{pkg}/tools/{t}/{v}"
				bp[f"runtime.tools.{t}.path"]=f"D:/boot/arduino/packages/{pkg}/tools/{t}/{v}"
	_print("Comparing Old Build Properties\x1b[38;2;100;100;100m...")
	if (ntpath.exists(f"{b_fp}build-properties.md5")):
		with open(f"{b_fp}build-properties.md5","r") as f:
			md5=f.read()
		if (md5[:32]!=hashlib.new("md5",bytes([(k,v) for k,v in bp.items() if not k.startswith("extra.time")].__repr__(),"utf-8")).hexdigest()):
			_print("\x1b[38;2;200;40;20mHash not Matching.\x1b[0m Rebuilding Everything\x1b[38;2;100;100;100m...")
			shutil.rmtree(b_fp)
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
					_print(f"Found Main Sketch File '{ntpath.join(r,fp)}'\x1b[38;2;100;100;100m...")
					with open(ntpath.join(r,fp),"rb") as f:
						dt=f.read()
						if (nh_inc==False and re.search(r"(?m)^\s*#\s*include\s*[<\"]Arduino\.h[>\"]",str(dt,"utf-8"))==None):
							bf.write(b"#include <Arduino.h>\n")
							l_off+=1
						nh_inc=True
						src+=dt+b"\n"
						bf.write(bytes(f"#line 1 \"{_quote_fp(ntpath.join(r,fp))}\"\n","utf-8")+dt+b"\n;\n")
						l_off+=(1 if ntpath.join(r,fp)==m_fp else 0)
		dl=[(e[0].replace("\\","/"),e[1].replace("\\","/")) for e in [(s_fp,s_fp)]+[(ntpath.join(r,d),r) for r,dl,_ in os.walk(s_fp) for d in dl]+[(e,e) for e in inc_l]]
		l=[e for e in re.findall(r"(?m)^\s*#\s*include\s*[<\"]([^>\"]+)[>\"]",str(src,"utf-8").lower()) if e!="arduino.h"]
		r_dl=[]
		for k in l:
			if (k[-2:]==".h"):
				l+=[k[:-2]+".cpp",k[:-2]+".c",k[:-2]+".s"]
			for d in dl:
				if (ntpath.exists(ntpath.join(d[0],k))):
					_print(f"Found Included Sketch File '{ntpath.join(d[0],k)}'\x1b[38;2;100;100;100m...")
					if (not ntpath.exists("/".join((b_fp+ntpath.join(d[0],k)[len(d[1]):]).replace("\\","/").split("/")[:-1]))):
						os.makedirs("/".join((b_fp+ntpath.join(d[0],k)[len(d[1]):]).replace("\\","/").split("/")[:-1]))
					with open("/".join((b_fp+ntpath.join(d[0],k)[len(d[1]):]).replace("\\","/").split("/")[:-1])+f"/{k}","wb") as wf,open(ntpath.join(d[0],k),"rb") as rf:
						dt=rf.read()
						l+=[e for e in re.findall(r"(?m)^\s*#\s*include\s*[<\"]([^>\"]+)[>\"]",str(dt,"utf-8").lower()) if e!="arduino.h" and e not in l]
						wf.write(bytes(f"#line 1 \"{_quote_fp(ntpath.join(d[0],k))}\"\n","utf-8")+dt+b"\n;\n")
					for e in inc_l:
						if (ntpath.join(d[0],k).replace("\\","/").startswith(e.replace("\\","/"))):
							if (e not in r_dl):
								r_dl+=[e]
							break
					break
		for k in r_dl:
			inc_l.remove(k)
	inc_l+=[bp["build.core.path"],b_fp]
	if (bp["build.variant.path"]!=""):
		inc_l+=[bp["build.variant.path"]]
	if (not ntpath.exists(f"{b_fp}preproc/")):
		os.mkdir(f"{b_fp}preproc/")
	_print("Generating Preprocessor Properties\x1b[38;2;100;100;100m...")
	pd={**bp,"source_file":b_fp+m_fp.split("/")[-1]+".cpp","preprocessed_file_path":f"{b_fp}preproc/preproc.cpp","includes":" ".join([f"\"-I{re.sub('('+chr(92)+r'|/)$','',e)}\"".replace("\\","/") for e in inc_l])}
	if ("recipe.preproc.macros" not in list(pd.keys())):
		pd["recipe.preproc.macros"]=pd["recipe.cpp.o.pattern"].replace("{compiler.cpp.flags}","{compiler.cpp.flags} {preproc.macros.flags}").replace("{object_file}","{preprocessed_file_path}")
	_print("Running Preprocessor\x1b[38;2;100;100;100m...")
	_run_cmd([e for e in _prepare_cmd(re.sub(r"\{.+?\}","",_expand_in_string(pd,pd["recipe.preproc.macros"]))) if e!="-MMD"]+["-DARDUINO_LIB_DISCOVERY_PHASE"])
	_print("Running Arduino Preprocessor\x1b[38;2;100;100;100m...")
	with open(b_fp+m_fp.split("/")[-1].split(".")[0]+".cpp","wb") as f:
		f.write(_run_cmd(_prepare_cmd(_expand_in_string({**bp,**{k[27:]:v for k,v in bp.items() if k[:26]=="tools.arduino-preprocessor"},"source_file":f"{b_fp}preproc/preproc.cpp","codecomplete":""},bp["tools.arduino-preprocessor.pattern"])),stdout=subprocess.PIPE).stdout)
	shutil.rmtree(f"{b_fp}preproc/")
	os.remove(b_fp+m_fp.split("/")[-1]+".cpp")
	_print("Running Recipe 'recipe.hooks.sketch.prebuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.sketch.prebuild",".pattern")
	_print("Compiling Files\x1b[38;2;100;100;100m...")
	s_of=_compile_files(bp,b_fp,b_fp,inc_l,False)+(_compile_files(bp,f"{b_fp}src/",f"{b_fp}src/",inc_l,True) if ntpath.exists(f"{b_fp}src/") else [])
	_print("Running Recipe 'recipe.hooks.sketch.postbuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.sketch.postbuild",".pattern")
	_print("Running Recipe 'recipe.hooks.core.prebuild'\x1b[38;2;100;100;100m...")
	_run_recipe(bp,"recipe.hooks.core.prebuild",".pattern")
	c_inc_l=[bp["build.core.path"]]+([bp["build.variant.path"]] if bp["build.variant.path"]!="" else [])
	_print("Buliding Core\x1b[38;2;100;100;100m...")
	if (not ntpath.exists(f"{b_fp}core/")):
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
	if (ntpath.exists(f"{s_fp}build/")):
		shutil.rmtree(f"{s_fp}build/",ignore_errors=True)
	os.mkdir(f"{s_fp}build/")
	for k in os.listdir(b_fp):
		if (k==f"{m_fp[len(s_fp):]}.hex"):
			with open(f"{s_fp}build/{m_fp[len(s_fp):]}.hex","wb") as wf,open(f"{b_fp}{k}","rb") as rf:
				wf.write(rf.read())
		if (k not in ["core","build-properties.md5"]):
			os.remove(f"{b_fp}{k}")
	return sz



def _upload_to_ard(s_fp,p,fqbn,bb,vu,inc_l):
	def _run_cmd(*a,**kw):
		o=subprocess.run(*a,**kw)
		if (o.returncode!=0):
			sys.exit(o.returncode)
		return o
	def _expand_in_string(d,s):
		while (True):
			ns=s+""
			for k,v in d.items():
				ns=ns.replace(f"{{{k}}}",v)
			if (ns==s):
				return s
			s=ns
	s_fp=ntpath.abspath(s_fp).replace("\\","/")
	fqbn=fqbn.split(":")
	if (not ntpath.exists(s_fp)):
		raise RuntimeError(f"Sketch {s_fp} doesn't Exist.")
	if (not ntpath.isdir(s_fp)):
		raise RuntimeError("Sketch Path must Be a Directory.")
	s_fp=s_fp.replace("\\","/")
	if (s_fp[-1]!="/"):
		s_fp+="/"
	_print("Searching For Build Directory\x1b[38;2;100;100;100m...")
	if (not ntpath.exists(f"{s_fp}build/")):
		_print("\x1b[38;2;200;40;20mSketch Build Directory Not Found.\x1b[0m Compiling\x1b[38;2;100;100;100m...")
		_compile_ard_prog(s_fp,":".join(fqbn),inc_l)
	if (not ntpath.exists(f"{s_fp}build/")):
		return
	_print("Searching For Main File\x1b[38;2;100;100;100m...")
	m_fp=None
	for k in ARDUINO_MAIN_SKETCH_FILE_EXTENSIONS:
		if (ntpath.exists(f"{s_fp}index{k}")==True and ntpath.isdir(f"{s_fp}index{k}")==False):
			if (m_fp!=None):
				raise RuntimeError("Sketch Contains Multiple Main Programs.")
			m_fp=f"{s_fp}index{k}"
	if (m_fp==None):
		raise RuntimeError("Sketch doesn't Contain a Main Program.")
	_print("Loading Packages\x1b[38;2;100;100;100m...")
	if (not ntpath.exists(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/")):
		raise RuntimeError(f"Package '{fqbn[0]}:{fqbn[1]}' isn't Installed.")
	h_fp=ntpath.abspath(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"+sorted(os.listdir(f"D:/boot/arduino/packages/{fqbn[0]}/hardware/{fqbn[1]}/"),reverse=True)[0])+"/"
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
		up[f"runtime.tools.{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}-{v}.path"]=f"D:/boot/arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}/{v}"
	up[f"runtime.tools.{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}.path"]=f"D:/boot/arduino/packages/arduino/tools/{h_pm[('bootloader.tool' if bb==True else 'upload.tool')]}/{v}"
	if (bb==False):
		up.update({"build.path":f"{s_fp}build/","build.project_name":m_fp[len(s_fp):]})
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
				raise RuntimeError("No Board Found.")
			time.sleep(0.5)
			p=b["location"]
			up.update({"serial.port":p,"serial.port.file":p})
		_print(f"Uploading Program to Board on Port '{p}'\x1b[38;2;100;100;100m...")
		_run_cmd([e for e in shlex.split(re.sub(r"\{.+?\}","",_expand_in_string(up,up["upload.pattern"]))) if len(e)>0])
	else:
		_print("Erasing Board\x1b[38;2;100;100;100m...")
		_run_cmd([e for e in shlex.split(re.sub(r"\{.+?\}","",_expand_in_string(up,up["erase.pattern"]))) if len(e)>0])
		_print("Burning Bootloader to Board\x1b[38;2;100;100;100m...")
		_run_cmd([e for e in shlex.split(re.sub(r"\{.+?\}","",_expand_in_string(up,up["bootloader.pattern"]))) if len(e)>0])
	_print("Upload Finished.")



def _rec_rm_pycache(bd):
	_print(f"Deleting PyCache For Folder '{bd}'\x1b[38;2;100;100;100m...")
	for sd in os.scandir(bd):
		if (sd.is_dir()==False or "\\Python38" in sd.path or "\\Python37" in sd.path or "\\Windows" in sd.path):
			continue
		if ("__pycache__" in sd.path):
			shutil.rmtree(sd.path,ignore_error=True)
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
		if (not ntpath.exists(p)):
			os.mkdir(p)
		i+=1
	with open(fn,"w") as f:
		f.write(txt)



def _open_prog_w(p):
	def _open_prog_w_f(p,p2,e,*f):
		op=False
		for fn in f:
			if (ntpath.isfile(fn)):
				subprocess.Popen([p,fn])
				op=True
		if (op==False):
			subprocess.Popen([p,glob.glob(f"{p2}**\\*.{e}",recursive=True)[0]])
	type_=p.split("-")[0].lower()
	_print(f"Opening Project: (name='{p[len(type_)+1:]}', type_='{type_}', path='D:\\K\\Coding\\{p}\\')\x1b[38;2;100;100;100m...")
	p="D:\\K\\Coding\\"+p+"\\"
	if (type_=="arduino"):
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"ino",f"{p}index.ino")
	elif (type_=="cpp"):
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"cpp",f"{p}index.cpp")
	elif (type_=="css"):
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"css",f"{p}index.html",f"{p}style.css")
	elif (type_=="fischertechnic"):
		_open_prog_w_f("C:\\Program Files\\ROBOPro\\ROBOPro.exe",p,"rpp",f"{p}index.rpp")
	elif (type_=="java"):
		c_nm=p.split("\\")[-2].split("-")[1].lower()
		if (ntpath.exists(f"{p}com\\krzem\\{c_nm}\\")):
			subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",f"{p}com\\krzem\\{c_nm}\\"])
		else:
			subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"java",f"{p}com\\krzem\\{p.split('-')[1].lower().replace(' ','_')}\\Main.java")
	elif (type_=="javascript"):
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"js",f"{p}index.html",f"{p}index.js")
	elif (type_=="php"):
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"php",p+"index.php")
	elif (type_=="processing"):
		os.system(f"start /min cmd /c \"{p}index\\index.pde\"")
	elif (type_=="python"):
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"py",f"{p}index.py")
	elif (type_=="three"):
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
		_open_prog_w_f("C:\\Program Files\\Sublime Text 3\\sublime_text.exe",p,"js",f"{p}index.html",f"{p}index.js")
	elif (type_=="mindstorm"):
		_open_prog_w_f("C:\\Program Files\\LEGO Software\\LEGO MINDSTORMS EV3 Home Edition\\MindstormsEV3.exe",p,"ev3",f"{p}index.ev3")
	else:
		_print("\x1b[38;2;200;40;20mUnknown type.\x1b[0m Defaulting to Editor\x1b[38;2;100;100;100m...")
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])



def _create_prog(type_,name,op=True,pr=True):
	if (pr==True):
		_print(f"Creating Project: (type='{type_}', name='{name}', open_on_creation={op})")
	type_=type_.lower()
	if (type_ not in "arduino,assembly,c,chromeext,cpp,css,ft,fischertechnic,java,js,javascript,mindstorm,php,processing,python,three,websocket".split(",")):
		_print(f"Unknown Prog Type: {type_}")
		return
	if (type_=="js"):
		type_="javascript"
	if (type_=="ft"):
		type_="fischertechnic"
	name=name.replace("_"," ").lower().title().replace(" ","_")
	p="D:\\K\\Coding\\"+type_.title()+"-"+name+"\\"
	fel=[]
	for r,_,fl in os.walk(p):
		for f in fl:
			fel+=[ntpath.join(r,f).split(".")[-1]]
	if (not ntpath.exists(p)):
		os.mkdir(p)
	if (not ntpath.exists(f"{p}.gitignore")):
		with open(f"{p}.gitignore","x") as f:
			f.write("### Github File Push Ignore\n\n")
		os.system(f"cd /d {p}&&attrib +h .gitignore")
	if (not ntpath.exists(f"{p}LICENSE")):
		with open(f"{p}LICENSE","x") as f:
			f.write(f"""Copyright (c) {datetime.datetime.now().year} Krzem\n\nPermission is hereby granted, free of charge, to any person obtaining a\ncopy of this software and associated documentation files (the\n"Software"), to deal in the Software without restriction, including without\nlimitation the rights to use, copy, modify, merge, publish, distribute,\nsublicense, and/or sell copies of the Software, and to permit persons\nto whom the Software is furnished to do so, subject to the following\nconditions:\n\nThe above copyright notice and this permission notice shall be included\nin all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY\nKIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE\nWARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR\nPURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL\nTHE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,\nDAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF\nCONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN\nCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS\nIN THE SOFTWARE.""")
	if (not ntpath.exists(f"{p}README.md")):
		with open(f"{p}README.md","x") as f:
			f.write(f"""# {type_.title()} - {name.replace('_',' ').title()}\n(This is an auto - generated file.)\n""")
	if (type_=="arduino"):
		if (not ntpath.exists(f"{p}index.ino") and "ino" not in fel):
			with open(f"{p}index.ino","x") as f:
				f.write("void setup(){\n\t\n}\n\n\n\nvoid loop(){\n\t\n}\n")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\nrm -rf build&&python D:\\boot\\boot.py 5 compile ./ arduino:avr:uno&&python D:\\boot\\boot.py 5 upload ./ COM3 arduino:avr:uno\n")
	elif (type_=="c"):
		if (not ntpath.exists(f"{p}src/main.c") and "c" not in fel):
			if (not ntpath.exists(f"{p}src")):
				os.mkdir(f"{p}src")
			if (not ntpath.exists(f"{p}src/{name.lower()}")):
				os.mkdir(f"{p}src/{name.lower()}")
			if (not ntpath.exists(f"{p}src/include")):
				os.mkdir(f"{p}src/include")
			with open(f"{p}src/main.c","x") as f:
				f.write("int main(int argc,const char** argv){\n\treturn 0;\n}")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\nset _INCLUDE=%INCLUDE%\nset INCLUDE=../src/include;%INCLUDE%\nif exist build rmdir /s /q build\nmkdir build\ncd build&&if %1.==. goto dbg\nif %1==-r (\n\tcl /c /permissive- /GS /W3 /Zc:wchar_t /Gm- /sdl /Zc:inline /fp:precise /D \"NDEBUG\"  /D \"_WINDOWS\" /D \"_USRDLL\" /D \"_WINDLL\" /D \"_UNICODE\" /D \"UNICODE\" /errorReport:none /WX /Zc:forScope /Gd /Oi /FC /D \"DLL1_EXPORTS\" /EHsc /nologo /diagnostics:column /GL /Gy /Zi /O2 /Oi /MD ../src/main.c ../src/{name.lower()}/*.c&&link *.obj /OUT:{name.lower()}.exe /DYNAMICBASE \"kernel32.lib\" \"user32.lib\" \"gdi32.lib\" \"winspool.lib\" \"comdlg32.lib\" \"advapi32.lib\" \"shell32.lib\" \"ole32.lib\" \"oleaut32.lib\" \"uuid.lib\" \"odbc32.lib\" \"odbccp32.lib\" /MACHINE:X64 /SUBSYSTEM:CONSOLE /ERRORREPORT:none /NOLOGO /TLBID:1 /WX /LTCG /OPT:REF /INCREMENTAL:NO /OPT:ICF&&goto run\n\tgoto end\n)\n:dbg\ncl /c /permissive- /GS /W3 /Zc:wchar_t /Gm- /sdl /Zc:inline /fp:precise /D \"_DEBUG\"  /D \"_WINDOWS\" /D \"_USRDLL\" /D \"_WINDLL\" /D \"_UNICODE\" /D \"UNICODE\" /errorReport:none /WX /Zc:forScope /Gd /Oi /FC /D \"DLL1_EXPORTS\" /EHsc /nologo /diagnostics:column /ZI /Od /RTC1 /MDd ../src/main.c ../src/{name.lower()}/*.c&&link *.obj /OUT:{name.lower()}.exe /DYNAMICBASE \"kernel32.lib\" \"user32.lib\" \"gdi32.lib\" \"winspool.lib\" \"comdlg32.lib\" \"advapi32.lib\" \"shell32.lib\" \"ole32.lib\" \"oleaut32.lib\" \"uuid.lib\" \"odbc32.lib\" \"odbccp32.lib\" /MACHINE:X64 /SUBSYSTEM:CONSOLE /ERRORREPORT:none /NOLOGO /TLBID:1 /WX /DEBUG /INCREMENTAL&&goto run\ngoto end\n:run\ndel *.obj\ndel *.pdb\ndel *.exp\ndel *.ilk\ndel *.idb\ncls\n{name.lower()}.exe\n:end\ncd ../\nset INCLUDE=%_INCLUDE%")
	elif (type_=="cpp"):
		if (not ntpath.exists(f"{p}index.cpp") and "cpp" not in fel):
			with open(f"{p}index.cpp","x") as f:
				f.write("int main(){\n\treturn 0;\n}")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\ndel *.obj&&del index.exe&&cl /EHsc *.cpp /link /OUT:index.exe&&del *.obj&&cls&&index.exe\nif exist index.exe (\n\trem del index.exe\n)")
	elif (type_=="css"):
		if (not ntpath.exists(f"{p}index.html") and "html" not in fel):
			with open(f"{p}index.html","x") as f:
				f.write(f"<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{name.replace('_',' ')}</title>\n\t\t<link href=\"./style.css\" rel=\"stylesheet\" type=\"text/css\">\n\t</head>\n\t<body>\n\t</body>\n</html>")
		if (not ntpath.exists(f"{p}style.css") and "css" not in fel):
			with open(f"{p}style.css","x") as f:
				f.write("body {\n\twidth: 100%;\n\theight: 100%\n}\nbody, body * {\n\tmargin: 0;\n\tpadding: 0;\n}")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/Google/Chrome Dev/Application/chrome.exe\" http://localhost:8020/{p}")
	elif (type_=="fischertechnic"):
		if (not ntpath.exists(f"{p}index.rpp") and "rpp" not in fel):
			with open(f"{p}index.rpp","x") as f:
				f.write(f"<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n\n<cvg classname=\"ftProDrawDcmt\">\n\t<title>{name.replace('_',' ')}</title>\n\t<desc>wxCanvasDocument generated by wxCANVAS</desc>\n\t<version>2</version>\n\t<roboprover>04010600</roboprover>\n\t<bluetooth>\n\t\t<centralswitch>2</centralswitch>\n\t</bluetooth>\n\t<camera camerawidth=\"320\" cameraheight=\"240\" cameraframerate=\"15\" cameraconnectpc=\"false\" cameramirror=\"false\" cameraflip=\"false\">\n\t</camera>\n\t<o classname=\"wxCanvasLayers\" flags=\" selectable visible draggable shadow filled snap\" hitflags=\" visible\">\n\t\t<o classname=\"wxLayerInfo\" name=\"layer default\" flags=\" selectable visible draggable shadow filled snap\" hitflags=\" visible\" layervisible=\"true\" layerselectable=\"true\" readlayer=\"true\" inmap=\"0\" outmap=\"0\" order=\"0\">\n\t\t\t\n\t\t\t<properties>\n\t\t\t\t<o classname=\"wxDocviewRefObjectProperty\" name=\"fill\">\n\t\t\t\t\t<o classname=\"wxCanvasOneColourFill\" id=\"1021682\" colour=\"GREY\">\n\t\t\t\t\t</o>\n\t\t\t\t</o>\n\t\t\t\t<o classname=\"wxDocviewRefObjectProperty\" name=\"stroke\">\n\t\t\t\t\t<o classname=\"wxCanvasOneColourStroke\" id=\"960046\" colour=\"BLACK\" pixelwidth=\"true\" width=\"1\">\n\t\t\t\t\t</o>\n\t\t\t\t</o>\n\t\t\t</properties>\n\t\t\t\n\t\t</o>\n\t\t\n\t\t<o classname=\"wxLayerInfo\" name=\"layer data wires\" layer=\"1\" flags=\" selectable visible draggable shadow filled snap\" hitflags=\" visible\" layervisible=\"true\" layerselectable=\"true\" readlayer=\"true\" inmap=\"1\" outmap=\"1\" order=\"1\">\n\t\t\t\n\t\t\t<properties>\n\t\t\t\t<o classname=\"wxDocviewRefObjectProperty\" name=\"fill\">\n\t\t\t\t\t<o classname=\"wxCanvasOneColourFill\" id=\"1021666\" colour=\"#E67300\">\n\t\t\t\t\t</o>\n\t\t\t\t</o>\n\t\t\t\t<o classname=\"wxDocviewRefObjectProperty\" name=\"stroke\">\n\t\t\t\t\t<o classname=\"wxCanvasOneColourStroke\" id=\"959956\" colour=\"#E67300\" width=\"0.5\">\n\t\t\t\t\t</o>\n\t\t\t\t</o>\n\t\t\t</properties>\n\t\t\t\n\t\t</o>\n\t\t\n\t\t<o classname=\"wxLayerInfo\" name=\"layer flow wires\" layer=\"2\" flags=\" selectable visible draggable shadow filled snap\" hitflags=\" visible\" layervisible=\"true\" layerselectable=\"true\" readlayer=\"true\" inmap=\"2\" outmap=\"2\" order=\"2\">\n\t\t\t\n\t\t\t<properties>\n\t\t\t\t<o classname=\"wxDocviewRefObjectProperty\" name=\"fill\">\n\t\t\t\t\t<o classname=\"wxCanvasOneColourFill\" id=\"1021594\" colour=\"#14007D\">\n\t\t\t\t\t</o>\n\t\t\t\t</o>\n\t\t\t\t<o classname=\"wxDocviewRefObjectProperty\" name=\"stroke\">\n\t\t\t\t\t<o classname=\"wxCanvasOneColourStroke\" id=\"960096\" colour=\"#14007D\" width=\"0.5\">\n\t\t\t\t\t</o>\n\t\t\t\t</o>\n\t\t\t</properties>\n\t\t\t\n\t\t</o>\n\t\t\n\t</o>\n\t<o classname=\"wxCanvasObject\" id=\"1029794\" flags=\" selectable visible draggable shadow filled snap\" hitflags=\" visible\">\n\t</o>\n</cvg>")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files (x86)/ROBOPro/ROBOPro.exe\" {p}index.rpp")
	elif (type_=="java"):
		if (not ntpath.exists(f"{p}com\\")):
			os.mkdir(f"{p}com\\")
		if (not ntpath.exists(f"{p}com\\krzem\\")):
			os.mkdir(f"{p}com\\krzem\\")
		if (not ntpath.exists(f"{p}com\\krzem\\{name.lower()}\\")):
			os.mkdir(f"{p}com\\krzem\\{name.lower()}\\")
		if (not ntpath.exists(f"{p}com\\krzem\\{name.lower()}\\Main.java") and "java" not in fel):
			with open(f"{p}com\\krzem\\{name.lower()}\\Main.java","x") as f:
				f.write("package com.krzem."+name.lower()+";\n\n\n\npublic class Main{\n\tpublic static void main(String[] args){\n\t\tnew Main();\n\t}\n\n\n\n\tpublic Main(){\n\t\t\n\t}\n}")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(p+"index.bat","x") as f:
				f.write(f"@echo off\necho NUL>_.class&&del /s /f /q *.class\ncls\njavac com/krzem/{name.lower().replace(' ','_')}/Main.java&&java com/krzem/{name.lower().replace(' ','_')}/Main\nstart /min cmd /c \"echo NUL>_.class&&del /s /f /q *.class\"")
	elif (type_=="javascript"):
		if (not ntpath.exists(f"{p}index.html") and "html" not in fel):
			with open(f"{p}index.html","x") as f:
				f.write(f"<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{name.replace('_',' ')}</title>\n\t\t<script type=\"text/javascript\" src=\"./index.js\"></script>\n\t</head>\n\t<body>\n\t</body>\n</html>")
		if (not ntpath.exists(f"{p}index.js") and "js" not in fel):
			with open(f"{p}index.js","x") as f:
				f.write("function init(){\n\t\n}\ndocument.addEventListener(\"DOMContentLoaded\",init,false)")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/Google/Chrome Dev/Application/chrome.exe\" http://localhost:8020/{p}")
	elif (type_=="php"):
		if (not ntpath.exists(f"{p}index.php") and "php" not in fel):
			with open(f"{p}index.php","x") as f:
				f.write("<?php\n\n?>")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/Google/Chrome Dev/Application/chrome.exe\" http://localhost:8020/{p}index.php")
	elif (type_=="processing"):
		if (not ntpath.exists(f"{p}index\\")):
			os.mkdir(f"{p}index\\")
		if (not ntpath.exists(f"{p}index\\index.pde")):
			with open(f"{p}index\\index.pde","x") as f:
				f.write("void setup(){\n\t\n}\n\nvoid draw(){\n\t\n}")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\nstart /min cmd /c \"{p}index\\index.pde\"")
	elif (type_=="python"):
		if (not ntpath.exists(f"{p}index.py") and "py" not in fel):
			with open(f"{p}index.py","x") as f:
				f.write("")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\npython index.py")
	elif (type_=="three"):
		if (not ntpath.exists(f"{p}index.html") and "html" not in fel):
			with open(f"{p}index.html","x") as f:
				f.write(f"<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{name.replace('_',' ')}</title>\n\t\t<script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/three.js/104/three.min.js\"></script>\n\t\t<script type=\"text/javascript\" src=\"https://threejs.org/js/controls/OrbitControls.js\"></script>\n\t\t<script type=\"text/javascript\" src=\"./index.js\"></script>\n\t\t<style type=\"text/css\">\n\t\t\tbody {{\n\t\t\t\tmargin: 0;\n\t\t\t\tpadding: 0;\n\t\t\t}}\n\t\t\tcanvas {{\n\t\t\t\twidth: 100%%;\n\t\t\t\theight: 100%%;\n\t\t\t}}\n\t\t</style>\n\t</head>\n\t<body>\n\t</body>\n</html>")
		if (not ntpath.exists(f"{p}index.js") and "js" not in fel):
			with open(f"{p}index.js","x") as f:
				f.write("var scene,cam,renderer,controls\nfunction init(){\n\tscene=new THREE.Scene()\n\tcam=new THREE.PerspectiveCamera(60,window.innerWidth/window.innerHeight,0.1,100000)\n\tcam.position.set(0,2000,0)\n\tcam.enablePan=false\n\tcam.lookAt(new THREE.Vector3(0,0,0))\n\trenderer=new THREE.WebGLRenderer({antialias:true})\n\trenderer.setSize(window.innerWidth,window.innerHeight)\n\tscene.background=new THREE.Color().setHSL(1,1,1)\n\tdocument.body.appendChild(renderer.domElement)\n\tambient=new THREE.AmbientLight(0xffffff,1)\n\tscene.add(ambient)\n\trenderer.render(scene,cam)\n\tcontrols=new THREE.OrbitControls(cam,renderer.domElement)\n\tcontrols.target=new THREE.Vector3(0,0,0)\n\twindow.addEventListener(\"resize\",resize,false)\n\twindow.addEventListener(\"keypress\",onkeypress)\n\trequestAnimationFrame(render)\n}\nfunction render(){\n\trenderer.render(scene,cam)\n\trequestAnimationFrame(render)\n}\nfunction resize(){\n\tcam.aspect=window.innerWidth/window.innerHeight\n\tcam.updateProjectionMatrix()\n\trenderer.setSize(window.innerWidth,window.innerHeight)\n}\nfunction onkeypress(e){\n\tswitch (e.keyCode){\n\t\t//\n\t}\n}\ndocument.addEventListener(\"DOMContentLoaded\",init,false)")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/Google/Chrome Dev/Application/chrome.exe\" http://localhost:8020/{p}")
	elif (type_=="mindstorm"):
		if (not ntpath.exists(f"{p}index.ev3") and "ev3" not in fel):
			with open(f"{p}index.ev3","wb") as f:
				f.write(b"PK\x03\x04\x14\x00\x00\x00\x08\x00T\x88VE\xa1\xf9\xe4\xb8\x06\x00\x00\x00\x04\x00\x00\x00\x10\x00\x00\x00___CopyrightYear3204\x01\x00PK\x03\x04\x14\x00\x00\x00\x08\x00T\x88VEr\xe9\x0e\xe0\t\x00\x00\x00\x07\x00\x00\x00\x0f\x00\x00\x00___ProjectTitle\x0b(\xca\xcfJM.\x01\x00PK\x03\x04\x14\x00\x00\x08\x08\x00\x05\x94\xa9N\x0e\xc5\xcb\xd7\x08\x00\x00\x00\x16\x00\x00\x00\x12\x00\x00\x00ActivityAssets.laz\x0b\xf0fec\xc0\x00\x00PK\x03\x04\x14\x00\x00\x08\x08\x00\x05\x94\xa9N\x89\x9fa\x01\xf6\x01\x00\x00\x04\x04\x00\x00\x0c\x00\x00\x00Activity.x3a\x95S\xddn\xda0\x14\xbe\x9f\xb4w\xb0|[-n\xdamBSB\xd5\xf2\x93\x95\x8d\xd2\x12\xca\xa4\xde\x19\xdb\x10\xa7\x8e\x9d%\x0e\x10^m\x17{\xa4\xbd\xc2N\x82 \x14\xc1\xa4E\x8ad\x9f\xf3\x9d\xcf\xe7;?\x7f~\xfd\xf6n\xd6\x89BK\x91\xe5\xd2h\x1f\xbb\xce%FB3\xc3\xa5^\xf8\xb8\xb0\xf3\x0f-|\xd3~\xff\xce\x0bM\x911\xd1\x97J\xa0\xe9\x01\xda\xb9r\\\x08\x01\x12\x9d\xfb8\xb26\xfdB\xc8j\xb5r\xb4t\x98I\xc86lh\xb8P\xce:\xe7\x18\xa8\x10|\xde\x03MD\x9eR&Pu\xf2\xf1cfb\xc1\xec\xce_c\x82Br\xc1\xbf\n\x95\x9e\xe7o0\x87\xf4{\x8aP\x81;?\xb26\x1e\xd4\x84\x87r\x03i\x84\tU\n\xf4Y\xc9\xa8\xc2\xa8\x06m\x13\xc4\xe8A\xac\xed]a\xad\xd1=MgJp\x1fO\xb2B`4\xd25\xae\x13Q\xbd\xa8\xac\x10\'\x17\x9a\xda\"\x83\xb8\xf8)\xa6\xe3\xeb\xe0\x95\xb6n\x03>\xb8\xeb\xb7dy\xc5_\xa2A\xc8?\xc5\xdau\xf9\xc8\x8eF\xeb\x90|\xef\xcfF\xd3\xa7\xf9\xf4\xc2\xfd\xf8Mw\x94z\x0c_\x97\xf3\xf1\xe62\xe0,\xb8_\x90\xc1p\xca\xf2\xe2e\xe3&\xb1\xce/\xae\x17\xbe\x8f\xd1D$\xa9\xa2V\xdcw}\xdc/\x94\xc2\'dn\xa5J\x00\x8a.\xb5\x14=k\xf9\xb3\xa8#\xc6\x92E\x13P4\x91V\x81\x86}O\xa1\x99\xcf\xb9\xc8z\\\xdaJ$PS\x95\x03\xe0G\xa5\xd0h\x9b\x19\xb5\xb3\x9dy\xaf~\xb3\xa2n{\xbbG\xba\x86\x15\x89\xd0\x16\xcd\x81!\xaf+\xed~\xc6\xf5mN\x13\xa9J\x1fC\x02\x9cj\xfa\x8fQ\xbaeV.\xa5-\x8fI\xb7\x8d\xf7\xd2\xb67k{\xa4\xfa\xe1H\x8eQ`\xaas:S#\xd2\x14\xe9\xbf\xca\xd8KR[\xbe-\x1f9G\xd0\x89\xa4\xe2\x99\xd0\'\x11\x90A5D\xc7\x03LNN\xb07\x14\\\xd2\xae\x84\x8a\x18M\xb3\xf2\r\xa3w\xb0\x14\xbbu#\xfb}\xabv\x994\xcb\xdc\xfe\x0bPK\x03\x04\x14\x00\x00\x08\x08\x00\x05\x94\xa9NHu\xf8\xec\x11\x03\x00\x008\n\x00\x00\t\x00\x00\x00Main.ev3p\xcdV\xcdn\xda@\x10\xbeW\xea;X\xee9\xb6\t$M]\x9c(\x84\xa0 \xa5!\x02Dr\xa8\x84\x16{\x0c\xdb\xd8\xbb\xee\xee\x1a\xc8\xb3\xf5\xd0G\xea+t\xbc`\xec\x00!\xd0\x1eZ\xec\x83=3\xdf\xcc7\x9e\x1f\xf6\xd7\x8f\x9f\xf5\x8by\x1c\x19S\x10\x92r\xe6\x99\x15\xcb1\r`>\x0f(\x1b{f\xaa\xc2\xa33\xf3\xe2\xfc\xfd\xbbz\x8f\xa7\xc2\x87\x16\x8d\xc0\x18\x94\xac\xadc\xab\x82\x10t\xc2\xa4gN\x94J\\\xdb\x9e\xcdf\x16\xa3\x96\xcfc{\x01\xfb\xc2\x03\x88\xac\xb9\x0cLte\xe0\xaf~Gb\x90\t\xf1\xc1\xc8\x9e<\xf3^\xf0o\xe0\xab\\\xafm\x06T\xa8\x94Dm&\x95Hc`\xcah\xcb>Ona\n\x91g\x86$\x92`\xa2\xa8\x0b\xa8\x12\x84\xa9\x95l\x8d \xf2\xeb`\x86\x82fIi*M\x08)\xa3\nm\xfa\xcf\tF\x7f\xac\x0e\xdaM\xee\xeb ;\x92\xd9 TNiE\xbb%8S\xf7\x84A\xb4\xa6\xd1\xda0\x11)S4\x06\xb7\xb0\xbb\"lJ\xe4Z\\\xe9O &\xd2\x8a\xa9/\xb8\xe4\xa1\xd2\x14f\x94\x85s\xfb\xd8qN\xed9\x89#;\x11 \x91\x08\xc9rY2w\xe7\x87\xf9\xc8a+f\x9e\xe9G\xe2\x88\xe5\x15r\xef\xb4\xf7r\xde\xd2\xba%\xa3A\xfb\xfa\xc1*\x92\xe8.\xc0\x9f\x89\x94\x10\x8f\xa2g\xef XNB\x97g\x1f\x02\xe5\xc6j\x82\xa4c\x06bw\xec\x12\x02\xa3\xb9\x8b\xbe+\x88\x98\x86V\xb9\xb9\xb3^*B\x0c\x8e\x8d\x99\x80P\x14\xa4\x85e\xea1\x92\xf4yg\x94\xf5*\x96\xaa/Rx\x1b\xf7g\xa0\t\x9fe\xc0\x8828\x08t\x85\t\t\x1e]\x06\\\xa0\xcd\n\xfa@\x035\xf1\xcc\xd3\x1aN\xc3\r\xd0\xf1\x04\xc7\xa5v\x86/\xf6z\xff\xda\xaf6p\xbd\x11q\xff\xa9I\xc9X\x90x9\xb8\xc3a\x97s\xb5\x94\r\x87\xe6\xb6\x9e\xef)\"\x94\xc6\x1a\xed\xc03Y\xc54\x1a<e\x01\x92\xab\x1d\x1b\xd5\x9a\xf1\xd11>\xa1\xb0O\xc4\x18T6\x8e_\xad[:r\x0b\\\x1f\xa4\xda\xe6Z\xbb\xc7\x8cC:N\x05\x19E\xf0\x05\xd4\x84\x07}\x101\xc5\xf2\xbf\x82\xd0\xa8\xdcFS\xea\x82L#\x1c\xfd&\x15X$\xbd;:\xa9J\xd2LD\x14Yl\x89\x06\xe7\x11\x10\x1c\xb3\x1b\xaed\xc2\x91\xa8c\x9d\x18\xa5d\x1cC_\x9b\xdf\xb4\xf8\xb6\x07s}\xc9\xb3\x07\xdfS\\\xcf\xd0I\xdf\"\xbbe\x02\xdc\xd2\x04\xb8\xb9\xa5t\x1f\xab\xb9\xd7\x07t\x98\xcbKYV\x0c\xcc\xb3\xc8\xf2\x04KV5*gxo\xcf\xb4n\x17\x85\xdbh\xaer\x0b\xad+\xdb>g\xdb\xfci\xc6\x8e\x9b\xa9u[\xfe\xebM\xb9\xe0s\xc8\x9a\x1c\xb4\x97Kj\xbf\xf5\x88\xe6/\xb7\xd5\xff\xb0\xa0\xf3\xadqr\xba\xda&\xd9c\x83\xf8Oc\x91\xf5\x86g~h\xb5\xae\x9d\xeczuV\x8b\xbf\xbfKFcM\xa0\xb4\xbfV2\xb9kr\xb7\xf8\x90\xd9\xd6#\xb8*\xc5\x8e\xd9\xfb\xcb\xd8\xa5\xb8\xd7S\xfcX%\xac~\xdf\x93\xb3\xb6=\x8c\xee\xde\xe1\xea\xf6\xfa\xa8l\xcc\xdf\xda\x8c\xd57\x0f5\xf9\x11\xcd^\x9d\xd1\xb2\xf3\x9f]\x1c\x00\xcf\x7f\x03PK\x03\x04\x14\x00\x00\x08\x08\x00\x05\x94\xa9Nv\x8c2j \x03\x00\x00\xc0\x0f\x00\x00\x0f\x00\x00\x00Project.lvprojx\xddW\xefn\xda0\x10\xff>i\xef\x10\xe5s\xeb\xb4\xe3\xcb4\x05\xaa\xb6@\x17\xa9\xb4\xa8tY\'!!\x93\x1c\xe0\xcd\xd8\x91\xe3\x04\xd8\xab\xed\xc3\x1ei\xaf0\x9b$$\xa4\t\xa3]\xd7uk%\x88r\xe7\xbb\xdf\xef\xfe\xf8\x8e\x1f\xdf\xbe\xdb\'\xcb95b\x10!\xe1\xaci\x1e\xa3#\xd3\x00\xe6q\x9f\xb0i\xd3\x8c\xe4\xe4\xf0\xady\xd2z\xfd\xca\x1e\xf0Hx\xd0%\x14\x0c\xb7\xa0\x8d\xde\xa0cuD\x19aa\xd3\x9cI\x19\xbc\xb3\xac\xc5b\x81\x18A\x1e\x9f[\xc9\xb1\x1e\xf7\x81\xa2e\xe8\x9b\xca\x94\xa1\xfe\xec+<\x870\xc0\x1e\x18\xfa\xa9i\xb6a\x82#*3\xf9Z\xa7/\xf8g\xf0d\xbd\xf1T\xa1hxs\xf8\x16\x8b)H\xa3\xcd\xbdh\x0eL\xde\xae\x02p|\xf5@&\x04D\xd3t\x1d\xb7\x97\xa8\x98)\x02\xd7\x19\x1a.\x112\xc2th\xf4\xb07#\x0c\xcaV\x8b\xb0n`\x02B\x85\n\x8c\xcdSb\xe8\nK\x15\x1dL\x1d\x16J\xb1v\x1e\"\xd7A\xa9\xed\xd42\xba\x89\x14\x969\x1cl\xa2y\x84\xd6\xfffn\xae\x8f\xe5\xaci\x9a\x86\xf5T(.\xf1\xd8u:\x1f\xd19\x17\xf0\xbb\xfe\xf3z\xc8!\x0c$\x17x\x9a\x9e;\xf5$\x89\x89\\\xa1e\x03k\xa3T\x01\x8aa\x87J]\xaa\xaa\x98\\D\xc4\x07\xff=\xd0\xa0+\x14\xdd\x05\x17_PRd\xb9$Kl\xe6e\x98\xb8y\x1c\x9b\x1e&\x0cA\xdc\x08j\xa8\x14\xe4\xd7\xaa\x9b\x04\xd1\rT\xc7\xe8\xae\xe1:\x99\xeca\xbc\xb3\x0c\xaazZ\xd3UN\xb2\xc2\xca\xd52\xe2\x1a\xd30\x05U\xc9Z5\x1daD{\xc9Y?\x04Mg)A\xa8w:n\x83(\x08\xb8\x909\xac\xa2P\x1b+\xa7\xe34\x0cA\x86CD\xf1W\xd38#L\x07Luy\x87\xc5|uP\x81\xec\xa03\x1f\x83\xafr\x9b\xbfI{\xc0\x910o\xabT\xb4\x05\x0f\xd2{d\x00\"&\x1e\xfc!\xdew\rt\x1a\x04\xea\xab\xcb\xa9\x0f\xe2\x92c\xf5\x99\x1b\xcd\x98\xc6D\xb1#\xe3\xd1#\xe9\xbd\xa4\xa4\x8dF\xa34\xd8\xb7DR\xf8\xd7\x12\xf6X\xce\xe7<X\t2\x9d\xc9O\x80\xc5\x7f^\xa5\xfd\xb3\x9b\'+T\xdbJfk\xf9u\x1a\x8a\x01H\xa9\xbdT\xb1\xd6\xa0\xfc\x0b\xca\xc7\x98\xb6\xb1\xc4\xf5\xc3\xff\xaeQR]\xaf\x01;\x87\xe5\xb5\xca%aFrc\x03;\xfc0\xb0\x1c\x96$\xdf\xea\n\x80>\xc5+\xa5:U#E_\x9b\xe6.\xe7[&w\xb8nc\x12\xae\xceg\xea*\xd6\x05g\\\xab\xb5\xa9\x8bi\x08\xfb\x18W_\x01\x08I \xcc\x17\xa8\x8aX\xd7Gu#\xcb\xd6.k\xb3w\xd5-b\xbfZ\x83\xec|s\xaag\x90\xeblc\xde\xc3\x7f\xd5x(\xba/vk=\x80\xa2V\xe5zX1\xc4[\xdb\xae\xb5g\xdb\xaa\xd2+\x99*\x8al\xabZ\xd1\xdeB\xb4\x7f46#\xa4h\xab\xdc\xc9\xf5a(kVo\xca\xea.iU\xdf\x11\xaa\x8f\xb5\xb0t@Ck\xc5d\r,\xe1P\xd6\xb8\xe4\xde\xfaB\xda*V\xfb\x1e\x9c\xfd\xe3P\x9e?\xcfT\x11%\xb7\x7f\xbd\x1c\xee\x8d\xa4\xe7\x8b\xc3\x96\xdf\x17\xd3\x17zh\xbd\xd4\xd6P\xd8\x9e\xbe;l+\xff\xa9\xd2\xfa\tPK\x01\x023\x00\x14\x00\x00\x00\x08\x00T\x88VE\xa1\xf9\xe4\xb8\x06\x00\x00\x00\x04\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00___CopyrightYearPK\x01\x023\x00\x14\x00\x00\x00\x08\x00T\x88VEr\xe9\x0e\xe0\t\x00\x00\x00\x07\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x004\x00\x00\x00___ProjectTitlePK\x01\x023\x00\x14\x00\x00\x08\x08\x00\x05\x94\xa9N\x0e\xc5\xcb\xd7\x08\x00\x00\x00\x16\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x00\x00\x00ActivityAssets.lazPK\x01\x023\x00\x14\x00\x00\x08\x08\x00\x05\x94\xa9N\x89\x9fa\x01\xf6\x01\x00\x00\x04\x04\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa2\x00\x00\x00Activity.x3aPK\x01\x023\x00\x14\x00\x00\x08\x08\x00\x05\x94\xa9NHu\xf8\xec\x11\x03\x00\x008\n\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc2\x02\x00\x00Main.ev3pPK\x01\x023\x00\x14\x00\x00\x08\x08\x00\x05\x94\xa9Nv\x8c2j \x03\x00\x00\xc0\x0f\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x05\x00\x00Project.lvprojxPK\x05\x06\x00\x00\x00\x00\x06\x00\x06\x00i\x01\x00\x00G\t\x00\x00\x00\x00")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/LEGO Software/LEGO MINDSTORMS EV3 Home Edition/MindstormsEV3.exe\" {p}index.ev3")
	if (op==True):
		_open_prog_w(type_.title()+"-"+name)



class _WebSocketServer_handle(WebSocket):
	def handleMessage(self):
		threading.Thread(target=self._h_msg,args=(),kwargs={}).start()
	def handleConnected(self):
		pass
	def handleClose(self):
		global SERIAL_L
		self.stop=True
	def _h_msg(self):
		global CMD_L,SERIAL_L
		def _h_std(self):
			global CMD_L
			l={}
			while (self._stop==False):
				for k in list(CMD_L[self.h_nm]["l"].keys()):
					if (k not in l.keys()):
						l[k]=0
					if (l[k]!=len(CMD_L[self.h_nm]["l"][k])):
						self.sendMessage(b"dt:"+CMD_L[self.h_nm]["l"][k][l[k]:])
						l[k]=len(CMD_L[self.h_nm]["l"][k][l[k]:])
				time.sleep(1e-6)
		t,msg=self.data[0],self.data[1:]
		self.sendMessage("null")
		if (t[0]=="0"):
			if (msg=="cmdl"):
				self.sendMessage("cmdl:"+"\x00".join(list(CMD_L.keys())))
			elif (msg[:4]=="cmd:"):
				if (msg[4:] not in list(CMD_L.keys())):
					self.sendMessage("cmd:0")
				else:
					self._stop=True
					self.h_nm=msg[4:]
					self.sendMessage(f"cmd:1{self.h_nm}")
					if (hasattr(self,"_thr")):
						self._thr.join()
					self._stop=False
					self._thr=threading.Thread(target=_h_std,args=(self,),kwargs={})
					self._thr.start()
			elif (msg[:3]=="in:"):
				if (hasattr(self,"h_nm")==False or self.h_nm==None):
					return
				CMD_L[self.h_nm]["h"].stdin.write(bytes(msg[3:],"utf-8"))
				CMD_L[self.h_nm]["h"].stdin.flush()



def _start_s(t):
	def _h_request(cs,a,ip):
		try:
			_dt=cs.recv(65536)
			if (len(_dt)==0):
				_print(f"\x1b[38;2;200;40;20mEmpty Request From '{a[0]}:{a[1]}'.\x1b[0mSkipping\x1b[38;2;100;100;100m..")
				return
			(t,url,v),h,dt=str(_dt.split(b"\r\n")[0],"utf-8").split(" "),{str(e.split(b":")[0],"utf-8"):e[len(e.split(b":")[0])+2:] for e in _dt.split(b"\r\n\r\n")[0].split(b"\r\n")[1:] if len(e)!=0},_dt[len(_dt.split(b"\r\n\r\n")[0])+4:]
			rc=-1
			_print(f"Request Recived: (type='{t}', url='{url}', http_version='{v}', ip='{a[0]}:{a[1]}')")
			if (t=="GET"):
				_print("Inspecting IP and URL\x1b[38;2;100;100;100m...")
				if (len(url)-len(url.replace("/",""))>=2):
					if (url.split("?")[0].split("#")[0].endswith(".php")):
						_print("Sending Request to PHP Server\x1b[38;2;100;100;100m...")
						php_s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						php_s.connect(("127.0.0.1",WORKSPACE_PHP_SERVER_PORT))
						php_s.send(_dt)
						_print("Redirecting Response\x1b[38;2;100;100;100m...")
						php_s=(php_s.recv(65536),php_s.close())[0]
						cs.send(php_s)
						rc=int(php_s.split(b"\r\n")[0].split(b" ")[1])
					else:
						_print("Patching URL\x1b[38;2;100;100;100m...")
						url=re.sub(r"\.+/",r"./",url.replace("\\","/"))
						if (url.endswith("/")):
							url+="index.html"
						if (url=="/serial_ports"):
							_print(f"Sending Serial Port List\x1b[38;2;100;100;100m...")
							cs.send(bytes(f"HTTP/1.1 200 OK\r\nContent-Type: text/json\r\nContent-Length: {len(json.dumps({k:{sk:sv for sk,sv in v.items() if sk not in '_cs,in'.split(',')} for k,v in SERIAL_L.items()}))}\r\n\r\n{json.dumps({k:{sk:sv for sk,sv in v.items() if sk not in '_cs,in'.split(',')} for k,v in SERIAL_L.items()})}","utf-8"))
							rc=200
						else:
							if (url[:10]=="/projects/"):
								url=f"D:\\K\\Coding\\.{url}"
							else:
								url=f".{url}"
							if (ntpath.isdir(url)):
								url+="/index.html"
							if (not ntpath.exists(url)):
								_print(f"\x1b[38;2;200;40;20mFile '{ntpath.abspath(url)}' Doesn't Exist.\x1b[0m Sending Redirect\x1b[38;2;100;100;100m...")
								cs.send(bytes(f"HTTP/1.1 301 Moved Permanently\r\nLocation: http://{ip}:8020/\r\n\r\n","utf-8"))
								rc=301
							else:
								mt=("text/plain" if url.split("?")[0].split("#")[0].split(".")[-1] not in list(MIME_TYPES.keys()) else MIME_TYPES[url.split("?")[0].split("#")[0].split(".")[-1]])
								_print(f"Sending Content of '{ntpath.abspath(url)}' as '{mt}'\x1b[38;2;100;100;100m...")
								f=open(ntpath.abspath(url),"rb")
								cs.send(bytes(f"HTTP/1.1 200 OK\r\nContent-Type: {mt}\r\nContent-Length: {str(os.fstat(f.fileno())[6])}\r\n\r\n","utf-8")+f.read())
								f.close()
								rc=200
				else:
					_print(f"\x1b[38;2;200;40;20mUnauthorised Request From '{a[0]}:{a[1]}'\x1b[38;2;200;40;20m for URL '{url}'\x1b[38;2;200;40;20m.\x1b[0m Discarding Request\x1b[38;2;100;100;100m...")
					cs.send(bytes(f"HTTP/1.1 401 Unauthorised\r\nContent-Type: text/html\r\nContent-Length: 0\r\n\r\n","utf-8"))
					rc=401
			elif (t=="PUT" and url=="/serial_ports"):
				dt=json.loads(dt)
				if (dt["op"]=="create"):
					_print(f"Starting Serial Reader on Port '{dt['port']}'\x1b[38;2;100;100;100m..")
					if (dt["port"] not in SERIAL_L.keys()):
						SERIAL_L[dt["port"]]={"cnt":1,"port":None,"in":[],"_cs":[]}
						_start_thr(_start_ser,"__core__",f"serial_reader_{dt['port'].lower()}",dt["port"])
					else:
						SERIAL_L[dt["port"]]["cnt"]+=1
					while (SERIAL_L[dt["port"]]["port"]==None):
						pass
					cs.send(bytes(f"HTTP/1.1 200 OK\r\nContent-Type: text/json\r\nContent-Length: {len(json.dumps({k:v for k,v in SERIAL_L[dt['port']].items() if k!='_cs'}))}\r\n\r\n{json.dumps({k:v for k,v in SERIAL_L[dt['port']].items() if k not in '_cs,in'.split(',')})}","utf-8"))
				else:
					_print(f"Stopping Serial Reader on Port '{dt['port']}'\x1b[38;2;100;100;100m..")
					SERIAL_L[dt["port"]]["cnt"]-=1
					cs.send(bytes("HTTP/1.1 200 OK\r\nContent-Type: text/json\r\nContent-Length: 2\r\n\r\n{}","utf-8"))
				rc=200
			else:
				_print(f"\x1b[38;2;200;40;20mUnimplemented Method '{t}'\x1b[38;2;200;40;20m Recived From '{a[0]}:{a[1]}'\x1b[38;2;200;40;20m for URL '{url}'\x1b[38;2;200;40;20m.\x1b[0m Discarding Request\x1b[38;2;100;100;100m...")
				cs.send(b"HTTP/1.1 501 Not Implemented\r\n\r\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\"><title>Error</title></head><body><h1>501</h1><h3>Not Implemented</h3></body></html>")
				rc=501
			_print(f"Finished Processing Request with Response Code {rc}.")
		except Exception as e:
			_print("\x1b[38;2;200;40;20mError Occured During Procesing of Request.\x1b[0m (Finished Processing Request with Response Code 500)")
			cs.send(b"HTTP/1.1 500 Internal Server Error\r\n\r\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\"><title>Error</title></head><body><h1>500</h1><h3>Internal Server Error</h3></body></html>")
			traceback.print_exception(None,e,e.__traceback__)
		cs.close()
	def _r_std_h(cs):
		threading.current_thread()._df=True
		bf=b""
		while (True):
			bf+=cs.recv(1024)
			if (b"\n" in bf):
				dt,bf=base64.b64decode(bf.split(b"\n")[0]),b"\n".join(bf.split(b"\n")[1:])
				threading.current_thread()._b_nm,threading.current_thread()._nm=str(dt,"utf-8").split("\x00")[:2]
				_print(str(dt[len(b" ".join(dt.split(b"\x00")[:2]))+1:],"utf-8"))
	if (t==0):
		_print(f"Starting WebSocket Listener on IP '127.0.0.1:8021'\x1b[38;2;100;100;100m...")
		ws_s=SimpleWebSocketServer("127.0.0.1",8021,_WebSocketServer_handle).serveforever()
	if (t==1):
		global WORKSPACE_PHP_PID
		_print(f"Starting PHP Server on IP '127.0.0.1:{WORKSPACE_PHP_SERVER_PORT}'\x1b[38;2;100;100;100m...")
		p=subprocess.Popen(["C:/Program Files/PHP/php.exe","-S",f"127.0.0.1:{WORKSPACE_PHP_SERVER_PORT}"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd="D:\\K\\Coding\\")
		WORKSPACE_PHP_PID=p.pid
		_r_cmd("php_server",lambda:None,p)
	elif (t==2):
		_print("Starting Remote Std Listener on '127.0.0.1:8022'\x1b[38;2;100;100;100m...")
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind(("127.0.0.1",8022))
		s.listen(5)
		while (True):
			threading.Thread(target=_r_std_h,args=(s.accept()[0],),kwargs={}).start()
		s.close()
	else:
		_print(f"Starting Server on IP '{('localhost' if t==3 else '127.0.0.1')}:8020'\x1b[38;2;100;100;100m...")
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind((("localhost" if t==3 else "127.0.0.1"),8020))
		s.listen(5)
		while (True):
			_h_request(*s.accept(),("localhost" if t==3 else "127.0.0.1"))
		s.close()



def _net_loop():
	global NETWORK
	_print("Starting Internet Status Loop\x1b[38;2;100;100;100m...")
	while (True):
		try:
			socket.socket(socket.AF_INET,socket.SOCK_STREAM).connect(("8.8.8.8",53))
			if (NETWORK==False):
				NETWORK=True
				_print("Internet Connection Found\x1b[38;2;100;100;100m...")
		except socket.error:
			if (NETWORK==True):
				NETWORK=False
				_print("Internet Connection Lost\x1b[38;2;100;100;100m...")
		time.sleep(30)



def _u_mcs(fp):
	_print(f"Starting Minecraft Server in Folder '{fp}'\x1b[38;2;100;100;100m...")
	if (not ntpath.exists(fp)):
		_print("\x1b[38;2;200;40;20mMinecraft Server Folder Missing.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		return
	_print("Downloading Metadata\x1b[38;2;100;100;100m...")
	json=requests.get(requests.get("https://launchermeta.mojang.com/mc/game/version_manifest.json").json()["versions"][0]["url"]).json()
	if (ntpath.exists(f"{fp}\\server.jar")):
		_print("Inspecting Current Version\x1b[38;2;100;100;100m...")
		h=hashlib.sha1()
		with open(f"{fp}\\server.jar","rb") as f:
			fb=f.read(2**16)
			while (len(fb)>0):
				h.update(fb)
				fb=f.read(2**16)
		_print(f"File Hash: {h.hexdigest()}, New Hash: {json['downloads']['server']['sha1']}")
		if (h.hexdigest()!=json["downloads"]["server"]["sha1"]):
			_print(f"Downloading Server For {json['id']}\x1b[38;2;100;100;100m...")
			urllib.request.urlretrieve(json["downloads"]["server"]["url"],f"{fp}\\server.jar")
	else:
		urllib.request.urlretrieve(json["downloads"]["server"]["url"],f"{fp}\\server.jar")
	_print("Starting Server\x1b[38;2;100;100;100m...")
	p=subprocess.Popen(["java","-Xms4G","-Xmx4G","-jar","server.jar","--nogui"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd=fp)
	_r_cmd(fp[fp.replace("/","\\").rfind("\\")+1:],lambda:(p.stdin.write(b"stop\n"),p.stdin.flush(),p.wait()),p)



def _end(a):
	global CMD_L
	print("Stopping all Servers\x1b[38;2;100;100;100m...")
	for v in list(CMD_L.values())[:]:
		v["_end"]()
	subprocess.Popen(["C:\\Windows\\System32\\shutdown.exe"]+a+["/f"])



if (len(sys.argv)==1):
	os.system("cls")
	ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),ctypes.wintypes.DWORD(7))
	CMD_L["__core__"]={"_end":lambda:None,"h":type("VoidHandle",(object,),{"stdin":io.StringIO}),"l":{"__main__":b""}}
	threading.current_thread()._b_nm="__core__"
	threading.current_thread()._nm="__main__"
	_print("Starting Boot Sequence\x1b[38;2;100;100;100m...\x1b[0m")
	_print("Starting Arduino Cache\x1b[38;2;100;100;100m...")
	_Arduino_Cache.init()
	_print("Starting Internet Status Loop\x1b[38;2;100;100;100m...")
	_start_thr(_net_loop,"__core__","network_status_loop")
	_print("Registering Keyboard Hotkeys\x1b[38;2;100;100;100m...")
	keyboard.add_hotkey("ctrl+alt+shift+z",lambda:_open_app("C:\\Windows\\System32\\charmap.exe"))
	keyboard.add_hotkey("ctrl+alt+shift+e",lambda:_open_app("C:\\Windows\\System32\\control.exe"))
	keyboard.add_hotkey("ctrl+alt+shift+c",lambda:_open_app(["python","D:\\boot\\boot.py","0"]))
	keyboard.add_hotkey("ctrl+alt+shift+q",lambda:_open_app(["python","D:\\boot\\boot.py","1"]))
	keyboard.add_hotkey("ctrl+alt+shift+a",lambda:_open_app("D:\\K",file=True))
	keyboard.add_hotkey("ctrl+alt+shift+r",lambda:_open_app(["javaw","-jar","D:\\boot\\ScreenBlocker.jar"]))
	keyboard.add_hotkey("ctrl+alt+shift+home",lambda:_end(["/l"]))
	keyboard.add_hotkey("ctrl+alt+shift+end",lambda:_end(["/s","/t","0"]))
	keyboard.add_hotkey("ctrl+alt+shift+w",lambda:_open_app("D:\\boot",file=True))
	keyboard.add_hotkey("ctrl+alt+shift+d",lambda:_open_app("C:\\Windows\\System32\\Taskmgr.exe"))
	keyboard.add_hotkey("ctrl+alt+shift+v",lambda:_open_app(["python","D:\\boot\\boot.py","2"]))
	_print("Starting Minecraft Server\x1b[38;2;100;100;100m...")
	_start_thr(_u_mcs,"__core__","minecraft_server_updater","D:\\boot\\mcs")
	_print("Registering All Projects\x1b[38;2;100;100;100m...")
	for k in os.listdir("D:\\K\\Coding"):
		_create_prog(k.split("-")[0],k[len(k.split("-")[0])+1:],op=False,pr=False)
	_print("Starting Github Project Push Check\x1b[38;2;100;100;100m...")
	_start_thr(_git_project_push,"__core__","github_project_push")
	_print("Starting WebSocket CMD Server\x1b[38;2;100;100;100m...")
	_start_thr(_start_s,"__core__","cmdline_websocket_server",0)
	_print("Starting PHP Server\x1b[38;2;100;100;100m...")
	_start_thr(_start_s,"__core__","php_server",1)
	_print(f"Startint Remote Std Listener\x1b[38;2;100;100;100m...")
	_start_thr(_start_s,"__core__","remote_std_server",2)
	_print("Starting Localhost Server\x1b[38;2;100;100;100m...")
	_start_thr(_start_s,"__core__","localhost_server",3)
	_print("Starting Local IP Server\x1b[38;2;100;100;100m...")
	_start_thr(_start_s,"__core__","local_ip_server",4)
	_print("Starting Infinite Loop\x1b[38;2;100;100;100m...")
	try:
		while (True):
			time.sleep(1e-6)
	except:
		pass
	os.system(f"taskkill /pid {os.getpid()} /f")
else:
	v=int(sys.argv[1])
	if (v==0):
		threading.current_thread()._b_nm="__core__"
		threading.current_thread()._nm="__core__"
		threading.current_thread()._r=2
		threading.current_thread()._dpt=True
		threading.current_thread()._dp=True
		_print("Starting Prettifying in Directory 'D:\\'\x1b[38;2;100;100;100m...")
		threading.current_thread()._df=True
		threading.current_thread()._r=0
		for fn in glob.iglob("D:\\**\\*.json",recursive=True):
			try:
				_print(fn)
				data={}
				with open(fn,"r") as f:
					data=json.loads(f.read())
				_save_f(fn,json.dumps(data,indent=4,sort_keys=True).replace("    ","\t"))
			except:
				_print("SKIPPING: "+fn)
		for fn in glob.iglob("D:\\**\\*.java",recursive=True):
			try:
				with open(fn,"r") as f:
					txt=f.read().split("\n")
				i=0
				imp=[]
				imps=[]
				sl=-1
				ch=False
				_print(fn)
				while (i<len(txt)):
					if (txt[i]=="" or txt[i][0]=="\t" or txt[i][0]==" "  or txt[i].startswith("//") or txt[i].startswith("/*") or txt[i].startswith("*/")):
						i+=1
						continue
					ln=txt[i]
					if (ln.startswith("package ")):
						p=ln.replace("package ","")[:-1].split(".")
						if (p.count("krzem")>0):
							rp=fn[fn.index("com\\krzem\\")+len("com\\krzem\\"):fn.rfind("\\")].replace("\\",".")
							if (".".join(p[2:])!=rp):
								txt[i]=f"package com.krzem.{rp};\n\n\n"
								ch=True
								sl=1
						pass
					elif (ln.startswith("import static ")):
						if (sl==-1):
							sl=i+0
						imps+=[ln]
					elif (ln.startswith("import ")):
						if (sl==-1):
							sl=i+0
						imp+=[ln]
					else:
						break
					i+=1
				if (len(imp)==0 and len(imps)==0 and ch==False):
					continue
				imp.sort()
				imps.sort()
				txt=txt[:sl]+imp+imps+(["","",""] if len(imp)+len(imps)>0 else [])+txt[i:]
				_save_f(fn,"\n".join(txt))
			except:
				_print("SKIPPING: "+fn)
		for fn in glob.iglob("D:\\**\\*.py",recursive=True):
			try:
				with open(fn,"r") as f:
					txt=f.read().split("\n")
				i=0
				imp=[]
				sl=-1
				_print(fn)
				while (i<len(txt)):
					if (txt[i]==""):
						i+=1
						continue
					ln=txt[i]
					if (ln.startswith("#")):
						pass
					if (ln.startswith("from ") or ln.startswith("import ")):
						if (sl==-1):
							sl=i+0
						imp+=[ln]
					else:
						break
					i+=1
				if (len(imp)==0):
					continue
				imp.sort()
				cimp=[]
				for k in imp:
					if (k.startswith("from")):
						k=k.replace("import*","import *").replace(", ",",").replace(",",", ")
						cimp+=[k]
					else:
						for m in k.replace("import ","").split(","):
							cimp+=["import "+m.strip()]
				txt=txt[:sl]+cimp+["","",""]+txt[i:]
				_save_f(fn,"\n".join(txt))
			except:
				_print("SKIPPING: "+fn)
		threading.current_thread()._df=False
		_rec_rm_pycache("D:\\")
	elif (v==1):
		while (True):
			p=input("> ").lower().strip()
			if (p=="list"):
				os.system("cls")
				_print("list, chrome, python, python37, processing, mindstorm, fischer, sublime, minecraft, vm, android, github, blender, scratch, print, serial, cad, ev3, <any file path>, <git clone url>, <any url>")
				continue
			elif (p=="chrome"):
				_open_app("C:\\Program Files\\Google\\Chrome Dev\\Application\\chrome.exe")
			elif (p=="python"):
				_open_app(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python38\\python.exe")
			elif (p=="python37"):
				_open_app(f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Programs\\Python\\Python37\\python.exe")
			elif (p=="processing"):
				_open_app("C:\\Program Files\\Processing\\processing.exe")
			elif (p=="mindstorm"):
				_open_app("C:\\Program Files\\LEGO Software\\LEGO MINDSTORMS EV3 Home Edition\\MindstormsEV3.exe")
			elif (p=="fischer"):
				_open_app("C:\\Program Files\\ROBOPro\\ROBOPro.exe")
			elif (p=="sublime"):
				_open_app("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
			elif (p=="minecraft"):
				_open_app("C:\\Program Files (x86)\\Minecraft Launcher\\MinecraftLauncher.exe")
			elif (p=="vm"):
				_open_app("C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe")
			elif (p=="android"):
				_open_app("C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe")
			elif (p=="github"):
				_open_app("C:\\Users\\aleks\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe")
			elif (p=="blender"):
				_open_app("C:\\Program Files\\Blender Foundation\\Blender\\blender.exe")
			elif (p=="scratch"):
				os.system("start \"\" \"C:\\Program Files\\Scratch Desktop\\Scratch Desktop.exe\"")
			elif (p=="print"):
				_open_app("C:\\Program Files\\RepetierGEEEtech\\RepetierHost.exe")
			elif (p=="work"):
				_open_app(["python","D:\\boot\\boot.py","2"])
			elif (p=="serial"):
				_open_app(["python","D:\\boot\\boot.py","3"])
			elif (p=="docs"):
				_open_app(["C:\\Program Files\\Google\\Chrome Dev\\Application\\chrome_proxy.exe","--profile-directory=Default","--app-id=ahiigpfcghkbjfcibpojancebdfjmoop"])
			elif (p=="cad"):
				_open_app("C:\\Program Files\\CAD\\FreeCAD 0.18\\bin\\FreeCAD.exe")
			elif (p=="ev3"):
				_open_app("C:\\Program Files\\PuTTY\\putty.exe")
			elif (ntpath.exists(p)):
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
		ctypes.windll.kernel32.GetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),ctypes.byref(out_cm))
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		ho=ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.create_string_buffer(22)
		ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ho,sbi)
		sz=struct.unpack("hhhhHhhhhhh",sbi.raw)
		ci=ctypes.create_string_buffer(5)
		ctypes.windll.kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		try:
			ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sz[0]*sz[1],ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sz[0]*sz[1],ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
			ctypes.windll.kernel32.SetConsoleCursorInfo(ho,ctypes.byref(ctypes.create_string_buffer(ci.raw[:4]+b"\x00")))
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
			w=sz[9]+1
			h=sz[10]
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
					ln=len(re.sub(r"\x1b\[[^m]*m","",o).replace("\n"," "*(sz[9]+1)))
					sys.__stdout__.write(f"\x1b[0;0H{o+(' '*(ll-ln) if ll>ln else '')}\x1b[0m")
					sys.__stdout__.flush()
					ll=ln
					u=False
				time.sleep(0.01)
			ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sz[0]*sz[1],ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sz[0]*sz[1],ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
		except Exception as e:
			traceback.print_exception(None,e,e.__traceback__)
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),inp_cm)
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),out_cm)
		ctypes.windll.kernel32.SetConsoleCursorInfo(ho,ctypes.byref(ci))
		ctypes.windll.kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(*sz[:2]))
		ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(ctypes.wintypes.SMALL_RECT(*sz[5:9])))
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
				self._p_dt=None
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
				self._r_bf=""
				self._cl_cache=[]
				self._dl=[]
			def loop(self):
				def _cmp(a,b):
					return (0 if a==b else (-1 if a<b else 1))
				while (True):
					self._o=[f"\x1b[0m\x1b[48;2;24;24;24m{' '*(self._sz[0]-1)}",f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ╔{'═'*(self._sz[0]-9)}╗   ",*(f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ║{' '*(self._sz[0]-9)}\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m║   ",)*(self._sz[1]-5),f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m   ╚{'═'*(self._sz[0]-9)}╝   ",f"\x1b[0m\x1b[48;2;24;24;24m\x1b[38;2;92;92;92m{' '*(self._sz[0]-1)}"]
					if (msvcrt.kbhit()==True):
						k=msvcrt.getch()
						if (k==b"\x03"):
							if (self._m==0):
								break
							elif (self._m==1):
								self._p_s.close()
								s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
								s.connect(("127.0.0.1",8020))
								s.send(bytes(f"PUT /serial_ports HTTP/1.1\r\n\r\n{json.dumps({'port':self._p['location'],'op':'delete'})}","utf-8"))
								s.recv(65536)
								s.close()
								self._m=0
								self._t=0
								self._pl=None
								self._pi=0
								self._p=None
								self._p_dt=None
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
								self._r_bf=""
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
						elif (self._k[0]==b"\xe0" and self._k[1]==b"H"):
							self._pi=((self._pi-1)+len(self._pl))%len(self._pl)
						elif (self._k[0]==b"\xe0" and self._k[1]==b"P"):
							self._pi=(self._pi+1)%len(self._pl)
						elif (self._k[0]==b"\r"):
							if (len(self._pl)>0):
								self._p=self._pl[self._pi]
								s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
								s.connect(("127.0.0.1",8020))
								s.send(bytes(f"PUT /serial_ports HTTP/1.1\r\n\r\n{json.dumps({'port':self._p['location'],'op':'create'})}","utf-8"))
								dt=str(s.recv(65536),"utf-8")
								s.close()
								self._p_dt=json.loads(dt[len(dt.split("\r\n\r\n")[0])+4:])
								self._p_s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
								self._p_s.connect(tuple(self._p_dt["port"]))
								self._p_thr=threading.Thread(target=self._thr,args=(),kwargs={})
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
							self._p_s.sendall(bytes(self._inp_bf,"utf-8"))
							self._inp_bf=""
							self._off[1]=0
							n_dt=True
							inp_ch=True
						elif (self._k[0]==b"\xe0" and self._k[1]==b"\x8d"):
							self._a_s=False
							self._off[0]=max(0,self._off[0]-1)
						elif (self._k[0]==b"\xe0" and self._k[1]==b"\x91"):
							self._off[0]+=1
							if (self._off[0]>=sum([len(e[1])-(1 if None in e else 0) for e in self._dt])):
								self._a_s=True
								self._off[0]=sum([len(e[1])-(1 if None in e else 0) for e in self._dt])
						elif (self._k[0]==b"\xe0" and self._k[1]==b"w"):
							self._a_s=False
							self._off[0]=0
						elif (self._k[0]==b"\xe0" and self._k[1]==b"u"):
							self._a_s=True
							self._off[0]=sum([len(e[1])-(1 if None in e else 0) for e in self._dt])
						elif (self._k[0]==b"\xe0" and self._k[1]==b"H"):
							if (self._mem_i!=0):
								inp_ch=True
							self._mem_i=max(0,self._mem_i-1)
							self._inp_bf=self._mem[self._mem_i]
							self._off[1]=len(self._inp_bf)
							inp_ch=True
						elif (self._k[0]==b"\xe0" and self._k[1]==b"P"):
							if (self._mem_i!=len(self._mem)-1):
								inp_ch=True
							self._mem_i=min(len(self._mem)-1,self._mem_i+1)
							self._inp_bf=self._mem[self._mem_i]
							self._off[1]=len(self._inp_bf)
						elif (self._k[0]==b"\xe0" and self._k[1]==b"K"):
							if (self._off[1]!=0):
								inp_ch=True
							self._off[1]=max(0,self._off[1]-1)
						elif (self._k[0]==b"\xe0" and self._k[1]==b"M"):
							if (self._off[1]!=len(self._inp_bf)):
								inp_ch=True
							self._off[1]=min(self._off[1]+1,len(self._inp_bf))
						elif (self._k[0]==b"\xe0" and self._k[1]==b"G"):
							if (self._off[1]!=0):
								inp_ch=True
							self._off[1]=0
						elif (self._k[0]==b"\xe0" and self._k[1]==b"O"):
							if (self._off[1]!=len(self._inp_bf)):
								inp_ch=True
							self._off[1]=len(self._inp_bf)
						elif (self._k[0]==b"\xe0" and self._k[1]==b"S"):
							t=self._inp_bf+""
							self._inp_bf=self._inp_bf[:self._off[1]]+self._inp_bf[self._off[1]+1:]
							if (t!=self._inp_bf):
								inp_ch=True
						elif (self._k[0]==b"\b"):
							t=self._inp_bf
							self._inp_bf=self._inp_bf[:max(self._off[1]-1,0)]+self._inp_bf[self._off[1]:]
							self._off[1]=max(self._off[1]-1,0)
							if (t!=self._inp_bf):
								inp_ch=True
						elif (self._k[0]==b"\x0c"):
							self._dt=[]
						elif (self._k[0]==b"\x14"):
							self._t=1-self._t
						elif (self._k[0]==b"\xe0"):
							raise RuntimeError(f"Ignoring Special Key {self._k[1]}...")
						elif (len(self._k[0])==1 and self._k[0] not in list(b"\x0a\x13")):
							self._inp_bf=self._inp_bf[:self._off[1]]+repr(self._k[0])[2:-1]+self._inp_bf[self._off[1]:]
							self._off[1]+=len(repr(self._k[0])[2:-1])
							inp_ch=True
						if (len(self._r_bf)>0):
							self._r_bf,t="",self._r_bf
							self._extend(0,re.sub(r"\r(\n|$)",r"\1",str(t,"utf-8")).replace("\t","    "))
							n_dt=True
						if (self._a_s==True and n_dt==True):
							self._dt=self._dt[-1000:]
							self._off[0]=max(0,sum([len(e[1])-(1 if None in e[1] else 0) for e in self._dt])-(self._sz[1]-9))
						if (inp_ch==False and self._b_tm<time.time()):
							self._b=not self._b
							self._b_tm=time.time()+0.65
						elif (inp_ch==True):
							self._b=True
							self._b_tm=time.time()+0.65
						if (self._nm_d_tm==-1):
							self._nm_d_tm=time.time()+2
						elif (self._nm_d_tm<time.time()):
							self._nm_d=not self._nm_d
							self._nm_d_tm=time.time()+2
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
									# ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏
									#
									# ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟
									#
									# ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯
									#
									# ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ ┽ ┾ ┿
									#
									# ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏
									#
									# ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟
									#
									# ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ ╭ ╮ ╯
									#
									# ╰ ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿
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
					sys.__stdout__.write("\x1b[0;0H"+"\n".join(self._o)+"\x1b[0m")
					time.sleep(0.01)
			def _thr(self):
				while (self._p_s!=None):
					self._r_bf+=self._p_s.recv(4096)
			def _draw_table(self,nm,d,s=-1):
				mw=self._sz[0]-11
				mx_l=[max([len(nm[list(nm.keys())[i]][0])]+[len(e[k]) for e in d])+2 for i,k in enumerate(list(nm.keys()))]
				off=((self._sz[0]-9-(sum(mx_l)+len(list(nm.keys()))+1))//2,3)
				self._set(off[0],off[1],"\x1b[38;2;156;156;156m┌"+"┬".join(["─"*mx_l[i] for i in range(0,len(mx_l))])+"┐")
				self._set(off[0],off[1]+1,"\x1b[38;2;156;156;156m|"+"\x1b[38;2;156;156;156m│".join([f"\x1b[38;2;{min(255,int(nm[e][1][1:3],16)+65)};{min(255,int(nm[e][1][3:5],16)+65)};{min(255,int(nm[e][1][5:7],16)+65)}m"+nm[e][0].center(mx_l[i]," ") for i,e in enumerate(list(nm.keys()))])+"\x1b[38;2;156;156;156m│")
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
		threading.current_thread()._b_nm="__core__"
		threading.current_thread()._nm="arduino_serial_terminal"
		threading.current_thread()._r=2
		_Arduino_Cache.init()
		inp_cm=ctypes.wintypes.DWORD(0)
		ctypes.windll.kernel32.GetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),ctypes.byref(inp_cm))
		out_cm=ctypes.wintypes.DWORD(0)
		ctypes.windll.kernel32.GetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),ctypes.byref(out_cm))
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),ctypes.wintypes.DWORD(0x80))
		ho=ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.SetConsoleMode(ho,ctypes.wintypes.DWORD(7))
		sbi=ctypes.create_string_buffer(22)
		ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ho,sbi)
		sz=struct.unpack("hhhhHhhhhhh",sbi.raw)
		ci=ctypes.create_string_buffer(5)
		ctypes.windll.kernel32.GetConsoleCursorInfo(ho,ctypes.byref(ci))
		ui=_UI((sz[9]+1,sz[10]))
		try:
			# ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(ctypes.wintypes.SMALL_RECT(*sz[5:9])))
			# ctypes.windll.kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(sz[9],sz[10]-1))
			# ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(ctypes.wintypes.SMALL_RECT(*sz[5:9])))
			ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sz[0]*sz[1],ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sz[0]*sz[1],ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
			ctypes.windll.kernel32.SetConsoleCursorInfo(ho,ctypes.byref(ctypes.create_string_buffer(ci.raw[:4]+b"\x00")))
			ui.loop()
			# ctypes.windll.kernel32.FillConsoleOutputCharacterA(ho,ctypes.c_char(b" "),sz[0]*sz[1],ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			# ctypes.windll.kernel32.FillConsoleOutputAttribute(ho,7,sz[0]*sz[1],ctypes.wintypes._COORD(0,0),ctypes.byref(ctypes.wintypes.DWORD()))
			# ctypes.windll.kernel32.SetConsoleCursorPosition(ho,ctypes.wintypes._COORD(0,0))
		except Exception as e:
			traceback.print_exception(None,e,e.__traceback__)
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-10),inp_cm)
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),out_cm)
		ctypes.windll.kernel32.SetConsoleCursorInfo(ho,ctypes.byref(ci))
		ctypes.windll.kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(*sz[:2]))
		ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(ctypes.wintypes.SMALL_RECT(*sz[5:9])))
		if (ui._p!=None):
			ui._p_s.close()
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect(("127.0.0.1",8020))
			s.send(bytes(f"PUT /serial_ports HTTP/1.1\r\n\r\n{json.dumps({'port':ui._p['location'],'op':'delete'})}","utf-8"))
			s.recv(65536)
			s.close()
	elif (v==4):
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),ctypes.wintypes.DWORD(7))
		if (len(sys.argv)==2):
			threading.current_thread()._b_nm="__core__"
			threading.current_thread()._nm="github_project_push_remote"
			threading.current_thread()._dpt=True
			threading.current_thread()._r=2
			_start_thr(_net_loop,"__core__","github_project_push_remote_network_loop")
			_git_project_push(r=True)
		else:
			if (sys.argv[2]=="*"):
				threading.current_thread()._b_nm="__core__"
				threading.current_thread()._nm="github_project_push_all"
				threading.current_thread()._dpt=True
				threading.current_thread()._r=2
				_start_thr(_net_loop,"__core__","github_project_push_all_network_loop")
				_git_project_push(r=True,fr=True)
			else:
				threading.current_thread()._b_nm="__core__"
				threading.current_thread()._nm="github_project_push_single"
				threading.current_thread()._dpt=True
				threading.current_thread()._r=2
				nm=(re.sub(r"[^A-Za-z0-9_.-]","",sys.argv[2].replace("D:\\K\\Coding\\","").split("\\")[0]) if sys.argv[2].lower().startswith("d:\\k") else "Boot_Program")
				dc=("None" if sys.argv[2].lower().startswith("d:\\k") else "'Boot Program'")
				msg=datetime.datetime.now().strftime('Push Update %m/%d/%Y, %H:%M:%S')
				_print(f"Pushing Project to Github: (path='{sys.argv[2]}', name='{nm}', desc={dc}, commit_message='{msg}')")
				threading.current_thread()._dp=True
				threading.current_thread()._df=True
				threading.current_thread()._r=1
				_update_repo(sys.argv[2],(re.sub(r"[^A-Za-z0-9_.-]","",sys.argv[2].lower().replace("d:\\k\\coding\\","").split("\\")[0]) if sys.argv[2].lower().startswith("d:\\k") else "Boot_Program"),msg)
				input("\x1b[38;2;50;50;50m<ENTER>\x1b[0m")
	elif (v==5):
		threading.current_thread()._b_nm="__core__"
		threading.current_thread()._nm="arduino_runner"
		threading.current_thread()._dpt=True
		threading.current_thread()._dp=True
		threading.current_thread()._r=1
		if (not ntpath.exists(f"D:/boot/arduino")):
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
			o=f"┌{'─'*mx_l[0]}┬{'─'*mx_l[1]}┬{'─'*mx_l[2]}┬{'─'*mx_l[3]}┐\n│{'Name'.center(mx_l[0])}│{'FQBN'.center(mx_l[1])}|{'Arch'.center(mx_l[2])}|{'Location'.center(mx_l[3])}│\n├{'─'*mx_l[0]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[1]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[2]}{('┴' if len(bl)==0 else '┼')}{'─'*mx_l[3]}┤"
			for k in bl:
				o+=f"\n|{k['name'].center(mx_l[0])}│{k['fqbn'].center(mx_l[1])}│{k['arch'].center(mx_l[2])}│{k['location'].center(mx_l[3])}|"
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
			if (len(sys.argv)<5):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			_compile_ard_prog(sys.argv[3],sys.argv[4],sys.argv[5:])
		elif (sys.argv[2]=="upload"):
			if (len(sys.argv)<6):
				_print("\x1b[38;2;200;40;20mNot enought Arguments.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
				sys.exit(1)
			_upload_to_ard(sys.argv[3],sys.argv[4],sys.argv[5],(True if "--burn-bootloader" in sys.argv[6:] else False),(True if "--verify" in sys.argv[6:] else False),[e for e in sys.argv[6:] if e not in ["--burn-bootloader","--verify"]])
		else:
			_print(f"\x1b[38;2;200;40;20mUnknown Switch '{sys.argv[2]}'.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
			sys.exit(1)

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from SimpleWebSocketServer import SimpleWebSocketServer,WebSocket
from PIL import Image
import keyboard
import socket
import subprocess
import os
import inspect
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



os.system("title  ")
with open("D:\\boot\\secret.dt","r") as f:
	f=f.read()



global BLK_PID,KB_PID,WORKSPACE_DATA,WORKSPACE_PHP_PID,SWAP_DATA,CMD_L,STDOUT_LOCK
STDOUT_LOCK=False
CMD_L={}
KB_PID=-1
BLK_PID=-1
WORKSPACE_DATA=[]
LOCAL_IP="127.0.0.1"
WORKSPACE_IP_WHITELIST=[LOCAL_IP]
WORKSPACE_PHP_SERVER_PORT=random.randint(9001,49151)
WORKSPACE_WORKSPACE_PHP_PID=""
GIT_CLONE_REGEX=re.compile(r"^([A-Za-z0-9]+@|http(|s)\:\/\/)([A-Za-z0-9.]+(:\d+)?)(?::|\/)([\d\/\w.-]+?)\.git$")
CODEWARS_KATA_URL_REGEX=re.compile(r"^(?:https?://)?www\.codewars\.com/kata/([0-9a-f]{24})(/.*)?$")
URL_REGEX=re.compile(r"^(?:(?:https?|ftp)://)(?:\S+(?::\S*)?@)?(?:(?!10(?:\.\d{1,3}){3})(?!127(?:\.\d{1,3}){3})(?!169\.254(?:\.\d{1,3}){2})(?!192\.168(?:\.\d{1,3}){2})(?!172\.(?:1[6-9]|2\d|3[0-1])(?:\.\d{1,3}){2})(?:[1-9]\d?|1\d\d|2[01]\d|22[0-3])(?:\.(?:1?\d{1,2}|2[0-4]\d|25[0-5])){2}(?:\.(?:[1-9]\d?|1\d\d|2[0-4]\d|25[0-4]))|(?:(?:[a-z\u00a1\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)(?:\.(?:[a-z\u00a1-\uffff0-9]+-?)*[a-z\u00a1-\uffff0-9]+)*(?:\.(?:[a-z\u00a1-\xffff]{2,})))(?::\d{2,5})?(?:/[^\s]*)?$",re.I|re.S)
SWAP_DATA=[]
SWAP_FILE_NAME="D:\\boot\\codewars-swapfile.dt"
CODEWARS_SIGNIN_URL="https://www.codewars.com/users/sign_in"
CODEWARS_SIGNIN_EMAIL_XPATH="/html/body/div[1]/div[1]/main/div[2]/form/div[2]/div/div/div/input"
CODEWARS_SIGNIN_PASSWORD_XPATH="/html/body/div[1]/div[1]/main/div[2]/form/div[3]/div/div/div/input"
CODEWARS_SIGNIN_LOGIN_BUTTON_XPATH="/html/body/div[1]/div[1]/main/div[2]/form/button"
USER_EMAIL,USER_PASSWORD,GITHUB_TOKEN=f.replace("\r","").split("\n")[:3]
CODEWARS_DASHBOARD_URL="https://www.codewars.com/dashboard"
KATA_METADATA_URL="https://www.codewars.com/kata/%s"
KATA_METADATA_LANGUAGE_LIST_CONTAINER_XPATH="/html/body/div[1]/div[1]/main/div[3]/div/div[2]/div/div[1]/div/div/dl"
KATA_METADATA_NAME_XPATH="/html/body/div[1]/div[1]/main/div[3]/div/div[1]/div[1]/h4"
KATA_LANGUAGES="python javascript java php cpp bf nasm powershell shell".split(" ")
KATA_SETUP_URL="https://www.codewars.com/kata/%s/train/%s"
KATA_SETUP_SOLUTION_CONTAINER_ID=1
KATA_SETUP_FIXTURE_TESTS_CONTAINER_ID=2
KATA_SETUP_CODEMIRROR_CONTAINER_XPATH="/html/body/div[1]/div[1]/main/div[3]/view/div[2]/div[2]/div[2]/div/div[%d]"
KATA_SETUP_CODEMIRROR_CONTAINER_LINES_XPATH="/html/body/div[1]/div[1]/main/div[3]/view/div[2]/div[2]/div[2]/div/div[%d]/div[2]/div/div[1]/div[1]/div[6]/div[1]/div/div/div/div[5]/div/pre"
KATA_SETUP_CODEMIRROR_SOLUTION_CONTAINER_FIRST_ELEMENT_XPATH="/html/body/div[1]/div[1]/main/div[3]/view/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[6]/div[1]/div/div/div/div[5]/div[1]/pre/span/span[1]"
KATA_SETUP_CODEMIRROR_TEST_CONTAINER_FIRST_ELEMENT_XPATH="/html/body/div[1]/div[1]/main/div[3]/view/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/div[6]/div[1]/div/div/div/div[5]/div[1]/pre/span/span[1]"
KATA_SETUP_SELECT_CODEMIRROR_SCRIPT="document.evaluate(arguments[0],document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.click();console.log(document.evaluate(arguments[0],document,null,XPathResult.FIRST_ORDERED_NODE_TYPE,null).singleNodeValue.outerHTML)"
KATA_SETUP_FINAL_TEST_BUTTON_XPATH="/html/body/div[1]/div[1]/main/div[3]/view/div[2]/div[2]/div[2]/div/div[3]/div[2]/a[2]"
KATA_SETUP_SUBMIT_TEST_BUTTON_XPATH="/html/body/div[1]/div[1]/main/div[3]/view/div[2]/div[2]/div[2]/div/div[3]/div[2]/a[3]"
KATA_SETUP_SCRIPT="return JSON.stringify(App.instance.data);"
KATA_BUILD_SYSTEM="@echo off\ncls\npython \"D:\\boot\\boot.py\" 3 %1"
KATA_LANGUAGE_EXTENSIONS={
	"python": "py",
	"javascript": "js",
	"java": "java",
	"php": "php",
	"cpp": "cpp",
	"bf": "bf",
	"nasm": "asm",
	"powershell": "ps1",
	"shell": "sh"
}
KATA_DIR="D:\\K\\Codewars\\%s"
KATA_DIR_LANG="D:\\K\\Codewars\\%s\\%s"
KATA_FILE="D:\\K\\Codewars\\%s\\%s\\%s.%s"



s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
try:
	s.connect(("10.255.255.255",1))
	LOCAL_IP=s.getsockname()[0]
except:
	pass
s.close()



def _set_print(*a):
	if (len(a)==1):
		threading.current_thread()._b_nm=t._b_nm
		threading.current_thread()._nm=t._nm
	else:
		threading.current_thread()._b_nm=a[0]
		threading.current_thread()._nm=a[1]



def _print(*a,end="\n"):
	global CMD_L,STDOUT_LOCK
	def _r_color_f(m):
		if (m.group(0)[0]=="'"):
			return f"\x1b[38;2;91;216;38m{m.group(0)}\x1b[0m"
		if (m.group(0)[0] in "-0123456789"):
			return f"\x1b[38;2;48;109;206m{m.group(0)}\x1b[0m"
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
			elif (m[i:].startswith("True")):
				o+="\x1b[38;2;239;128;15mTrue"
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
	a=" ".join([str(e) for e in a])
	if (not hasattr(threading.current_thread(),"_df") or threading.current_thread()._df==False):
		i=0
		while (i<len(a)):
			_im=re.match(r"\x1b\[[^m]+m",a[i:])
			if (_im!=None):
				i+=len(_im.group(0))
			m=re.match(r"\(( *[A-Za-z0-9_]+ *= *(?:False|True|-?[0-9]+(?:\.[0-9]+)?|'[^']*'),?)+ *\)|'[^']*'|-?[0-9]+(?:\.[0-9]+)?",a[i:])
			if (m!=None):
				o=_r_color_f(m)
				a=a[:i]+o+a[i+len(m[0]):]
				i+=len(o)-1
			i+=1
	if (hasattr(threading.current_thread(),"_r") and threading.current_thread()._r>=1):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.connect(("127.0.0.1",8022))
		s.send(bytes(f"{threading.current_thread()._b_nm}\x00{threading.current_thread()._nm}\x00{a}","utf-8"))
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
			time.sleep(0.05)
	CMD_L[nm]={"_end":e,"h":h,"l":{"__main__":b""}}
	_start_thr(_h_s,nm,"_stdout_redirect",nm,"out")
	_start_thr(_h_s,nm,"_stderr_redirect",nm,"err")



def _codewars_wr():
	global SWAP_DATA
	def _sawp_thr():
		global SWAP_DATA
		_print("Starting Data Swap Loop\x1b[38;2;100;100;100m...")
		while (SWAP_DATA!=None):
			try:
				if (ntpath.getsize(SWAP_FILE_NAME)>0 or len(SWAP_DATA)>0):
					with open(SWAP_FILE_NAME,"r") as f:
						f=f.read()
						SWAP_DATA+=[e for e in f.split("\n") if len(e)>0]
					with open(SWAP_FILE_NAME,"w"):
						pass
			except TypeError as e:
				if (SWAP_DATA==None):
					break
				else:
					traceback.print_exception(None,e,e.__traceback__)
			time.sleep(0.1)
		_print("\x1b[38;2;200;40;20mData Swap Loop Stopped.\x1b[0m")
	_print("Starting Data Swap Loop\x1b[38;2;100;100;100m...")
	_start_thr(_sawp_thr,"__core__","codewars_driver_swap_loop")
	_print("Starting ChromeDriver\x1b[38;2;100;100;100m...")
	if (not ntpath.exists("C:\\Program Files\\ChromeDriver\\chromedriver.exe")):
		SWAP_DATA=None
		_print("\x1b[38;2;200;40;20mChromeDriver.exe Not Found.\x1b[0m Quitting\x1b[38;2;100;100;100m...")
		return
	opts=webdriver.ChromeOptions()
	opts.headless=True
	driver=webdriver.Chrome(executable_path="C:\\Program Files\\ChromeDriver\\chromedriver.exe",options=opts)
	_print("Logging In\x1b[38;2;100;100;100m...")
	driver.get(CODEWARS_SIGNIN_URL)
	wait=WebDriverWait(driver,100)
	try:
		e=wait.until(EC.presence_of_element_located((By.XPATH,CODEWARS_SIGNIN_EMAIL_XPATH))).send_keys(USER_EMAIL)
		e=wait.until(EC.presence_of_element_located((By.XPATH,CODEWARS_SIGNIN_PASSWORD_XPATH))).send_keys(USER_PASSWORD)
		_print("Submiting Log In\x1b[38;2;100;100;100m...")
		wait.until(EC.presence_of_element_located((By.XPATH,CODEWARS_SIGNIN_LOGIN_BUTTON_XPATH))).click()
		while (driver.current_url!=CODEWARS_DASHBOARD_URL):
			pass
		_print("Starting Listener\x1b[38;2;100;100;100m...")
		while (True):
			if (len(SWAP_DATA)>0):
				open_,kid,SWAP_DATA=SWAP_DATA[0][0],SWAP_DATA[0][1:].replace("https://www.codewars.com/kata/","").split("/"),SWAP_DATA[1:]
				_print(f"Request Found: (url='https://www.codewars.com/kata/{'/'.join(kid)}', id='{kid[0]}', language={(chr(39)+kid[2]+chr(39) if len(kid)>=3 else 'unknown')}, open_in_editor={open_})")
				kid,k_o_nm=kid[0],(kid[2] if len(kid)>=3 else None)
				while (True):
					try:
						_print(f"Querying URL '{KATA_METADATA_URL%(kid)}'\x1b[38;2;100;100;100m...")
						driver.get(KATA_METADATA_URL%(kid))
						lce=wait.until(EC.presence_of_element_located((By.XPATH,KATA_METADATA_LANGUAGE_LIST_CONTAINER_XPATH)))
						k_f_nm=re.sub(r"[^a-z0-9\_\-]","",wait.until(EC.presence_of_element_located((By.XPATH,KATA_METADATA_NAME_XPATH))).get_attribute("innerText").replace(" ","_").lower())
						_print(f"Creatting Output Dir '{KATA_DIR%(k_f_nm)}'\x1b[38;2;100;100;100m...")
						if (not ntpath.exists(KATA_DIR%(k_f_nm))):
							os.mkdir(KATA_DIR%(k_f_nm))
						psd=None
						_print(f"Cloning All Languages... ({', '.join([e.get_attribute('data-value') for e in lce.find_elements_by_css_selector('dd[data-value]') if e.get_attribute('data-value') in KATA_LANGUAGES])})")
						for l in [e.get_attribute("data-value") for e in lce.find_elements_by_css_selector("dd[data-value]") if e.get_attribute("data-value") in KATA_LANGUAGES]:
							_print(f"Querying URL '{KATA_SETUP_URL%(kid,l)}'\x1b[38;2;100;100;100m...")
							driver.get(KATA_SETUP_URL%(kid,l))
							_print("Waiting Until Content Loads\x1b[38;2;100;100;100m...")
							wait.until(EC.presence_of_element_located((By.XPATH,KATA_SETUP_CODEMIRROR_CONTAINER_XPATH%(KATA_SETUP_SOLUTION_CONTAINER_ID))))
							wait.until(EC.presence_of_element_located((By.XPATH,KATA_SETUP_CODEMIRROR_CONTAINER_XPATH%(KATA_SETUP_FIXTURE_TESTS_CONTAINER_ID))))
							while (len(driver.find_elements_by_xpath(KATA_SETUP_CODEMIRROR_CONTAINER_LINES_XPATH%(KATA_SETUP_SOLUTION_CONTAINER_ID)))==0 or len(driver.find_elements_by_xpath(KATA_SETUP_CODEMIRROR_CONTAINER_LINES_XPATH%(KATA_SETUP_FIXTURE_TESTS_CONTAINER_ID)))==0):
								pass
							_print("Requesting Data\x1b[38;2;100;100;100m...")
							kdt=json.loads(driver.execute_script(KATA_SETUP_SCRIPT))
							_print("Cleaning-Up Previous Output\x1b[38;2;100;100;100m...")
							if (psd==None):
								if (kdt["previousSolutions"]==None):
									psd={}
								else:
									psd={ps["sym"]:ps for ps in kdt["previousSolutions"] if ps["sym"] in KATA_LANGUAGES}
							if (not ntpath.exists(KATA_DIR_LANG%(k_f_nm,l))):
								os.mkdir(KATA_DIR_LANG%(k_f_nm,l))
							_print("Writing Files\x1b[38;2;100;100;100m...")
							for k in os.listdir(KATA_DIR_LANG%(k_f_nm,l)):
								if (k.split("-")[0]!="solution" or k.split(".")[0]=="solution-working"):
									continue
								os.remove(KATA_DIR_LANG%(k_f_nm,l)+"\\"+k)
							if (not ntpath.exists(KATA_FILE%(k_f_nm,l,"","codewars-data"))):
								with open(KATA_FILE%(k_f_nm,l,"","codewars-data"),"w") as f:
									f.write("id="+kid+"\nsol-id="+kdt["languageInfo"]["solutionId"]+"\nlang="+kdt["languageInfo"]["languageName"]+"\nlang-ver="+kdt["languageInfo"]["activeVersion"]+"\ntest-fr="+kdt["languageInfo"]["testFramework"]+"\nfixture="+kdt["languageInfo"]["fixture"].replace("\n","")+"\nsetup="+kdt["languageInfo"]["package"].replace("\n",""))
								os.system(f"cd /d \"{KATA_DIR_LANG%(k_f_nm,l)}\"&&attrib +h .codewars-data")
							with open(KATA_FILE%(k_f_nm,l,"run","bat"),"w") as f:
								f.write(KATA_BUILD_SYSTEM)
							with open(KATA_FILE%(k_f_nm,l,"challenge","md"),"wb") as f:
								f.write(kdt["description"].encode("utf-8"))
							if (not ntpath.exists(KATA_FILE%(k_f_nm,l,"solution-working",KATA_LANGUAGE_EXTENSIONS[l])) or (l in psd.keys() and kdt["languageInfo"]["workingCode"] in psd[l]["solutions"])):
								if (kdt["languageInfo"]["workingFixture"]==None):
									kdt["languageInfo"]["workingFixture"]=kdt["languageInfo"]["exampleFixture"]
								if (kdt["languageInfo"]["workingCode"]==None):
									kdt["languageInfo"]["workingCode"]=kdt["languageInfo"]["setup"]
								with open(KATA_FILE%(k_f_nm,l,"solution-working",KATA_LANGUAGE_EXTENSIONS[l]),"wb") as f:
									f.write(kdt["languageInfo"]["workingCode"].encode("utf-8"))
								with open(KATA_FILE%(k_f_nm,l,"tdd_local",KATA_LANGUAGE_EXTENSIONS[l]),"wb") as f:
									f.write(kdt["languageInfo"]["workingFixture"].encode("utf-8"))
							if (l not in psd.keys()):
								continue
							_print("Writing Previous Solutions\x1b[38;2;100;100;100m...")
							for pss in psd[l]["solutions"]:
								psl=[f.split(".")[0] for f in os.listdir(KATA_DIR_LANG%(k_f_nm,psd[l]["sym"])) if "solution-" in f]
								s_id=0
								while ("solution-"+str(s_id) in psl):
									s_id+=1
								with open(KATA_FILE%(k_f_nm,psd[l]["sym"],"solution-"+str(s_id),KATA_LANGUAGE_EXTENSIONS[psd[l]["sym"]]),"wb") as f:
									f.write(bytes(pss,"utf-8"))
						break
					except:
						_print(f"Failed to Process Request. Retrying... (id='{kid}')")
				if (open_=="1"):
					if (k_o_nm==None):
						_print("Opening Cloned Files in File Explorer\x1b[38;2;100;100;100m...")
						_open_app(KATA_DIR%(k_f_nm),file=True)
					else:
						_print("Opening Cloned Files in Editor\x1b[38;2;100;100;100m...")
						_open_app(f"C:\\Program Files\\Sublime Text 3\\sublime_text.exe {KATA_FILE%(k_f_nm,k_o_nm,'solution-working',KATA_LANGUAGE_EXTENSIONS[k_o_nm])}")
						_open_app(f"C:\\Program Files\\Sublime Text 3\\sublime_text.exe {KATA_FILE%(k_f_nm,k_o_nm,'challenge','md')}")
				_print(f"Finished Processing Request (id='{kid}')")
	except Exception as e:
		f=io.StringIO()
		traceback.print_exception(None,e,e.__traceback__,file=f)
		CMD_L[threading.current_thread()._b_nm]["l"][threading.current_thread()._nm]+=bytes("\x1b[38;2;200;40;20m"+f.getvalue(),"utf-8")
		print(f.getvalue(),file=sys.__stderr__,end="")
	_print("Stopping ChromeDriver\x1b[38;2;100;100;100m...")
	SWAP_DATA=None
	driver.quit()



def _render_cwr(tp):#######################################
	def _center_ignore(o,l):
		while (len(re.sub(r"\x1b\[[^m]+m","",o))<l):
			o+=" "
			if (len(re.sub(r"\x1b\[[^m]+m","",o))==l):
				break
			o=" "+o
		return o
	def _ljust_ignore(o,l):
		while (len(re.sub(r"\x1b\[[^m]+m","",o))<l):
			o+=" "
		return o
	def _render_elem(e,ppe,pe,i):
		o=[]
		if (e["t"]=="describe" or e["t"]=="it"):
			cl=("\x1b[38;2;183;38;38m" if e["p"]==False else "\x1b[38;2;72;183;38m")
			o+=[[("" if pe==None and ppe!=None and (ppe["t"]=="it" or ppe["t"]=="describe") else "\n")+" "*i+cl+"■ \x1b[38;2;238;238;238m"+e["v"].replace("\t","    ").replace("\r",""),i]]
			for ei,ce in enumerate(e["items"]):
				o+=_render_elem(ce,e,(None if ei==0 else e["items"][ei-1]),i+4)
		elif ("items" not in e.keys() and e["t"]!="log" and e["t"]!="completedin"):
			cl=("\x1b[38;2;183;38;38m" if e["t"]=="failed" else "\x1b[38;2;72;183;38m")
			o+=[[("" if ((pe!=None and pe["t"]=="log") or (pe==None and ppe!=None)) else "\n")+" "*(i-2)+cl+"» "+e["v"].replace("\t","    ").replace("\r",""),i]]
		elif (e["t"]=="log"):
			o+=[[("" if pe!=None and (pe["t"]=="log" or pe["t"]=="it" or pe["t"]=="describe") else "\n")+" "*i+"\x1b[38;2;138;138;138mLOG:\n\x1b[38;2;238;238;238m"+" "*i+str(e["v"][:-1]).replace("\n","\n"+" "*i).replace("\t","    ").replace("\r",""),i+2]]
		elif (e["t"]=="completedin"):
			o+=[[" "*(i-2)+"\x1b[38;2;138;138;138m"+str(e["v"]).replace("\t","    ").replace("\r","")+"ms",i-2]]
		else:
			o+=[["UNKNOWN"+e["t"]+" => "+e["v"].replace("\t","    ").replace("\r",""),0]]
		return o
	def _wrap(l,mx,ws):
		p=" "*len(re.sub(r"\x1b\[[^m]+m","",l)[:ws])
		i=0
		ll=0
		st=""
		while (i<len(l)):
			if (l[i]=="\x1b"):
				st+=l[i]
				i+=1
				while (l[i-1]!="m"):
					st+=l[i]
					i+=1
				continue
			if (l[i]=="\n"):
				l=l[:i+1]+st+l[i+1:]
				i+=len(st)+1
				ll=0
				continue
			if (ll>=mx):
				l=l[:i]+"\n"+p+st+l[i:]
				i+=len(p)+len(st)+1
				ll=ws
			i+=1
			ll+=1
		return l.split("\n")
	cmd={"ciphered":["setup"]}
	with open(".codewars-data","r") as f:
		s={e.split("=")[0]:"=".join(e.split("=")[1:]) for e in f.read().split("\n") if len(e.split("="))>=2}
	if (tp=="--local"):
		with open([x for x in os.listdir("./") if x.split(".")[0]=="tdd_local"][0],"r") as f:
			cmd["fixture"]=f.read()
	else:
		cmd["fixture"]=s["fixture"]
		cmd["ciphered"]+=["fixture"]
	cmd["relayId"]=s["sol-id"]
	cmd["setup"]=s["setup"]
	with open([x for x in os.listdir("./") if x.split(".")[0]=="solution-working"][0],"r") as f:
		cmd["code"]=f.read()
	cmd["language"]=s["lang"]
	cmd["languageVersion"]=s["lang-ver"]
	cmd["testFramework"]=s["test-fr"]
	dt=None
	try:
		dt=urllib.request.urlopen(urllib.request.Request("https://runner.codewars.com/run",data=bytes(json.dumps(cmd),"utf-8")),timeout=20)
	except Exception as e:
		dt=e.file
	JSON=json.loads(dt.read())
	bg="\x1b[0m\x1b[48;2;24;24;24m"
	b_cl=("\x1b[38;2;84;04;04m" if JSON["result"]["completed"]==False else "\x1b[38;2;85;212;85m")
	o=["\x1b[38;2;138;138;138mTime: \x1b[38;2;238;238;238m"+str(JSON["wallTime"])+"ms    \x1b[38;2;138;138;138mPassed: \x1b[38;2;238;238;238m"+str(JSON["result"]["assertions"]["passed"])+"    \x1b[38;2;183;38;38mFailed: \x1b[38;2;213;98;98m"+str(JSON["result"]["assertions"]["failed"])+"    \x1b[38;2;183;38;38mExit Code: \x1b[38;2;213;98;98m"+str(JSON["exitCode"])]
	for i,rs in enumerate(JSON["result"]["output"]):
		o+=_render_elem(rs,None,(None if i==0 else JSON["result"]["output"][i-1]),0)
	if (len(JSON["message"])>0):
		o+=[["",0],["\x1b[38;2;183;38;38mERROR: \x1b[38;2;213;98;98m"+JSON["message"].replace("\t","    ").replace("\r",""),7],["",0]]
	if (len(JSON["stdout"])>0):
		o+=[["\x1b[38;2;138;138;138mSTDOUT:\n\x1b[38;2;238;238;238m"+JSON["stdout"].replace("\t","    ").replace("\r",""),0]]
	if (len(JSON["stderr"])>0):
		o+=[["\x1b[38;2;138;138;138mSTDERR:\n\x1b[38;2;238;238;238m"+JSON["stderr"].replace("\t","    ").replace("\r",""),0]]
	ho=ctypes.windll.kernel32.GetStdHandle(-10)
	dw_m=ctypes.wintypes.DWORD()
	ctypes.windll.kernel32.GetConsoleMode(ho,ctypes.byref(dw_m))
	dw_m.value=0
	ctypes.windll.kernel32.SetConsoleMode(ho,dw_m)
	ho=ctypes.windll.kernel32.GetStdHandle(-11)
	dw_m=ctypes.wintypes.DWORD()
	ctypes.windll.kernel32.GetConsoleMode(ho,ctypes.byref(dw_m))
	dw_m.value|=4
	ctypes.windll.kernel32.SetConsoleMode(ho,dw_m)
	sbi=ctypes.create_string_buffer(22)
	ctypes.windll.kernel32.GetConsoleScreenBufferInfo(ho,sbi)
	dt=struct.unpack("hhhhHhhhhhh",sbi.raw)
	o,co=[o[0]],o[1:]
	for l in co:
		o+=_wrap(l[0],dt[9]-8,l[1])
	mx=min(max([len(re.sub(r"\x1b\[[^m]+m","",e)) for e in o]),dt[9]-8)
	o=[bg+" "*(mx+8),bg+b_cl+"  ╔"+"═"*(mx+2)+"╗  ",b_cl+"  ║ "+_center_ignore(o[0],mx)+b_cl+" ║  ",b_cl+"  ╠"+"═"*(mx+2)+"╣  "]+[b_cl+"  ║ "+_ljust_ignore(l,mx)+b_cl+" ║  " for l in o[1:]]+[b_cl+"  ╚"+"═"*(mx+2)+"╝  ",bg+" "*(mx+8)]
	ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(ctypes.wintypes.SMALL_RECT(0,0,min(mx+7,dt[9]-1),min(len(o)-1,dt[10]-1))))
	ctypes.windll.kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(min(mx+8,dt[9]),len(o)))
	ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(ctypes.wintypes.SMALL_RECT(0,0,min(mx+7,dt[9]-1),min(len(o)-1,dt[10]-1))))
	_print("\n".join(o)+"\x1b[0m",end="")
	ex=False
	while (True):
		c=sys.stdin.read(1)
		if (c=="\x03"):
			ex=True
			break
		elif (c=="\n"):
			break
	os.system("cls")
	ctypes.windll.kernel32.SetConsoleScreenBufferSize(ho,ctypes.wintypes._COORD(*dt[:2]))
	ctypes.windll.kernel32.SetConsoleWindowInfo(ho,True,ctypes.byref(ctypes.wintypes.SMALL_RECT(*dt[5:9])))
	if (ex==True):
		return
	_render_cwr(tp)



def _update_repo(p,b_nm,r_desc,msg):#######################################
	def _parse_gitignore(dt):
		o=[]
		for ln in dt.split("\n"):
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
						o+=[[iv,ln.replace("**/","")]]
					o+=[[iv,ln]]
		return o
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
					return True
				ig=True
		if (ig==True):
			return False
		return True
	def _request(m="get",**kwargs):
		r=None
		if (m=="get"):
			r=requests.get(**kwargs)
		elif (m=="post"):
			r=requests.post(**kwargs)
		elif (m=="put"):
			r=requests.put(**kwargs)
		elif (m=="patch"):
			r=requests.patch(**kwargs)
		if ("X-RateLimit-Remaining" in r.headers.keys() and r.headers["X-RateLimit-Remaining"]=="0"):
			_print(r.headers)
			sys.exit(1)
		time.sleep(0.72)
		if ("message" in r.json().keys() and r.json()["message"]=="Server Error"):
			return None
		return r.json()
	def _get_tree(r_nm,sha):
		def _rec_get(r_nm,sha,p):
			r=_request("get",url=f"https://api.github.com/repos/Krzem5/{r_nm}/git/trees/{sha}",data=json.dumps({"recursive":"false"}),headers={"Authorization":f"token {GITHUB_TOKEN}"})
			o={}
			for e in r["tree"]:
				if (e["type"]=="tree"):
					o.update(_rec_get(r_nm,e["sha"],p+"/"+e["path"]))
				elif ((p+"/"+e["path"]).replace("./","")!="_"):
					o[(p+"/"+e["path"]).replace("./","")]={"sz":e["size"],"sha":e["sha"]}
			return o
		return _rec_get(r_nm,sha,".")
	def _match_f(fp,dt):
		try:
			with open(fp,"r") as f:
				f=f.read().replace("\r\n","\n")
				if (len(f)!=dt["sz"]):
					return False
				return (True if hashlib.sha1(f"blob {len(f)}\x00{f}".encode()).hexdigest()==dt["sha"] else False)
		except UnicodeDecodeError:
			if (os.stat(fp).st_size!=dt["sz"]):
				return False
			with open(fp,"rb") as f:
				return (True if hashlib.sha1(f"blob {os.stat(fp).st_size}\x00".encode()+f.read()).hexdigest()==dt["sha"] else False)
	r_nm=re.sub(r"[^A-Za-z0-9_\.]|\-",r"",b_nm)
	_request("post",url="https://api.github.com/user/repos",data=json.dumps({"name":r_nm,"description":(b_nm.split("-")[0]+" - "+b_nm.split("-")[1].replace("_"," ").title() if r_desc==None else r_desc),"private":False,"has_ssues":True,"has_projects":True,"has_wiki":True}),headers={"Authorization":f"token {GITHUB_TOKEN}"})
	with open(p+"\\.gitignore","r") as f:
		gdt=_parse_gitignore(f.read())
	r_tf_p=False
	try:
		bt_sha=_request("get",url=f"https://api.github.com/repos/Krzem5/{r_nm}/git/ref/heads/master",headers={"Authorization":f"token {GITHUB_TOKEN}","User-Agent":"Update API"})["object"]["sha"]
	except:
		_request("put",url=f"https://api.github.com/repos/Krzem5/{r_nm}/contents/_",data=json.dumps({"message":msg,"content":""}),headers={"Authorization":f"token {GITHUB_TOKEN}"})
		bt_sha=_request("get",url=f"https://api.github.com/repos/Krzem5/{r_nm}/git/ref/heads/master",headers={"Authorization":f"token {GITHUB_TOKEN}","User-Agent":"Update API"})["object"]["sha"]
		r_tf_p=True
	r_t=_get_tree(r_nm,bt_sha)
	bl=[]
	cnt=[0,0,0,0]
	for r,_,fl in os.walk(p):
		for f in fl:
			fp=ntpath.join(r,f).replace(p,"")[(1 if not p.endswith("\\") else 0):].replace("\\","/")
			if (_gitigonre_match(gdt,fp)==False):
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
			dt="File too Large (size = %d b)"%(os.stat(ntpath.join(r,f)).st_size)
			b_sha=False
			if (os.stat(ntpath.join(r,f)).st_size<=50*1024*1024):
				b64=True
				try:
					with open(ntpath.join(r,f),"r") as rbf:
						dt=rbf.read().replace("\r\n","\n")
					b64=False
				except:
					pass
				try:
					Image.open(ntpath.join(r,f)).close()
					b64=True
				except:
					pass
				if (b64==True):
					b_sha=True
					with open(ntpath.join(r,f),"rb") as rbf:
						dt=str(base64.b64encode(rbf.read()))[2:-1]
					if (len(dt)>50*1024*1024):
						b_sha=False
						dt="File too Large (size = %d b)"%(len(dt))
					else:
						b=_request("post",url=f"https://api.github.com/repos/Krzem5/{r_nm}/git/blobs",data=json.dumps({"content":dt,"encoding":"base64"}),headers={"Authorization":f"token {GITHUB_TOKEN}","User-Agent":"Update API"})
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
	if (any([(True if b[1]!=None else False) for b in bl])):
		_request("patch",url=f"https://api.github.com/repos/Krzem5/{r_nm}/git/refs/heads/master",data=json.dumps({"sha":_request("post",url=f"https://api.github.com/repos/Krzem5/{r_nm}/git/commits",data=json.dumps({"message":msg,"tree":_request("post",url=f"https://api.github.com/repos/Krzem5/{r_nm}/git/trees",data=json.dumps({"base_tree":bt_sha,"tree":[b[1] for b in bl if b[1]!=None]+([{"path":"_","mode":"100644","type":"blob","sha":None}] if r_tf_p==True else [])}),headers={"Authorization":f"token {GITHUB_TOKEN}","User-Agent":"Update API"})["sha"],"parents":[bt_sha]}),headers={"Authorization":f"token {GITHUB_TOKEN}","User-Agent":"Update API"})["sha"],"force":True}),headers={"Authorization":f"token {GITHUB_TOKEN}","User-Agent":"Update API"})
	_print(f"\x1b[38;2;40;210;190m{b_nm} => \x1b[38;2;70;210;70m+{cnt[0]}\x1b[38;2;40;210;190m, \x1b[38;2;230;210;40m?{cnt[1]}\x1b[38;2;40;210;190m, \x1b[38;2;190;0;220m!{cnt[2]}\x1b[38;2;40;210;190m, \x1b[38;2;210;40;40m-{cnt[3]}\x1b[0m")



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



def _save_w():
	_print("Saving Workspace Data\x1b[38;2;100;100;100m...")
	global WORKSPACE_DATA
	WORKSPACE_DATA=sorted(WORKSPACE_DATA,key=lambda x:x["name"])
	with open("D:\\boot\\workspace-data.json","w") as f:
		f.write(json.dumps(WORKSPACE_DATA,indent=4,sort_keys=True).replace("    ","\t"))



def _open_prog_w(p):###############################################
	_print(f"Opening Program {p}\x1b[38;2;100;100;100m...")
	def _open_prog_w_f(p,p2,e,*f):
		op=False
		for fn in f:
			if (ntpath.isfile(fn)):
				subprocess.Popen([p,fn])
				op=True
		if (op==False):
			subprocess.Popen([p,glob.glob(f"{p2}**\\*.{e}",recursive=True)[0]])
	type_=p.split("-")[0].lower()
	p="D:\\K\\Coding\\projects\\"+p+"\\"
	if (type_=="cpp"):
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
		subprocess.Popen(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",p])
	_save_w()



def _create_prog(type_,name,op=True):##############################
	_print(f"Creating Project: (type='{type_}', name='{name}', open_on_creation={op})")
	type_=type_.lower()
	if (type_ not in "chromeext,cpp,css,ft,fischertechnic,java,js,javascript,mindstorm,php,processing,python,three,websocket".split(",")):
		_print(f"UNKNOWN TYPE: {type_}")
		return
	if (type_=="js"):
		type_="javascript"
	if (type_=="ft"):
		type_="fischertechnic"
	name=name.replace("_"," ").lower().title().replace(" ","_")
	p="D:\\K\\Coding\\projects\\"+type_.title()+"-"+name+"\\"
	if (not ntpath.exists(p)):
		os.mkdir(p)
	if (not ntpath.exists(f"{p}.gitignore")):
		with open(f"{p}.gitignore","x") as f:
			f.write("### Github File Push Ignore\n\n")
		os.system(f"cd /d {p}&&attrib +h .gitignore")
	global WORKSPACE_DATA
	if (type_.title()+"-"+name.replace("_"," ").lower().title().replace(" ","_") not in [e["name"] for e in WORKSPACE_DATA]):
		WORKSPACE_DATA.append({"name":type_.title()+"-"+name.replace("_"," ").lower().title().replace(" ","_"),"year":datetime.datetime.now().year,"desc":"[null]"})
	if (type_=="cpp"):
		if (not ntpath.exists(f"{p}index.cpp")):
			with open(f"{p}index.cpp","x") as f:
				f.write("int main(){\n\treturn 0;\n}")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\nset LIB=C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.25.28610\\lib\\x64;C:\\Program Files (x86)\\Windows Kits\\NETFXSDK\\4.8\\lib\\um\\x64;C:\\Program Files (x86)\\Windows Kits\\10\\lib\\10.0.18362.0\\ucrt\\x64;C:\\Program Files (x86)\\Windows Kits\\10\\lib\\10.0.18362.0\\um\\x64;\nset INCLUDE=C:\\Program Files (x86)\\Microsoft Visual Studio\\2019\\BuildTools\\VC\\Tools\\MSVC\\14.25.28610\\include;C:\\Program Files (x86)\\Windows Kits\\NETFXSDK\\4.8\\include\\um;C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.18362.0\\ucrt;C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.18362.0\\shared;C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.18362.0\\um;C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.18362.0\\winrt;C:\\Program Files (x86)\\Windows Kits\\10\\include\\10.0.18362.0\\cppwinrt\ndel *.obj&&del index.exe&&cl /EHsc *.cpp /link /OUT:index.exe&&del *.obj&&cls&&index.exe\nif exist index.exe (\n\trem del index.exe\n)")
	elif (type_=="css"):
		if (not ntpath.exists(f"{p}index.html")):
			with open(f"{p}index.html","x") as f:
				f.write(f"<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{name.replace('_',' ')}</title>\n\t\t<link href=\"./style.css\" rel=\"stylesheet\" type=\"text/css\">\n\t</head>\n\t<body>\n\t</body>\n</html>")
		if (not ntpath.exists(f"{p}style.css")):
			with open(f"{p}style.css","x") as f:
				f.write("body {\n\twidth: 100%;\n\theight: 100%\n}\nbody, body * {\n\tmargin: 0;\n\tpadding: 0;\n}")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe\" http://localhost:8020/{p}")
	elif (type_=="fischertechnic"):
		if (not ntpath.exists(f"{p}index.rpp")):
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
		if (not ntpath.exists(f"{p}com\\krzem\\{name.lower()}\\Main.java")):
			with open(f"{p}com\\krzem\\{name.lower()}\\Main.java","x") as f:
				f.write("package com.krzem."+name.lower()+";\n\n\n\npublic class Main{\n\tpublic static void main(String[] args){\n\t\tnew Main();\n\t}\n\n\n\n\tpublic Main(){\n\t\t\n\t}\n}")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(p+"index.bat","x") as f:
				f.write(f"@echo off\necho NUL>_.class&&del /s /f /q *.class\ncls\njavac com/krzem/{name.lower().replace(' ','_')}/Main.java&&java com/krzem/{name.lower().replace(' ','_')}/Main\nstart /min cmd /c \"echo NUL>_.class&&del /s /f /q *.class\"")
	elif (type_=="javascript"):
		if (not ntpath.exists(f"{p}index.html")):
			with open(f"{p}index.html","x") as f:
				f.write(f"<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{name.replace('_',' ')}</title>\n\t\t<script type=\"text/javascript\" src=\"./index.js\"></script>\n\t</head>\n\t<body>\n\t</body>\n</html>")
		if (not ntpath.exists(f"{p}index.js")):
			with open(f"{p}index.js","x") as f:
				f.write("function init(){\n\t\n}\ndocument.addEventListener(\"DOMContentLoaded\",init,false)")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe\" http://localhost:8020/{p}")
	elif (type_=="php"):
		if (not ntpath.exists(f"{p}index.php")):
			with open(f"{p}index.php","x") as f:
				f.write("<?php\n\n?>")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe\" http://localhost:8020/{p}index.php")
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
		if (not ntpath.exists(f"{p}index.py")):
			with open(f"{p}index.py","x") as f:
				f.write("")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\npython index.py")
	elif (type_=="three"):
		if (not ntpath.exists(f"{p}index.html")):
			with open(f"{p}index.html","x") as f:
				f.write(f"<!DOCTYPE html>\n<html>\n\t<head>\n\t\t<title>{name.replace('_',' ')}</title>\n\t\t<script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/three.js/104/three.min.js\"></script>\n\t\t<script type=\"text/javascript\" src=\"https://threejs.org/js/controls/OrbitControls.js\"></script>\n\t\t<script type=\"text/javascript\" src=\"./index.js\"></script>\n\t\t<style type=\"text/css\">\n\t\t\tbody {{\n\t\t\t\tmargin: 0;\n\t\t\t\tpadding: 0;\n\t\t\t}}\n\t\t\tcanvas {{\n\t\t\t\twidth: 100%%;\n\t\t\t\theight: 100%%;\n\t\t\t}}\n\t\t</style>\n\t</head>\n\t<body>\n\t</body>\n</html>")
		if (not ntpath.exists(f"{p}index.js")):
			with open(f"{p}index.js","x") as f:
				f.write("var scene,cam,renderer,controls\nfunction init(){\n\tscene=new THREE.Scene()\n\tcam=new THREE.PerspectiveCamera(60,window.innerWidth/window.innerHeight,0.1,100000)\n\tcam.position.set(0,2000,0)\n\tcam.enablePan=false\n\tcam.lookAt(new THREE.Vector3(0,0,0))\n\trenderer=new THREE.WebGLRenderer({antialias:true})\n\trenderer.setSize(window.innerWidth,window.innerHeight)\n\tscene.background=new THREE.Color().setHSL(1,1,1)\n\tdocument.body.appendChild(renderer.domElement)\n\tambient=new THREE.AmbientLight(0xffffff,1)\n\tscene.add(ambient)\n\trenderer.render(scene,cam)\n\tcontrols=new THREE.OrbitControls(cam,renderer.domElement)\n\tcontrols.target=new THREE.Vector3(0,0,0)\n\twindow.addEventListener(\"resize\",resize,false)\n\twindow.addEventListener(\"keypress\",onkeypress)\n\trequestAnimationFrame(render)\n}\nfunction render(){\n\trenderer.render(scene,cam)\n\trequestAnimationFrame(render)\n}\nfunction resize(){\n\tcam.aspect=window.innerWidth/window.innerHeight\n\tcam.updateProjectionMatrix()\n\trenderer.setSize(window.innerWidth,window.innerHeight)\n}\nfunction onkeypress(e){\n\tswitch (e.keyCode){\n\t\t//\n\t}\n}\ndocument.addEventListener(\"DOMContentLoaded\",init,false)")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files (x86)/Google/Chrome/Application/chrome.exe\" http://localhost:8020/{p}")
	elif (type_=="mindstorm"):
		if (not ntpath.exists(f"{p}indexev3")):
			with open(f"{p}index.ev3","wb") as f:
				f.write(b"PK\x03\x04\x14\x00\x00\x00\x08\x00T\x88VE\xa1\xf9\xe4\xb8\x06\x00\x00\x00\x04\x00\x00\x00\x10\x00\x00\x00___CopyrightYear3204\x01\x00PK\x03\x04\x14\x00\x00\x00\x08\x00T\x88VEr\xe9\x0e\xe0\t\x00\x00\x00\x07\x00\x00\x00\x0f\x00\x00\x00___ProjectTitle\x0b(\xca\xcfJM.\x01\x00PK\x03\x04\x14\x00\x00\x08\x08\x00\x05\x94\xa9N\x0e\xc5\xcb\xd7\x08\x00\x00\x00\x16\x00\x00\x00\x12\x00\x00\x00ActivityAssets.laz\x0b\xf0fec\xc0\x00\x00PK\x03\x04\x14\x00\x00\x08\x08\x00\x05\x94\xa9N\x89\x9fa\x01\xf6\x01\x00\x00\x04\x04\x00\x00\x0c\x00\x00\x00Activity.x3a\x95S\xddn\xda0\x14\xbe\x9f\xb4w\xb0|[-n\xdamBSB\xd5\xf2\x93\x95\x8d\xd2\x12\xca\xa4\xde\x19\xdb\x10\xa7\x8e\x9d%\x0e\x10^m\x17{\xa4\xbd\xc2N\x82 \x14\xc1\xa4E\x8ad\x9f\xf3\x9d\xcf\xe7;?\x7f~\xfd\xf6n\xd6\x89BK\x91\xe5\xd2h\x1f\xbb\xce%FB3\xc3\xa5^\xf8\xb8\xb0\xf3\x0f-|\xd3~\xff\xce\x0bM\x911\xd1\x97J\xa0\xe9\x01\xda\xb9r\\\x08\x01\x12\x9d\xfb8\xb26\xfdB\xc8j\xb5r\xb4t\x98I\xc86lh\xb8P\xce:\xe7\x18\xa8\x10|\xde\x03MD\x9eR&Pu\xf2\xf1cfb\xc1\xec\xce_c\x82Br\xc1\xbf\n\x95\x9e\xe7o0\x87\xf4{\x8aP\x81;?\xb26\x1e\xd4\x84\x87r\x03i\x84\tU\n\xf4Y\xc9\xa8\xc2\xa8\x06m\x13\xc4\xe8A\xac\xed]a\xad\xd1=MgJp\x1fO\xb2B`4\xd25\xae\x13Q\xbd\xa8\xac\x10\'\x17\x9a\xda\"\x83\xb8\xf8)\xa6\xe3\xeb\xe0\x95\xb6n\x03>\xb8\xeb\xb7dy\xc5_\xa2A\xc8?\xc5\xdau\xf9\xc8\x8eF\xeb\x90|\xef\xcfF\xd3\xa7\xf9\xf4\xc2\xfd\xf8Mw\x94z\x0c_\x97\xf3\xf1\xe62\xe0,\xb8_\x90\xc1p\xca\xf2\xe2e\xe3&\xb1\xce/\xae\x17\xbe\x8f\xd1D$\xa9\xa2V\xdcw}\xdc/\x94\xc2\'dn\xa5J\x00\x8a.\xb5\x14=k\xf9\xb3\xa8#\xc6\x92E\x13P4\x91V\x81\x86}O\xa1\x99\xcf\xb9\xc8z\\\xdaJ$PS\x95\x03\xe0G\xa5\xd0h\x9b\x19\xb5\xb3\x9dy\xaf~\xb3\xa2n{\xbbG\xba\x86\x15\x89\xd0\x16\xcd\x81!\xaf+\xed~\xc6\xf5mN\x13\xa9J\x1fC\x02\x9cj\xfa\x8fQ\xbaeV.\xa5-\x8fI\xb7\x8d\xf7\xd2\xb67k{\xa4\xfa\xe1H\x8eQ`\xaas:S#\xd2\x14\xe9\xbf\xca\xd8KR[\xbe-\x1f9G\xd0\x89\xa4\xe2\x99\xd0\'\x11\x90A5D\xc7\x03LNN\xb07\x14\\\xd2\xae\x84\x8a\x18M\xb3\xf2\r\xa3w\xb0\x14\xbbu#\xfb}\xabv\x994\xcb\xdc\xfe\x0bPK\x03\x04\x14\x00\x00\x08\x08\x00\x05\x94\xa9NHu\xf8\xec\x11\x03\x00\x008\n\x00\x00\t\x00\x00\x00Main.ev3p\xcdV\xcdn\xda@\x10\xbeW\xea;X\xee9\xb6\t$M]\x9c(\x84\xa0 \xa5!\x02Dr\xa8\x84\x16{\x0c\xdb\xd8\xbb\xee\xee\x1a\xc8\xb3\xf5\xd0G\xea+t\xbc`\xec\x00!\xd0\x1eZ\xec\x83=3\xdf\xcc7\x9e\x1f\xf6\xd7\x8f\x9f\xf5\x8by\x1c\x19S\x10\x92r\xe6\x99\x15\xcb1\r`>\x0f(\x1b{f\xaa\xc2\xa33\xf3\xe2\xfc\xfd\xbbz\x8f\xa7\xc2\x87\x16\x8d\xc0\x18\x94\xac\xadc\xab\x82\x10t\xc2\xa4gN\x94J\\\xdb\x9e\xcdf\x16\xa3\x96\xcfc{\x01\xfb\xc2\x03\x88\xac\xb9\x0cLte\xe0\xaf~Gb\x90\t\xf1\xc1\xc8\x9e<\xf3^\xf0o\xe0\xab\\\xafm\x06T\xa8\x94Dm&\x95Hc`\xcah\xcb>Ona\n\x91g\x86$\x92`\xa2\xa8\x0b\xa8\x12\x84\xa9\x95l\x8d \xf2\xeb`\x86\x82fIi*M\x08)\xa3\nm\xfa\xcf\tF\x7f\xac\x0e\xdaM\xee\xeb ;\x92\xd9 TNiE\xbb%8S\xf7\x84A\xb4\xa6\xd1\xda0\x11)S4\x06\xb7\xb0\xbb\"lJ\xe4Z\\\xe9O &\xd2\x8a\xa9/\xb8\xe4\xa1\xd2\x14f\x94\x85s\xfb\xd8qN\xed9\x89#;\x11 \x91\x08\xc9rY2w\xe7\x87\xf9\xc8a+f\x9e\xe9G\xe2\x88\xe5\x15r\xef\xb4\xf7r\xde\xd2\xba%\xa3A\xfb\xfa\xc1*\x92\xe8.\xc0\x9f\x89\x94\x10\x8f\xa2g\xef XNB\x97g\x1f\x02\xe5\xc6j\x82\xa4c\x06bw\xec\x12\x02\xa3\xb9\x8b\xbe+\x88\x98\x86V\xb9\xb9\xb3^*B\x0c\x8e\x8d\x99\x80P\x14\xa4\x85e\xea1\x92\xf4yg\x94\xf5*\x96\xaa/Rx\x1b\xf7g\xa0\t\x9fe\xc0\x8828\x08t\x85\t\t\x1e]\x06\\\xa0\xcd\n\xfa@\x035\xf1\xcc\xd3\x1aN\xc3\r\xd0\xf1\x04\xc7\xa5v\x86/\xf6z\xff\xda\xaf6p\xbd\x11q\xff\xa9I\xc9X\x90x9\xb8\xc3a\x97s\xb5\x94\r\x87\xe6\xb6\x9e\xef)\"\x94\xc6\x1a\xed\xc03Y\xc54\x1a<e\x01\x92\xab\x1d\x1b\xd5\x9a\xf1\xd11>\xa1\xb0O\xc4\x18T6\x8e_\xad[:r\x0b\\\x1f\xa4\xda\xe6Z\xbb\xc7\x8cC:N\x05\x19E\xf0\x05\xd4\x84\x07}\x101\xc5\xf2\xbf\x82\xd0\xa8\xdcFS\xea\x82L#\x1c\xfd&\x15X$\xbd;:\xa9J\xd2LD\x14Yl\x89\x06\xe7\x11\x10\x1c\xb3\x1b\xaed\xc2\x91\xa8c\x9d\x18\xa5d\x1cC_\x9b\xdf\xb4\xf8\xb6\x07s}\xc9\xb3\x07\xdfS\\\xcf\xd0I\xdf\"\xbbe\x02\xdc\xd2\x04\xb8\xb9\xa5t\x1f\xab\xb9\xd7\x07t\x98\xcbKYV\x0c\xcc\xb3\xc8\xf2\x04KV5*gxo\xcf\xb4n\x17\x85\xdbh\xaer\x0b\xad+\xdb>g\xdb\xfci\xc6\x8e\x9b\xa9u[\xfe\xebM\xb9\xe0s\xc8\x9a\x1c\xb4\x97Kj\xbf\xf5\x88\xe6/\xb7\xd5\xff\xb0\xa0\xf3\xadqr\xba\xda&\xd9c\x83\xf8Oc\x91\xf5\x86g~h\xb5\xae\x9d\xeczuV\x8b\xbf\xbfKFcM\xa0\xb4\xbfV2\xb9kr\xb7\xf8\x90\xd9\xd6#\xb8*\xc5\x8e\xd9\xfb\xcb\xd8\xa5\xb8\xd7S\xfcX%\xac~\xdf\x93\xb3\xb6=\x8c\xee\xde\xe1\xea\xf6\xfa\xa8l\xcc\xdf\xda\x8c\xd57\x0f5\xf9\x11\xcd^\x9d\xd1\xb2\xf3\x9f]\x1c\x00\xcf\x7f\x03PK\x03\x04\x14\x00\x00\x08\x08\x00\x05\x94\xa9Nv\x8c2j \x03\x00\x00\xc0\x0f\x00\x00\x0f\x00\x00\x00Project.lvprojx\xddW\xefn\xda0\x10\xff>i\xef\x10\xe5s\xeb\xb4\xe3\xcb4\x05\xaa\xb6@\x17\xa9\xb4\xa8tY\'!!\x93\x1c\xe0\xcd\xd8\x91\xe3\x04\xd8\xab\xed\xc3\x1ei\xaf0\x9b$$\xa4\t\xa3]\xd7uk%\x88r\xe7\xbb\xdf\xef\xfe\xf8\x8e\x1f\xdf\xbe\xdb\'\xcb95b\x10!\xe1\xaci\x1e\xa3#\xd3\x00\xe6q\x9f\xb0i\xd3\x8c\xe4\xe4\xf0\xady\xd2z\xfd\xca\x1e\xf0Hx\xd0%\x14\x0c\xb7\xa0\x8d\xde\xa0cuD\x19aa\xd3\x9cI\x19\xbc\xb3\xac\xc5b\x81\x18A\x1e\x9f[\xc9\xb1\x1e\xf7\x81\xa2e\xe8\x9b\xca\x94\xa1\xfe\xec+<\x870\xc0\x1e\x18\xfa\xa9i\xb6a\x82#*3\xf9Z\xa7/\xf8g\xf0d\xbd\xf1T\xa1hxs\xf8\x16\x8b)H\xa3\xcd\xbdh\x0eL\xde\xae\x02p|\xf5@&\x04D\xd3t\x1d\xb7\x97\xa8\x98)\x02\xd7\x19\x1a.\x112\xc2th\xf4\xb07#\x0c\xcaV\x8b\xb0n`\x02B\x85\n\x8c\xcdSb\xe8\nK\x15\x1dL\x1d\x16J\xb1v\x1e\"\xd7A\xa9\xed\xd42\xba\x89\x14\x969\x1cl\xa2y\x84\xd6\xfffn\xae\x8f\xe5\xaci\x9a\x86\xf5T(.\xf1\xd8u:\x1f\xd19\x17\xf0\xbb\xfe\xf3z\xc8!\x0c$\x17x\x9a\x9e;\xf5$\x89\x89\\\xa1e\x03k\xa3T\x01\x8aa\x87J]\xaa\xaa\x98\\D\xc4\x07\xff=\xd0\xa0+\x14\xdd\x05\x17_PRd\xb9$Kl\xe6e\x98\xb8y\x1c\x9b\x1e&\x0cA\xdc\x08j\xa8\x14\xe4\xd7\xaa\x9b\x04\xd1\rT\xc7\xe8\xae\xe1:\x99\xeca\xbc\xb3\x0c\xaazZ\xd3UN\xb2\xc2\xca\xd52\xe2\x1a\xd30\x05U\xc9Z5\x1daD{\xc9Y?\x04Mg)A\xa8w:n\x83(\x08\xb8\x909\xac\xa2P\x1b+\xa7\xe34\x0cA\x86CD\xf1W\xd38#L\x07Luy\x87\xc5|uP\x81\xec\xa03\x1f\x83\xafr\x9b\xbfI{\xc0\x910o\xabT\xb4\x05\x0f\xd2{d\x00\"&\x1e\xfc!\xdew\rt\x1a\x04\xea\xab\xcb\xa9\x0f\xe2\x92c\xf5\x99\x1b\xcd\x98\xc6D\xb1#\xe3\xd1#\xe9\xbd\xa4\xa4\x8dF\xa34\xd8\xb7DR\xf8\xd7\x12\xf6X\xce\xe7<X\t2\x9d\xc9O\x80\xc5\x7f^\xa5\xfd\xb3\x9b\'+T\xdbJfk\xf9u\x1a\x8a\x01H\xa9\xbdT\xb1\xd6\xa0\xfc\x0b\xca\xc7\x98\xb6\xb1\xc4\xf5\xc3\xff\xaeQR]\xaf\x01;\x87\xe5\xb5\xca%aFrc\x03;\xfc0\xb0\x1c\x96$\xdf\xea\n\x80>\xc5+\xa5:U#E_\x9b\xe6.\xe7[&w\xb8nc\x12\xae\xceg\xea*\xd6\x05g\\\xab\xb5\xa9\x8bi\x08\xfb\x18W_\x01\x08I \xcc\x17\xa8\x8aX\xd7Gu#\xcb\xd6.k\xb3w\xd5-b\xbfZ\x83\xec|s\xaag\x90\xeblc\xde\xc3\x7f\xd5x(\xba/vk=\x80\xa2V\xe5zX1\xc4[\xdb\xae\xb5g\xdb\xaa\xd2+\x99*\x8al\xabZ\xd1\xdeB\xb4\x7f46#\xa4h\xab\xdc\xc9\xf5a(kVo\xca\xea.iU\xdf\x11\xaa\x8f\xb5\xb0t@Ck\xc5d\r,\xe1P\xd6\xb8\xe4\xde\xfaB\xda*V\xfb\x1e\x9c\xfd\xe3P\x9e?\xcfT\x11%\xb7\x7f\xbd\x1c\xee\x8d\xa4\xe7\x8b\xc3\x96\xdf\x17\xd3\x17zh\xbd\xd4\xd6P\xd8\x9e\xbe;l+\xff\xa9\xd2\xfa\tPK\x01\x023\x00\x14\x00\x00\x00\x08\x00T\x88VE\xa1\xf9\xe4\xb8\x06\x00\x00\x00\x04\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00___CopyrightYearPK\x01\x023\x00\x14\x00\x00\x00\x08\x00T\x88VEr\xe9\x0e\xe0\t\x00\x00\x00\x07\x00\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x004\x00\x00\x00___ProjectTitlePK\x01\x023\x00\x14\x00\x00\x08\x08\x00\x05\x94\xa9N\x0e\xc5\xcb\xd7\x08\x00\x00\x00\x16\x00\x00\x00\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00j\x00\x00\x00ActivityAssets.lazPK\x01\x023\x00\x14\x00\x00\x08\x08\x00\x05\x94\xa9N\x89\x9fa\x01\xf6\x01\x00\x00\x04\x04\x00\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa2\x00\x00\x00Activity.x3aPK\x01\x023\x00\x14\x00\x00\x08\x08\x00\x05\x94\xa9NHu\xf8\xec\x11\x03\x00\x008\n\x00\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc2\x02\x00\x00Main.ev3pPK\x01\x023\x00\x14\x00\x00\x08\x08\x00\x05\x94\xa9Nv\x8c2j \x03\x00\x00\xc0\x0f\x00\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfa\x05\x00\x00Project.lvprojxPK\x05\x06\x00\x00\x00\x00\x06\x00\x06\x00i\x01\x00\x00G\t\x00\x00\x00\x00")
		if (not ntpath.exists(f"{p}index.bat")):
			with open(f"{p}index.bat","x") as f:
				f.write(f"@echo off\ncls\n\"C:/Program Files/LEGO Software/LEGO MINDSTORMS EV3 Home Edition/MindstormsEV3.exe\" {p}index.ev3")
	if (op==True):
		_open_prog_w(type_.title()+"-"+name)
	_save_w()



class _CMDLineWebSocketServer_handle(WebSocket):##############################
	def handleMessage(self):
		threading.Thread(target=self._h_msg,args=(),kwargs={}).start()



	def handleConnected(self):
		pass



	def handleClose(self):
		pass



	def _h_msg(self):
		global CMD_L
		def _h_std(self,t):
			global CMD_L
			l={}
			while (self._stop==False):
				for k in list(CMD_L[self.h_nm]["l"].keys()):
					if (k not in l.keys()):
						l[k]=0
					if (l[k]!=len(CMD_L[self.h_nm]["l"][k])):
						l[k]=self.sendMessage(bytes(t+":","utf-8")+CMD_L[self.h_nm]["l"][k][l[k]:])
						l[k]=len(CMD_L[self.h_nm]["l"][k])
				time.sleep(0.05)
		msg=self.data
		self.sendMessage("null")
		if (msg=="cmdl"):
			self.sendMessage("cmdl:"+"\x00".join(list(CMD_L.keys())))
		elif (msg[:4]=="cmd:"):
			if (msg[4:] not in list(CMD_L.keys())):
				self.sendMessage("cmd:0")
			else:
				self._stop=True
				self.h_nm=msg[4:]
				self.sendMessage(f"cmd:1{self.h_nm}")
				if (hasattr(self,"_thr_l")):
					for k in self._thr_l:
						k.join()
				self._stop=False
				self._thr_l=[threading.Thread(target=_h_std,args=(self,"out"),kwargs={}),threading.Thread(target=_h_std,args=(self,"err"),kwargs={})]
				self._thr_l[0].start()
				self._thr_l[1].start()
		elif (msg[:3]=="in:"):
			if (hasattr(self,"h_nm")==False or self.h_nm==None):
				return
			CMD_L[self.h_nm]["h"].stdin.write(bytes(msg[3:],"utf-8"))
			CMD_L[self.h_nm]["h"].stdin.flush()



def _start_ws(t):
	def _h_request(cs,a,ip):
		global WORKSPACE_DATA
		try:
			_dt=cs.recv(65536)
			if (len(_dt)==0):
				_print(f"Skipping Empty Request From '{a[0]}:{a[1]}'\x1b[38;2;100;100;100m..")
				return
			(t,url,v),h,dt=str(_dt.split(b"\r\n")[0],"utf-8").split(" "),{str(e.split(b":")[0],"utf-8"):e[len(e.split(b":")[0])+2:] for e in _dt.split(b"\r\n\r\n")[0].split(b"\r\n")[1:] if len(e)!=0},_dt[len(_dt.split(b"\r\n\r\n")[0])+4:]
			rc=-1
			_print(f"Request Recived: (type='{t}', url='{url}', http_version='{v}', ip='{a[0]}:{a[1]}')")
			if (t=="GET"):
				_print("Inspecting IP and URL\x1b[38;2;100;100;100m...")
				if ((a[0]=="127.0.0.1" or a[0]==LOCAL_IP or a[0] in WORKSPACE_IP_WHITELIST) and (url=="/" or url=="/cmd" or len(url)-len(url.replace("/",""))>=2)):
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
						if (url=="/cmd"):
							url="/server.html"
						if (url.endswith("/")):
							url+="index.html"
						url="."+url
						if (not ntpath.exists(url)):
							_print(f"\x1b[38;2;200;40;20mFile '{url}' Doesn't Exist.\x1b[0m Sending Redirect\x1b[38;2;100;100;m100...")
							cs.send(bytes(f"HTTP/1.1 301 Moved Permanently\r\nLocation: http://{ip}:8020/\r\n\r\n","utf-8"))
							rc=301
						else:
							_print(f"Sending Content of '{url}'\x1b[38;2;100;100;100m...")
							f=open(url,"rb")
							cs.send(bytes(f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nContent-Length: {str(os.fstat(f.fileno())[6])}\r\n\r\n","utf-8")+f.read())
							rc=200
				else:
					_print(f"\x1b[38;2;200;40;20mUnauthorised Request From '{a[0]}:{a[1]}'\x1b[38;2;200;40;20m for URL '{url}'\x1b[38;2;200;40;20m.\x1b[0m Sending Blocking Request\x1b[38;2;100;100;100m...")
					f=open("no_access.html","rb")
					cs.send(bytes(f"HTTP/1.1 401 Unauthorised\r\nContent-Type: text/html\r\nContent-Length: {str(os.fstat(f.fileno())[6])}\r\n\r\n","utf-8")+f.read())
					f.close()
					rc=401
			elif (t=="CHANGE_DESC"):
				pg=url[1:].split("~")[0]
				dc=urllib.parse.unquote("~".join(url[1:].split("~")[1:]),errors="surrogatepass")
				_print(f"Changing Description for Project '{pg}' to '{dc}'\x1b[38;2;100;100;100m...")
				for o in WORKSPACE_DATA:
					if (o["name"]==pg):
						o["desc"]=dc
				_save_w()
				cs.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 0\r\n\r\n")
				rc=200
			elif (t=="START_PROG"):
				_print(f"Opening Project '{url[1:]}'\x1b[38;2;100;100;100m...")
				_open_prog_w(url[1:])
				cs.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 0\r\n\r\n")
				rc=200
			elif (t=="VIEW_PROG"):
				if (ntpath.exists(f"D:\\K\\Coding\\projects\\{url[1:]}\\index.bat")):
					_print(f"Viewing Project '{url[1:]}' in Console\x1b[38;2;100;100;100m...")
					os.system(f"start /min cmd /c \"@echo off&&cls&&cd /d D:\\K\\Coding\\projects\\{url[1:]}\\&&index.bat\"")
				else:
					_print(f"Viewing Project '{url[1:]}' in File Explorer\x1b[38;2;100;100;100m...")
					subprocess.run([os.path.join(os.getenv("WINDIR"),"explorer.exe"),"/select,"+os.path.normpath(os.getcwd()+os.sep+f"D:\\K\\Coding\\projects\\{url[1:]}"+"/"+os.listdir(p)[0])])
				cs.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 0\r\n\r\n")
				rc=200
			elif (t=="NEW_PROG"):
				_print(f"Creating Project (type='{url[1:].split('~')[0]}', name='{url[1:].split('~')[1]}')\x1b[38;2;100;100;100m...")
				_create_prog(*url[1:].split("~"))
				cs.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 0\r\n\r\n")
				rc=200
			elif (t=="LIST_PROGS"):
				_print(f"Sending Project List\x1b[38;2;100;100;100m...")
				s=""
				for d in WORKSPACE_DATA:
					s+=str(d["name"])+","+str(d["year"])+","+str(d["desc"])+"|"
				cs.send(bytes(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(s[:-1])}\r\n\r\n{s[:-1]}","utf-8"))
				rc=200
			elif (t=="DOWNLOAD_PROG"):
				_print(f"Zipping Project '{url[1:]}'\x1b[38;2;100;100;100m...")
				fnm=f"D:\\boot\\tmp\\{time.time()}.zip"
				zipf=zipfile.ZipFile(fnm,"w",zipfile.ZIP_DEFLATED)
				for root,_,fs in os.walk(f"D:\\K\\Coding\\projects\\{url[1:]}\\"):
					for f in fs:
						_print("Zipping: "+os.path.join(root.replace(f"D:\\K\\Coding\\projects\\{url[1:]}\\",""),f))
						zipf.write(os.path.join(root,f),arcname=os.path.join(root.replace(f"D:\\K\\Coding\\projects\\{url[1:]}\\",""),f))
				zipf.close()
				cs.send(bytes(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(fnm.split(chr(92))[-1])+4}\r\n\r\ntmp/{fnm.split(chr(92))[-1]}","utf-8"))
				rc=200
			else:
				cs.send(b"HTTP/1.1 501 Not Implemented\r\n\r\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\"><title>Error</title></head><body><h1>501</h1><h3>Not Implemented</h3></body></html>")
				rc=501
			_print(f"Finished Processing Request with Response Code {rc}.")
		except Exception as e:
			_print("\x1b[38;2;200;40;20mError Occured During Procesing of Request.\x1b[0m (Finished Processing Request with Response Code 500)")
			cs.send(b"HTTP/1.1 500 Internal Server Error\r\n\r\n<html><head><meta http-equiv=\"Content-Type\" content=\"text/html;charset=utf-8\"><title>Error</title></head><body><h1>500</h1><h3>Internal Server Error</h3></body></html>")
			traceback.print_exception(None,e,e.__traceback__)
		cs.close()
	if (t==0):
		_print(f"Starting WebSocket Listener on IP '{LOCAL_IP}:8021'\x1b[38;2;100;100;100m...")
		ws_s=SimpleWebSocketServer(LOCAL_IP,8021,_CMDLineWebSocketServer_handle).serveforever()
	if (t==1):
		global WORKSPACE_PHP_PID
		_print(f"Starting PHP Server on IP '127.0.0.1:{WORKSPACE_PHP_SERVER_PORT}'\x1b[38;2;100;100;100m...")
		p=subprocess.Popen(["C:/Program Files/PHP/php.exe","-S",f"127.0.0.1:{WORKSPACE_PHP_SERVER_PORT}"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,cwd="D:\\K\\Coding\\")
		WORKSPACE_PHP_PID=p.pid
		_r_cmd("php_server",lambda:None,p)
	elif (t==2):
		_print("Starting Remote Std Listener on '127.0.0.1:8022'\x1b[38;2;100;100;100m...")
		threading.current_thread()._df=True
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind(("127.0.0.1",8022))
		s.listen(5)
		while (True):
			cs=s.accept()[0]
			dt=cs.recv(65536)
			threading.current_thread()._b_nm,threading.current_thread()._nm=str(dt,"utf-8").split("\x00")[:2]
			_print(str(dt[len(b" ".join(dt.split(b"\x00")[:2]))+1:],"utf-8"))
			cs.close()
		s.close()
	else:
		_print(f"Starting Server on IP '{('localhost' if t==3 else LOCAL_IP)}:8020'\x1b[38;2;100;100;100m...")
		s_a=socket.getaddrinfo(("localhost" if t==3 else LOCAL_IP),8020,0,socket.SOCK_STREAM,socket.IPPROTO_TCP,socket.AI_PASSIVE)
		s=socket.socket(*s_a[0][:2])
		s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		s.bind(s_a[0][4])
		s.listen(5)
		while (True):
			_h_request(*s.accept(),("localhost" if t==3 else LOCAL_IP))
		s.close()



def _sw_kb():
	global KB_PID
	_set_print("__core__","onscreen_keyboard")
	try:
		subprocess.check_output(f"taskkill /pid {KB_PID} /f")
		KB_PID=-1
		_print("Disabling On-Screen Keyboard\x1b[38;2;100;100;100m...")
	except:
		KB_PID=subprocess.Popen(["javaw","-jar","D:\\boot\\Keyboard.jar"]).pid
		_print("Enabling On-Screen Keyboard\x1b[38;2;100;100;100m...")



def _chk_a():
	return True############################
	try:
		return ctypes.windll.shell32.IsUserAnAdmin()
	except:
		return False



def _ut_k():
	_print("Starting Useless Task Kill Loop\x1b[38;2;100;100;100m...")
	while (True):
		tl=subprocess.run("tasklist",stdout=subprocess.PIPE).stdout.lower().decode("utf-8")
		for v in ["totalav.exe","nvsphelper64.exe","\"nvidia share.exe\"","\"nvidia web helper.exe\"","\"nvdisplay.container.exe\""]:
			if (v.replace("\"","") in tl):
				os.system(f"taskkill /im {v} /f")
		time.sleep(5)



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
		_print(f"File Hash: {h.hexdigest()}, New Hash: {json['sha1']}")
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
	print("Stopping all Server\x1b[38;2;100;100;100m...")
	for v in list(CMD_L.values())[:]:
		v["_end"]()
	subprocess.Popen(["C:\\Windows\\System32\\shutdown.exe"]+a+["/f"])



os.system("cls")
if (len(sys.argv)==1):
	if (_chk_a()==True):
		ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),ctypes.wintypes.DWORD(7))
		CMD_L["__core__"]={"_end":lambda:None,"h":type("VoidHandle",(object,),{"stdin":io.StringIO}),"l":{"__main__":b""}}
		threading.current_thread()._b_nm="__core__"
		threading.current_thread()._nm="__main__"
		_print("Starting Boot Sequence...\nClearing Temp Dir\x1b[38;2;100;100;100m...")
		for fnm in os.listdir("D:\\boot\\tmp\\"):
			os.remove(f"D:\\boot\\tmp\\{fnm}")
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
		keyboard.add_hotkey("ctrl+alt+shift+k",_sw_kb)
		keyboard.add_hotkey("ctrl+alt+shift+v",lambda:_open_app(["python","D:\\boot\\boot.py","2"]))
		_print("Starting Minecraft Servers\x1b[38;2;100;100;100m...")
		_start_thr(_u_mcs,"__core__","minecraft_redstone_server_updater","D:\\boot\\mcs")
		_start_thr(_u_mcs,"__core__","minecraft_survival_server_updater","D:\\boot\\mcs-s")
		_print("Starting Codewars ChromeDriver\x1b[38;2;100;100;100m...")
		_start_thr(_codewars_wr,"__core__","codewars_driver")
		_print("Starting Useless Task Kill Loop\x1b[38;2;100;100;100m...")
		_start_thr(_ut_k,"__core__","useless_task_kill")
		# _print("Starting Backup Check\x1b[38;2;100;100;100m...")
		# with open("./_backup_tmp.bat","w") as f:
		# 	f.write(f"@echo off\ncls\ncd /d \"D:\\boot\"\npython boot.py 4\ndel _backup_tmp.bat")
		# os.system("vdesk create:3&&vdesk on:3 run:cmd /c \"_backup_tmp.bat\"&&vdesk on:1 run:cmd /c \"echo\"")
		_print("Removing Old Project Registry\x1b[38;2;100;100;100m...")
		nm=[]
		p_nm_l=[e.lower() for e in os.listdir("D:\\K\\Coding\\projects\\")]
		with open("D:\\boot\\workspace-data.json","r") as f:
			WORKSPACE_DATA=json.loads(f.read())
			for k in [*WORKSPACE_DATA]:
				if (k["name"].lower() not in p_nm_l):
					WORKSPACE_DATA.remove(k)
					continue
				# _create_prog(k["name"].split("-")[0].lower(),k["name"].split("-")[1].lower(),op=False)
				nm+=[k["name"].lower()]
		_print("Registering New Projects\x1b[38;2;100;100;100m...")
		for f in os.listdir("D:\\K\\Coding\\projects\\"):
			if (f.lower() not in nm):
				WORKSPACE_DATA+=[{"name":f.split("-")[0]+"-"+"_".join([e.title() for e in f.split("-")[1].split("_")]),"desc":"[null]","year":datetime.datetime.now().year}]
				_create_prog(k["name"].split("-")[0].lower(),k["name"].split("-")[1].lower(),op=False)
		_print("Saving Project Registry\x1b[38;2;100;100;100m...")
		_save_w()
		_print("Starting WebSocket CMD Server\x1b[38;2;100;100;100m...")
		_start_thr(_start_ws,"__core__","cmdline_websocket_server",0)
		_print("Starting PHP Server\x1b[38;2;100;100;100m...")
		_start_thr(_start_ws,"__core__","php_server",1)
		_print(f"Startint Remote Std Listener\x1b[38;2;100;100;100m...")
		_start_thr(_start_ws,"__core__","remote_std_server",2)
		_print("Starting Localhost Server\x1b[38;2;100;100;100m...")
		_start_thr(_start_ws,"__core__","localhost_server",3)
		_print("Starting Local IP Server\x1b[38;2;100;100;100m...")
		_start_thr(_start_ws,"__core__","local_ip_server",4)
		_print("Starting Infinite Loop\x1b[38;2;100;100;100m...")
		try:
			while (True):
				time.sleep(1e6)
		except:
			pass
		os.system(f"taskkill /pid {os.getpid()} /f")
	else:
		ctypes.windll.shell32.ShellExecuteW(None,"runas",sys.executable,"D:\\boot\\boot.py",None,1)
else:
	v=int(sys.argv[1])
	if (v==0):
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
		_rec_rm_pycache("D:\\")
	elif (v==1):
		while (True):
			p=input("> ").lower().strip()
			if (p=="list"):
				os.system("cls")
				_print("list, chrome, python, python37, processing, mindstorm, fischer, sublime, minecraft, batexe, vm, android, github, blender, scratch, idea, print, work, cad, regedit, ev3, <kata url>, <git clone url>, <any url>")
				continue
			elif (p=="chrome"):
				_open_app("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
			elif (p=="python"):
				_open_app("%appdata%\\..\\Local\\Programs\\Python\\Python38\\python.exe")
			elif (p=="python37"):
				_open_app("%appdata%\\..\\Local\\Programs\\Python\\Python37\\python.exe")
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
			elif (p=="batexe"):
				_open_app("C:\\Program Files\\Bat To Exe Converter\\Bat_To_Exe_Converter.exe")
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
			elif (p=="idea"):
				_open_app(r"D:\K\.IDEA",file=True)
				_open_app(["C:\\Program Files\\Sublime Text 3\\sublime_text.exe","--add",r"D:\K\.IDEA\.IDEA"])
			elif (p=="print"):
				_open_app("C:\\Program Files\\RepetierGEEEtech\\RepetierHost.exe")
			elif (p=="work"):
				_open_app(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",f"http:/{LOCAL_IP}:8020/"])
			elif (p=="cad"):
				_open_app("C:\\Program Files\\CAD\\FreeCAD 0.18\\bin\\FreeCAD.exe")
			elif (p=="regedit"):
				_open_app("C:\\Windows\\regedit.exe")
			elif (p=="ev3"):
				_open_app("C:\\Program Files\\PuTTY\\putty.exe")
			elif (GIT_CLONE_REGEX.match(p)!=None):
				os.system(f"cd /d D:\\K\\Downloads\\&&git clone {p}")
				_open_app("D:\\K\\Downloads\\"+p.split(".git")[0].split("/")[-1],file=True)
			elif (CODEWARS_KATA_URL_REGEX.match(p)!=None):
				with open("D:\\boot\\codewars-swapfile.dt","a") as f:
					f.write("1"+p)
			elif (URL_REGEX.match(p)!=None):
				_open_app(["C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",p])
			elif (p=="" or p=="exit"):
				break
			else:
				os.system("cls")
				continue
			break
	elif (v==2):
		jar=input("File Path?\t")
		type_=input("Exe Type?\t")
		mc=None
		jar_zip=zipfile.ZipFile(jar,"r")
		for k in str(jar_zip.read("META-INF/MANIFEST.MF"))[2:-1].split("\\n"):
			if (k.startswith("Main-Class:")):
				mc=k.split(":")[1].strip().replace("\\r","")
		st=time.time()
		cp=ntpath.abspath(f"D:\\boot\\tmp\\xml-{st}.xml")
		op=ntpath.abspath(f"D:\\boot\\tmp\\{st}.exe")
		with open(f"D:\\boot\\tmp\\xml-{st}.xml","w") as f:
			f.write(f"""
<?xml version="1.0" encoding="UTF-8"?>
<launch4jConfig>
	<dontWrapJar>false</dontWrapJar>
	<headerType>{type_}</headerType>
	<jar>{jar}</jar>
	<outfile>{op}</outfile>
	<errTitle></errTitle>
	<cmdLine></cmdLine>
	<chdir>.</chdir>
	<priority>normal</priority>
	<downloadUrl>http://java.com/download</downloadUrl>
	<supportUrl></supportUrl>
	<stayAlive>true</stayAlive>
	<restartOnCrash>false</restartOnCrash>
	<manifest></manifest>
	<icon></icon>
	<classPath>
		<mainClass>{mc}</mainClass>
	</classPath>
	<jre>
		<path>C:\\Program Files (x86)\\Java\\jre1.8.0_231\\</path>
		<bundledJre64Bit>true</bundledJre64Bit>
		<bundledJreAsFallback>false</bundledJreAsFallback>
		<minVersion></minVersion>
		<maxVersion></maxVersion>
		<jdkPreference>preferJre</jdkPreference>
		<runtimeBits>64/32</runtimeBits>
	</jre>
</launch4jConfig>
		""")
		os.chdir("\\".join(jar.split("\\")[:-1]))
		os.system(f"\"C:\\Program Files (x86)\\Launch4j\\launch4jc.exe\" {cp}")
		shutil.copyfile(op,jar.split("\\")[-1]+".exe")
		os.remove(cp)
		os.remove(op)
	elif (v==3):
		if (sys.argv[2] not in ["--local","--final"]):
			_print(f"Unknown Switch: '{sys.argv[2]}'")
		else:
			_render_cwr(sys.argv[2])
	elif (v==4):
		if (len(sys.argv)==2):
			ho=ctypes.windll.kernel32.GetStdHandle(-11)
			dw_m=ctypes.wintypes.DWORD()
			ctypes.windll.kernel32.GetConsoleMode(ho,ctypes.byref(dw_m))
			dw_m.value|=4
			ctypes.windll.kernel32.SetConsoleMode(ho,dw_m)
			msg=datetime.datetime.now().strftime("Push Update %m/%d/%Y, %H:%M:%S")
			tm=int(time.time()//604800)
			with open("./backup.dt","r") as f:
				b_dt=f.read().replace("\r","").split("\n")
			with open("./backup.dt","w") as f:
				if (len(b_dt[0])==0 or int(b_dt[0])<tm):
					b_dt=[None]
				f.write(str(tm)+"\n")
				f.flush()
				for p in os.listdir("D:\\K\\Coding\\projects"):
					if (p in b_dt[1:]):
						f.write(p+"\n")
						f.flush()
						continue
					_update_repo(f"D:\\K\\Coding\\projects\\{p}",p,p.split("-")[0]+" - "+p.split("-")[1].replace("_"," ").title(),msg)
					f.write(p+"\n")
					f.flush()
				if ("Boot_Program" in b_dt[1:]):
					f.write(p+"\n")
					f.flush()
				else:
					_update_repo("D:\\boot\\Boot_Program",p,"Boot Program",msg)
					f.write(p+"\n")
					f.flush()
		else:
			ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),ctypes.wintypes.DWORD(7))
			threading.current_thread()._b_nm="__core__"
			threading.current_thread()._nm="github_project_push"
			threading.current_thread()._dpt=True
			threading.current_thread()._r=2
			nm=(re.sub(r"[^A-Za-z0-9_.-]","",sys.argv[2].replace("D:\\K\\Coding\\projects\\","").split("\\")[0]) if sys.argv[2].lower().startswith("d:\\k") else "Boot_Program")
			dc=("None (auto)" if sys.argv[2].lower().startswith("d:\\k") else "'Boot Program'")
			msg=datetime.datetime.now().strftime('Push Update %m/%d/%Y, %H:%M:%S')
			_print(f"Pushing Project to Github: (path='{sys.argv[2]}', name='{nm}', desc={dc}, commit_message='{msg}')")
			threading.current_thread()._dp=True
			threading.current_thread()._df=True
			threading.current_thread()._r=1
			_update_repo(sys.argv[2],(re.sub(r"[^A-Za-z0-9_.-]","",sys.argv[2].replace("D:\\K\\Coding\\projects\\","").split("\\")[0]) if sys.argv[2].lower().startswith("d:\\k") else "Boot_Program"),(None if sys.argv[2].lower().startswith("d:\\k") else "Boot Program"),msg)
			input("\x1b[38;2;50;50;50m<ENTER>\x1b[0m")

@echo off
cd "C:\Users\aleks\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\boot"
vdesk create:3
vdesk on:3 noswitch:true run:python boot.py
vdesk on:1 run:echo

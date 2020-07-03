@echo off
cd /d "D:\boot"
vdesk create:3
vdesk on:3 noswitch:true run:cmd /k "python boot.py"
vdesk on:1 run:cmd /c "echo"

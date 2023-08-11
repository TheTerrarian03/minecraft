: Sources:
: request admin:       https://stackoverflow.com/questions/206114/batch-files-how-to-read-a-file
: turn on/off wifi:    https://forums.tomshardware.com/threads/i-want-to-turn-wifi-on-off-with-a-desktop-shortcut.2611220/
: start a program:     https://stackoverflow.com/questions/324539/how-can-i-run-a-program-from-a-batch-file-without-leaving-the-console-open-after
: current directories: https://stackoverflow.com/questions/4419868/what-is-the-current-directory-in-a-batch-file
: defining variables:  https://stackoverflow.com/questions/10552812/defining-and-using-a-variable-in-batch-file
: reading files:       https://stackoverflow.com/questions/206114/batch-files-how-to-read-a-file
: 
: made by Logan on 08102023

@echo off
title auto-run minecraft!

echo asking for admin access
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /b
)

: echo disabling wifi
: netsh interface set interface "Wi-Fi" Disable
: 
: echo wifi disabled
: echo renaming account to "nova"
: python %~dp0change_name.py
: 
: echo done, starting minecraft
: start "" "C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe"
: 
: pause
: netsh interface set interface "Wi-Fi" Enable

: set location=Bob
: echo %location%
: echo "We're working with %location%"
: pause

set TRUE=1==1
set FALSE=1==0

set SETTINGS_FILE=%~dp0bat_settings.ini

for /f "tokens=1,2 delims==" %%a in (%SETTINGS_FILE%) do (
    : disabling/enabling wifi
    if %%a==disableAndEnableWifi if %%b==True set TOGGLEWIFI=%TRUE%
    if %%a==disableAndEnableWifi if %%b==False set TOGGLEWIFI=%FALSE%

    : setting name
    if %%a==setName if %%b==True set SETNAME=%TRUE%
    if %%a==setName if %%b==False set SETNAME=%FALSE%

    : new name
    if %%a==newName set NEWNAME=%%b

    : banana
    if %%a
)

if %toggleWifi% (
    echo success
)

echo %toggleWifi%
pause

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
@REM title auto-run minecraft!

set TRUE=1==1
set FALSE=1==0

: write settings for profile
start /wait python3 %~dp0write_settings.py

: assign settings file
set SETTINGS_FILE=%~dp0bat_settings.ini

: getting bat settings
for /f "tokens=1,2 delims==" %%a in (%SETTINGS_FILE%) do (
    : disabling/enabling wifi
    if %%a==run_offline if %%b==True set OFFLINE=%TRUE%
    if %%a==run_offline if %%b==False set OFFLINE=%FALSE%

    : setting name
    if %%a==change_name if %%b==True set SETNAME=%TRUE%
    if %%a==change_name if %%b==False set SETNAME=%FALSE%

    : new name
    if %%a==new_name set NEWNAME=%%b

    : auto click play button
    if %%a==auto_click_play if %%b==True set AUTOCLICK=%TRUE%
    if %%a==auto_click_play if %%b==False set AUTOCLICK=%FALSE%
)

: if working with wifi, ask for admin access
if %OFFLINE% (
        if not "%1"=="am_admin" (
        powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
        exit /b
    )
)

: now, disable wifi if needed
if %OFFLINE% (
    netsh interface set interface "Wi-Fi" Disable
    netsh interface set interface "Ethernet" Disable
)

: run minecraft
python -c "import subprocess; subprocess.Popen(['C:\Program Files (x86)\Minecraft Launcher\MinecraftLauncher.exe'])"

: run press button
if %AUTOCLICK% (
    : run python script to look for button to press
    python3 %~dp0auto_click_play.py %~dp0 30
    echo %~dp0
) else (
    : pause and ask user to press enter when minecraft played
    cscript //nologo %~dp0send_message.vbs "Please press ENTER or RETURN here once you have pressed the PLAY button."
)

if %OFFLINE% (
    netsh interface set interface "Wi-Fi" Enable
    netsh interface set interface "Ethernet" Enable
)

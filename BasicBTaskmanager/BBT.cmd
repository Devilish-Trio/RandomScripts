@echo off
title BBT (a Basic B*tch Taskmanger)
color 04

hostname
systeminfo | findstr /C:"Total Physical Memory"
echo.
tasklist | sort /R /+58
echo Calculating TOTAL Memory Usage...#systeminfo |find "Available Physical Memory"
echo.
echo.
echo Type what process you want to kill with the .EXE - eg. chrome.exe
echo.
set /p name=Taskkill /IM %name% /f ----- 
taskkill /IM %name% /f
pause
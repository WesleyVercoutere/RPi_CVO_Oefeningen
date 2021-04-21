@echo off

SET count=0
SET /p subnet=Please enter IP address range (for example, 192.168.0)

:start
SET /a count=%count%+1

cls
ECHO. & ECHO Trying %subnet%.%count% & ECHO.

ping -n 1 -w 1000 %subnet%.%count% >nul  
IF %errorlevel%==0 echo %subnet%.%count% UP >> D:\Temp\pingnet.log  
IF %errorlevel%==1 echo %subnet%.%count% DOWN >> D:\Temp\pingnet.log

IF %count%==254 goto :eof

GOTO start
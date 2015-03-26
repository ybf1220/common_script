@echo off
cls
goto :begin


:begin
echo --------------------------------------------------
echo Search Who Use BTS manager Logined Specific ENODEB
echo --------------------------------------------------
set /p IP=Input Enodeb Ip address or all:
if "%IP%"=="" (
cls
goto begin
)
if "%IP%"=="all" (
cls
goto all
)else (
goto process
)

:process
echo Searching ......
netstat -ano |findstr "%IP%:12000" >T:\bts_program.txt
for /F "tokens=5" %%p in (T:\bts_program.txt) do (
  tasklist /V |findstr %%p >T:\bts_user.txt
  for /F "tokens=8" %%i in (T:\bts_user.txt) do (
     echo/
     echo %%i Connected %IP%  PID is  %%p
     echo Use "taskkill /PID %%p /F" To Kill This Connection     
  ) 
)
pause

:all
echo Searching all connection......
netstat -ano |findstr "12000" >T:\bts_program.txt
for /F "tokens=3,5*" %%a in (T:\bts_program.txt) do (
  rem echo IP:%%a  PID:%%b
  tasklist /V |findstr %%b >T:\bts_user.txt
  for /F "tokens=7,8,10,12*" %%i in (T:\bts_user.txt) do (
     echo/
     echo %%i %%j Connected %%a PID is  %%b
     echo Use "taskkill /PID %%b /F" To Kill This Connection
     echo/       
  ) 
)
pause


@echo off
cls
goto :begin
goto :process



:begin
echo --------------------------------------------------
echo Search Who Use BTS manager Logined Specific ENODB
echo --------------------------------------------------
set /p IP=Input Enodeb Ip address:
if "%IP%"=="" (
cls
goto begin
)

:process
echo Searching ......
netstat -ano |findstr "%IP%:12000" >D:\bts_program.txt
for /F "tokens=5" %%p in (D:\bts_program.txt) do (
  tasklist /V |findstr %%p >D:\bts_user.txt
  for /F "tokens=8" %%u in (D:\bts_user.txt) do (
     echo %%u Connected %IP%  PID is  %%p
     echo Use "taskkill /PID %%p /F" to Kill This Connection
  ) 

)
pause



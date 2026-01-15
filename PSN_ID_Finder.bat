@echo off
title PSN Online ID Finder by lI_Isekai_Il

:begin
cls
echo.
echo               UwU
echo.


python ".\.py"
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [!] Warning: Python script exited with errors.
    echo.
)


:ask
echo.
set /p choice="Do you want to run it again, Babe? (UwU/UHHH to exit): "
if /I "%choice%"=="UwU" goto begin
if /I "%choice%"=="UHHH" exit
echo Invalid choice, please type UWU or UHHH.
goto ask

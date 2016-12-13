rem Official Spigot bat found at https://www.spigotmc.org/wiki/buildtools/#windows
@echo off
set startdir=%~dp0
set bashdir="C:\Program Files\Git\bin\bash.exe"
%bashdir% --login -i -c "java -jar ""%startdir%\buildtools.jar"""
pause

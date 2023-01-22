@echo off
cls

chcp 65001 > nul

title Setup by zPuerta 

color 06

echo ███████╗███████╗████████╗██╗   ██╗██████╗             ██╗
echo ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗           ███║
echo ███████╗█████╗     ██║   ██║   ██║██████╔╝ ██║   ██║ ╚██║
echo ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝  ██╗   ██╝  ██║
echo ███████║███████╗   ██║   ╚██████╔╝██║       ╚████╔╝   ██║
echo ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝        ╚═══╝    ╚═╝

set /p menu="Would you like to automatically install the dependencies? [Y/N]"
       if %menu%==Y goto InstallDep
       if %menu%==y goto InstallDep
       if %menu%==N goto Run
       if %menu%==n goto Run


:InstallDep:
color 0A
echo - Installing Dependencies
pip install pystyle > nul 
echo -- PyStyle
pip install alive-progress > nul
echo -- Alive Progress
set /p menu="Would you like to automatically run the script? [Y/N]"
       if %menu%==Y goto Run
       if %menu%==y goto Run
       if %menu%==N exit
       if %menu%==n exit

:Run:
py DaysLeftTo_v1.py



                                                       

@echo off
call "%~dp0env_for_icons.bat"
cd/D "%WINPYWORKDIR%"
if exist "%WINPYDIR%\Lib\site-packages\PyQt5\examples\qtdemo\qtdemo.py" (
    "%WINPYDIR%\python.exe" "%WINPYDIR%\Lib\site-packages\PyQt5\examples\qtdemo\qtdemo.py"
)  
if exist "%WINPYDIR%\Lib\site-packages\PyQt4\examples\demos\qtdemo\qtdemo.pyw" (
    "%WINPYDIR%\pythonw.exe" "%WINPYDIR%\Lib\site-packages\PyQt4\examples\demos\qtdemo\qtdemo.pyw"
)

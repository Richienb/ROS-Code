@echo off
call "%~dp0env_for_icons.bat"
cd/D "%WINPYWORKDIR%"
if "%QT_API%"=="pyqt5" (
    if exist "%WINPYDIR%\Lib\site-packages\pyqt5-tools\designer.exe" (
        "%WINPYDIR%\Lib\site-packages\pyqt5-tools\designer.exe" %*
    ) else (
        "%WINPYDIR%\Lib\site-packages\PyQt5\designer.exe" %*
    )
) else (
    "%WINPYDIR%\Lib\site-packages\PyQt4\designer.exe" %*
)

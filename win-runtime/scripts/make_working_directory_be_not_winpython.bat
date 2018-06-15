@echo off
set winpython_ini=%~dp0..\\settings\winpython.ini
echo [debug]>"%winpython_ini%"
echo state = disabled>>"%winpython_ini%"
echo [environment]>>"%winpython_ini%"
echo ## <?> Uncomment lines to override environment variables>>"%winpython_ini%"
echo HOME = %%HOMEDRIVE%%%%HOMEPATH%%\Documents\WinPython%%WINPYVER%%\settings>>"%winpython_ini%"
echo JUPYTER_DATA_DIR = %%HOME%%>>"%winpython_ini%"
echo WINPYWORKDIR = %%HOMEDRIVE%%%%HOMEPATH%%\Documents\WinPython%%WINPYVER%%\Notebooks>>"%winpython_ini%"

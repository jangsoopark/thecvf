@echo off


SET MAIN_DIR=%~dp0\..
SET SRC=src/main.py

SET TITLE=cvpr
SET YEAR=2022
SET TYPE=main

PUSHD %MAIN_DIR%

python %SRC%  ^
    --title=%TITLE% ^
    --year=%YEAR% ^
    --type=%TYPE%

POPD
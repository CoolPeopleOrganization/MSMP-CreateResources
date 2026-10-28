@echo off
cd /d "%~dp0"

python "%~dp0incr_version_script.py" "%~dp0pack.toml"

echo.
pause
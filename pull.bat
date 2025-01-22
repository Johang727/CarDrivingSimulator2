@echo off

git pull
if %errorlevel% neq 0 (
    echo Git was unable to pull. Ensure you are logged in!
    echo Pull aborted.
    exit /b %errorlevel%
)

python sb3-repackage.py
if %errorlevel% neq 0 (
    echo Python script failed. Ensure Python is installed! 
    echo Pull aborted.
    exit /b %errorlevel%
)

exit
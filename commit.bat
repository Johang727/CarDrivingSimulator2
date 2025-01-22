@echo off
python sb3-unpack.py
if %errorlevel% neq 0 (
    echo Python script failed. Commit aborted.
    exit /b %errorlevel%
)
git add -A
git commit -a

:prompt
set /p response=Would you like to push changes? (Y/n) 

if /i "%response%"=="Y" (
    git push
) else if /i "%response%"=="N" (
    echo Changes not pushed.
) else (
    echo Invalid input. Please enter Y or N.
    goto prompt
)

exit
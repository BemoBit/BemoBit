@echo off
echo Initializing Git repository and generating commit history...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python and try again.
    exit /b 1
)

:: Check if Git is installed
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Git is not installed or not in PATH. Please install Git and try again.
    exit /b 1
)

:: Initialize Git repository if not already initialized
if not exist .git (
    git init
    echo Git repository initialized.
)

:: Configure Git user if not already configured
git config user.name >nul 2>&1
if %errorlevel% neq 0 (
    echo Please enter your Git username:
    set /p GIT_USERNAME=
    git config user.name "%GIT_USERNAME%"
)

git config user.email >nul 2>&1
if %errorlevel% neq 0 (
    echo Please enter your Git email:
    set /p GIT_EMAIL=
    git config user.email "%GIT_EMAIL%"
)

:: Run the Python script
python git_history_generator.py

echo.
echo Done! Now you can push this repository to GitHub.
echo Use the following commands:
echo git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
echo git branch -M main
echo git push -u origin main --force
echo.
echo Note: You may need to use --force when pushing to override GitHub's history.
pause

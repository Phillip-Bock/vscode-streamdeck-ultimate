@echo off
echo ========================================
echo  Organizing Repository Files
echo ========================================
echo.

REM Create folders if they don't exist
if not exist "docs" mkdir docs
if not exist "assets" mkdir assets
if not exist "config" mkdir config
if not exist "scripts" mkdir scripts

echo Creating folder structure...
echo.

REM Move documentation files to docs folder
echo Moving documentation files...
if exist "START-HERE.txt" move "START-HERE.txt" "docs\" >nul
if exist "FILE-GUIDE.txt" move "FILE-GUIDE.txt" "docs\" >nul
if exist "GITHUB-README.md" move "GITHUB-README.md" "docs\" >nul
if exist "GITHUB-SETUP-GUIDE.txt" move "GITHUB-SETUP-GUIDE.txt" "docs\" >nul
if exist "GITHUB-TEMPLATES-SETUP.txt" move "GITHUB-TEMPLATES-SETUP.txt" "docs\" >nul
if exist "streamdeck-profile-guide.txt" move "streamdeck-profile-guide.txt" "docs\" >nul
if exist "streamdeck-setup-step-by-step.txt" move "streamdeck-setup-step-by-step.txt" "docs\" >nul
if exist "streamdeck-reference-guide.md" move "streamdeck-reference-guide.md" "docs\" >nul
if exist "streamdeck-commands-list.md" move "streamdeck-commands-list.md" "docs\" >nul
if exist "streamdeck-visual-layout.md" move "streamdeck-visual-layout.md" "docs\" >nul
if exist "streamdeck-setup-instructions.md" move "streamdeck-setup-instructions.md" "docs\" >nul

REM Move page files to docs folder
echo Moving page configuration files...
move "page-*.txt" "docs\" >nul 2>&1

REM Move HTML to assets folder
echo Moving cheat sheet to assets...
if exist "streamdeck-cheatsheet.html" move "streamdeck-cheatsheet.html" "assets\" >nul

REM Move config files to config folder
echo Moving configuration files...
if exist "streamdeck-config-generator.json" move "streamdeck-config-generator.json" "config\" >nul
if exist "streamdeck-custom-template.json" move "streamdeck-custom-template.json" "config\" >nul
if exist "streamdeck-import.csv" move "streamdeck-import.csv" "config\" >nul

REM Move Python scripts to scripts folder
echo Moving Python scripts...
if exist "generate_streamdeck_config.py" move "generate_streamdeck_config.py" "scripts\" >nul
if exist "quick_configurator.py" move "quick_configurator.py" "scripts\" >nul

REM Move workflow file to .github/workflows
echo Moving GitHub workflow...
if not exist ".github\workflows" mkdir ".github\workflows"
if exist "validate.yml" move "validate.yml" ".github\workflows\" >nul

REM Move PR template to .github
echo Moving PR template...
if exist "PULL_REQUEST_TEMPLATE.md" move "PULL_REQUEST_TEMPLATE.md" ".github\" >nul

REM Move issue template config to .github/ISSUE_TEMPLATE
echo Moving issue template config...
if exist "config.yml" move "config.yml" ".github\ISSUE_TEMPLATE\" >nul

REM Delete duplicate template files from root (they should only be in .github/ISSUE_TEMPLATE)
echo Removing duplicate template files from root...
if exist "bug_report.md" del "bug_report.md" >nul
if exist "feature_request.md" del "feature_request.md" >nul
if exist "question.md" del "question.md" >nul
if exist "share_config.md" del "share_config.md" >nul

echo.
echo ========================================
echo  Reorganization Complete!
echo ========================================
echo.
echo Your repository is now properly organized:
echo   - docs\ folder with all documentation
echo   - assets\ folder with HTML cheat sheet
echo   - config\ folder with JSON and CSV files
echo   - scripts\ folder with Python scripts
echo   - .github\ folder with templates and workflows
echo.
echo Next step: Commit and push to GitHub!
echo.
pause

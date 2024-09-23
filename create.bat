@echo off
:: Create directories
mkdir client_management
mkdir client_management\templates
mkdir client_management\static
mkdir client_management\static\css
mkdir client_management\static\js

:: Create files
cd client_management
echo. > app.py
echo. > clients.db
echo. > requirements.txt
echo. > README.md

cd templates
echo. > base.html
echo. > login.html
echo. > add_client.html
echo. > view_clients.html
echo. > update_client.html

cd ..\static\css
echo. > styles.css

cd ..\static\js
echo. > scripts.js

cd ..
@echo Folder and file structure created successfully!

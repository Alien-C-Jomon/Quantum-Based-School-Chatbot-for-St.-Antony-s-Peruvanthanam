@echo off
title Q-AI Launcher
cd /d "C:\Users\Alien C Jomon\Documents\Q-AI"

echo Starting Q-AI Backend...
start "Q-AI Backend" cmd /k "qai-env\Scripts\activate && python api.py"

timeout /t 3 /nobreak >nul

echo Starting Q-AI Website...
cd /d "C:\Users\Alien C Jomon\Documents\Q-AI\Website"
start "Q-AI Website" cmd /k "npm run dev"

timeout /t 5 /nobreak >nul

echo Opening Q-AI...
start "" "http://localhost:8080/"

exit
@echo off
echo [✔] Memulai setup lingkungan Python...

REM -- Coba aktifkan pip
python -m ensurepip --default-pip

REM -- Upgrade pip
python -m pip install --upgrade pip

REM -- Install dependency
python -m pip install openai flask python-dotenv

echo.
echo [✔] Instalasi selesai!
echo --------------------------------
echo Menjalankan aplikasi chatbot...
echo --------------------------------

REM -- Jalankan app.py
python app.py

pause
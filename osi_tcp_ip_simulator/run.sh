#!/bin/bash
# Quick Start Script for OSI vs TCP/IP Model Simulator (Linux/macOS)

clear
echo "============================================================"
echo "OSI vs TCP/IP Model Visual Simulator"
echo "============================================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed"
    echo "Please install Python from https://www.python.org/"
    exit 1
fi

echo "[*] Checking for Flask installation..."
python3 -c "import flask" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "[!] Flask not found, installing dependencies..."
    python3 -m pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install dependencies"
        exit 1
    fi
    echo "[OK] Dependencies installed"
fi

echo ""
echo "============================================================"
echo "Starting Flask Server..."
echo "============================================================"
echo ""
echo "[*] Server is starting at http://localhost:5000"
echo "[*] Opening browser..."
echo ""
echo "Press CTRL+C to stop the server"
echo "============================================================"
echo ""

# Wait a moment
sleep 2

# Try to open browser (works on macOS and some Linux systems)
if command -v xdg-open &> /dev/null; then
    xdg-open "http://localhost:5000"
elif command -v open &> /dev/null; then
    open "http://localhost:5000"
else
    echo "[*] Please open http://localhost:5000 in your web browser"
fi

# Run Flask app
python3 app.py

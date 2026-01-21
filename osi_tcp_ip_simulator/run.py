#!/usr/bin/env python
"""
Quick Start Script for OSI vs TCP/IP Model Simulator
Run this script to automatically start the Flask application
"""

import os
import sys
import subprocess
import webbrowser
import time

def main():
    # Get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("OSI vs TCP/IP Model Visual Simulator")
    print("=" * 60)
    print()
    
    # Check if Flask is installed
    try:
        import flask
        print("✓ Flask is installed")
    except ImportError:
        print("✗ Flask is not installed")
        print("\nInstalling required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", 
                              os.path.join(script_dir, "requirements.txt")])
        print("✓ Dependencies installed")
    
    print("\n" + "=" * 60)
    print("Starting Flask Server...")
    print("=" * 60)
    print()
    
    # Change to script directory
    os.chdir(script_dir)
    
    # Start Flask application
    print("Server is starting at http://localhost:5000")
    print("Opening browser in 2 seconds...")
    print()
    print("Press CTRL+C to stop the server")
    print("-" * 60)
    
    # Wait a moment for server to start
    time.sleep(2)
    
    try:
        # Try to open browser
        webbrowser.open('http://localhost:5000')
    except:
        print("\nCould not open browser automatically.")
        print("Please open http://localhost:5000 manually in your web browser")
    
    # Run Flask app
    from app import app
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        sys.exit(0)

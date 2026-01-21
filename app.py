"""
Flask entrypoint for Vercel deployment
"""

import sys
import os

# Change working directory to osi_tcp_ip_simulator so imports work correctly
os.chdir(os.path.join(os.path.dirname(__file__), 'osi_tcp_ip_simulator'))
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'osi_tcp_ip_simulator'))

# Import and run the Flask app
from app import app

if __name__ == '__main__':
    app.run(debug=False)

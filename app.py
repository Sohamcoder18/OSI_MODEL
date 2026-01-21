"""
Flask entrypoint for Vercel deployment
"""

import sys
import os

# Add the osi_tcp_ip_simulator directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'osi_tcp_ip_simulator'))

# Import and run the Flask app
from osi_tcp_ip_simulator.app import app

if __name__ == '__main__':
    app.run(debug=False)

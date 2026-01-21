"""
Flask entrypoint for Vercel deployment
"""

import sys
import os
from pathlib import Path

# Get the root directory
ROOT_DIR = Path(__file__).parent
SIMULATOR_DIR = ROOT_DIR / 'osi_tcp_ip_simulator'

# Add paths for imports
sys.path.insert(0, str(SIMULATOR_DIR))

# Import Flask and configure paths
from flask import Flask, render_template, jsonify
import json
import socket

# Create Flask app with correct template and static paths
app = Flask(
    __name__,
    template_folder=str(SIMULATOR_DIR / 'templates'),
    static_folder=str(SIMULATOR_DIR / 'static'),
    static_url_path='/static'
)
app.config['SECRET_KEY'] = 'osi-model-simulator-secret-key'

# Import models from osi_tcp_ip_simulator
from models import OSIModel, TCPIPModel, ENCAPSULATION_SEQUENCE, DECAPSULATION_SEQUENCE

# Initialize models
osi_model = OSIModel()
tcpip_model = TCPIPModel()

@app.route('/')
def index():
    """Serve main page"""
    return render_template('index.html')

@app.route('/api/osi-layers')
def get_osi_layers():
    """API endpoint to get OSI layers"""
    layers = []
    for layer in osi_model.layers:
        layers.append({
            'number': layer.number,
            'name': layer.name,
            'functions': layer.functions,
            'protocols': layer.protocols,
            'data_unit': layer.data_unit,
            'color': layer.color
        })
    return jsonify({'layers': layers})

@app.route('/api/tcpip-layers')
def get_tcpip_layers():
    """API endpoint to get TCP/IP layers"""
    layers = []
    for layer in tcpip_model.layers:
        layers.append({
            'number': layer.number,
            'name': layer.name,
            'functions': layer.functions,
            'protocols': layer.protocols,
            'data_unit': layer.data_unit,
            'color': layer.color
        })
    return jsonify({'layers': layers})

@app.route('/api/osi-layer/<int:layer_num>')
def get_osi_layer(layer_num):
    """API endpoint to get specific OSI layer details"""
    for layer in osi_model.layers:
        if layer.number == layer_num:
            return jsonify({
                'number': layer.number,
                'name': layer.name,
                'functions': layer.functions,
                'protocols': layer.protocols,
                'data_unit': layer.data_unit,
                'color': layer.color
            })
    return jsonify({'error': 'Layer not found'}), 404

@app.route('/api/tcpip-layer/<int:layer_num>')
def get_tcpip_layer(layer_num):
    """API endpoint to get specific TCP/IP layer details"""
    for layer in tcpip_model.layers:
        if layer.number == layer_num:
            return jsonify({
                'number': layer.number,
                'name': layer.name,
                'functions': layer.functions,
                'protocols': layer.protocols,
                'data_unit': layer.data_unit,
                'color': layer.color
            })
    return jsonify({'error': 'Layer not found'}), 404

@app.route('/api/encapsulation')
def get_encapsulation():
    """API endpoint to get encapsulation sequence"""
    return jsonify({'sequence': ENCAPSULATION_SEQUENCE})

@app.route('/api/decapsulation')
def get_decapsulation():
    """API endpoint to get decapsulation sequence"""
    return jsonify({'sequence': DECAPSULATION_SEQUENCE})

@app.route('/api/layer-mapping')
def get_layer_mapping():
    """API endpoint to get OSI to TCP/IP layer mapping"""
    mapping = {}
    for osi_layer in osi_model.layers:
        for tcpip_layer in tcpip_model.layers:
            if osi_layer.number in [4, 5, 6, 7] and tcpip_layer.number == 4:
                mapping[f'osi_{osi_layer.number}'] = f'tcpip_{tcpip_layer.number}'
            elif osi_layer.number in [1, 2] and tcpip_layer.number == 1:
                mapping[f'osi_{osi_layer.number}'] = f'tcpip_{tcpip_layer.number}'
            elif osi_layer.number == 3 and tcpip_layer.number == 2:
                mapping[f'osi_{osi_layer.number}'] = f'tcpip_{tcpip_layer.number}'
    return jsonify({'mapping': mapping})

if __name__ == '__main__':
    app.run(debug=False)

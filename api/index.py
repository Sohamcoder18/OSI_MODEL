"""
Vercel API route for Flask app
"""

import sys
import os
from pathlib import Path

# Add simulator to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'osi_tcp_ip_simulator'))

from flask import Flask, render_template, jsonify
from models import OSIModel, TCPIPModel, ENCAPSULATION_SEQUENCE, DECAPSULATION_SEQUENCE

app = Flask(__name__, template_folder='../osi_tcp_ip_simulator/templates', static_folder='../osi_tcp_ip_simulator/static')
app.config['SECRET_KEY'] = 'osi-model-simulator-secret-key'

osi_model = OSIModel()
tcpip_model = TCPIPModel()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/osi-layers')
def get_osi_layers():
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
    return jsonify({'sequence': ENCAPSULATION_SEQUENCE})

@app.route('/api/decapsulation')
def get_decapsulation():
    return jsonify({'sequence': DECAPSULATION_SEQUENCE})

@app.route('/api/layer-mapping')
def get_layer_mapping():
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

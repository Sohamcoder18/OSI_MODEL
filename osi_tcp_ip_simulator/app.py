"""
Flask backend for OSI vs TCP/IP Model Visual Simulator
"""

from flask import Flask, render_template, jsonify
import json
import socket

app = Flask(__name__)
app.config['SECRET_KEY'] = 'osi-model-simulator-secret-key'

# Import models
from models import OSIModel, TCPIPModel, ProtocolDatabase, ENCAPSULATION_SEQUENCE, DECAPSULATION_SEQUENCE

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
            'color': layer.color,
            'description': layer.description,
            'examples': layer.examples
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
            'osi_layers': layer.osi_layers,
            'color': layer.color,
            'description': layer.description,
            'examples': layer.examples
        })
    return jsonify({'layers': layers})


@app.route('/api/osi-layer/<int:layer_num>')
def get_osi_layer_details(layer_num):
    """API endpoint to get specific OSI layer details"""
    layer = osi_model.get_layer_by_number(layer_num)
    if layer:
        return jsonify({
            'success': True,
            'layer': {
                'number': layer.number,
                'name': layer.name,
                'functions': layer.functions,
                'protocols': layer.protocols,
                'data_unit': layer.data_unit,
                'color': layer.color,
                'description': layer.description,
                'examples': layer.examples
            }
        })
    return jsonify({'success': False, 'error': 'Layer not found'}), 404


@app.route('/api/tcpip-layer/<int:layer_num>')
def get_tcpip_layer_details(layer_num):
    """API endpoint to get specific TCP/IP layer details"""
    layer = tcpip_model.get_layer_by_number(layer_num)
    if layer:
        return jsonify({
            'success': True,
            'layer': {
                'number': layer.number,
                'name': layer.name,
                'functions': layer.functions,
                'protocols': layer.protocols,
                'osi_layers': layer.osi_layers,
                'color': layer.color,
                'description': layer.description,
                'examples': layer.examples
            }
        })
    return jsonify({'success': False, 'error': 'Layer not found'}), 404


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
    for tcpip_layer in tcpip_model.layers:
        mapping[f'tcpip_{tcpip_layer.number}'] = {
            'name': tcpip_layer.name,
            'osi_layers': tcpip_layer.osi_layers
        }
    return jsonify({'mapping': mapping})


@app.route('/api/protocols')
def get_all_protocols():
    """API endpoint to get all protocols"""
    protocols = {}
    for name, protocol in ProtocolDatabase.get_all_protocols().items():
        protocols[name] = {
            'name': protocol.name,
            'layer': protocol.layer,
            'osi_layer_num': protocol.osi_layer_num,
            'description': protocol.description,
            'key_points': protocol.key_points,
            'ports': protocol.ports,
            'use_cases': protocol.use_cases,
            'alternatives': protocol.alternatives
        }
    return jsonify({'protocols': protocols})


@app.route('/api/protocol/<protocol_name>')
def get_protocol_details(protocol_name):
    """API endpoint to get specific protocol details"""
    protocol = ProtocolDatabase.get_protocol(protocol_name)
    if protocol:
        return jsonify({
            'success': True,
            'protocol': {
                'name': protocol.name,
                'layer': protocol.layer,
                'osi_layer_num': protocol.osi_layer_num,
                'description': protocol.description,
                'key_points': protocol.key_points,
                'ports': protocol.ports,
                'use_cases': protocol.use_cases,
                'alternatives': protocol.alternatives
            }
        })
    return jsonify({'success': False, 'error': 'Protocol not found'}), 404


@app.route('/api/protocols/layer/<layer_name>')
def get_protocols_by_layer(layer_name):
    """API endpoint to get protocols by layer"""
    protocols = ProtocolDatabase.get_protocols_by_layer(layer_name)
    result = {}
    for name, protocol in protocols.items():
        result[name] = {
            'name': protocol.name,
            'layer': protocol.layer,
            'osi_layer_num': protocol.osi_layer_num,
            'description': protocol.description,
            'key_points': protocol.key_points,
            'ports': protocol.ports,
            'use_cases': protocol.use_cases,
            'alternatives': protocol.alternatives
        }
    return jsonify({'protocols': result})


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🌐 OSI vs TCP/IP Model Visual Simulator")
    print("="*60)
    print("✓ Server running on: http://localhost:5000")
    print("="*60 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)

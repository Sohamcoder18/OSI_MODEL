"""
Network Models - OSI and TCP/IP model definitions
"""


class OSILayer:
    """Represents an OSI layer"""
    
    def __init__(self, number, name, functions, protocols, data_unit, color):
        self.number = number
        self.name = name
        self.functions = functions
        self.protocols = protocols
        self.data_unit = data_unit
        self.color = color


class OSIModel:
    """OSI 7-Layer Model"""
    
    def __init__(self):
        self.layers = [
            OSILayer(
                7, "Application Layer",
                ["User Interface", "Email, Web Services", "Resource Sharing"],
                ["HTTP", "HTTPS", "FTP", "SMTP", "POP3", "IMAP", "DNS", "TELNET"],
                "Data",
                "#FF6B6B"
            ),
            OSILayer(
                6, "Presentation Layer",
                ["Data Encryption", "Compression", "Translation"],
                ["SSL/TLS", "JPEG", "MPEG", "GIF", "ASCII"],
                "Data",
                "#FF8C42"
            ),
            OSILayer(
                5, "Session Layer",
                ["Connection Management", "Dialogue Control", "Synchronization"],
                ["NetBIOS", "SAP", "SMB", "SSH"],
                "Data",
                "#FFC93C"
            ),
            OSILayer(
                4, "Transport Layer",
                ["End-to-End Communication", "Flow Control", "Error Checking"],
                ["TCP", "UDP", "SCTP", "DCCP"],
                "Segment",
                "#FFE66D"
            ),
            OSILayer(
                3, "Network Layer",
                ["Routing", "IP Addressing", "Logical Addressing"],
                ["IP", "ICMP", "ARP", "IGMP", "IPsec"],
                "Packet",
                "#95E1D3"
            ),
            OSILayer(
                2, "Data Link Layer",
                ["Frame Creation", "MAC Addressing", "Physical Addressing"],
                ["Ethernet", "PPP", "MAC", "HDLC", "Frame Relay"],
                "Frame",
                "#38ADA9"
            ),
            OSILayer(
                1, "Physical Layer",
                ["Bit Transmission", "Medium", "Signal"],
                ["Copper Wire", "Fiber Optic", "Wireless", "Bluetooth"],
                "Bits",
                "#078282"
            ),
        ]
    
    def get_layer_by_number(self, number):
        """Get layer by number (1-7)"""
        for layer in self.layers:
            if layer.number == number:
                return layer
        return None


class TCPIPLayer:
    """Represents a TCP/IP layer"""
    
    def __init__(self, number, name, functions, protocols, osi_layers, color):
        self.number = number
        self.name = name
        self.functions = functions
        self.protocols = protocols
        self.osi_layers = osi_layers  # Corresponding OSI layers
        self.color = color


class TCPIPModel:
    """TCP/IP 4-Layer Model"""
    
    def __init__(self):
        self.layers = [
            TCPIPLayer(
                4, "Application Layer",
                ["Email", "File Transfer", "Web Browsing", "Remote Access"],
                ["HTTP", "HTTPS", "FTP", "SMTP", "DNS", "SSH", "Telnet", "SNMP"],
                [7, 6, 5],  # Maps to OSI layers 7, 6, 5
                "#FF6B6B"
            ),
            TCPIPLayer(
                3, "Transport Layer",
                ["End-to-End Communication", "Flow Control", "Reliability"],
                ["TCP", "UDP", "SCTP"],
                [4],  # Maps to OSI layer 4
                "#FFE66D"
            ),
            TCPIPLayer(
                2, "Internet Layer",
                ["Routing", "Logical Addressing", "IP Management"],
                ["IP", "ICMP", "ARP", "IGMP"],
                [3],  # Maps to OSI layer 3
                "#95E1D3"
            ),
            TCPIPLayer(
                1, "Link Layer",
                ["Physical Transmission", "MAC Addressing", "Hardware Addressing"],
                ["Ethernet", "PPP", "MAC", "Wi-Fi"],
                [2, 1],  # Maps to OSI layers 2, 1
                "#078282"
            ),
        ]
    
    def get_layer_by_number(self, number):
        """Get layer by number (1-4)"""
        for layer in self.layers:
            if layer.number == number:
                return layer
        return None


# Encapsulation sequence showing data transformation
ENCAPSULATION_SEQUENCE = [
    {"stage": 1, "data": "Application Data", "header": "Layer 7", "result": "Data"},
    {"stage": 2, "data": "Data", "header": "Layer 6 (Encrypt)", "result": "Data"},
    {"stage": 3, "data": "Data", "header": "Layer 5 (Session)", "result": "Data"},
    {"stage": 4, "data": "Data", "header": "+ TCP/UDP Header", "result": "Segment"},
    {"stage": 5, "data": "Segment", "header": "+ IP Header", "result": "Packet"},
    {"stage": 6, "data": "Packet", "header": "+ MAC Header", "result": "Frame"},
    {"stage": 7, "data": "Frame", "header": "Physical Layer", "result": "Bits"},
]

DECAPSULATION_SEQUENCE = [
    {"stage": 1, "data": "Bits (110101...)", "header": "Physical Layer", "result": "Frame"},
    {"stage": 2, "data": "Frame", "header": "- MAC Header", "result": "Packet"},
    {"stage": 3, "data": "Packet", "header": "- IP Header", "result": "Segment"},
    {"stage": 4, "data": "Segment", "header": "- TCP/UDP Header", "result": "Data"},
    {"stage": 5, "data": "Data", "header": "Layer 5 (Session)", "result": "Data"},
    {"stage": 6, "data": "Data", "header": "Layer 6 (Decrypt)", "result": "Data"},
    {"stage": 7, "data": "Data", "header": "Layer 7 (Application)", "result": "Original Message"},
]

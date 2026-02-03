"""
Network Models - OSI and TCP/IP model definitions
"""


class OSILayer:
    """Represents an OSI layer"""
    
    def __init__(self, number, name, functions, protocols, data_unit, color, description=None, examples=None):
        self.number = number
        self.name = name
        self.functions = functions
        self.protocols = protocols
        self.data_unit = data_unit
        self.color = color
        self.description = description or ""
        self.examples = examples or []


class OSIModel:
    """OSI 7-Layer Model"""
    
    def __init__(self):
        self.layers = [
            OSILayer(
                7, "Application Layer",
                ["User Interface", "Email, Web Services", "Resource Sharing"],
                ["HTTP", "HTTPS", "FTP", "SMTP", "POP3", "IMAP", "DNS", "TELNET"],
                "Data",
                "#FF6B6B",
                "The Application Layer is the topmost layer that provides network services directly to user applications. It handles user requests and returns responses, managing all user interactions with the network. This layer is where web browsers, email clients, and file transfer applications operate.",
                [
                    "🌐 Web Browsing: HTTP/HTTPS protocols deliver web pages to your browser",
                    "📧 Email: SMTP sends emails, POP3/IMAP retrieves them from servers",
                    "📁 File Transfer: FTP allows uploading and downloading files",
                    "🔍 DNS: Translates domain names (google.com) to IP addresses",
                    "🖥️ Remote Access: SSH and Telnet allow remote server access"
                ]
            ),
            OSILayer(
                6, "Presentation Layer",
                ["Data Encryption", "Compression", "Translation"],
                ["SSL/TLS", "JPEG", "MPEG", "GIF", "ASCII"],
                "Data",
                "#FF8C42",
                "The Presentation Layer is responsible for preparing data for transmission and display. It handles data encryption for security, compression to reduce size, and formatting to ensure compatibility between different systems. Think of it as a translator and formatter for data.",
                [
                    "🔒 Encryption: SSL/TLS encrypts sensitive data (like passwords) for secure transmission",
                    "📸 Image Compression: Converting images to JPEG format reduces file size",
                    "🎬 Video Compression: MPEG codec compresses video for streaming",
                    "📝 Character Encoding: Converting between ASCII, Unicode, and other formats",
                    "💾 Data Compression: ZIP files compress data before transmission"
                ]
            ),
            OSILayer(
                5, "Session Layer",
                ["Connection Management", "Dialogue Control", "Synchronization"],
                ["NetBIOS", "SAP", "SMB", "SSH"],
                "Data",
                "#FFC93C",
                "The Session Layer manages the conversation (session) between applications. It establishes, maintains, and terminates connections between computers. This layer ensures that data exchange happens in an organized manner and handles session recovery if connections are lost.",
                [
                    "🤝 Connection Setup: Establishes communication between two applications",
                    "💬 Dialogue Control: Determines who talks when (half-duplex or full-duplex)",
                    "🔄 Synchronization: Keeps data streams synchronized during long transfers",
                    "⏱️ Timeout Management: Detects and recovers from inactive connections",
                    "📞 Call Waiting: Pauses one conversation to handle another (like phone call hold)"
                ]
            ),
            OSILayer(
                4, "Transport Layer",
                ["End-to-End Communication", "Flow Control", "Error Checking"],
                ["TCP", "UDP", "SCTP", "DCCP"],
                "Segment",
                "#FFE66D",
                "The Transport Layer ensures reliable end-to-end communication between applications. It determines whether data should be sent reliably (TCP) or quickly (UDP), manages data flow to prevent overwhelming, and checks for errors. Port numbers are used to identify specific applications.",
                [
                    "🚚 TCP (Reliable): Guarantees data arrives in order without loss - used for email, web",
                    "⚡ UDP (Fast): No guarantee but faster - used for video streaming, online games",
                    "🔢 Port Numbers: Identify which application receives data (80=Web, 25=Email, 53=DNS)",
                    "🚦 Flow Control: Prevents fast sender from overwhelming slow receiver",
                    "✅ Error Detection: Checks for corrupted data and requests retransmission"
                ]
            ),
            OSILayer(
                3, "Network Layer",
                ["Routing", "IP Addressing", "Logical Addressing"],
                ["IP", "ICMP", "ARP", "IGMP", "IPsec"],
                "Packet",
                "#95E1D3",
                "The Network Layer handles routing - determining the best path for data to travel from sender to receiver across multiple networks. It uses IP addresses (logical addresses) to identify computers on the internet and routers to forward data between networks.",
                [
                    "🛣️ Routing: Routers use IP addresses to find the best path to destination",
                    "🏷️ IP Addressing: IPv4 (192.168.1.1) and IPv6 identify computers globally",
                    "🗺️ Packet Forwarding: Data is divided into packets that may take different routes",
                    "🔍 ICMP: Ping command uses ICMP to test if hosts are reachable",
                    "🌍 Inter-Network Communication: Enables communication across different networks"
                ]
            ),
            OSILayer(
                2, "Data Link Layer",
                ["Frame Creation", "MAC Addressing", "Physical Addressing"],
                ["Ethernet", "PPP", "MAC", "HDLC", "Frame Relay"],
                "Frame",
                "#38ADA9",
                "The Data Link Layer manages communication between adjacent nodes on the same network. It uses MAC addresses (physical addresses like 00:1A:2B:3C:4D:5E) to identify devices on a local network segment. It also handles error detection and organizes data into frames.",
                [
                    "🖧 Ethernet: Most common wired network technology connecting devices on same network",
                    "📱 Wi-Fi: Wireless technology using MAC addresses for local communication",
                    "🔗 MAC Addressing: Physical address like 48:21:0B:84:41:1E identifies your network card",
                    "🖼️ Frame Structure: Data wrapped with MAC header, trailer, and error checking codes",
                    "🚫 Collision Detection: Ethernet detects when multiple devices transmit simultaneously"
                ]
            ),
            OSILayer(
                1, "Physical Layer",
                ["Bit Transmission", "Medium", "Signal"],
                ["Copper Wire", "Fiber Optic", "Wireless", "Bluetooth"],
                "Bits",
                "#078282",
                "The Physical Layer is the lowest layer dealing with the actual hardware and physical transmission of data. It converts data into electrical, optical, or radio signals and transmits them through physical media. It defines how devices connect physically.",
                [
                    "🔌 Copper Cables: CAT5/CAT6 Ethernet cables transmit electrical signals",
                    "💡 Fiber Optics: Uses light pulses for high-speed, long-distance transmission",
                    "📶 Wireless: Radio waves transmit data through the air (Wi-Fi, 4G, 5G)",
                    "⚡ Signal Encoding: Converts 1s and 0s into voltage levels or light pulses",
                    "🔋 Power Supply: Provides electrical power to network devices like switches and routers"
                ]
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
    
    def __init__(self, number, name, functions, protocols, osi_layers, color, description=None, examples=None):
        self.number = number
        self.name = name
        self.functions = functions
        self.protocols = protocols
        self.osi_layers = osi_layers  # Corresponding OSI layers
        self.color = color
        self.description = description or ""
        self.examples = examples or []


class TCPIPModel:
    """TCP/IP 4-Layer Model"""
    
    def __init__(self):
        self.layers = [
            TCPIPLayer(
                4, "Application Layer",
                ["Email", "File Transfer", "Web Browsing", "Remote Access"],
                ["HTTP", "HTTPS", "FTP", "SMTP", "DNS", "SSH", "Telnet", "SNMP"],
                [7, 6, 5],  # Maps to OSI layers 7, 6, 5
                "#FF6B6B",
                "The Application Layer combines the functionalities of the OSI's Application, Presentation, and Session layers. It provides network services directly to applications and end-users, handling all user-facing operations like web browsing, email, and file transfers.",
                [
                    "🌐 Web Browsing: HTTP/HTTPS enables users to access websites",
                    "📧 Email: SMTP/POP3/IMAP manage email sending and retrieval",
                    "📁 File Transfer: FTP and SFTP allow file uploads and downloads",
                    "🔍 DNS: Resolves domain names to IP addresses",
                    "🔐 Encryption & Security: SSL/TLS provides secure communication",
                    "🖥️ Remote Access: SSH enables secure remote server management"
                ]
            ),
            TCPIPLayer(
                3, "Transport Layer",
                ["End-to-End Communication", "Flow Control", "Reliability"],
                ["TCP", "UDP", "SCTP"],
                [4],  # Maps to OSI layer 4
                "#FFE66D",
                "The Transport Layer establishes end-to-end communication channels between applications. It chooses between reliable delivery (TCP) and fast delivery (UDP), manages ports to identify applications, and handles flow control and error recovery.",
                [
                    "🚚 TCP: Reliable, ordered delivery - used for important data (email, web)",
                    "⚡ UDP: Fast, connectionless delivery - used for real-time data (video, games)",
                    "🔢 Port Numbers: 80=Web, 443=Secure Web, 25=SMTP, 22=SSH, 53=DNS",
                    "🚦 Flow Control: Prevents data congestion on the network",
                    "✅ Error Recovery: TCP retransmits lost packets automatically"
                ]
            ),
            TCPIPLayer(
                2, "Internet Layer",
                ["Routing", "Logical Addressing", "IP Management"],
                ["IP", "ICMP", "ARP", "IGMP"],
                [3],  # Maps to OSI layer 3
                "#95E1D3",
                "The Internet Layer handles routing and logical addressing of data packets across networks. IP (Internet Protocol) is the core protocol that enables computers across different networks to communicate using IP addresses as unique identifiers.",
                [
                    "🛣️ Routing: Determines optimal paths for packets across networks",
                    "🏷️ IP Addressing: IPv4 (192.168.1.1) and IPv6 provide unique identifiers",
                    "📦 Packet Forwarding: Routers forward packets based on destination IP",
                    "🌍 Internet Connectivity: Enables global communication across any network",
                    "🔍 ICMP: Ping uses ICMP to test connectivity and diagnose network issues"
                ]
            ),
            TCPIPLayer(
                1, "Link Layer",
                ["Physical Transmission", "MAC Addressing", "Hardware Addressing"],
                ["Ethernet", "PPP", "MAC", "Wi-Fi"],
                [2, 1],  # Maps to OSI layers 2, 1
                "#078282",
                "The Link Layer combines the OSI's Data Link and Physical layers. It handles the actual transmission of data over physical media using MAC addresses for local network delivery and manages the hardware interface for sending and receiving data.",
                [
                    "🔌 Wired: Ethernet cables transmit electrical signals between devices",
                    "📶 Wireless: Wi-Fi uses radio waves for cordless communication",
                    "🖧 MAC Addressing: 48-bit addresses identify network cards on same segment",
                    "🖼️ Frame Formatting: Data packaged with headers and error checking",
                    "🔋 Hardware Driver: Manages network card operations and signal transmission"
                ]
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
    {"stage": 1, "data": "Application Data", "header": "Layer 7 - Application", "result": "Data", "description": "User creates message"},
    {"stage": 2, "data": "Data", "header": "Layer 6 - Presentation (Encrypt)", "result": "Data", "description": "Encryption & compression applied"},
    {"stage": 3, "data": "Data", "header": "Layer 5 - Session (Setup)", "result": "Data", "description": "Session established"},
    {"stage": 4, "data": "Data", "header": "Layer 4 + TCP/UDP Header", "result": "Segment", "description": "Source & destination ports added"},
    {"stage": 5, "data": "Segment", "header": "Layer 3 + IP Header", "result": "Packet", "description": "Source & destination IP added"},
    {"stage": 6, "data": "Packet", "header": "Layer 2 + MAC Header", "result": "Frame", "description": "Source & destination MAC added"},
    {"stage": 7, "data": "Frame", "header": "Layer 1 - Physical (Transmit)", "result": "Bits", "description": "Converted to electrical/radio signals"},
]

DECAPSULATION_SEQUENCE = [
    {"stage": 1, "data": "Bits (110101...)", "header": "Layer 1 - Physical (Receive)", "result": "Frame", "description": "Signals converted back to data"},
    {"stage": 2, "data": "Frame", "header": "Layer 2 - Remove MAC Header", "result": "Packet", "description": "MAC header checked & removed"},
    {"stage": 3, "data": "Packet", "header": "Layer 3 - Remove IP Header", "result": "Segment", "description": "IP header checked & removed"},
    {"stage": 4, "data": "Segment", "header": "Layer 4 - Remove TCP/UDP Header", "result": "Data", "description": "Port numbers checked & removed"},
    {"stage": 5, "data": "Data", "header": "Layer 5 - Session (Close)", "result": "Data", "description": "Session closed properly"},
    {"stage": 6, "data": "Data", "header": "Layer 6 - Presentation (Decrypt)", "result": "Data", "description": "Decompression & decryption done"},
    {"stage": 7, "data": "Data", "header": "Layer 7 - Application (Display)", "result": "Original Message", "description": "Message displayed to user"},
]

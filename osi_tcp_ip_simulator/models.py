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
                ["HTTP", "HTTPS", "FTP", "SFTP", "SMTP", "POP3", "IMAP", "DNS", "SSH", "TELNET", "SNMP"],
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
                ["SSL"],
                "Data",
                "#FF8C42",
                "The Presentation Layer is responsible for preparing data for transmission and display. It handles data encryption for security, compression to reduce size, and formatting to ensure compatibility between different systems. Think of it as a translator and formatter for data. Note: JPEG, MPEG, GIF, ASCII are data formats handled by this layer but aren't network protocols themselves.",
                [
                    "🔒 Encryption: SSL/TLS encrypts sensitive data (like passwords) for secure transmission",
                    "📸 Image Compression: Formats like JPEG compress images for transmission",
                    "🎬 Video Compression: Codecs like MPEG compress video for streaming",
                    "📝 Character Encoding: Converting between ASCII, Unicode, and other formats",
                    "💾 Data Compression: ZIP and other compression algorithms reduce transmission size"
                ]
            ),
            OSILayer(
                5, "Session Layer",
                ["Connection Management", "Dialogue Control", "Synchronization"],
                ["NetBIOS", "SMB"],
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
                ["Ethernet", "Wi-Fi", "PPP", "MAC", "HDLC", "Frame Relay"],
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


class Protocol:
    """Represents a network protocol with detailed information"""
    
    def __init__(self, name, layer, osi_layer_num, description, key_points, ports=None, use_cases=None, alternatives=None):
        self.name = name
        self.layer = layer  # Application, Transport, Network, Link, or Physical
        self.osi_layer_num = osi_layer_num
        self.description = description
        self.key_points = key_points  # List of key features
        self.ports = ports or []
        self.use_cases = use_cases or []
        self.alternatives = alternatives or []


class ProtocolDatabase:
    """Database of all network protocols with detailed descriptions"""
    
    protocols = {
        # Application Layer Protocols (Layer 7)
        "HTTP": Protocol(
            "HTTP (HyperText Transfer Protocol)",
            "Application",
            7,
            "HTTP is a stateless, application-level protocol designed for transferring hypertext documents and other resources across the internet. It operates on a client-server model where a client (typically a web browser) sends HTTP requests to a web server, which responds with the requested resources. Each request is completely independent - the server doesn't maintain client state between requests. HTTP uses URI/URL (Uniform Resource Identifiers) to identify resources and employs methods like GET, POST, PUT, and DELETE to specify what action to perform on those resources. While HTTP revolutionized the web, its fundamental design meant all data is transmitted in plaintext without encryption, making it vulnerable to eavesdropping.",
            [
                "🌐 Stateless Protocol: Each request is independent; server doesn't track previous requests - enables scalability but requires cookies/sessions for state",
                "📝 Plain Text Transmission: All data including headers sent as readable ASCII - fast but vulnerable to interception without encryption",
                "🔗 Request-Response Model: Client always initiates; server responds - no server push capability in HTTP/1.1 (HTTP/2 changed this)",
                "📄 Resource Identification: Uses URLs/URIs with format scheme://host:port/path?query#fragment - incredibly flexible for web architecture",
                "🔄 HTTP Methods: GET (safe, idempotent), POST (creates resource), PUT (updates), DELETE (removes), HEAD (metadata only), OPTIONS (capabilities), PATCH (partial update)",
                "🏷️ Headers: Metadata like Content-Type, User-Agent, Accept, Authorization - allows content negotiation and protocol control",
                "🔢 Status Codes: 1xx (info), 2xx (success), 3xx (redirection), 4xx (client error), 5xx (server error) - critical for understanding responses",
                "📦 HTTP Versions: HTTP/1.0 (simple, one request per connection), HTTP/1.1 (persistent connections, pipelining), HTTP/2 (multiplexing, binary), HTTP/3 (uses UDP/QUIC)"
            ],
            [80],
            [
                "Accessing websites and web applications globally",
                "Downloading files and resources from servers",
                "RESTful API calls between web services and applications",
                "Loading images, videos, CSS, and JavaScript files",
                "Form submission and data entry on web pages",
                "Web crawling and indexing by search engines",
                "Progressive Web App (PWA) functionality"
            ],
            ["HTTPS"]
        ),
        
        "HTTPS": Protocol(
            "HTTPS (HTTP Secure)",
            "Application",
            7,
            "HTTPS is the secure variant of HTTP that encrypts all communication between client and server using SSL/TLS (Secure Sockets Layer / Transport Layer Security) protocols. It addresses HTTP's fundamental security weakness by adding a layer of encryption that makes data incomprehensible to eavesdroppers. HTTPS also includes server authentication through digital certificates - the client can verify it's communicating with the legitimate server and not an imposter. The protocol involves a TLS handshake where cryptographic keys are exchanged before any HTTP data is transmitted. Modern browsers display security indicators for HTTPS connections, and search engines prioritize HTTPS websites. All sensitive data transmission should use HTTPS including banking, e-commerce, and any personally identifiable information.",
            [
                "🔒 SSL/TLS Encryption: Symmetric encryption (AES-256) protects data from eavesdroppers - can't read traffic even if intercepted",
                "🔐 Server Authentication: Digital certificates signed by trusted Certificate Authorities verify server identity - prevents man-in-the-middle attacks",
                "🤝 Certificate Verification: Browsers verify certificate validity, expiration, domain match - users see 'secure' padlock icon when valid",
                "📊 Data Integrity: HMAC (Hash-based Message Authentication Code) ensures data wasn't modified in transit - detects tampering",
                "🔑 Public Key Infrastructure (PKI): Two-key cryptography (public for encryption, private for decryption) enables secure key exchange without pre-shared secrets",
                "⚡ Performance: TLS handshake adds latency; encryption/decryption uses CPU; modern techniques minimize overhead",
                "🔄 Forward Secrecy: Modern TLS uses ephemeral keys - even if long-term key compromised, past sessions remain secure",
                "📜 Certificate Chain: Root CA → Intermediate CA → Server Certificate validates entire chain of trust"
            ],
            [443],
            [
                "Secure login systems with username/password protection",
                "E-commerce and online shopping with payment processing",
                "Banking and financial transactions (mandatory for security)",
                "Healthcare portals and HIPAA-compliant applications",
                "Email access (Gmail, Outlook use HTTPS)",
                "Cloud storage and file sharing services",
                "Any transmission of personally identifiable information (PII)"
            ],
            ["HTTP", "TLS/SSL"]
        ),
        
        "FTP": Protocol(
            "FTP (File Transfer Protocol)",
            "Application",
            7,
            "FTP is a legacy file transfer protocol developed in 1971 enabling users to upload/download files between systems over networks. FTP uses a two-connection model: a control connection (port 21) for commands and a separate data connection (port 20 for active mode, dynamically assigned for passive) for actual file transfer. This dual-connection architecture was designed when bandwidth efficiency required separating metadata from data. FTP supports both ASCII and binary file transfer modes. The protocol requires explicit username/password authentication transmitted in plaintext, making it a security risk. FTP operates in active mode (server initiates data connection to client) or passive mode (client initiates data connection to server) - passive mode required behind NAT/firewalls. Directory listing, file deletion, and file renaming are supported. However, FTP's lack of encryption, cumbersome two-connection model, and poor NAT traversal led to its decline. Modern alternatives like SFTP (SSH File Transfer Protocol) tunnel file transfer through encrypted SSH, providing both security and simplicity.",
            [
                "📂 File Transfer: Upload files (PUT) and download files (GET) between systems",
                "🔗 Dual Connections: Control connection (port 21) separate from data connection (port 20/passive)",
                "📋 Directory Operations: List remote files/directories, rename, delete, create directories",
                "📝 Transfer Modes: ASCII mode (text, line-ending conversion) vs Binary mode (raw bytes)",
                "👤 Authentication: Username and password required - transmitted plaintext (security risk)",
                "🔄 Active vs Passive: Active (server→client) for direct connections, Passive (client→server) for NAT",
                "⚠️ No Encryption: Credentials and data sent unencrypted - vulnerable to eavesdropping",
                "❌ Legacy Status: Deprecated in favor of SFTP due to security and usability issues"
            ],
            [21],  # Control port 21, data port 20
            [
                "Uploading website files to web servers (legacy)",
                "Downloading software and files from repositories",
                "Backup and archival operations (legacy)",
                "Anonymous file sharing (public repositories)",
                "Embedded device firmware/configuration transfer",
                "Legacy system file transfers without SSH"
            ],
            ["SFTP", "FTPS", "SCP"]
        ),
        
        "SFTP": Protocol(
            "SFTP (SSH File Transfer Protocol)",
            "Application",
            7,
            "SFTP is the modern secure replacement for traditional FTP, tunneling all file transfer operations through an encrypted SSH (Secure Shell) connection. Developed to address FTP's fundamental security and usability flaws, SFTP provides confidentiality (all data encrypted), integrity (detection of tampering), and strong authentication (password or key-based). Unlike FTP's separate control/data connections, SFTP multiplexes everything over single SSH tunnel on port 22, simplifying firewall rules and eliminating NAT issues. SFTP supports the full set of file operations - copy, move, delete, rename, change permissions, set timestamps - with semantics closer to filesystem operations than FTP. SSH public-key authentication enables keyless file transfers essential for automated backups and deployment scripts. SFTP clients include OpenSSH sftp command, WinSCP, FileZilla, and most IDEs. The protocol is binary-safe (no ASCII vs binary mode confusion) and supports efficient partial file transfers. SFTP has become the industry standard replacing not just FTP but also rsh (remote shell) and other legacy insecure file transfer tools.",
            [
                "🔒 SSH Encryption: All traffic (commands, filenames, data) encrypted with AES/ChaCha20",
                "🔐 Strong Authentication: Password-based or public-key SSH authentication with no plaintext credentials",
                "📂 Full File Operations: Copy, move, delete, rename, chmod, chown, symlink support",
                "🔗 Single Connection: Single SSH tunnel multiplexes all operations (no active/passive complexity)",
                "📁 Directory Traversal: Full remote filesystem access with directory listing and navigation",
                "🔄 Resumable Transfers: Can pause and resume interrupted transfers from last position",
                "🛡️ Data Integrity: SSH MACs detect tampering ensuring file content integrity",
                "🔑 Automation: Public-key authentication enables unattended automated transfers"
            ],
            [22],
            [
                "Secure file uploads to web hosting providers",
                "Protected backup and disaster recovery transfers",
                "Secure file transfer between data centers",
                "Administration of remote systems and servers",
                "Automated deployment and configuration management",
                "Secure synchronization of development environments",
                "Cross-platform file sharing between organizations",
                "HIPAA/PCI-compliant healthcare and financial transfers"
            ],
            ["FTP", "FTPS", "SCP"]
        ),
        
        "SMTP": Protocol(
            "SMTP (Simple Mail Transfer Protocol)",
            "Application",
            7,
            "SMTP is the protocol responsible for sending emails across the internet, routing messages from mail clients to mail servers and between mail servers globally. Developed in 1982, SMTP only handles outgoing mail - incoming email uses POP3 or IMAP. SMTP clients (mail applications) connect to SMTP servers on port 25 (server-to-server relay), port 587 (client submission with authentication), or port 465 (SMTPS with TLS wrapper). The protocol uses simple text commands: HELO (greeting), AUTH (authentication), MAIL FROM (sender), RCPT TO (recipient), DATA (message content), QUIT. SMTP works with DNS MX records - when sending to user@example.com, the SMTP server queries DNS for example.com's MX record to find the recipient's mail server. Mail servers implement queue-and-retry logic - if delivery fails, the message is retried periodically for days. Modern SMTP requires authentication to prevent open relay abuse (historical issue enabling spam). SMTP can operate with STARTTLS to upgrade plaintext connections to encrypted TLS, though modern deployments prefer port 465 (implicit TLS) for better security.",
            [
                "📤 Outgoing Email: Handles email transmission from client to server and server-to-server",
                "📮 SMTP Relay: Mail servers relay messages through chain of servers to destination",
                "🔍 DNS MX Lookup: Uses MX records to find recipient domain's mail server",
                "🔐 STARTTLS: Upgrades connection from plaintext to TLS encryption",
                "👤 SMTP Authentication: Username/password prevents open relay abuse and spam",
                "📏 Message Size Limits: Bounce large messages exceeding server limits",
                "🔄 Queue & Retry: Failed deliveries queued and retried with exponential backoff",
                "✉️ Message Formatting: RFC 5321 defines headers, body, attachments, multipart MIME"
            ],
            [25, 587, 465],  # 25 unrestricted, 587 submission, 465 SMTPS
            [
                "Sending emails from web applications and services",
                "Automated email notifications and alerts",
                "Email marketing campaigns and bulk mailing",
                "System administration notifications and alerts",
                "Transactional email (password resets, confirmations)",
                "Customer communication from SaaS applications",
                "Mail server-to-server relay infrastructure",
                "Bounce and non-delivery report handling"
            ],
            ["POP3", "IMAP"]
        ),
        
        "POP3": Protocol(
            "POP3 (Post Office Protocol version 3)",
            "Application",
            7,
            "POP3 is a simple protocol for retrieving emails from mail servers, designed for single-device email access. When a POP3 client connects, it downloads emails from the server to local storage and typically deletes them from the server. POP3 is ideal for users who access email from one primary device and prefer having emails stored locally for offline reading. The protocol is stateless - each session independent with no persistent state on server. POP3 supports two operational modes: most-deleted (default, deletes emails after download) and keep (clients manually delete). POP3 identifies messages by number based on their order on server, and supports TOP command for header-only preview before full download. The protocol is lightweight requiring minimal server resources - no mailbox synchronization complexity like IMAP. POP3 operates on port 110 (plaintext, insecure) or port 995 (POP3S with SSL/TLS wrapper, recommended). However, POP3 is limited - no server-side folder management, no synchronization across devices, can't search server-side, and no way to mark emails as read on server. These limitations led to IMAP becoming preferred for multi-device scenarios.",
            [
                "📥 Email Retrieval: Downloads message copies from server to local client",
                "🗑️ Server Deletion: Typically deletes emails from server after download (unless KEEP mode)",
                "💾 Offline Access: Emails stored locally enabling reading without internet connection",
                "👤 Authentication: Username and password required (plaintext vulnerable, use POP3S)",
                "🔒 POP3S: Secure version using SSL/TLS encryption on port 995",
                "📏 Stateless: No persistent connection state - each session independent",
                "📋 Message Operations: List messages, delete messages, retrieve by number",
                "⚠️ No Synchronization: Changes on one device don't sync to others"
            ],
            [110, 995],  # 110 plain, 995 SSL/TLS (POP3S)
            [
                "Single-device email access for power users",
                "Offline email reading and local archival",
                "Lightweight email clients with minimal resources",
                "Legacy email systems and older clients",
                "Email backup to local archives",
                "Mobile devices with limited storage/bandwidth",
                "Embedded systems and IoT devices",
                "Email consolidation from multiple accounts"
            ],
            ["IMAP"]
        ),
        
        "IMAP": Protocol(
            "IMAP (Internet Message Access Protocol)",
            "Application",
            7,
            "IMAP is the modern protocol for accessing emails on remote mail servers, designed for multi-device synchronization and server-side organization. Unlike POP3 which downloads emails to local storage, IMAP keeps messages on the server with clients retrieving content on-demand. This enables seamless access from multiple devices (phone, tablet, laptop, desktop) with synchronized state - mark-as-read on phone automatically reflects on laptop. IMAP supports server-side folder/mailbox management - clients create, organize, and manage folders directly on server. The SELECT command opens a mailbox; FETCH retrieves message headers, body, or structure without full download. Clients can perform server-side searches using SEARCH command rather than downloading everything. IMAP4 (current version) supports IDLE for push notifications when new mail arrives, eliminating polling. Connection is persistent with server tracking mailbox state and message flags. IMAP operates on port 143 (plaintext) or 993 (IMAPS with SSL/TLS). IMAP's complexity and server resource requirements (maintaining persistent state per client) make it heavier than POP3, but its multi-device synchronization makes it industry standard for modern email.",
            [
                "☁️ Server-Based Storage: Messages remain on server, retrievable from any device",
                "📱 Multi-Device Sync: Changes (read/unread/deleted) synchronized across all clients",
                "📂 Server-Side Folders: Create, rename, delete, organize mailboxes on server",
                "📥 Selective Download: Download headers only initially; fetch full content on-demand",
                "🔍 Server-Side Search: Search IMAP server-side returning only matching messages",
                "🔔 IDLE Push: Stay connected receiving real-time notify of new messages (no polling)",
                "🚩 Message Flags: Mark messages as read, flagged, drafts, junk, custom flags on server",
                "🔒 IMAPS: Secure version using SSL/TLS encryption on port 993"
            ],
            [143, 993],  # 143 plain, 993 SSL/TLS (IMAPS)
            [
                "Multi-device email access from phone/tablet/computer",
                "Synchronization of mailbox state across devices",
                "Organized email management with server-side folders",
                "Modern business email with Outlook/Gmail/Apple Mail",
                "Email archival and long-term storage on server",
                "Mobile-first users wanting unified inbox",
                "Enterprise deployments with central email storage",
                "Email collaboration and shared mailboxes"
            ],
            ["POP3"]
        ),
        
        "DNS": Protocol(
            "DNS (Domain Name System)",
            "Application",
            7,
            "DNS is the internet's distributed hierarchical directory service translating human-readable domain names (google.com) into IP addresses (142.250.185.46). Without DNS, users would need memorizing IP addresses instead of intuitive hostnames. DNS operates through a decentralized system of authoritative nameservers managed cooperatively - Root Nameservers (13 sets globally) point to TLD nameservers, which point to Authoritative nameservers. When resolving google.com, a recursive resolver queries Root (What's TLD for .com?), TLD (What nameserver has google.com?), Authoritative (What's IP for google.com?). DNS uses caching aggressively - recursive resolvers cache results (TTL-based), browsers cache (memory), operating systems cache - reducing root/TLD query load. DNS supports multiple record types: A (IPv4), AAAA (IPv6), MX (mail), CNAME (alias), NS (nameserver), SOA (authority). DNS protocol operates on UDP port 53 for queries/responses (fast, connectionless), TCP 53 for zone transfers (reliable, large transfers). DNSSEC adds cryptographic signing ensuring authoritative answers. DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) provide privacy preventing ISP eavesdropping.",
            [
                "🔍 Name Resolution: Maps friendly domain names to IP addresses enabling web browsing",
                "🌍 Hierarchical Architecture: Root → TLD → Authoritative nameservers with delegation",
                "⚡ Distributed Caching: Multiple cache layers (recursive resolver, ISP, client OS, browser) reduce authoritative load",
                "📝 Record Types: A (IPv4), AAAA (IPv6), MX (mail), CNAME (alias), NS (nameserver), SOA (authority), TXT",
                "🔄 Recursive vs Iterative: Recursive (client askes resolver to do full work), Iterative (each hop returns next step)",
                "🔐 DNSSEC: Cryptographic signing prevents DNS spoofing and cache poisoning attacks",
                "⚙️ Zone Files: Authoritative servers maintain records for their zones; propagate via DNS zone transfers",
                "🕐 TTL: Time-To-Live controls cache duration - short for frequently changing, long for stable records"
            ],
            [53],
            [
                "Website access (resolves URLs to IP addresses)",
                "Email routing using MX records",
                "Load balancing using DNS round-robin",
                "CDN optimization and geographic traffic routing",
                "Reverse DNS lookups for diagnostics",
                "Service discovery (SRV records)",
                "DKIM/SPF/DMARC authentication for email",
                "Privacy-preserving DNS (DoH/DoT) alternatives"
            ],
            []
        ),
        
        "SSH": Protocol(
            "SSH (Secure Shell)",
            "Application",
            7,
            "SSH is a cryptographic protocol enabling secure remote login, command execution, and secure tunneling over insecure networks. Developed by Tatu Ylönen as a secure replacement for rm (remote shell), telnet, and ftp which transmitted passwords in plaintext, SSH uses strong encryption protecting credentials and data from eavesdropping. The SSH protocol has two parts: SSH transport layer (provides encryption, authentication, compression on port 22) and SSH user authentication layer (password, public-key, keyboard-interactive methods). SSH typically uses public-key cryptography for server authentication and authentication - users generate keypair (private key kept secret, public key on servers). Password-based authentication falls back when keys unavailable, but is less secure. SSH connection establishes through handshake: version negotiation, algorithm negotiation (encryption, MAC, compression), key exchange (Diffie-Hellman), server authentication, user authentication, then channel opening. SSH supports X11 forwarding (remote GUI), port forwarding (tunneling other protocols through SSH), and SOCKS proxy. The protocol is stateful - multiple channels (shell, file transfer) multiplex over single connection. OpenSSH (de facto standard) is free, widely deployed, and part of most Unix/Linux distributions.",
            [
                "🔒 Encryption: Symmetric encryption (AES-256, AES-128, ChaCha20) protects confidentiality",
                "🔐 Application: Public-key authentication (RSA, ECDSA, Ed25519) or password authentication",
                "🤝 Key Exchange: Diffie-Hellman or Elliptic Curve Diffie-Hellman negotiates shared session key",
                "🖥️ Remote Shell: Execute interactive shell on remote server securely",
                "🔑 Passwordless Auth: Public-key authentication enables unattended script execution",
                "🚇 Tunneling: Forward ports and create encrypted tunnels for other protocols",
                "📁 File Transfer: Includes SFTP (subsystem) for secure file transfers",
                "🔄 Multiplexing: Multiple channels (shell, tunnels) over single SSH connection"
            ],
            [22],
            [
                "Secure remote server administration and management",
                "Executing commands on remote machines safely",
                "Automating deployment and configuration via SSH",
                "Creating secure encrypted tunnels for other protocols",
                "Secure file transfer via SFTP subsystem",
                "Secure Git code repository access (SSH keys)",
                "Database administration and MySQL tunneling",
                "Bastion/Jump host access for secure network entry"
            ],
            ["Telnet", "RDP"]
        ),
        
        "TELNET": Protocol(
            "TELNET (Telecommunications Network)",
            "Application",
            7,
            "TELNET is a legacy protocol for remote terminal access developed in 1969 for the ARPANET, predating modern security concepts. TELNET provides a text-based terminal interface allowing users to log into remote systems and execute commands as if sitting at that computer. The protocol is simple: establishes TCP connection to port 23, negotiates terminal properties through options (terminal type, line editing), then provides bidirectional character stream. However, TELNET has critical security flaws - all communication including usernames and passwords transmitted in plaintext, making it vulnerable to eavesdropping, packet sniffing, and man-in-the-middle attacks on networks shared with untrusted users. TELNET also lacks encryption and integrity protection. Today TELNET is deprecated - SSH (Secure Shell) completely supersedes it for remote access. However, TELNET persists in narrow use cases: testing network services (HTTP, SMTP, etc. by connecting to their ports), embedded device management consoles where security less critical, and legacy systems without SSH. TELNET clients exist on nearly every operating system (telnet command on Unix, various GUI apps on Windows), making ad-hoc diagnostics easy despite security concerns.",
            [
                "🖥️ Remote Terminal: Text-based terminal interface to remote systems",
                "⚠️ Plaintext Communication: All data including passwords transmitted unencrypted",
                "👤 Username/Password: Basic authentication via plaintext exchange",
                "📝 Terminal Negotiation: Negotiates terminal type and options such as WILL/WON'T",
                "🔀 Cross-Platform: Available on Unix, Linux, Windows, and most operating systems",
                "📋 Line Editing: Basic editing capabilities depend on remote server setup",
                "❌ Deprecated: No longer recommended due to severe security implications",
                "🔧 Testing & Diagnostics: Still useful for testing services (SMTP, HTTP) by hand"
            ],
            [23],
            [
                "Legacy system administration (superseded by SSH)",
                "Network device configuration (legacy routers/switches)",
                "Diagnostic testing of remote services",
                "Troubleshooting network connectivity interactively",
                "Embedded system console access (if SSH unavailable)",
                "Historical network infrastructure",
                "Ad-hoc service testing (connecting to HTTP/SMTP/POP3 ports)"
            ],
            ["SSH", "RDP"]
        ),
        
        "SNMP": Protocol(
            "SNMP (Simple Network Management Protocol)",
            "Application",
            7,
            "SNMP is the standard protocol for collecting management information from network devices and managing them remotely. SNMP enables monitoring of routers, switches, servers, firewalls, printers, and other network infrastructure. Devices run SNMP agents (software processes) that maintain a Management Information Base (MIB) - a database of objects representing device state (CPU utilization, memory usage, interface statistics, temperatures). NMS (Network Management Systems) like Nagios, Zabbix, and MRTG query agents using SNMP to gather metrics. SNMP uses agents listening on UDP port 161 for queries and port 162 for traps (unsolicited notifications of problems). The protocol is lightweight enabling high-scale polling. SNMP Version 1 (SNMPv1) uses simple plaintext community strings as authentication - vulnerable but still widely deployed in trusted networks. SNMPv2c improved message formats but kept weak community-based authentication. SNMPv3 added strong authentication and encryption using usernames and AES encryption. SNMP supports three operations: GET (retrieve value), SET (change value), TRAP (device alerts on events). Many organizations implement SNMP community strings as public (read-only) and private (administrative) to segregate permissions.",
            [
                "📊 Performance Monitoring: Collects CPU, memory, disk, interface utilization statistics",
                "🚨 Alert Notifications: Devices send TRAP messages for critical events (fan failure, power loss)",
                "🔧 Remote Configuration: SET operations enable changing device settings remotely",
                "📈 Historical Trending: Time-series data enables trend analysis and capacity planning",
                "🏢 Multi-Vendor Support: Standardized agent interfaces work across vendor products",
                "🔐 Authentication: SNMPv1/v2c use community strings; SNMPv3 adds username/AES encryption",
                "📏 Thresholds & Notifications: Alerts triggered when metrics exceed defined limits",
                "🔓 Network Access: Agents respond to queries from authorized NMS servers"
            ],
            [161, 162],
            [
                "Monitoring network device health, performance, and status",
                "Collecting bandwidth usage and traffic statistics",
                "Receiving alerts about network problems and failures",
                "Environmental monitoring (temperature, power supply)",
                "Automated network inventory and asset management",
                "Printer status and consumable tracking",
                "Unified infrastructure monitoring across vendors",
                "Capacity planning and performance trending"
            ],
            []
        ),
        
        # Transport Layer Protocols (Layer 4)
        "TCP": Protocol(
            "TCP (Transmission Control Protocol)",
            "Transport",
            4,
            "TCP is a reliable, connection-oriented transport layer protocol that forms the foundation of most modern internet applications. It establishes a persistent connection through a three-way handshake, then transmits data in a stream ensuring every byte arrives in the correct order without loss or duplication. TCP automatically detects errors, requests retransmission of lost packets, manages the rate of data transmission to prevent overwhelming the receiver, and gracefully closes connections. While TCP has more overhead than UDP due to these reliability mechanisms, it's essential for applications where data integrity matters more than speed, such as financial transactions, email, and file transfers.",
            [
                "🤝 Three-Way Handshake: SYN → SYN-ACK → ACK establishes connection state on both endpoints before data transfer begins",
                "✅ Reliable Delivery: Guarantees delivery using sequence numbers and acknowledgments - receiver must confirm receipt of each packet",
                "🔄 In-Order Delivery: Packets automatically reassembled in correct sequence even if they arrive out of order",
                "🚦 Flow Control: Sliding window mechanism prevents fast sender from overwhelming slow receiver - negotiated buffer sizes",
                "❌ Error Detection: Checksum verifies every packet for corruption - detected errors trigger automatic retransmission",
                "🔢 Connection Management: Four-way FIN/ACK handshake for graceful connection termination ensures no data loss on close",
                "⏱️ Congestion Control: AIMD (Additive Increase Multiplicative Decrease) algorithm prevents network overload by adjusting transmission rate",
                "🔀 Multiplexing: Port numbers allow multiple concurrent TCP connections on single host - fundamental to multi-tasking on networks"
            ],
            [],  # Ports are application-specific
            [
                "Web browsing (HTTP/HTTPS) requiring complete HTML page delivery",
                "Email transmission (SMTP, POP3, IMAP) where messages must arrive intact",
                "File transfer (FTP, SFTP) where every byte of file must match original",
                "SSH remote access where commands must execute reliably",
                "Database connections requiring transactional integrity",
                "Online banking and e-commerce where accuracy is critical"
            ],
            ["UDP", "SCTP"]
        ),
        
        "UDP": Protocol(
            "UDP (User Datagram Protocol)",
            "Transport",
            4,
            "UDP is a lightweight, connectionless transport layer protocol designed for applications that prioritize speed and low latency over guaranteed delivery. Unlike TCP, UDP has minimal overhead - it doesn't establish connections, doesn't guarantee packet delivery or order, and doesn't provide flow control or error recovery. UDP simply sends individual datagrams (packets) to a destination without knowing if they arrive. This makes it ideal for real-time applications where occasional packet loss is acceptable but delays are not, such as video streaming, voice calls, and online games. UDP also supports broadcasting and multicasting - sending a single packet to multiple destinations simultaneously.",
            [
                "⚡ Connectionless: No connection setup or teardown - application sends datagrams immediately to UDP port",
                "🚀 Low Overhead: Only 8-byte header compared to TCP's 20+ bytes - minimizes bandwidth consumption",
                "📦 Datagram-Based: Each packet is independent unit with no relationship to others - application responsible for coherence",
                "⚠️ No Delivery Guarantee: Packets may be lost, duplicated, reordered, or delayed - application must handle this",
                "🏃 Low Latency: Minimal transmission delay since no flow control or error recovery mechanisms",
                "📍 Broadcasting/Multicasting: Can send single packet to multiple recipients simultaneously - efficient for group communication",
                "🔢 Port Numbers: Enable multiplexing of multiple UDP applications on single host",
                "⏱️ No State Management: Stateless protocol reduces server resource requirements - can handle many concurrent clients"
            ],
            [],  # Ports are application-specific
            [
                "Live video streaming where occasional frame loss acceptable",
                "VoIP phone calls and audio conferencing with real-time requirements",
                "Online gaming requiring fast updates with low latency",
                "DNS queries where client can retry if response lost",
                "DHCP server discovery and address assignment",
                "Network monitoring and SNMP queries",
                "Streaming media and multimedia conferencing protocols"
            ],
            ["TCP", "SCTP"]
        ),
        
        "SCTP": Protocol(
            "SCTP (Stream Control Transmission Protocol)",
            "Transport",
            4,
            "SCTP is a reliable, message-oriented transport protocol that combines the best features of both TCP and UDP. Developed by the IETF for telecommunications, SCTP establishes associations between endpoints and guarantees delivery of messages without requiring strict ordering. Unlike TCP's single stream of data, SCTP can multiplex multiple independent streams within one association, enabling each stream to preserve message boundaries without blocking other streams. SCTP supports multi-homing, allowing a single association to use multiple IP addresses for redundancy and failover. This is particularly valuable in telecommunications networks where high availability and fault tolerance are critical. SCTP includes congestion control, flow control, selective acknowledgment, and heartbeat mechanisms similar to TCP, but adds message orientation and multi-streaming capabilities that make it ideal for modern signaling protocols and applications requiring both reliability and message structure.",
            [
                "🔗 Association-Based: Establishes logical connections with four-way handshake before transferring data",
                "📨 Message-Oriented: Preserves application message boundaries - each message treated as atomic unit",
                "🔄 Multi-Stream: Multiple independent streams within single association - stream blocking doesn't affect others",
                "✅ Reliable Ordered Delivery: In-sequence delivery within streams with retransmission of lost chunks",
                "🏠 Multi-Homing: Can bind/use multiple IP addresses per endpoint for redundancy and failover resilience",
                "🤝 Flow/Congestion Control: TCP-like mechanisms prevent network congestion - adjusts transmission rate dynamically",
                "📞 Selective Acknowledgment: Acknowledges only received chunks reducing overhead compared to cumulative ACKs",
                "💓 Heartbeat Mechanism: Periodic heartbeats detect silent failures on idle associations enabling quick failover"
            ],
            [],  # Ports are application-specific
            [
                "Telecommunications signaling protocols (replacement for older SS7 protocol)",
                "SIP (Session Initiation Protocol) signaling in VoIP over IP networks",
                "H.248 media gateway controllers for telecom infrastructure",
                "DIAMETER protocol for AAA (Authentication, Authorization, Accounting)",
                "3GPP IMS (IP Multimedia Subsystem) signaling traffic",
                "Applications requiring multiple reliable ordered streams",
                "High availability network applications needing fault tolerance capabilities"
            ],
            ["TCP", "UDP"]
        ),
        
        # Network Layer Protocols (Layer 3)
        "IP": Protocol(
            "IP (Internet Protocol)",
            "Network",
            3,
            "IP (Internet Protocol) is the fundamental protocol enabling all modern internet communication. It provides logical addressing through IP addresses and packet routing across networks of varying types and sizes. IP operates at Layer 3 (Network Layer) and encapsulates higher-layer data into packets, each with a source and destination IP address. There are two major versions: IPv4 uses 32-bit addresses (supporting ~4.3 billion unique addresses), while IPv6 uses 128-bit addresses (supporting vast address space for future growth). IP is connectionless and unreliable - it makes no guarantees about packet delivery, ordering, or non-duplication. Higher-layer protocols like TCP handle reliability. IP routing employs forwarding algorithms where routers examine the destination IP address and consult routing tables to determine optimal next hops. The Time-To-Live (TTL) field prevents packets from circulating indefinitely in case of routing loops. IPv6 improves upon IPv4 with better security, automatic address configuration (SLAAC), improved multicast, and address hierarchy enabling more efficient routing.",
            [
                "🏷️ Logical Addressing: IPv4 (32-bit, e.g., 192.168.1.1) or IPv6 (128-bit, e.g., 2001:db8::1) uniquely identifies devices",
                "🛣️ Routing and Forwarding: Routers examine destination IP and forward packets toward destination using routing tables",
                "🌐 Inter-Network Communication: Enables seamless communication across diverse network types and topologies",
                "📦 Packet Structure: Adds IP header (20 bytes IPv4, 40 bytes IPv6) containing source/dest addresses, TTL, protocol type",
                "⏱️ TTL (Time-To-Live): Counter decremented at each hop preventing infinite loops; packet discarded when TTL=0",
                "🔗 Connectionless Protocol: No connection establishment; each packet independently routed based on destination",
                "↑✅ IPv6 Improvements: 128-bit addressing (340 undecillion addresses), integrated security, auto-configuration, better multicast",
                "🚫 No Reliability Guarantee: Best-effort delivery; TCP/UDP handle retransmission and ordering as needed"
            ],
            [],
            [
                "Complete internet infrastructure - every online device uses IP",
                "Email delivery across servers globally",
                "Web browsing and HTTP/HTTPS traffic routing",
                "Video streaming and multimedia delivery",
                "VoIP and real-time communications between networks",
                "Cloud computing and data center networking",
                "IoT device communication globally"
            ],
            []
        ),
        
        "ICMP": Protocol(
            "ICMP (Internet Control Message Protocol)",
            "Network",
            3,
            "ICMP is an auxiliary protocol operating at the Network Layer that provides diagnostic and error-reporting capabilities for IP networks. Unlike TCP and UDP which carry user data, ICMP carries control information. When an IP packet encounters problems during transmission (unreachable destination, TTL expired, network congestion), devices send ICMP messages back to the source reporting the issue. ICMP is encapsulated within IP packets and includes message types like Echo Request/Reply (ping), Destination Unreachable, Time Exceeded, Parameter Problem, and Redirect. The ping utility uses ICMP Echo Request/Reply to test host reachability and measure round-trip time. Traceroute leverages ICMP Time Exceeded messages to map the path packets take toward a destination by incrementally increasing TTL values. ICMP is essential for network troubleshooting and maintenance - administrators rely on ICMP diagnostics to understand network behavior and isolate connectivity problems. Modern networks sometimes rate-limit ICMP to prevent its misuse in denial-of-service attacks, but this can complicate legitimate diagnostics.",
            [
                "🔍 Echo Request/Reply: Ping command sends Echo Request, receiving Echo Reply confirms host is reachable and alive",
                "📍 Traceroute Path Discovery: Time Exceeded messages reveal each router hop in path to destination",
                "❌ Destination Unreachable: Reports when host, network, port, or protocol is unreachable",
                "⏱️ Time Exceeded: Alerts when packet's TTL reaches zero or reassembly time limit exceeded",
                "🔄 Redirect Messages: Router tells host of better route for future packets to destination",
                "⚙️ Parameter Problem: Reports issues with IP header fields that routers can't process",
                "📡 Network Diagnostics: Essential for troubleshooting connectivity, latency, and routing issues",
                "🚫 Rate Limiting Considerations: Modern networks may limit ICMP for DDoS protection complicating legitimate troubleshooting"
            ],
            [],
            [
                "Network connectivity testing and diagnosis with ping",
                "Route path mapping and hop-by-hop analysis with traceroute",
                "Receiving unreachable destination notifications from routers",
                "Network performance and latency analysis",
                "Identifying router configuration and routing issues",
                "Detecting network congestion through Time Exceeded messages",
                "Network maintenance and infrastructure troubleshooting"
            ],
            []
        ),
        
        "ARP": Protocol(
            "ARP (Address Resolution Protocol)",
            "Network",
            3,
            "ARP bridges the gap between Layer 3 (logical IP addresses) and Layer 2 (physical MAC addresses) by dynamically discovering the MAC address associated with an IP address on a local network segment. Although IP handles routing across networks, within a single network link (e.g., Ethernet LAN), devices must know each other's physical addresses to send frames. When a host needs to communicate with another IP address on the same network, it first checks its ARP cache. If not found, it broadcasts an ARP request asking 'Who has this IP address?' across the network. The device with that IP responds with its MAC address. This address mapping is cached locally to avoid repeated broadcasts. ARP operates at Layer 2.5 (between network and link layers) and is crucial for local network communication. However, ARP's broadcast nature and lack of authentication make it vulnerable to ARP spoofing attacks where an attacker sends false ARP responses claiming to own certain IP addresses, enabling man-in-the-middle attacks. Gratuitous ARP allows devices to announce or update their own MAC address information proactively.",
            [
                "🔗 IP-to-MAC Resolution: Discovers physical MAC address for target IP on same network segment",
                "📡 Broadcast Request: Sends ARP request frame to all devices asking 'Who has this IP?'",
                "💾 ARP Cache: Locally stores IP-to-MAC mappings with TTL for performance optimization",
                "🔄 Request-Reply Exchange: Target responds with unicast ARP reply containing its MAC address",
                "🛡️ Spoofing Vulnerability: No authentication - attackers can send false ARP replies for MITM attacks",
                "🔃 Gratuitous ARP: Device proactively announces its own IP-MAC mapping to all network devices",
                "⏱️ Cache Timeout: Entries expire if not refreshed preventing stale mappings from being used",
                "🌐 Essential for Local Communication: Absolutely required for devices to find each other on LANs"
            ],
            [],
            [
                "Local network device discovery and communication",
                "Translating IP addresses to MAC addresses for frame transmission",
                "Network troubleshooting to verify IP-MAC address associations",
                "Interface failover and virtual IP management with Gratuitous ARP",
                "ARP spoofing and man-in-the-middle attack detection",
                "DHCP address assignment verification",
                "Load balancer and failover cluster communications"
            ],
            []
        ),
        
        "IGMP": Protocol(
            "IGMP (Internet Group Management Protocol)",
            "Network",
            3,
            "IGMP manages multicast group membership on IP networks, enabling efficient one-to-many communication. In traditional unicast, sending the same data to multiple recipients requires duplicate transmissions. Multicast allows a single source to send packets to a multicast group address, and only hosts that have expressed interest in that group receive the traffic. IGMP enables hosts to join/leave multicast groups and informs local routers about group membership interests. When a host wants to receive multicast traffic for a group, it sends an IGMP join message. Routers maintain group membership tables and only forward multicast traffic onto network segments where interested members exist, significantly reducing unnecessary bandwidth consumption. Routers periodically query group membership, and hosts respond indicating which groups they're still interested in. IGMP exists in multiple versions - IGMPv1 (basic), IGMPv2 (group-specific queries), and IGMPv3 (source-specific multicast allowing hosts to specify which sources' traffic they want). Multicast is critical for bandwidth-efficient distribution of video streams, IPTV, gaming updates, and other group communication applications.",
            [
                "📺 Multicast Groups: Enables efficient one-to-many communication using multicast IP addresses (224.0.0.0-239.255.255.255)",
                "🔔 Group Join/Leave: Hosts send IGMP messages to join/leave multicast groups",
                "🎯 Interest Declaration: Informs local routers about interest in specific multicast traffic",
                "🔄 Query-Response Model: Routers query membership periodically; hosts respond confirming interests",
                "📊 Bandwidth Efficiency: Routers only forward multicast traffic to segments with interested members",
                "📡 Source-Specific Multicast (SSMv3): IGMPv3 allows specifying which sources to receive from",
                "⏱️ Membership Timeout: Entries removed if host stops responding to queries",
                "🌐 Layer 2 Integration: Works with IGMP snooping on switches for further optimization"
            ],
            [],
            [
                "Multicast video streaming and live broadcast distribution",
                "IPTV content delivery to subscriber groups",
                "Online gaming server updates and state synchronization",
                "Network resource discovery and service announcements",
                "Real-time conferencing and collaborative applications",
                "Emergency alerts and information dissemination",
                "Bandwidth-efficient multimedia content distribution"
            ],
            []
        ),
        
        "IPsec": Protocol(
            "IPsec (IP Security)",
            "Network",
            3,
            "IPsec is a comprehensive protocol suite providing encryption, authentication, and integrity checking at the Network Layer. By securing IP itself, IPsec protects all applications above it without requiring application-level modifications. IPsec operates in two modes: Transport mode encrypts only the payload while using original IP headers (end-to-end security), and Tunnel mode encrypts entire IP packets including headers, encapsulating them in new IP packets (network-to-network security useful for VPNs). IPsec uses two main protocols: Authentication Header (AH) provides authentication and integrity but not encryption, while Encapsulating Security Payload (ESP) provides authentication, integrity, and encryption. IPsec employs IKE (Internet Key Exchange) protocol for dynamic key agreement and management, replacing manual key distribution. The IPsec security association (SA) defines encryption algorithm, authentication method, encryption keys, and other parameters. IPsec's primary modern use is VPN implementation, allowing secure tunnels through untrusted networks. However, IPsec complexity and per-packet overhead led to TLS/SSL becoming the dominant security protocol for application-level security.",
            [
                "🔒 End-to-End Encryption: Protects IP payload confidentiality preventing eavesdropping",
                "🔐 Authentication & Integrity: Verifies packet source and detects tampering",
                "🚄 Transport vs Tunnel Mode: Transport (end-to-end between hosts), Tunnel (network-to-network, VPN)",
                "🔑 Dynamic Key Management: IKE protocol negotiates and manages encryption/authentication keys automatically",
                "🤝 Security Association: Stateful connection defining encryption algorithms, keys, and parameters",
                "📝 Authentication Header (AH): Provides authentication & integrity without encryption for authentication-only needs",
                "📦 Encapsulating Security Payload (ESP): Provides authentication, integrity AND encryption in single protocol",
                "🌐 VPN Foundation: Standard protocol for site-to-site VPNs and remote access VPN solutions"
            ],
            [],
            [
                "Virtual Private Networks (VPNs) for secure site-to-site connections",
                "Remote employee secure access to corporate networks",
                "Protecting sensitive communications between branch offices",
                "Securing cloud infrastructure and hybrid IT networks",
                "Government and military secure communications networks",
                "Protecting IoT device communications across untrusted networks",
                "Enterprise network security and data protection"
            ],
            ["TLS", "SSL"]
        ),
        
        # Link Layer / Data Link Layer Protocols (Layer 2)
        "Ethernet": Protocol(
            "Ethernet",
            "Link/Data Link",
            2,
            "Ethernet is the dominant physical (Layer 1) and data link (Layer 2) technology for local area networks. Developed in the 1970s at Xerox Palo Alto Research Center, Ethernet originally operated at 10 Mbps and has evolved to support speeds up to 400 Gbps today. Ethernet frames contain destination and source MAC addresses, enabling devices on the same network segment to find each other using ARP. Early Ethernet used CSMA/CD (Carrier Sense Multiple Access with Collision Detection) on shared bus topologies where devices collided when transmitting simultaneously. Modern Ethernet moved to star topology with switches that learn MAC addresses and forward frames only to appropriate ports, eliminating collisions. Ethernet operates using encapsulation - IP packets become Ethernet frames with MAC headers. The frame includes CRC (Cyclic Redundancy Check) for error detection. Standard Ethernet cable types evolved: 10BaseT, 100BaseTX, 1000BaseT (gigabit), and fiber increasingly used for 10G/100G+ links. Ethernet's simplicity, reliability, backward compatibility, and cost-efficiency made it the universal LAN standard. Power over Ethernet (PoE) extensions deliver power through cables for devices like VoIP phones and cameras.",
            [
                "🖧 MAC Addressing: 48-bit addresses uniquely identify network interface cards on LANs",
                "📡 Frame Format: Destination MAC, Source MAC, Type, Payload, CRC checksum",
                "🔄 CSMA/CD (Legacy): Devices listen before transmitting, detect collisions in shared-media networks",
                "🌐 Switch-Based (Modern): Star topology with intelligent switches learning MAC port mappings",
                "📊 Collision Domains: Switches isolate collision domains per port enabling full-duplex communication",
                "⚡ Speed Evolution: 10 Mbps → 100 Mbps → 1 Gbps → 10 Gbps → 100 Gbps → 400 Gbps",
                "🔌 Media Types: UTP (Cat5/Cat6), STP, Fiber Optic (Single-mode/Multi-mode)",
                "⚡ Power over Ethernet: PSE injects power into cables simultaneously with data transmission"
            ],
            [],
            [
                "Office and enterprise LAN connectivity",
                "High-speed server-to-switch backbone connections",
                "Wired internet access for desktops and workstations",
                "Data center east-west networking",
                "IP phone and security camera connectivity with PoE",
                "Storage networks and SAN infrastructure",
                "Industrial and IoT device networking"
            ],
            ["Wi-Fi", "PPP"]
        ),
        
        "PPP": Protocol(
            "PPP (Point-to-Point Protocol)",
            "Link/Data Link",
            2,
            "PPP is a data link protocol enabling direct communication between two network nodes over serial or point-to-point links. Developed in the early 1990s, PPP operates at Layer 2 and is protocol-independent - it can encapsulate and transport various network layer protocols including IP, IPX, and AppleTalk. PPP architecture consists of three main components: LCP (Link Control Protocol) for establishing and configuring links, NCP (Network Control Protocol) for negotiating network layer protocols, and authentication protocols (PAP/CHAP). The connection process begins with Link Establishment Phase where LCP negotiates parameters like maximum frame size and compression. After authentication, NCP configures network layer details like IP address assignment. PPP supports authentication via PAP (Password Authentication Protocol) for basic authentication and CHAP (Challenge Handshake Authentication Protocol) for more secure challenge-response authentication. PPP's simplicity and authentication support made it standard for dial-up internet, ISDN, T1/E1 WAN connections, and mobile broadband. Modern PPP variants include PPPoE (PPP over Ethernet) for DSL, PPPoA (PPP over ATM), and L2TP (Layer 2 Tunneling Protocol) that tunnels PPP over IP.",
            [
                "☎️ Point-to-Point Link: Establishes direct connection between two nodes (not multi-access like Ethernet)",
                "🔗 Link Control Protocol (LCP): Negotiates link parameters - MTU size, compression, encryption options",
                "🌐 Network Control Protocol (NCP): Configures network layer - IP address assignment, compression",
                "🔐 Authentication: PAP (Password) or CHAP (Challenge-Handshake) for secure connection establishment",
                "📦 Multiple Protocols: Can transport IPv4, IPv6, IPX, AppleTalk and other protocols",
                "💚 Stateful Connection: Tracks connection lifecycle through phases - establish, authenticate, open, close",
                "📱 WAN Links: Widely used for serial, dial-up, ISDN, Frame Relay, ATM, and mobile data connections",
                "🔄 PPP Variants: PPPoE (DSL), PPPoA (ATM), L2TP (IP tunneled PPP), PPTP (Windows VPN)"
            ],
            [],
            [
                "Dial-up internet access from residential users",
                "Mobile broadband data connections (3G/4G/LTE)",
                "WAN links connecting remote office routers",
                "ADSL and DSL internet connections via PPPoE",
                "Modem connections to ISPs",
                "Serial links in industrial and embedded systems",
                "VPN connections using PPTP/L2TP/IPsec",
                "Point-to-point WAN circuits"
            ],
            ["Ethernet", "Wi-Fi"]
        ),
        
        "MAC": Protocol(
            "MAC (Media Access Control)",
            "Link/Data Link",
            2,
            "MAC (Media Access Control) is the lower sublayer of Layer 2 (Data Link Layer), responsible for controlling device access to shared network media and handling frame transmission. While LLC (Logical Link Control) provides flow control and error correction, MAC handles the physical addressing and media access mechanics. MAC sublayer defines how devices share transmission medium - on Ethernet this evolved from CSMA/CD collision detection on shared bus to modern switching where devices have dedicated paths. Each network interface has a unique 48-bit MAC address (like 00:1A:2B:3C:4D:5E) used for local network communication. Switches learn MAC addresses and maintain forwarding tables mapping MACs to physical ports. When a unicast frame arrives, the switch forwards it only to the port associated with the destination MAC, reducing unnecessary traffic. Broadcast frames (destination MAC FF:FF:FF:FF:FF:FF) reach all ports on the VLAN. Multicast frames reach specific groups. MAC also handles frame formatting with headers, trailers, and CRC error detection. Modern features include VLAN tagging allowing logical network segmentation over shared infrastructure.",
            [
                "📍 MAC Addressing: 48-bit (OUI manufacturer prefix + device ID) uniquely identifies network interface",
                "🖥️ MAC Address Structure: First 3 bytes manufacturer OUI, last 3 bytes burned-in-address (BIA)",
                "🔄 Media Access Mechanism: CSMA/CD (legacy shared) or switched (modern point-to-point)",
                "🌐 Address Types: Unicast (individual), Broadcast (FF:FF:FF:FF:FF:FF), Multicast (managed by IGMP)",
                "📦 Frame Structure: Destination MAC, Source MAC, Type, Payload, CRC/FCS error checking",
                "🔀 Switching: Switches maintain MAC forwarding tables learning port associations",
                "🛡️ Error Detection: Frame Check Sequence (FCS) detects transmission errors corrupting frames",
                "🏷️ VLAN Tagging: 802.1Q tags add VLAN ID to frames enabling network segmentation"
            ],
            [],
            [
                "Local area network switching and frame forwarding",
                "ARP protocol uses MAC addresses to resolve IPs locally",
                "Spanning Tree Protocol (STP) prevents loops in redundant topologies",
                "Virtual LAN (VLAN) implementation and segmentation",
                "Network segmentation and logical isolation",
                "LAG (Link Aggregation) combining multiple ports",
                "MAC address filtering and network access control",
                "Network troubleshooting and switching table management"
            ],
            []
        ),
        
        "Wi-Fi": Protocol(
            "Wi-Fi (802.11)",
            "Link/Data Link",
            2,
            "Wi-Fi (Wireless Fidelity) implements the IEEE 802.11 standards for wireless local area networks (WLANs), enabling devices to connect to networks using radio waves instead of cables. Operating in unlicensed frequency bands (2.4 GHz and 5 GHz), Wi-Fi has become ubiquitous in homes, offices, and public spaces. The 2.4 GHz band offers longer range but has only three non-overlapping channels, causing interference in crowded environments. The 5 GHz band provides more channels and potentially less interference but shorter range. Modern Wi-Fi 6 (802.11ax) also uses 6 GHz band expansion. Multiple standards provide progressive improvements: 802.11b (11 Mbps), 802.11g (54 Mbps), 802.11n (600 Mbps), 802.11ac (1.3 Gbps), and 802.11ax Wi-Fi 6 (9.6 Gbps). Wi-Fi uses CSMA/CA (Collision Avoidance) instead of detection due to wireless medium challenges. Security evolved through WEP (deprecated), WPA, WPA2 with CCMP encryption, and WPA3 with advanced cryptography. Wi-Fi networks require SSID (Service Set Identifier) for identification and operate in Infrastructure mode (with access point) or Ad-hoc mode (direct device-to-device).",
            [
                "📶 Wireless Radio Transmission: 2.4 GHz (longer range, more interference) and 5 GHz (shorter range, less interference) bands",
                "🔐 Security Protocols: WEP (broken), WPA (TKIP), WPA2 (CCMP AES encryption), WPA3 (Simultaneous Authentication of Equals)",
                "🎯 SSID Broadcast: Service Set Identifier transmitted in beacons identifying network name",
                "📡 Channel Management: Multiple non-overlapping channels reduce interference between neighboring networks",
                "⚡ Speed Evolution: 802.11b (11 Mbps) → 11g (54 Mbps) → 11n (600 Mbps) → 11ac (1.3 Gbps) → 11ax (9.6 Gbps)",
                "🔄 CSMA/CA: Carrier Sense Multiple Access with Collision Avoidance - listen before transmitting to minimize collisions",
                "🏠 Range Limitations: 30-100 meters depending on obstacles, interference, and antenna gain",
                "🤝 Infrastructure/Ad-hoc: Infrastructure mode (via AP) for networks, Ad-hoc for device-to-device"
            ],
            [],
            [
                "Home and office wireless internet network access",
                "Mobile devices (smartphones, tablets, laptops) connectivity",
                "Public hotspots in cafes, airports, hotels",
                "IoT device networking and smart home applications",
                "Guest networks for visitor access",
                "Mesh networks for extended coverage",
                "Enterprise WLANs with centralized management",
                "Outdoor wireless bridging between buildings"
            ],
            ["Ethernet", "Cellular"]
        ),
        
        # Physical Layer Protocols (Layer 1)
        "Copper Wire": Protocol(
            "Copper Wire",
            "Physical",
            1,
            "Copper wire is the most widely deployed physical medium for networks, transmitting data as electrical signals through twisted pair cables. Twisted pair cables reduce electromagnetic interference by twisting two insulated conductors together, canceling external field interference. Two main types exist: UTP (Unshielded Twisted Pair) used in Ethernet, and STP (Shielded Twisted Pair) with foil or braided shield for additional protection in electrically noisy environments. The cable category determines maximum speed and frequency - Cat5e supports 1 Gbps to 100 meters, Cat6 supports 10 Gbps to 55 meters, while Cat6a and Cat7 enable 10 Gbps to full 100-meter distances. Coaxial cables (used in cable television) have center conductor surrounded by shield, enabling longer distances than twisted pair. Despite electromagnetic interference vulnerability and distance limitations compared to fiber, copper's cost-effectiveness, ease of installation (existing infrastructure), and socket availability in every device make it standard. Power over Ethernet (PoE) delivers power through copper cables while transmitting data, eliminating separate power cables for VoIP phones, cameras, and access points.",
            [
                "⚡ Electrical Signal Transmission: Data encoded as voltage variations on copper conductor",
                "🔌 Twisted Pair Construction: Two insulated wires twisted together canceling electromagnetic interference",
                "🛡️ Shielding Options: UTP (unshielded basic), STP (foil shield), ScTP (braided shield)",
                "📏 Distance Limitations: 100 meters standard for Ethernet regardless of speed variant",
                "🔄 Signal Attenuation: Electrical resistance causes signal degradation over distance",
                "📊 Cable Categories: Cat3 (10 Mbps), Cat5e (1 Gbps), Cat6 (10 Gbps/55m), Cat6a (10 Gbps/100m)",
                "💡 Backward Compatible: Different speeds negotiated automatically (autonegotiation)",
                "⚡ PoE Integration: Power and data delivered simultaneously eliminating separate power runs"
            ],
            [],
            [
                "Office LAN connections for workstations",
                "ISP to home connections (broadband internet)",
                "Data center access networks and ToR (Top of Rack)",
                "Industrial network infrastructure",
                "Structured cabling in buildings",
                "Network of devices not requiring long distances",
                "Existing deployed infrastructure (trillions installed globally)"
            ],
            ["Fiber Optic", "Wireless"]
        ),
        
        "Fiber Optic": Protocol(
            "Fiber Optic",
            "Physical",
            1,
            "Fiber optic cables transmit data as pulses of light through strands of extremely pure glass or plastic fibers. Each fiber has a core (8-50 micrometers) surrounded by cladding with different refractive index, confining light within the core by total internal reflection. Fiber offers dramatically superior performance compared to copper - speeds exceeding terabits per second, transmission distances of 100+ kilometers without amplification, complete immunity to electromagnetic interference, and inherent security since light doesn't radiate. Two major types: Single-Mode Fiber (SMF) with tiny core used for long distances allowing only one light mode, and Multi-Mode Fiber (MMF) with larger core used for shorter distances supporting multiple light paths. Short-reach 850 nm and longer-reach 1550 nm wavelengths are common. Fiber typically costs more per meter than copper but total cost of ownership favors fiber for high-speed, long-distance, or electrically noisy environments. Fiber dominates internet backbones, undersea cables connecting continents (transatlantic/transpacific), data center cores requiring 40-400 Gbps throughput, and locations near electrical equipment (power plants, railroads). Installation requires trained technicians and precision splicing.",
            [
                "💡 Light Pulse Transmission: Data encoded as modulated light pulses through glass/plastic fiber",
                "🚀 Extreme Bandwidth: Terabits per second throughput enabling massive data pipes",
                "📏 Long Distance: 100+ km transmission without repeaters (single-mode); DWDM enables even greater capacity",
                "🛡️ EMI Immune: Complete immunity to electromagnetic interference from power lines, motors, industrial equipment",
                "🔒 Inherent Security: Light confined to fiber - no emissions radiating outward enabling tapping",
                "📊 Two Types: Single-Mode (tiny core, long distance) vs Multi-Mode (larger core, short distance)",
                "⚡ Low Attenuation: Signal loss only 0.2 dB/km (vs copper ~5 dB/100m) enabling long spans",
                "🌐 Wavelength Division Multiplexing: Multiple colors (wavelengths) simultaneously on single fiber"
            ],
            [],
            [
                "Internet backbone infrastructure and core networks",
                "Long-distance telecommunications between cities/countries",
                "Submarine cables connecting continents underwater",
                "Data center core networks handling 100+ Gbps",
                "Cable television infrastructure (hybrid fiber-coaxial)",
                "Military and government secure communications",
                "Locations with extreme EMI (power plants, factories)",
                "Future-proofing critical infrastructure"
            ],
            ["Copper Wire", "Wireless"]
        ),
        
        "Wireless": Protocol(
            "Wireless Transmission",
            "Physical",
            1,
            "Wireless transmission uses electromagnetic radiation (radio waves) to transmit data through air or vacuum without physical cables. Different frequency bands and modulation techniques enable diverse wireless technologies spanning from long-distance satellite to short-range Bluetooth. The electromagnetic spectrum spans from extremely low frequency (ELF) through radio, microwave, infrared, visible light, ultraviolet, and ionizing radiation. Network systems use licensed bands (cellular carriers obtain exclusive licenses) and unlicensed ISM (Industrial Scientific Medical) bands (2.4 GHz and 5 GHz) shared freely. Modulation techniques encode data onto carrier waves - amplitude modulation (AM), frequency modulation (FM), phase shift keying (PSK), quadrature amplitude modulation (QAM), and orthogonal frequency-division multiplexing (OFDM) used in Wi-Fi/4G/5G. Signal propagation through air involves path loss (inverse square law), fading from multipath reflections, and Doppler shifts when transmitters/receivers move. Obstacles attenuate signals significantly - walls cause 10+ dB loss, metal reflects signals, water absorbs heavily. Wireless enables mobility impossible with fixed wires, though with reduced reliability and security considerations.",
            [
                "📡 Electromagnetic Radiation: Data transmitted as radio waves through air/space",
                "🔄 Modulation: Encodes data onto carrier wave - AM, FM, PSK, QAM, OFDM techniques",
                "🌍 Frequency Bands: Licensed (cellular providers) and unlicensed ISM (2.4 GHz, 5 GHz) spectrum",
                "📏 Path Loss: Signal power decreases with inverse square of distance (exponential attenuation)",
                "🔃 Multipath Propagation: Signals reflect off surfaces creating interference and fading",
                "🛡️ Obstacles: Walls attenuate significantly (10+ dB), metal reflects, water absorbs heavily",
                "🚗 Doppler Effect: Motion causes frequency shifts affecting reception quality",
                "📊 Multiple Technologies: Cellular (licensed), Wi-Fi (unlicensed), Bluetooth (short-range), Satellite"
            ],
            [],
            [
                "Wi-Fi local area networks in offices and homes",
                "Cellular mobile networks (3G/4G/5G) for phones/tablets",
                "Satellite communication for remote/maritime areas",
                "Bluetooth and Zigbee for IoT/wearable devices",
                "Microwave backhaul between cell towers",
                "Terrestrial TV and radio broadcasting",
                "Radar systems for navigation and weather",
                "Short-range wireless (NFC, RFID) for payment/identification"
            ],
            ["Copper Wire", "Fiber Optic"]
        ),
        
        "Bluetooth": Protocol(
            "Bluetooth",
            "Physical",
            1,
            "Bluetooth is a short-range wireless Personal Area Network (PAN) technology using spread-spectrum frequency hopping (SSFH) to transmit on the 2.4 GHz ISM band. Developed by Ericsson (Nokia) and standardized by the Bluetooth SIG, it was designed for low-power wireless connections between adjacent devices without line-of-sight requirement. Bluetooth operates in unlicensed 2.4 GHz band shared with Wi-Fi, Zigbee, and microwave ovens. Frequency hopping (1600 hops/second) switches between 79 channels (1 MHz each) pseudo-randomly, creating resilience against interference and narrow-band jammers. Bluetooth divides the band into 625 microsecond time slots, establishing point-to-point connections between master (initiating) and slave (responding) devices in a piconet. Up to 7 slaves connect per master in classic Bluetooth; one master and multiple slaves form a scatternet when piconets overlap. Bluetooth Low Energy (BLE) introduced in 4.0 uses fewer channels (37 vs 79), simpler protocol, and aggressive power management extending battery life from hours to months/years. Modern Bluetooth 5.x adds extended range (240 meters), mesh networking, and higher throughput. Core applications include wireless audio (headphones, speakers), wearables (watches, fitness trackers), IoT devices, and mobile phone peripherals.",
            [
                "📱 Short Range: 10-100 meters typical (Bluetooth 5 extends to 240m)",
                "⚡ Low Power: BLE designed for months/years battery life in wearables",
                "🔄 Frequency Hopping SSFH: Pseudo-randomly switches 1600 hops/second across 79 channels for interference resilience",
                "🔗 Pairing/Bonding: Devices establish trusted relationships storing keys for future connections",
                "📊 Master-Slave: Master initiates piconets; slaves respond (up to 7 per master in classic)",
                "🎯 Bluetooth Low Energy (BLE): Simplified protocol for ultra-low power IoT/wearables",
                "🌐 Mesh Networking (5.1+): Devices relay messages extending range and reliability",
                "🎧 Audio Profiles: A2DP (stereo audio), HFP (handsfree calls), AVRCP (media control)"
            ],
            [],
            [
                "Wireless headphones and stereo speakers",
                "Smartwatches and fitness tracker wearables",
                "Medical devices (heart monitors, pulse oximeters)",
                "IoT sensors and environmental monitoring",
                "Keyboard/mouse/trackpad wireless input devices",
                "Mobile phone connectivity to car audio/hands-free",
                "Home automation and smart lighting control",
                "Asset tracking and location services"
            ],
            ["Wi-Fi", "NFC"]
        ),
        
        # Additional Layer 2 Protocols
        "HDLC": Protocol(
            "HDLC (High-Level Data Link Control)",
            "Link/Data Link",
            2,
            "HDLC is an ISO standard bit-oriented data link protocol designed for synchronous, point-to-point and multipoint communications. Developed in the 1970s and standardized by ISO, HDLC-based protocols became foundational for WAN technologies. HDLC operates at the bit level (not character level like earlier asynchronous protocols) using flag sequences (01111110) to delimit frames and bit stuffing to prevent flags appearing in data. HDLC supports both connection-oriented (after establishing connection) and connectionless modes. As a synchronous protocol, it requires synchronized clocks between sender and receiver, typically using timing signals from the physical layer. HDLC includes sophisticated flow control with sliding window mechanisms and selective repeat for efficient, reliable transmission. The frame structure includes address and control fields for multipoint operation where a primary station manages multiple secondary stations. Error checking uses 16-bit or 32-bit CRC (Cyclic Redundancy Check) polynomials. HDLC became the basis for many specialized protocols - LAPD (Link Access Procedure for D-channel) in ISDN, Frame Relay's DLC protocol, and X.25. While HDLC itself is less common in modern networks, its variants and descendants remain critical for telecommunications infrastructure.",
            [
                "🔄 Bit-Oriented Protocol: Operates at bit level enabling efficient use of synchronous links",
                "📡 Synchronous Transmission: Requires synchronized clocks between endpoints for bit-level operations",
                "🚩 Frame Delimiters: Flag bytes (01111110) mark frame boundaries; bit stuffing prevents flags in payload",
                "🤝 Multiple Modes: Unbalanced (primary-secondary multipoint), balanced (peer-to-peer), asymmetric",
                "🔒 Strong Error Detection: 16-bit or 32-bit CRC detects burst errors and transmission issues",
                "🔄 Flow Control: Sliding window (not stop-and-wait) for efficient pipelining of frames",
                "📊 Frame Structure: Flag, Address, Control, Payload, FCS checksum, Flag enabling multipoint operation",
                "🌐 Foundation Protocol: Basis for LAPD (ISDN), Frame Relay DLC, X.25, and telecom protocols"
            ],
            [],
            [
                "WAN connections and serial links",
                "ISDN data channels (LAPD protocol derivative)",
                "Frame Relay switching networks",
                "X.25 packet switching networks",
                "Telecommunications equipment",
                "Legacy and specialized network connections",
                "Industrial control and embedded systems",
                "Point-to-point leased line communications"
            ],
            ["PPP", "Frame Relay"]
        ),
        
        "Frame Relay": Protocol(
            "Frame Relay",
            "Link/Data Link",
            2,
            "Frame Relay is a packet-switched wide-area network technology that emerged in the 1990s to provide cost-effective connectivity between geographically distributed sites. Unlike circuit-switched networks (traditional dedicated leased lines), Frame Relay uses virtual circuits sharing the same physical infrastructure - connection bandwidth is multiplexed, reducing customer costs. The Frame Relay network operates as a cloud where customer equipment connects to Frame Relay switches via access links. The service provider creates permanent virtual circuits (PVCs) between sites with defined committed information rates (CIR). The minimal processing (no error correction, flow control, or retransmission) allows high throughput. Data Link Connection Identifiers (DLCIs) identify virtual circuits. Congestion notification mechanisms (FECN/BECN) alert endpoints when the network experiences congestion, allowing graceful degradation. Frame Relay supported fast switching speeds (56 Kbps to 45 Mbps) and enabled organizations to consolidate multiple dedicated lines onto single shared access. However, Frame Relay declined with IP VPN alternatives (MPLS, IPsec VPN) that offered greater flexibility, better quality of service control, and improved security. While largely replaced, some legacy installations remain.",
            [
                "📦 Frame-Based Switching: Transmits variable-length frames with minimal processing",
                "🌐 Multi-Site Connectivity: Virtual circuits connect multiple branch offices through shared network",
                "💰 Multiplexed Bandwidth: Multiple PVCs share single access link reducing circuit costs",
                "📊 Permanent Virtual Circuits (PVCs): Pre-configured paths defined by provider for guaranteed availability",
                "🎯 DLCIs: Data Link Connection Identifiers identify virtual circuits within access link",
                "📈 Committed Information Rate (CIR): Service provider guarantees minimum bandwidth with burst ability",
                "🔔 Congestion Notification: FECN (Forward Explicit Congestion Notification) and BECN alert endpoints",
                "⚠️ Minimal Error Handling: Relies on upper-layer protocols for error recovery unlike X.25"
            ],
            [],
            [
                "Enterprise WAN connectivity between branch offices",
                "Cost-effective alternative to dedicated leased lines",
                "Multi-site corporate network infrastructure",
                "VoIP and multimedia transport over WAN",
                "Legacy network infrastructure still in use",
                "Scheduled data transfer and backup operations",
                "Financial institution private networks",
                "Telecom carrier backhaul networks"
            ],
            ["PPP", "MPLS"]
        ),
        
        # Additional Layer 5 Protocols
        "NetBIOS": Protocol(
            "NetBIOS (Network Basic Input/Output System)",
            "Session",
            5,
            "NetBIOS is a legacy network protocol that provided session layer naming and communication services for local area networks, predating modern TCP/IP. Developed by IBM and Symantics in the 1980s, NetBIOS offered a simple API for network applications to communicate locally. Originally ran over IPX/SPX, later implementations (NetBT) tunneled NetBIOS over TCP/IP. NetBIOS enabled computer name-to-address resolution (WINS), session establishment between computers, and datagram services. Computers registered 16-character names on the network (e.g., MYCOMPUTER), and applications could establish sessions by computer name without needing IP addresses. NetBIOS became synonymous with Windows File Sharing through SMB protocol. However, NetBIOS has significant security limitations - it broadcasts on networks, lacks encryption, and is vulnerable to spoofing and man-in-the-middle attacks. Modern Windows systems support NetBT only for backward compatibility with legacy systems. The industry moved toward DNS (superior scalability), Kerberos (robust authentication), and LDAP (directory services). Direct Hosting (NetBIOS-less SMB over TCP 445) replaces NetBT, avoiding NetBIOS limitations.",
            [
                "👤 Name Registration: Computers register 16-character NetBIOS names on LAN for identification",
                "🤝 Session Layer Services: Establishes named sessions between computers for communication",
                "📊 NetBT (NetBIOS over TCP): Tunneled NetBIOS over TCP/IP ports 137-139 for compatibility",
                "🌐 Broadcast-Based Discovery: Uses broadcasts for name resolution limiting to local networks",
                "🔐 No Encryption: Plain-text communication vulnerable to eavesdropping and spoofing",
                "🖥️ Windows Centric: Primary use in Windows networks; modern systems prefer Direct Hosting",
                "❌ Security Risks: Lack of authentication and encryption causes exposure in modern networks",
                "⏱️ Legacy Only: Modern deployments disable NetBIOS, using Kerberos and DNS instead"
            ],
            [137, 138, 139],
            [
                "Windows file sharing (SMB/CIFS) on legacy systems",
                "Network resource and computer discovery",
                "Legacy network printing services",
                "Computer browser service in older domains",
                "Backward compatibility with pre-2000s systems",
                "NetBIOS-based application development (historical)",
                "Migrating older Windows networks to modern infrastructure",
                "troubleshooting legacy network issues"
            ],
            ["TCP/IP", "Kerberos"]
        ),
        
        "SMB": Protocol(
            "SMB (Server Message Block)",
            "Session",
            5,
            "SMB (Server Message Block) is the primary network file sharing and print sharing protocol used by Windows and increasingly by Linux/Mac through Samba. SMB operates at session layer enabling applications to read/write files, access printers, and communicate with servers on networks. Originally called CIFS (Common Internet File System), SMB evolved from a simple file sharing mechanism in NT 3.1 through to modern SMB 3.1.1 with robust security. SMB protocol defines message formats for file operations (open, read, write, close), printer access, and inter-process communication (IPC). Authentication progressed from LAN Manager and NTLM (legacy, vulnerable) to Kerberos (modern enterprise standard). Early SMB transmitted data in plaintext; SMB3 added AES encryption and signing for integrity. SMB3 also includes Multichannel (bonding multiple connections for throughput), Directory Leasing (caching optimization), and Persistent Handles (continuous connectivity during disconnects). Direct Hosting (SMB over TCP 445) bypasses NetBIOS port 139. Modern deployment on Linux (Samba) and Mac (native support) enables cross-platform file sharing. SMB remains critical for Windows environment and increasingly standard for NAS (Network Attached Storage) and enterprise file servers.",
            [
                "📁 File Sharing: Remote applications open, read/write, delete, and manage files on servers",
                "🖨️ Printer Sharing: Access network printers for printing jobs remotely",
                "🔐 Authentication: LAN Manager→NTLM (legacy/vulnerable)→Kerberos (modern enterprise)",
                "🔒 Encryption: SMB3 adds AES encryption and message signing for confidentiality/integrity",
                "🚄 Multichannel (SMB3): Bonds multiple TCP connections aggregating bandwidth",
                "💾 Caching: Directory Leasing and opportunistic locks improve performance for collaborative files",
                "🌐 Cross-Platform: Native Windows, Samba on Linux, native support on macOS",
                "🔄 Session Management: Long-lived persistent connections with Tree Connect for resource access"
            ],
            [445, 139],
            [
                "Windows file and print sharing (primary use case)",
                "Network attached storage (NAS) access",
                "Office document collaboration and file synchronization",
                "Linux file sharing via Samba (SMB server)",
                "Cross-platform file sharing between Windows/Mac/Linux",
                "Enterprise network storage with Active Directory integration",
                "Backup and archival systems",
                "Virtual machine file service in hypervisor environments"
            ],
            ["NFS", "SFTP"]
        ),
        
        # Additional Layer 6 Protocols
        "SSL": Protocol(
            "SSL/TLS (Secure Sockets Layer / Transport Layer Security)",
            "Presentation",
            6,
            "TLS (Transport Layer Security) is the modern cryptographic protocol enabling secure, authenticated communication over networks. The original SSL was developed by Netscape in the 1990s; after security vulnerabilities emerged, it evolved into TLS standards. TLS operates between Application and Transport layers (sometimes called Layer 4.5), wrapping insecure protocols in a security layer. The TLS handshake establishes a secure connection through public-key cryptography - client and server exchange certificates, verify each other, and negotiate a shared session key for symmetric encryption. Certificates contain a server's public key and are signed by trusted Certificate Authorities (CAs), enabling clients to verify server identity. TLS protects three critical properties: confidentiality (encryption prevents eavesdropping), integrity (MACs detect tampering), and authentication (server identity verification). Modern TLS supports various cipher suites combining key exchange (RSA, ECDHE), authentication (RSA, ECDSA), encryption (AES-GCM, ChaCha20), and hash (SHA256, SHA384) algorithms. TLS 1.3 (2018) modernized the protocol with 0-RTT resumption, all-cipher-suite adoption, and simpler handshake. HTTPS, SMTPS, POP3S, and IMAPS layer TLS over HTTP, SMTP, POP3, and IMAP respectively, securing sessions.",
            [
                "🔒 Confidentiality Encryption: Symmetric encryption (AES, ChaCha20) protects data from eavesdropping",
                "🔐 Authenticity Verification: Server certificates signed by trusted CAs verify server identity preventing MITM attacks",
                "🤝 Key Exchange: Public-key cryptography (RSA, ECDHE) safely negotiates shared symmetric keys",
                "🔄 TLS Handshake: Multi-message protocol establishing secure connection - client hello, server hello, certificate, finished",
                "📊 Cipher Suites: Combinations of encryption (AES-GCM, ChaCha20), key exchange (ECDHE, RSA), hash (SHA-256, SHA-384)",
                "🎀 Forward Secrecy (ECDHE): Ephemeral key exchange prevents past sessions being compromised if keys stolen",
                "⏱️ Version Evolution: SSLv3 (obsolete), TLS 1.0 (deprecated), 1.1 (deprecated), 1.2 (current), 1.3 (modern, 2018)",
                "📜 Certificate Chain: Server cert → Intermediate CA → Root CA enabling trust model"
            ],
            [443],  # Common for HTTPS
            [
                "HTTPS secure web browsing protecting passwords, banking, e-commerce",
                "Email security: SMTPS (submission), POP3S, IMAPS for mail client-server",
                "API endpoint security for mobile apps and web services",
                "VPN connections using TLS-style cryptography (OpenVPN)",
                "Secure messaging and chat applications",
                "Cloud service authentication and data protection",
                "DNS over HTTPS (DoH) for privacy-preserving name resolution",
                "Enterprise security for internal application communication"
            ],
            []
        ),
        
        # Additional Layer 4 Protocols
        "DCCP": Protocol(
            "DCCP (Datagram Congestion Control Protocol)",
            "Transport",
            4,
            "DCCP is a message-oriented transport protocol that fills the gap between UDP and TCP by providing congestion control without the full overhead and reliability guarantees of TCP. While UDP offers speed but lacks congestion awareness, and TCP provides reliability but with higher latency, DCCP strikes a balance for real-time applications that can tolerate some packet loss but require network-friendly congestion control. DCCP uses a connection setup similar to TCP and implements sophisticated congestion control mechanisms, but it's datagram-based like UDP, preserving message boundaries and avoiding the head-of-line blocking problem that TCP suffers. DCCP supports multiple congestion control algorithms, allowing applications to choose the best strategy for their needs. This makes it ideal for video streaming, online gaming, VoIP, and other real-time applications where occasional packet loss is acceptable but network congestion awareness is essential to avoid overloading network resources.",
            [
                "💬 Connection-Oriented: Establishes connections like TCP but with lower overhead",
                "📦 Datagram-Based: Preserves message boundaries - no stream reassembly required",
                "🚦 Congestion Awareness: Actively monitors network congestion and adapts transmission rate",
                "⚡ Low Latency: Immediate transmission without waiting for acknowledgments or retransmissions",
                "🎯 Flexible Delivery: Supports different delivery modes - reliable, semi-reliable, unreliable based on need",
                "🔧 Pluggable Congestion Control: Multiple algorithms (CCID) - TCP-Friendly, TFRC, cubic implementations",
                "⏱️ Real-Time Friendly: Optimized for applications valuing timeliness over perfect delivery",
                "📊 Connection State: Maintains connection state for congestion control decisions without TCP's reliability guarantees"
            ],
            [],
            [
                "Video streaming and multimedia conferencing with adaptive quality",
                "Online gaming requiring responsive gameplay with network awareness",
                "VoIP and voice over IP with congestion control",
                "Interactive real-time applications where updates must be timely",
                "Streaming media where occasional frame loss acceptable but buffering not",
                "Remote desktop applications needing responsiveness without reliability overhead",
                "Applications requiring middle ground between UDP speed and TCP safety"
            ],
            ["UDP", "TCP", "SCTP"]
        ),
        
        # Layer 3 protocols SAP would be here, but it's not really a network layer protocol, so I'll skip it
    }
    
    @staticmethod
    def get_protocol(name):
        """Get protocol by name"""
        return ProtocolDatabase.protocols.get(name)
    
    @staticmethod
    def get_all_protocols():
        """Get all protocols as dictionary"""
        return ProtocolDatabase.protocols
    
    @staticmethod
    def get_protocols_by_layer(layer_name):
        """Get all protocols for a specific layer"""
        return {
            name: proto for name, proto in ProtocolDatabase.protocols.items()
            if proto.layer == layer_name
        }


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

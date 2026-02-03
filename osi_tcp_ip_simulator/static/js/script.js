// OSI vs TCP/IP Model Simulator - JavaScript

// Tips data for educational content
const NETWORK_TIPS = [
    {
        title: "TCP vs UDP",
        content: "TCP ensures reliable delivery but is slower (like email), while UDP is faster but may lose packets (like video streaming)."
    },
    {
        title: "IP Addresses",
        content: "IPv4 uses 32 bits (like 192.168.1.1), while IPv6 uses 128 bits created for the growing number of devices."
    },
    {
        title: "MAC Addresses",
        content: "MAC addresses identify devices on a local network, while IP addresses identify them across the internet."
    },
    {
        title: "DNS Service",
        content: "DNS translates domain names (google.com) into IP addresses. Without it, you'd need to remember every website's IP!"
    },
    {
        title: "Encapsulation",
        content: "As data moves down layers, each adds its header. Like putting letters in envelopes within boxes within boxes!"
    },
    {
        title: "Decapsulation",
        content: "Headers are removed at each layer going up. The reverse process of unwrapping nested packages."
    },
    {
        title: "Ports",
        content: "Ports (0-65535) allow multiple applications to run simultaneously. Port 80=Web, 25=Email, 22=SSH, 443=HTTPS."
    },
    {
        title: "Firewalls",
        content: "Firewalls control which packets can enter or leave based on source/destination IP and port numbers."
    },
    {
        title: "Routers",
        content: "Routers find the best path for packets across networks using routing tables at Layer 3."
    },
    {
        title: "Latency",
        content: "Time for data to travel from source to destination. Lower latency = faster response, critical for gaming!"
    },
    {
        title: "Bandwidth",
        content: "Maximum data transmitted in given time. Higher bandwidth = faster speeds and more simultaneous connections."
    },
    {
        title: "OSI vs TCP/IP",
        content: "OSI is theoretical (7 layers) while TCP/IP is practical (4 layers). TCP/IP powers the modern internet!"
    },
    {
        title: "HTTP Protocol",
        content: "HyperText Transfer Protocol - stateless protocol for web. HTTP (port 80) is unencrypted, HTTPS (port 443) is secure."
    },
    {
        title: "SMTP Protocol",
        content: "Simple Mail Transfer Protocol sends emails. Usually runs on port 25, 587, or 465 with encryption."
    },
    {
        title: "POP3 & IMAP",
        content: "Both retrieve emails but differ: POP3 downloads emails (removes from server), IMAP keeps them synchronized online."
    },
    {
        title: "ARP Protocol",
        content: "Address Resolution Protocol maps IP addresses to MAC addresses. Essential for local network communication!"
    },
    {
        title: "ICMP Protocol",
        content: "Internet Control Message Protocol used for diagnostics. Ping and Traceroute commands use ICMP."
    },
    {
        title: "Packet Structure",
        content: "Each packet has headers from multiple layers. Encapsulation creates: Data → Segment → Packet → Frame → Bits."
    },
    {
        title: "TCP Handshake",
        content: "TCP uses 3-way handshake (SYN, SYN-ACK, ACK) to establish connection before data transmission."
    },
    {
        title: "Checksums",
        content: "Used to detect errors in transmission. Receiver calculates checksum; if it doesn't match, packet is discarded."
    },
    {
        title: "Subnet Mask",
        content: "Determines which part of IP address is network and which is host. Example: 255.255.255.0 for Class C network."
    },
    {
        title: "Default Gateway",
        content: "Router's IP address that devices use to reach other networks. Without it, traffic can't leave your local network!"
    },
    {
        title: "DHCP Service",
        content: "Dynamic Host Configuration Protocol automatically assigns IP addresses to devices on a network."
    },
    {
        title: "SSL/TLS Protocol",
        content: "Encryption protocols that secure data in transit. Used by HTTPS, SMTP over TLS, and many other services."
    },
    {
        title: "VPN Technology",
        content: "Virtual Private Network encrypts all traffic and routes through secure server. Hides your IP from websites!"
    },
    {
        title: "Proxy Server",
        content: "Intermediary between client and server. Useful for caching, filtering, and protecting internal network."
    },
    {
        title: "Load Balancing",
        content: "Distributes network traffic across multiple servers to prevent overload and ensure high availability."
    },
    {
        title: "NAT Protocol",
        content: "Network Address Translation allows multiple devices to share one public IP address. Used in home routers!"
    },
    {
        title: "MTU Size",
        content: "Maximum Transmission Unit (usually 1500 bytes) is largest packet that can be transmitted without fragmentation."
    },
    {
        title: "QoS Management",
        content: "Quality of Service prioritizes certain traffic types (video, voice) over others for better performance."
    },
    {
        title: "VLAN Technology",
        content: "Virtual LANs segment networks logically even if connected physically. Each VLAN is isolated from others."
    },
    {
        title: "Network Switches",
        content: "Layer 2 devices that connect network segments using MAC addresses. Faster than hubs with collision prevention."
    },
    {
        title: "Network Bridges",
        content: "Connect two network segments and forward frames based on MAC addresses. Similar to switches but with fewer ports."
    },
    {
        title: "Spanning Tree Protocol",
        content: "STP prevents loops in network by creating a tree topology. Automatically reroutes if link fails."
    },
    {
        title: "Subnetting",
        content: "Dividing a network into smaller subnetworks improves performance, security, and organization."
    },
    {
        title: "Port Forwarding",
        content: "Maps external port on router to internal IP/port. Allows external devices to reach services inside network."
    },
    {
        title: "UPnP Technology",
        content: "Universal Plug and Play allows devices to automatically configure port forwarding without manual setup."
    },
    {
        title: "IGMP Protocol",
        content: "Internet Group Management Protocol enables multicast communication. Devices join multicast groups."
    },
    {
        title: "Multicast Communication",
        content: "One sender to multiple recipients efficiently. Used for video streaming and online games."
    },
    {
        title: "Broadcast Communication",
        content: "Message sent to all devices on a network. Limited to single network segment due to broadcast domain."
    },
    {
        title: "Unicast Communication",
        content: "Traditional one-to-one communication between two devices. Most common type of network communication."
    },
    {
        title: "Network Redundancy",
        content: "Having backup paths and duplicate components ensures network continues working if primary fails."
    },
    {
        title: "Failover Mechanism",
        content: "Automatic switching to backup system when primary fails. Critical for high-availability networks."
    },
    {
        title: "CDN Services",
        content: "Content Delivery Networks distribute content across multiple servers globally for faster access."
    },
    {
        title: "DNS Caching",
        content: "DNS servers cache results to reduce lookup time. Your device also caches DNS for faster browsing."
    },
    {
        title: "Network Monitoring",
        content: "Tools track network traffic and performance. Important for troubleshooting and security detection."
    },
    {
        title: "Packet Sniffing",
        content: "Capture and analyze network packets for troubleshooting. Tools like Wireshark are essential for network admins."
    },
    {
        title: "RTP Protocol",
        content: "Real-time Transport Protocol carries audio/video over networks. Optimized for time-sensitive data."
    },
    {
        title: "RDP Protocol",
        content: "Remote Desktop Protocol allows remote access to other computers. Runs on port 3389 by default."
    },
    {
        title: "SSH Protocol",
        content: "Secure Shell provides encrypted remote access. More secure than older Telnet protocol (port 22)."
    },
    {
        title: "FTP Protocol",
        content: "File Transfer Protocol transfers files between computers. Port 21 for control, port 20 for data."
    },
    {
        title: "SFTP Protocol",
        content: "SSH File Transfer Protocol is secure alternative to FTP. Encrypts both commands and data."
    },
    {
        title: "FTPS Protocol",
        content: "FTP over SSL/TLS adds encryption to traditional FTP. More secure than plain FTP."
    },
    {
        title: "SIP Protocol",
        content: "Session Initiation Protocol establishes VoIP calls. Works with RTP for media transmission."
    },
    {
        title: "IP Fragmentation",
        content: "Large packets split into smaller fragments if they exceed MTU. Reassembled at destination."
    },
    {
        title: "TCP Congestion Control",
        content: "Mechanisms like slow start and congestion avoidance prevent network overload."
    },
    {
        title: "Network Topology - Star",
        content: "All devices connect through central switch. Single point of failure but easy to manage."
    },
    {
        title: "Network Topology - Ring",
        content: "Devices arranged in ring. Data travels in one direction but offers redundancy with dual rings."
    },
    {
        title: "Network Topology - Mesh",
        content: "Every device connects to multiple others. Very redundant but expensive and complex to implement."
    },
    {
        title: "Network Slicing",
        content: "Dividing network resources virtually to create isolated environments. Important for 5G networks."
    },
    {
        title: "SDN Networks",
        content: "Software-Defined Networking separates control plane from data plane for flexible management."
    },
    {
        title: "Network Virtualization",
        content: "Creating virtual networks on physical infrastructure. Allows multiple isolated networks on shared hardware."
    },
    {
        title: "Zero Trust Security",
        content: "Never trust, always verify. Every access request is authenticated regardless of network location."
    },
    {
        title: "Network Segmentation",
        content: "Dividing network into separate zones improves security by limiting lateral movement of attackers."
    },
    {
        title: "DDoS Attacks",
        content: "Distributed Denial of Service floods target with traffic from multiple sources. Difficult to defend."
    },
    {
        title: "Man-in-the-Middle Attack",
        content: "Attacker intercepts communication between two parties. HTTPS prevents this with encryption."
    },
    {
        title: "Network Authentication",
        content: "Verifying user/device identity before allowing access. Methods include passwords, certificates, biometrics."
    },
    {
        title: "Access Control Lists",
        content: "ACLs define which traffic is allowed or denied. Fundamental security feature on routers/firewalls."
    },
    {
        title: "IP Whitelisting",
        content: "Only allows connections from specific IP addresses. Effective but can block legitimate users."
    },
    {
        title: "Rate Limiting",
        content: "Restricting number of requests per time period prevents abuse and DDoS attacks."
    },
    {
        title: "Network Logging",
        content: "Recording network events for analysis. Essential for security audits and troubleshooting."
    },
    {
        title: "Syslog Protocol",
        content: "Standard protocol for sending log messages over network. Centralized logging for analysis."
    },
    {
        title: "Network Time Protocol",
        content: "NTP synchronizes time across network devices. Critical for logging and security."
    },
    {
        title: "SNMP Protocol",
        content: "Simple Network Management Protocol monitors network devices. Port 161 for queries, 162 for traps."
    },
    {
        title: "Network Performance",
        content: "Measured by bandwidth, latency, jitter, and packet loss. All affect user experience."
    },
    {
        title: "Jitter",
        content: "Variation in latency causes packets to arrive at inconsistent times. Bad for voice/video calls."
    },
    {
        title: "Packet Loss",
        content: "Packets failing to reach destination. Even 1% loss can significantly degrade performance."
    },
    {
        title: "Network Troubleshooting",
        content: "Use ping, traceroute, netstat, and packet sniffing to diagnose network issues systematically."
    },
    {
        title: "Echo Request/Reply",
        content: "Ping uses ICMP Echo Request/Reply to test connectivity. Simple but powerful diagnostic tool."
    },
    {
        title: "Traceroute Command",
        content: "Shows all hops between source and destination. Helps identify where connection fails."
    },
    {
        title: "Network Interfaces",
        content: "Physical or virtual connections to network. Each has MAC address and can have multiple IP addresses."
    },
    {
        title: "Loopback Interface",
        content: "Virtual interface (127.0.0.1) used for testing. Traffic doesn't leave the device."
    },
    {
        title: "Network Bonding",
        content: "Combining multiple network interfaces into one logical interface for redundancy and performance."
    },
    {
        title: "Link Aggregation",
        content: "Grouping multiple network links together to increase bandwidth. Uses LACP protocol."
    },
    {
        title: "DHCP Lease",
        content: "Time period for which DHCP assigns IP address to device. After expiration, must renew."
    },
    {
        title: "APIPA Address",
        content: "Automatic Private IP Addressing assigns IP from 169.254.x.x when DHCP unavailable."
    },
    {
        title: "Network Simulation",
        content: "Testing network behavior under different conditions. Tools like GNS3 simulate network environments."
    }
];

class NetworkSimulator {
    constructor() {
        this.osiLayers = [];
        this.tcpipLayers = [];
        this.encapsulationSequence = [];
        this.decapsulationSequence = [];
        this.isAnimating = false;
        this.selectedOSILayer = null;
        this.selectedTCPIPLayer = null;
        this.currentTipIndex = 0;
        this.tipRotationInterval = null;

        this.init();
    }

    async init() {
        await this.loadData();
        this.setupEventListeners();
        this.renderOSILayers();
        this.renderTCPIPLayers();
        this.renderFlowVisualization();
        this.renderLayerMapping();
        this.initializeTips();
    }

    // Load data from backend API
    async loadData() {
        try {
            const [osiRes, tcpipRes, encapRes, decapRes] = await Promise.all([
                fetch('/api/osi-layers'),
                fetch('/api/tcpip-layers'),
                fetch('/api/encapsulation'),
                fetch('/api/decapsulation')
            ]);

            const osiData = await osiRes.json();
            const tcpipData = await tcpipRes.json();
            const encapData = await encapRes.json();
            const decapData = await decapRes.json();

            this.osiLayers = osiData.layers;
            this.tcpipLayers = tcpipData.layers;
            this.encapsulationSequence = encapData.sequence;
            this.decapsulationSequence = decapData.sequence;
        } catch (error) {
            console.error('Error loading data:', error);
        }
    }

    // Setup event listeners
    setupEventListeners() {
        // Control buttons
        document.getElementById('resetBtn').addEventListener('click', () => this.resetSimulator());
        document.getElementById('helpBtn').addEventListener('click', () => this.showHelp());

        // Message animation buttons
        document.getElementById('sendMessageBtn').addEventListener('click', () => this.sendMessage());
        document.getElementById('messageInput').addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                this.sendMessage();
            }
        });

        // Tab buttons
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.addEventListener('click', (e) => this.switchTab(e.target));
        });

        // Tips buttons
        document.getElementById('tipsPrevBtn').addEventListener('click', () => {
            this.clearTipRotation();
            this.previousTip();
            this.startTipRotation();
        });
        document.getElementById('tipsNextBtn').addEventListener('click', () => {
            this.clearTipRotation();
            this.nextTip();
            this.startTipRotation();
        });

        // Close modal
        document.querySelector('.close').addEventListener('click', () => this.closeModal());
        window.addEventListener('click', (e) => {
            const modal = document.getElementById('helpModal');
            if (e.target === modal) {
                this.closeModal();
            }
        });
    }

    // Render OSI layers
    renderOSILayers() {
        const container = document.getElementById('osiContainer');
        container.innerHTML = '';

        // Reverse order to display Layer 7 at top
        const reversedLayers = [...this.osiLayers].reverse();

        reversedLayers.forEach((layer, index) => {
            const layerEl = document.createElement('div');
            layerEl.className = 'layer';
            layerEl.style.backgroundColor = layer.color;
            layerEl.innerHTML = `
                <span class="layer-number">L${layer.number}</span>
                <span class="layer-name">${layer.name}</span>
                <span class="layer-unit">${layer.data_unit}</span>
            `;

            layerEl.addEventListener('click', () => this.selectOSILayer(layer));
            layerEl.addEventListener('mouseenter', () => this.highlightOSILayer(layer.number));
            layerEl.addEventListener('mouseleave', () => this.clearHighlight());

            container.appendChild(layerEl);
        });
    }

    // Render TCP/IP layers
    renderTCPIPLayers() {
        const container = document.getElementById('tcpipContainer');
        container.innerHTML = '';

        // Reverse order to display Layer 4 at top
        const reversedLayers = [...this.tcpipLayers].reverse();

        reversedLayers.forEach((layer) => {
            const layerEl = document.createElement('div');
            layerEl.className = 'layer';
            layerEl.style.backgroundColor = layer.color;
            layerEl.innerHTML = `
                <span class="layer-number">L${layer.number}</span>
                <span class="layer-name">${layer.name}</span>
                <span class="layer-unit">OSI: ${layer.osi_layers.join(',')}</span>
            `;

            layerEl.addEventListener('click', () => this.selectTCPIPLayer(layer));
            layerEl.addEventListener('mouseenter', () => this.highlightTCPIPLayers(layer.osi_layers));
            layerEl.addEventListener('mouseleave', () => this.clearHighlight());

            container.appendChild(layerEl);
        });
    }

    // Render encapsulation and decapsulation flows
    renderFlowVisualization() {
        // Encapsulation
        const encapContainer = document.getElementById('encapsulationFlow');
        encapContainer.innerHTML = '';

        const encapWrapper = document.createElement('div');
        encapWrapper.className = 'flow-wrapper';

        this.encapsulationSequence.forEach((step, index) => {
            const stepEl = document.createElement('div');
            stepEl.className = 'flow-step-item';
            stepEl.innerHTML = `
                <div class="flow-step">
                    <div class="flow-step-title">S${step.stage}</div>
                    <div class="flow-step-layer">${step.header}</div>
                    <div class="flow-step-content"><strong>${step.result}</strong></div>
                    ${step.description ? `<div class="flow-step-description">${step.description}</div>` : ''}
                </div>
                ${index < this.encapsulationSequence.length - 1 ? '<div class="flow-arrow-connector">→</div>' : ''}
            `;
            encapWrapper.appendChild(stepEl);
        });

        encapContainer.appendChild(encapWrapper);

        // Decapsulation
        const decapContainer = document.getElementById('decapsulationFlow');
        decapContainer.innerHTML = '';

        const decapWrapper = document.createElement('div');
        decapWrapper.className = 'flow-wrapper';

        this.decapsulationSequence.forEach((step, index) => {
            const stepEl = document.createElement('div');
            stepEl.className = 'flow-step-item';
            stepEl.innerHTML = `
                <div class="flow-step">
                    <div class="flow-step-title">S${step.stage}</div>
                    <div class="flow-step-layer">${step.header}</div>
                    <div class="flow-step-content"><strong>${step.result}</strong></div>
                    ${step.description ? `<div class="flow-step-description">${step.description}</div>` : ''}
                </div>
                ${index < this.decapsulationSequence.length - 1 ? '<div class="flow-arrow-connector">→</div>' : ''}
            `;
            decapWrapper.appendChild(stepEl);
        });

        decapContainer.appendChild(decapWrapper);
    }

    // Render layer mapping table
    async renderLayerMapping() {
        try {
            const response = await fetch('/api/layer-mapping');
            const data = await response.json();
            const tbody = document.getElementById('mappingBody');
            tbody.innerHTML = '';

            // Data units and details for each TCP/IP layer
            const layerDetails = {
                4: {
                    dataUnit: 'Message/Segment',
                    protocols: 'HTTP, HTTPS, FTP, SMTP, SSH, Telnet, DNS, DHCP',
                    examples: 'Web Browsers, Email Clients, FTP Software',
                    characteristics: 'User interaction, Application logic, End-user services'
                },
                3: {
                    dataUnit: 'Segment/Datagram',
                    protocols: 'TCP, UDP, SCTP',
                    examples: 'TCP/UDP Headers, Port Numbers, Flow Control',
                    characteristics: 'Reliability, Flow Control, Multiplexing, Error Detection'
                },
                2: {
                    dataUnit: 'Packet/Datagram',
                    protocols: 'IP (IPv4, IPv6), ICMP, IGMP',
                    examples: 'Routers, IP Addresses, Gateways, Network Interfaces',
                    characteristics: 'Logical Addressing, Routing, Network Forwarding'
                },
                1: {
                    dataUnit: 'Frame',
                    protocols: 'Ethernet, Wi-Fi (802.11), PPP, Cellular Protocols',
                    examples: 'Network Adapters, Switches, MAC Addresses, Hubs',
                    characteristics: 'Physical Transmission, Hardware Addressing, Media Access'
                }
            };

            // Get TCP/IP layers in order
            const tcpipLayers = [4, 3, 2, 1];

            tcpipLayers.forEach(layerNum => {
                const tcpipLayer = this.tcpipLayers.find(l => l.number === layerNum);
                if (tcpipLayer) {
                    const row = document.createElement('tr');
                    const osiLayerNames = tcpipLayer.osi_layers
                        .map(num => this.osiLayers.find(l => l.number === num)?.name || `Layer ${num}`)
                        .join(', ');
                    const details = layerDetails[layerNum] || {};
                    
                    row.innerHTML = `
                        <td><strong>${tcpipLayer.name}</strong></td>
                        <td>${osiLayerNames}</td>
                        <td><span class="pdu-badge">${details.dataUnit || 'N/A'}</span></td>
                        <td>${details.protocols || 'N/A'}</td>
                        <td>${tcpipLayer.functions.join(', ')}</td>
                        <td>${details.examples || 'N/A'}</td>
                        <td>${details.characteristics || 'N/A'}</td>
                    `;
                    tbody.appendChild(row);
                }
            });
        } catch (error) {
            console.error('Error rendering mapping:', error);
        }
    }

    // Select OSI layer
    selectOSILayer(layer) {
        this.selectedOSILayer = layer.number;
        this.updateInfoPanel(layer.name, this.formatLayerInfo(layer));
        this.highlightOSILayer(layer.number);
    }

    // Select TCP/IP layer
    selectTCPIPLayer(layer) {
        this.selectedTCPIPLayer = layer.number;
        const osiLayerNames = layer.osi_layers
            .map(num => this.osiLayers.find(l => l.number === num)?.name)
            .filter(name => name)
            .join(', ');
        
        let info = `
            <div class="layer-section">
                <h4>🔗 Equivalent OSI Layers</h4>
                <p>${osiLayerNames}</p>
            </div>
        `;
        info += this.formatLayerInfo(layer);
        
        this.updateInfoPanel(layer.name, info);
        this.highlightTCPIPLayers(layer.osi_layers);
    }

    // Highlight OSI layer
    highlightOSILayer(layerNum) {
        const layers = document.querySelectorAll('#osiContainer .layer');
        layers.forEach(layer => {
            const text = layer.textContent;
            if (text.includes(`L${layerNum}`)) {
                layer.classList.add('active');
            } else {
                layer.classList.remove('active');
            }
        });
    }

    // Highlight TCP/IP layers
    highlightTCPIPLayers(osiLayerNums) {
        const osiLayers = document.querySelectorAll('#osiContainer .layer');
        osiLayers.forEach(layer => {
            const text = layer.textContent;
            const isActive = osiLayerNums.some(num => text.includes(`L${num}`));
            if (isActive) {
                layer.classList.add('active');
            } else {
                layer.classList.remove('active');
            }
        });
    }

    // Clear highlights
    clearHighlight() {
        if (this.selectedOSILayer === null && this.selectedTCPIPLayer === null) {
            document.querySelectorAll('.layer.active').forEach(layer => {
                layer.classList.remove('active');
            });
        }
    }

    // Format layer information
    formatLayerInfo(layer) {
        let html = '';
        
        // Add description
        if (layer.description) {
            html += `<div class="layer-description"><p><strong>📝 What This Layer Does:</strong></p><p>${layer.description}</p></div>`;
        }
        
        // Add functions
        html += '<div class="layer-section"><h4>🎯 Functions</h4><ul>';
        layer.functions.forEach(func => {
            html += `<li>${func}</li>`;
        });
        html += '</ul></div>';
        
        // Add examples
        if (layer.examples && layer.examples.length > 0) {
            html += '<div class="layer-section"><h4>💡 Real-World Examples</h4><ul>';
            layer.examples.forEach(example => {
                html += `<li>${example}</li>`;
            });
            html += '</ul></div>';
        }
        
        // Add protocols
        html += '<div class="layer-section"><h4>🔧 Protocols & Standards</h4><ul>';
        layer.protocols.forEach(proto => {
            html += `<li><strong>${proto}</strong></li>`;
        });
        html += '</ul></div>';
        
        return html;
    }

    // Update info panel
    updateInfoPanel(title, content) {
        document.getElementById('infoTitle').textContent = title;
        document.getElementById('infoContent').innerHTML = content;
    }

    // Start transmission animation
    async startTransmission() {
        if (this.isAnimating) return;

        this.isAnimating = true;

        // Animate encapsulation (sender side - top to bottom)
        await this.animateEncapsulation();

        // Animate decapsulation (receiver side - bottom to top)
        await this.animateDecapsulation();

        this.isAnimating = false;
        this.updateInfoPanel('Transmission Complete!', '<p>Data has been successfully transmitted and received through all layers.</p>');
    }

    // Animate encapsulation
    async animateEncapsulation() {
        const layers = [7, 6, 5, 4, 3, 2, 1];

        for (const layerNum of layers) {
            const layer = this.osiLayers.find(l => l.number === layerNum);
            if (layer) {
                this.highlightOSILayer(layerNum);
                this.updateInfoPanel(`Layer ${layerNum}: ${layer.name}`, 
                    `<p><strong>Encapsulation Process (Sender Side)</strong></p>` + this.formatLayerInfo(layer));
                
                // Highlight corresponding flow step
                this.highlightFlowStep(8 - layerNum, 'encapsulationFlow');
            }
            await this.sleep(800);
        }
    }

    // Animate decapsulation
    async animateDecapsulation() {
        const layers = [1, 2, 3, 4, 5, 6, 7];

        for (const layerNum of layers) {
            const layer = this.osiLayers.find(l => l.number === layerNum);
            if (layer) {
                this.highlightOSILayer(layerNum);
                this.updateInfoPanel(`Layer ${layerNum}: ${layer.name} (Receiver Side)`, 
                    `<p><strong>Decapsulation Process (Receiver Side)</strong></p>` + this.formatLayerInfo(layer));
                
                // Highlight corresponding flow step
                this.highlightFlowStep(layerNum, 'decapsulationFlow');
            }
            await this.sleep(800);
        }
    }

    // Highlight flow step
    highlightFlowStep(stepIndex, containerId) {
        const container = document.getElementById(containerId);
        const steps = container.querySelectorAll('.flow-step');
        steps.forEach((step, index) => {
            if (index === stepIndex - 1) {
                step.classList.add('active');
            } else {
                step.classList.remove('active');
            }
        });
    }

    // Sleep utility
    sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }

    // Switch tabs
    switchTab(button) {
        // Remove active class from all buttons
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.classList.remove('active');
        });

        // Hide all tab panes
        document.querySelectorAll('.tab-pane').forEach(pane => {
            pane.classList.remove('active');
        });

        // Add active class to clicked button
        button.classList.add('active');

        // Show corresponding tab pane
        const tabName = button.getAttribute('data-tab');
        document.getElementById(tabName).classList.add('active');
    }

    // Reset simulator
    resetSimulator() {
        this.selectedOSILayer = null;
        this.selectedTCPIPLayer = null;
        
        document.querySelectorAll('.layer.active').forEach(layer => {
            layer.classList.remove('active');
        });

        document.querySelectorAll('.flow-step.active').forEach(step => {
            step.classList.remove('active');
        });

        const welcomeContent = `
            <div class="layer-section">
                <h4>👋 Welcome to the OSI vs TCP/IP Model Simulator</h4>
                <p style="margin: 0;">This interactive tool helps you understand how network communication works by visualizing the OSI and TCP/IP models.</p>
            </div>
            <div class="layer-section">
                <h4>🎯 How to Use:</h4>
                <ul style="margin: 0;">
                    <li><strong>Click on any layer</strong> on the left or right to see detailed information about what that layer does</li>
                    <li><strong>Send a Message:</strong> Enter text and click "Send Message" to see how it flows through all layers</li>
                    <li><strong>View Encapsulation/Decapsulation:</strong> See how data is wrapped with headers going down and unwrapped going up</li>
                    <li><strong>Compare Models:</strong> See how the 7 OSI layers map to the 4 practical TCP/IP layers</li>
                </ul>
            </div>
            <div class="layer-section">
                <h4>📚 Quick Overview:</h4>
                <p><strong>OSI Model (7 Layers):</strong> A theoretical reference model for network communication</p>
                <p><strong>TCP/IP Model (4 Layers):</strong> The practical model used on the modern internet</p>
            </div>
        `;
        
        this.updateInfoPanel('Welcome to the Network Simulator', welcomeContent);
    }

    // Show help modal
    showHelp() {
        document.getElementById('helpModal').style.display = 'block';
    }

    // Close help modal
    closeModal() {
        document.getElementById('helpModal').style.display = 'none';
    }

    // Send Message Animation
    async sendMessage() {
        const messageInput = document.getElementById('messageInput');
        const message = messageInput.value.trim();

        if (!message) {
            alert('Please enter a message to send');
            return;
        }

        if (this.isAnimating) {
            alert('Wait for current animation to complete');
            return;
        }

        this.isAnimating = true;
        document.getElementById('sendMessageBtn').disabled = true;

        // Update sender message
        document.getElementById('senderMessage').textContent = message;

        // Start transmission animation
        await this.animateMessageTransmission(message);

        this.isAnimating = false;
        document.getElementById('sendMessageBtn').disabled = false;
    }

    // Animate message transmission through layers
    async animateMessageTransmission(message) {
        const messageBubble = document.getElementById('messageBubble');
        const statusText = document.getElementById('statusText');
        const progressBar = document.getElementById('progressBar');

        // Reset receiver
        document.getElementById('receiverMessage').textContent = 'Waiting...';
        progressBar.style.width = '0%';

        // Phase 1: Encapsulation (Layers 7 to 1)
        statusText.textContent = '📤 Transmission started - Encapsulating message...';
        await this.sleep(500);

        for (let layer = 7; layer >= 1; layer--) {
            const osiLayer = this.osiLayers.find(l => l.number === layer);
            if (osiLayer) {
                // Update layer info
                this.updateLayerAnimation(osiLayer, message, layer, 'down');
                this.highlightOSILayer(layer);
                
                // Update progress
                const progress = ((8 - layer) / 8) * 50;
                progressBar.style.width = progress + '%';
                statusText.textContent = `⬇️ Processing at Layer ${layer}: ${osiLayer.name}`;
            }

            await this.sleep(5000);
        }

        // Phase 2: Message travels across network
        statusText.textContent = '🌐 Message traveling across network...';
        progressBar.style.width = '50%';
        messageBubble.classList.remove('receiving');
        messageBubble.classList.add('sending');
        await this.sleep(2000);

        // Phase 3: Decapsulation (Layers 1 to 7)
        statusText.textContent = '📥 Message received - Decapsulating...';
        messageBubble.classList.remove('sending');
        messageBubble.classList.add('receiving');
        
        for (let layer = 1; layer <= 7; layer++) {
            const osiLayer = this.osiLayers.find(l => l.number === layer);
            if (osiLayer) {
                // Update layer info
                this.updateLayerAnimation(osiLayer, message, layer, 'up');
                this.highlightOSILayer(layer);

                // Update progress
                const progress = 50 + ((layer / 7) * 50);
                progressBar.style.width = progress + '%';
                statusText.textContent = `⬆️ Processing at Layer ${layer}: ${osiLayer.name}`;
            }

            await this.sleep(5000);
        }

        // Phase 4: Message received
        progressBar.style.width = '100%';
        document.getElementById('receiverMessage').textContent = message;
        statusText.textContent = `✅ Message successfully received at receiver! "${message}"`;
        messageBubble.classList.remove('receiving');

        // Show completion message
        this.updateInfoPanel(
            '🎉 Transmission Complete!',
            `<p><strong>Message:</strong> "${message}"</p>
             <p><strong>Path:</strong> Sender → Layer 7 → Layer 6 → Layer 5 → Layer 4 → Layer 3 → Layer 2 → Layer 1 → Network → Layer 1 → Layer 2 → Layer 3 → Layer 4 → Layer 5 → Layer 6 → Layer 7 → Receiver</p>
             <p><strong>Status:</strong> Message successfully transmitted and received!</p>`
        );

        // Re-enable button after delay
        await this.sleep(1000);
    }

    // Update layer animation display
    updateLayerAnimation(layer, message, layerNum, direction) {
        const currentLayerName = document.getElementById('currentLayerName');
        const currentLayerNumber = document.getElementById('currentLayerNumber');
        const currentLayerAction = document.getElementById('currentLayerAction');
        const currentLayerData = document.getElementById('currentLayerData');

        currentLayerName.textContent = `Layer ${layer.number}: ${layer.name}`;
        currentLayerNumber.textContent = `${direction === 'down' ? '⬇️ DOWN' : '⬆️ UP'}`;

        // Build comprehensive layer information for students
        let infoHTML = '';
        
        // Add description
        if (layer.description) {
            infoHTML += `<div class="animation-description"><strong>📝 What's Happening:</strong><p>${layer.description}</p></div>`;
        }
        
        // Add specific action
        let action = '';
        let data = '';

        if (direction === 'down') {
            switch (layer.number) {
                case 7:
                    action = 'Application Layer - Preparing message for transmission';
                    data = `Original Message: "${message}"`;
                    break;
                case 6:
                    action = 'Presentation Layer - Encrypting and formatting data';
                    data = `Encrypted: ${this.encryptMessage(message)}`;
                    break;
                case 5:
                    action = 'Session Layer - Establishing session connection';
                    data = `Session ID: ${Math.random().toString(36).substr(2, 9)}`;
                    break;
                case 4:
                    action = 'Transport Layer - Adding TCP/UDP header (Port info)';
                    data = `Segment: [Header: Port 80] + Data + [Checksum]`;
                    break;
                case 3:
                    action = 'Network Layer - Adding IP header (Source & Destination IP)';
                    data = `Packet: [IP Header] + Segment + [Trailer]`;
                    break;
                case 2:
                    action = 'Data Link Layer - Adding MAC header (Physical addresses)';
                    data = `Frame: [MAC Header] + Packet + [MAC Trailer]`;
                    break;
                case 1:
                    action = 'Physical Layer - Converting to bits for transmission';
                    data = `Bits: 11010110101011010...`;
                    break;
            }
        } else {
            switch (layer.number) {
                case 1:
                    action = 'Physical Layer - Receiving bits and converting back to frames';
                    data = `Bits: 11010110101011010... → Frame`;
                    break;
                case 2:
                    action = 'Data Link Layer - Removing MAC header';
                    data = `Frame → [Removed MAC Header] → Packet`;
                    break;
                case 3:
                    action = 'Network Layer - Removing IP header and routing';
                    data = `Packet → [Removed IP Header] → Segment`;
                    break;
                case 4:
                    action = 'Transport Layer - Removing TCP/UDP header';
                    data = `Segment → [Removed Port Info] → Data`;
                    break;
                case 5:
                    action = 'Session Layer - Closing session connection';
                    data = `Session properly terminated`;
                    break;
                case 6:
                    action = 'Presentation Layer - Decrypting and decompressing data';
                    data = `Decrypted: "${message}"`;
                    break;
                case 7:
                    action = 'Application Layer - Delivering message to user';
                    data = `Received Message: "${message}"`;
                    break;
            }
        }

        infoHTML += `<div class="animation-action"><strong>⚙️ Action:</strong><p>${action}</p></div>`;
        infoHTML += `<div class="animation-data"><strong>📦 Data State:</strong><p style="font-family: monospace; background: #f0f0f0; padding: 8px; border-radius: 4px; margin: 0;">${data}</p></div>`;
        
        // Add key examples/functions for this layer
        if (layer.examples && layer.examples.length > 0) {
            infoHTML += `<div class="animation-examples"><strong>💡 Key Concepts:</strong><ul>`;
            layer.examples.slice(0, 2).forEach(example => {
                infoHTML += `<li>${example}</li>`;
            });
            infoHTML += `</ul></div>`;
        }

        currentLayerAction.innerHTML = infoHTML;
        currentLayerData.textContent = '';
    }

    // Helper function: Encrypt message (simple Caesar cipher for demo)
    encryptMessage(message) {
        return message.split('').map(char => {
            if (char.match(/[a-z]/i)) {
                const code = char.charCodeAt(0);
                return String.fromCharCode(code + 3);
            }
            return char;
        }).join('');
    }

    // Helper function: Convert text to binary (first few chars)
    textToBinary(text) {
        return text.split('').map(char => 
            char.charCodeAt(0).toString(2).padStart(8, '0')
        ).join(' ');
    }

    // Initialize tips
    initializeTips() {
        this.displayRandomTip();
        this.startTipRotation();
    }

    // Display random tip
    displayRandomTip() {
        const randomIndex = Math.floor(Math.random() * NETWORK_TIPS.length);
        this.displayTip(randomIndex);
    }

    // Display specific tip
    displayTip(index) {
        const tip = NETWORK_TIPS[index];
        const tipsContent = document.getElementById('tipsContent');
        
        tipsContent.innerHTML = `
            <div class="tips-text">
                <h4>${tip.title}</h4>
                <p>${tip.content}</p>
            </div>
        `;
        
        // Update progress bar with random progress
        const progress = Math.random() * 100;
        document.getElementById('tipsProgressBar').style.width = progress + '%';
        
        this.currentTipIndex = index;
    }

    // Next tip (random)
    nextTip() {
        this.displayRandomTip();
    }

    // Previous tip (random)
    previousTip() {
        this.displayRandomTip();
    }

    // Start tip rotation (every 10 seconds - shuffled)
    startTipRotation() {
        this.tipRotationInterval = setInterval(() => {
            this.displayRandomTip();
        }, 10000);
    }

    // Clear tip rotation
    clearTipRotation() {
        if (this.tipRotationInterval) {
            clearInterval(this.tipRotationInterval);
            this.tipRotationInterval = null;
        }
    }
}

// Initialize simulator when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('🌐 DOM Loaded - Initializing...');
    new NetworkSimulator();
    new MultiUserManager();
    console.log('✅ All systems initialized');
});

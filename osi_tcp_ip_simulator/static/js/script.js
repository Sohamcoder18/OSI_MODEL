// OSI vs TCP/IP Model Simulator - JavaScript

class NetworkSimulator {
    constructor() {
        this.osiLayers = [];
        this.tcpipLayers = [];
        this.encapsulationSequence = [];
        this.decapsulationSequence = [];
        this.isAnimating = false;
        this.selectedOSILayer = null;
        this.selectedTCPIPLayer = null;

        this.init();
    }

    async init() {
        await this.loadData();
        this.setupEventListeners();
        this.renderOSILayers();
        this.renderTCPIPLayers();
        this.renderFlowVisualization();
        this.renderLayerMapping();
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
        document.getElementById('startBtn').addEventListener('click', () => this.startTransmission());
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

        this.encapsulationSequence.forEach((step, index) => {
            const stepEl = document.createElement('div');
            stepEl.className = 'flow-step';
            stepEl.innerHTML = `
                <div class="flow-step-title">Stage ${step.stage}</div>
                <div class="flow-step-layer">${step.header}</div>
                <div class="flow-step-content"><strong>${step.result}</strong></div>
                ${step.description ? `<div class="flow-step-description">${step.description}</div>` : ''}
            `;
            encapContainer.appendChild(stepEl);

            if (index < this.encapsulationSequence.length - 1) {
                const arrow = document.createElement('div');
                arrow.className = 'flow-arrow';
                arrow.innerHTML = '↓';
                encapContainer.appendChild(arrow);
            }
        });

        // Decapsulation
        const decapContainer = document.getElementById('decapsulationFlow');
        decapContainer.innerHTML = '';

        this.decapsulationSequence.forEach((step, index) => {
            const stepEl = document.createElement('div');
            stepEl.className = 'flow-step';
            stepEl.innerHTML = `
                <div class="flow-step-title">Stage ${step.stage}</div>
                <div class="flow-step-layer">${step.header}</div>
                <div class="flow-step-content"><strong>${step.result}</strong></div>
                ${step.description ? `<div class="flow-step-description">${step.description}</div>` : ''}
            `;
            decapContainer.appendChild(stepEl);

            if (index < this.decapsulationSequence.length - 1) {
                const arrow = document.createElement('div');
                arrow.className = 'flow-arrow';
                arrow.innerHTML = '↑';
                decapContainer.appendChild(arrow);
            }
        });
    }

    // Render layer mapping table
    async renderLayerMapping() {
        try {
            const response = await fetch('/api/layer-mapping');
            const data = await response.json();
            const tbody = document.getElementById('mappingBody');
            tbody.innerHTML = '';

            // Get TCP/IP layers in order
            const tcpipLayers = [4, 3, 2, 1];

            tcpipLayers.forEach(layerNum => {
                const tcpipLayer = this.tcpipLayers.find(l => l.number === layerNum);
                if (tcpipLayer) {
                    const row = document.createElement('tr');
                    const osiLayerNames = tcpipLayer.osi_layers
                        .map(num => this.osiLayers.find(l => l.number === num)?.name || `Layer ${num}`)
                        .join(', ');
                    
                    row.innerHTML = `
                        <td><strong>${tcpipLayer.name}</strong></td>
                        <td>${osiLayerNames}</td>
                        <td>${tcpipLayer.functions.join(', ')}</td>
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
        document.getElementById('startBtn').disabled = true;

        // Animate encapsulation (sender side - top to bottom)
        await this.animateEncapsulation();

        // Animate decapsulation (receiver side - bottom to top)
        await this.animateDecapsulation();

        this.isAnimating = false;
        document.getElementById('startBtn').disabled = false;
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

        // Determine action and data based on layer and direction
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
                    data = `Bits: ${this.textToBinary(message.slice(0, 3))}...`;
                    break;
            }
        } else {
            switch (layer.number) {
                case 1:
                    action = 'Physical Layer - Receiving bit stream';
                    data = `Bits Received: ${this.textToBinary(message.slice(0, 3))}...`;
                    break;
                case 2:
                    action = 'Data Link Layer - Removing MAC header';
                    data = `Frame Removed, Packet extracted`;
                    break;
                case 3:
                    action = 'Network Layer - Removing IP header';
                    data = `IP Header removed, Segment extracted`;
                    break;
                case 4:
                    action = 'Transport Layer - Removing TCP/UDP header';
                    data = `Transport Header removed, Data extracted`;
                    break;
                case 5:
                    action = 'Session Layer - Closing session connection';
                    data = `Session ID verified and closed`;
                    break;
                case 6:
                    action = 'Presentation Layer - Decrypting data';
                    data = `Decrypted: "${message}"`;
                    break;
                case 7:
                    action = 'Application Layer - Delivering message to user';
                    data = `Final Message: "${message}"`;
                    break;
            }
        }

        currentLayerAction.textContent = action;
        currentLayerData.textContent = data;
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
}

// Initialize simulator when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    console.log('🌐 DOM Loaded - Initializing...');
    new NetworkSimulator();
    new MultiUserManager();
    console.log('✅ All systems initialized');
});

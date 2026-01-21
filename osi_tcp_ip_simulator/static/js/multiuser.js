/**
 * Multi-user Network Session Manager
 * Handles WebSocket communication, session creation/joining, and QR codes
 */

class MultiUserManager {
    constructor() {
        console.log('🚀 MultiUserManager initialized');
        this.socket = null;
        this.sessionId = null;
        this.userId = this.generateUserId();
        this.userName = `User-${this.userId.substring(0, 4)}`;
        this.isConnected = false;
        this.isSessionActive = false;
        this.initializeEventListeners();
        this.checkUrlForSession();
    }

    generateUserId() {
        return 'user_' + Math.random().toString(36).substr(2, 9);
    }

    initializeEventListeners() {
        const sessionToggleBtn = document.getElementById('sessionToggleBtn');
        const sessionModal = document.getElementById('sessionModal');
        const closeBtn = document.querySelector('.close');
        const createSessionBtn = document.getElementById('createSessionBtn');
        const joinSessionBtn = document.getElementById('joinSessionBtn');
        const copySessionBtn = document.getElementById('copySessionBtn');
        const continueBtn = document.getElementById('continueBtn');

        console.log('🔧 Setting up event listeners...');
        console.log('  - sessionModal:', sessionModal ? '✓' : '✗');
        console.log('  - closeBtn:', closeBtn ? '✓' : '✗');
        console.log('  - createSessionBtn:', createSessionBtn ? '✓' : '✗');

        // Show modal on page load
        if (sessionModal) {
            sessionModal.classList.add('show');
            console.log('📱 Modal shown on page load');
        }

        sessionToggleBtn.addEventListener('click', () => {
            sessionModal.classList.add('show');
            console.log('🔘 Session button clicked - modal shown');
        });

        closeBtn.addEventListener('click', () => {
            sessionModal.classList.remove('show');
            console.log('❌ Close button clicked - modal hidden');
        });

        window.addEventListener('click', (e) => {
            if (e.target === sessionModal) {
                sessionModal.classList.remove('show');
                console.log('👁️ Clicked outside modal - hidden');
            }
        });

        createSessionBtn.addEventListener('click', () => this.createSession());
        joinSessionBtn.addEventListener('click', () => this.joinSession());
        copySessionBtn.addEventListener('click', () => this.copySessionId());
        continueBtn.addEventListener('click', () => {
            sessionModal.classList.remove('show');
            console.log('➡️ Continue button clicked - modal hidden');
        });
    }

    checkUrlForSession() {
        const params = new URLSearchParams(window.location.search);
        const sessionId = params.get('session');
        if (sessionId) {
            console.log(`📱 Session parameter detected in URL: ${sessionId}`);
            document.getElementById('joinSessionId').value = sessionId.toUpperCase();
            // Auto-join after a short delay to ensure page is ready
            setTimeout(() => this.joinSession(), 500);
        }
    }

    async createSession() {
        try {
            const response = await fetch('/api/create-session');
            const data = await response.json();
            this.sessionId = data.session_id;
            this.isSessionActive = true;

            // Display session ID and QR code
            document.getElementById('createdSessionId').style.display = 'block';
            document.getElementById('sessionIdDisplay').textContent = this.sessionId;
            document.getElementById('copySessionBtn').style.display = 'inline-block';

            // Generate QR code
            await this.generateQRCode();

            // Initialize WebSocket
            this.initializeWebSocket();

            // Show participants panel
            this.showParticipantsPanel();
        } catch (error) {
            console.error('Error creating session:', error);
            alert('Failed to create session. Please try again.');
        }
    }

    async generateQRCode() {
        try {
            const response = await fetch(`/api/qrcode/${this.sessionId}`);
            const data = await response.json();
            const qrcodeImg = document.getElementById('qrcodeImg');
            qrcodeImg.src = data.qrcode;
            qrcodeImg.style.display = 'block';
            
            // Display server IP and session URL
            const serverInfoDiv = document.getElementById('serverInfo');
            serverInfoDiv.style.display = 'block';
            
            const mobileUrlDiv = document.getElementById('mobileUrl');
            const serverIp = data.server_ip;
            const sessionUrl = `http://${serverIp}:5000/?session=${this.sessionId}`;
            mobileUrlDiv.innerHTML = `<strong>🌐 Link for Phone:</strong><br>${sessionUrl}`;
            
            // Add copy button for URL
            const copyUrlBtn = document.createElement('button');
            copyUrlBtn.textContent = 'Copy Link';
            copyUrlBtn.className = 'btn btn-secondary';
            copyUrlBtn.style.marginTop = '10px';
            copyUrlBtn.onclick = () => {
                navigator.clipboard.writeText(sessionUrl).then(() => {
                    alert('Link copied to clipboard!');
                });
            };
            mobileUrlDiv.appendChild(copyUrlBtn);
            
            // Log for debugging
            console.log('Server IP:', serverIp);
            console.log('Session URL:', sessionUrl);
        } catch (error) {
            console.error('Error generating QR code:', error);
            const serverInfoDiv = document.getElementById('serverInfo');
            serverInfoDiv.style.display = 'block';
            const mobileUrlDiv = document.getElementById('mobileUrl');
            mobileUrlDiv.innerHTML = '<strong style="color: red;">⚠️ Error generating QR code. Check browser console.</strong>';
        }
    }

    copySessionId() {
        const sessionId = this.sessionId;
        navigator.clipboard.writeText(sessionId).then(() => {
            alert(`Session ID copied: ${sessionId}`);
        }).catch(() => {
            alert(`Session ID: ${sessionId}`);
        });
    }

    joinSession() {
        const joinInput = document.getElementById('joinSessionId');
        this.sessionId = joinInput.value.trim().toUpperCase();

        if (!this.sessionId) {
            alert('Please enter a session ID');
            return;
        }

        // Show loading indicator
        joinInput.parentElement.style.display = 'none';
        document.getElementById('joinSessionBtn').style.display = 'none';
        const joinTips = document.getElementById('joinTips');
        if (joinTips) {
            joinTips.style.display = 'none';
        }
        
        // Show loading message
        const loadingMsg = document.createElement('p');
        loadingMsg.id = 'joiningLoadingMsg';
        loadingMsg.innerHTML = '<strong>⏳ Connecting to session...</strong>';
        loadingMsg.style.color = '#078282';
        loadingMsg.style.textAlign = 'center';
        loadingMsg.style.marginTop = '15px';
        document.querySelector('.option-box:last-of-type').appendChild(loadingMsg);

        // Verify session exists before trying to join
        this.verifySessionExists(this.sessionId).then(exists => {
            // Remove loading message
            const msg = document.getElementById('joiningLoadingMsg');
            if (msg) msg.remove();
            
            if (exists) {
                this.isSessionActive = true;
                
                // DO NOT hide modal immediately - show participants panel instead
                // User will click "Continue" button to close it
                
                // Hide session input areas
                document.getElementById('createSessionBtn').parentElement.style.display = 'none';

                this.initializeWebSocket();
                this.showParticipantsPanel();
            } else {
                alert(`Session "${this.sessionId}" not found. Please check the session ID and try again.`);
                console.error(`Session ${this.sessionId} not found on server`);
                
                // Show input again
                joinInput.parentElement.style.display = 'block';
                document.getElementById('joinSessionBtn').style.display = 'block';
                if (joinTips) {
                    joinTips.style.display = 'block';
                }
            }
        }).catch(error => {
            console.error('Error verifying session:', error);
            alert('Error verifying session. Please try again.');
            
            // Show input again
            const msg = document.getElementById('joiningLoadingMsg');
            if (msg) msg.remove();
            joinInput.parentElement.style.display = 'block';
            document.getElementById('joinSessionBtn').style.display = 'block';
            if (joinTips) {
                joinTips.style.display = 'block';
            }
        });
    }

    async verifySessionExists(sessionId) {
        try {
            const response = await fetch(`/api/verify-session/${sessionId}`);
            if (response.ok) {
                const data = await response.json();
                console.log(`✓ Session ${sessionId} verified. Participants: ${data.participants_count}`);
                return true;
            } else {
                const data = await response.json();
                console.error(`✗ Session ${sessionId} not found:`, data.error);
                return false;
            }
        } catch (error) {
            console.error('Error checking session:', error);
            return false;
        }
    }

    initializeWebSocket() {
        this.socket = io();

        this.socket.on('connect', () => {
            console.log('✓ WebSocket connected');
            this.isConnected = true;
            
            // Emit join request
            this.socket.emit('join_session', {
                session_id: this.sessionId,
                user_id: this.userId,
                user_name: this.userName
            });
            
            // Fetch current participants to ensure sync
            this.fetchParticipants();
        });

        this.socket.on('user_joined', (data) => {
            console.log('👥 User joined session:', data);
            console.log(`   Total participants: ${data.total_count}`);
            this.updateParticipants(data.participants);
        });

        this.socket.on('session_joined_confirmation', (data) => {
            console.log('✅ Session join confirmed:', data);
            this.updateParticipants(data.participants);
        });

        this.socket.on('message_sent', (data) => {
            console.log('Remote message received:', data);
            this.displayRemoteMessage(data);
        });

        this.socket.on('animation_update', (data) => {
            console.log('Animation update received:', data);
            this.displayRemoteAnimation(data);
        });

        this.socket.on('error', (data) => {
            console.error('✗ Socket error:', data.message);
            alert(`Error: ${data.message}`);
        });

        this.socket.on('disconnect', () => {
            console.warn('⚠️ WebSocket disconnected');
            this.isConnected = false;
        });
    }

    async fetchParticipants() {
        // Fetch current participants from server to ensure synchronization
        try {
            const response = await fetch(`/api/session/${this.sessionId}/participants`);
            if (response.ok) {
                const data = await response.json();
                console.log(`📋 Fetched ${data.count} participants from server`);
                this.updateParticipants(data.participants);
            }
        } catch (error) {
            console.error('Error fetching participants:', error);
        }
    }

    showParticipantsPanel() {
        document.getElementById('participantsPanel').style.display = 'block';
        document.getElementById('continueBtn').style.display = 'inline-block';
        
        // On mobile devices, auto-close modal after 3 seconds so user can interact with simulator
        const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
        if (isMobile) {
            console.log('📱 Mobile detected - auto-closing modal in 3 seconds or when continue is clicked...');
            const autoCloseTimer = setTimeout(() => {
                document.getElementById('sessionModal').classList.remove('show');
                console.log('✅ Modal auto-closed - simulator now fully visible');
            }, 3000);
            
            // Cancel auto-close if user manually clicks continue
            const continueBtn = document.getElementById('continueBtn');
            continueBtn.addEventListener('click', () => {
                clearTimeout(autoCloseTimer);
            }, { once: true });
        }
    }

    updateParticipants(participants) {
        const participantsList = document.getElementById('participantsList');
        participantsList.innerHTML = '';
        
        if (!participants || participants.length === 0) {
            participantsList.innerHTML = '<li style="color: #999;">No participants yet</li>';
            return;
        }
        
        participants.forEach(p => {
            const li = document.createElement('li');
            li.textContent = `👤 ${p.user_name}`;
            li.style.padding = '8px 0';
            participantsList.appendChild(li);
        });
        
        // Show participant count
        const countDisplay = document.getElementById('participantCount');
        if (countDisplay) {
            countDisplay.textContent = `(${participants.length} connected)`;
        }
    }

    sendMessage(message) {
        if (!this.isSessionActive || !this.socket) {
            return;
        }

        this.socket.emit('send_message', {
            session_id: this.sessionId,
            user_id: this.userId,
            user_name: this.userName,
            message: message,
            timestamp: new Date().toLocaleTimeString()
        });
    }

    broadcastAnimation(layer, progress, status) {
        if (!this.isSessionActive || !this.socket) {
            return;
        }

        this.socket.emit('broadcast_animation', {
            session_id: this.sessionId,
            user_name: this.userName,
            layer: layer,
            progress: progress,
            status: status
        });
    }

    displayRemoteMessage(data) {
        // Display other users' messages on the current user's screen
        const messageLog = document.getElementById('messageLog');
        if (!messageLog) return;

        const msgDiv = document.createElement('div');
        msgDiv.className = 'remote-message';
        msgDiv.innerHTML = `
            <strong>${data.user_name}:</strong> ${data.message}
            <span class="timestamp">${data.timestamp}</span>
        `;
        messageLog.appendChild(msgDiv);
    }

    displayRemoteAnimation(data) {
        // Display animation progress from other users
        const animationLog = document.getElementById('animationLog');
        if (!animationLog) return;

        const animDiv = document.createElement('div');
        animDiv.className = 'remote-animation';
        animDiv.innerHTML = `
            <strong>${data.user_name}:</strong> ${data.status} (Layer ${data.layer})
        `;
        animationLog.appendChild(animDiv);
    }
}

// Initialize multi-user manager when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.multiUserManager = new MultiUserManager();
});

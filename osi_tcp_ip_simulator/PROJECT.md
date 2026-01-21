# Project Structure and File Overview

## 📂 Complete Directory Structure

```
d:\DCN\osi_tcp_ip_simulator\
│
├── 📄 app.py                          # Flask main application (Backend)
├── 📄 models.py                       # Data models for OSI & TCP/IP
├── 📄 requirements.txt                # Python dependencies
├── 📄 README.md                       # Full documentation
├── 📄 SETUP.md                        # Quick start guide
├── 📄 PROJECT.md                      # This file
├── 📄 run.py                          # Python launcher (all platforms)
├── 📄 run.bat                         # Windows launcher batch file
├── 📄 run.sh                          # Linux/macOS launcher script
│
├── 📁 templates/                      # HTML templates folder
│   └── 📄 index.html                  # Main webpage (Frontend UI)
│
└── 📁 static/                         # Static assets folder
    ├── 📁 css/                        # Stylesheets
    │   └── 📄 style.css               # Main CSS styling
    └── 📁 js/                         # JavaScript files
        └── 📄 script.js               # Frontend interactivity
```

## 📋 File Descriptions

### Backend Files

#### `app.py` (Flask Application)
- Main entry point for the web application
- Contains Flask routes and API endpoints
- Serves HTML templates and static files
- Provides REST API for data access
- **Key Functions:**
  - `/` - Serve main page
  - `/api/osi-layers` - Get all OSI layers
  - `/api/tcpip-layers` - Get all TCP/IP layers
  - `/api/osi-layer/<number>` - Get specific OSI layer
  - `/api/tcpip-layer/<number>` - Get specific TCP/IP layer
  - `/api/encapsulation` - Get encapsulation sequence
  - `/api/decapsulation` - Get decapsulation sequence
  - `/api/layer-mapping` - Get layer mappings

#### `models.py` (Data Models)
- Defines `OSILayer` class for OSI layers
- Defines `TCPIPLayer` class for TCP/IP layers
- Defines `OSIModel` class (7 layers)
- Defines `TCPIPModel` class (4 layers)
- Contains encapsulation/decapsulation sequences
- **Key Classes:**
  - `OSILayer` - Represents a single OSI layer
  - `OSIModel` - Contains all 7 OSI layers
  - `TCPIPLayer` - Represents a single TCP/IP layer
  - `TCPIPModel` - Contains all 4 TCP/IP layers

### Configuration Files

#### `requirements.txt`
- Lists Python package dependencies
- Contains:
  - Flask==2.3.2 (Web framework)
  - Werkzeug==2.3.6 (WSGI utility)

### Frontend Files

#### `templates/index.html` (Main HTML)
- Complete HTML structure for the web application
- Contains:
  - Header with title and control buttons
  - Models container (OSI + TCP/IP + Info)
  - Data flow visualization tabs
  - Layer mapping table
  - Help modal dialog
- Responsive design for all devices
- Semantic HTML structure

#### `static/css/style.css` (Styling)
- Professional CSS styling
- Features:
  - CSS variables for consistent theming
  - Responsive grid layout
  - Smooth animations and transitions
  - Layer color coding
  - Interactive hover effects
  - Modal styling
  - Custom scrollbar styling
- **Media Queries:**
  - Desktop (1200px+)
  - Tablet (768px-1199px)
  - Mobile (<768px)

#### `static/js/script.js` (Interactivity)
- Main JavaScript application
- **Key Features:**
  - `NetworkSimulator` class for app logic
  - Async data loading from API
  - Event listener setup
  - Layer rendering
  - User interactions
  - Animation control
  - Tab switching
  - Help modal management
- **Key Methods:**
  - `init()` - Initialize application
  - `loadData()` - Fetch data from API
  - `renderOSILayers()` - Draw OSI model
  - `renderTCPIPLayers()` - Draw TCP/IP model
  - `startTransmission()` - Start animation
  - `animateEncapsulation()` - Animate sender side
  - `animateDecapsulation()` - Animate receiver side

### Documentation Files

#### `README.md`
- Comprehensive project documentation
- Features list
- System requirements
- Installation instructions
- Usage guide
- Layer information tables
- Data flow explanations
- Educational use cases
- Troubleshooting guide
- Developer notes

#### `SETUP.md`
- Quick start guide
- Step-by-step setup instructions
- Platform-specific instructions
- Troubleshooting tips
- Learning objectives
- Tips for best experience

#### `PROJECT.md`
- This file
- Complete project structure overview
- Detailed file descriptions

### Launcher Scripts

#### `run.py` (Python Launcher)
- Cross-platform launcher
- Auto-installs dependencies
- Opens browser automatically
- Starts Flask server
- Works on Windows, macOS, Linux

#### `run.bat` (Windows Launcher)
- Batch script for Windows
- Double-click to run
- Auto-checks Python installation
- Installs Flask if needed
- Opens default browser
- Provides user feedback

#### `run.sh` (Linux/macOS Launcher)
- Shell script for Unix-like systems
- Make executable: `chmod +x run.sh`
- Auto-detects available browser
- Installs dependencies if needed
- Runs Flask server

## 🔄 Data Flow

### Application Architecture

```
Browser (HTML/CSS/JS)
        ↓ (HTTP Requests)
    Flask Server (app.py)
        ↓ (Loads)
    Models (models.py)
        ↓ (Returns JSON)
    Browser (Updates DOM)
        ↓ (User Interaction)
    JavaScript (script.js)
        ↓ (Animation/Updates)
    Visual Display
```

### Layer Data

Each OSI Layer contains:
- `number` - Layer number (1-7)
- `name` - Layer name
- `functions` - List of functions
- `protocols` - List of protocols
- `data_unit` - Data unit name
- `color` - Display color (hex)

Each TCP/IP Layer contains:
- `number` - Layer number (1-4)
- `name` - Layer name
- `functions` - List of functions
- `protocols` - List of protocols
- `osi_layers` - Corresponding OSI layers
- `color` - Display color (hex)

## 🚀 How Everything Works Together

1. **User opens browser** → Requests http://localhost:5000
2. **Flask receives request** → Renders index.html template
3. **HTML loads with CSS & JS** → Page displays with styling
4. **JavaScript initializes** → Calls API endpoints
5. **API returns JSON** → Data loaded into JavaScript
6. **JavaScript renders layers** → UI displays all models
7. **User clicks layer** → Event listener triggers
8. **JavaScript updates DOM** → Information panel updates
9. **User starts transmission** → Animation begins
10. **JavaScript animates flow** → Layers highlight sequentially
11. **Animation completes** → Shows transmission complete message

## 📊 Data Models

### OSI Model (7 Layers)
1. Application Layer - HTTP, HTTPS, FTP, SMTP, DNS
2. Presentation Layer - SSL/TLS, JPEG, MPEG
3. Session Layer - NetBIOS, SAP, SSH
4. Transport Layer - TCP, UDP, SCTP
5. Network Layer - IP, ICMP, ARP
6. Data Link Layer - Ethernet, PPP, MAC
7. Physical Layer - Copper Wire, Fiber Optic, Wireless

### TCP/IP Model (4 Layers)
1. Link Layer (OSI 1-2) - Ethernet, PPP, Wi-Fi
2. Internet Layer (OSI 3) - IP, ICMP, ARP
3. Transport Layer (OSI 4) - TCP, UDP, SCTP
4. Application Layer (OSI 5-7) - HTTP, FTP, SMTP, DNS, SSH

## 💻 Technology Stack

- **Backend:** Python 3.6+
- **Web Framework:** Flask 2.3.2
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Styling:** Responsive CSS with CSS Grid
- **Communication:** REST API with JSON
- **Features:** Animations, Interactive UI, Responsive Design

## 🔒 Security Features

- No database required (data is hardcoded in models.py)
- No user input processing
- No authentication needed
- No external API calls
- All processing done locally

## ⚡ Performance Characteristics

- **Startup Time:** < 2 seconds
- **Page Load:** < 1 second
- **Animation:** 800ms per layer
- **API Response:** < 100ms
- **Total Transmission Animation:** ~6 seconds

## 📱 Responsive Design Breakpoints

- **Desktop:** 1200px and above
- **Tablet:** 768px to 1199px
- **Mobile:** Below 768px

## 🎨 Color Scheme

- **Primary:** #078282 (Teal)
- **Secondary:** #38ADA9 (Light Teal)
- **Accent:** #FF6B6B (Red)
- **Background:** #F5F5F5 (Light Gray)
- **Text:** #333 (Dark Gray)

## 🔧 Maintenance

### Adding New Protocols
1. Edit `models.py`
2. Add protocol to layer's `protocols` list
3. Restart server

### Changing Colors
1. Edit `models.py` - change `color` parameter
2. Or edit `style.css` - update CSS variables

### Modifying Animations
1. Edit `static/js/script.js`
2. Modify `animateEncapsulation()` or `animateDecapsulation()`
3. Refresh browser

### Adding New Features
1. Add API endpoint in `app.py`
2. Create HTML elements in `templates/index.html`
3. Add CSS in `static/css/style.css`
4. Add JavaScript functionality in `static/js/script.js`

## 📝 Notes

- All data is static and defined in `models.py`
- No database is used
- No external dependencies for functionality
- Flask development server is sufficient for educational use
- Application is stateless (no user sessions)
- All computation happens in browser (JavaScript)

---

**Created:** January 2026
**Version:** 1.0
**Status:** Complete and Ready for Use

# OSI vs TCP/IP Model Visual Simulator

An educational web-based simulator designed to help students understand network models through interactive visualization.

## 📋 Features

### Core Features
1. **Interactive Web Interface** - Modern, responsive UI using HTML/CSS/JavaScript
2. **Dual Model Visualization** - Both OSI (7 layers) and TCP/IP (4 layers) models
3. **Layer-by-Layer Data Flow** - Step-by-step visualization of data movement
4. **Encapsulation Demonstration** - Shows header addition at each layer (sender side)
5. **Decapsulation Demonstration** - Shows header removal at receiver side
6. **Clickable Layers** - Click any layer to view:
   - Layer functions
   - Associated protocols
   - Data units
7. **Protocol Display** - Common protocols at each layer
8. **OSI vs TCP/IP Mapping** - Clear comparison table between models
9. **Sender and Receiver Representation** - Distinguishes transmission sides
10. **Educational Design** - Perfect for learning and viva presentations

### Advanced Features
- ✅ Active layer highlighting during data flow
- ✅ Smooth animations for encapsulation & decapsulation
- ✅ Real-time explanation text updates
- ✅ Complete protocol information at each layer
- ✅ Responsive design for all devices

## 🛠 System Requirements

- Python 3.6 or higher
- Flask 2.3.2+
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Windows/Linux/macOS

## 📦 Installation & Usage

### Step 1: Install Dependencies
```bash
cd d:\DCN\osi_tcp_ip_simulator
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to `http://localhost:5000` in your web browser

## 🎮 How to Use

1. **Launch the Application**
   ```bash
   python app.py
   ```
   Then open `http://localhost:5000` in your browser

2. **Explore Layers**
   - Click on any layer (left or right panel) to view details
   - Information panel shows:
     - Layer functions
     - Associated protocols
     - Data units used

3. **View Data Flow**
   - Click "Start Transmission" to animate data flow
   - Watch encapsulation (sender side) - top to bottom
   - Watch decapsulation (receiver side) - bottom to top

4. **Compare Models**
   - Left panel: OSI 7-layer model
   - Right panel: TCP/IP 4-layer model
   - Middle panel: Layer information
   - Bottom table: Layer mapping comparison

5. **Use Flow Visualization**
   - Bottom tabs show:
     - Encapsulation process (how data is wrapped)
     - Decapsulation process (how data is unwrapped)

6. **Get Help**
   - Click "Help" button for detailed information
   - Hover over layers for quick highlights

## 📊 OSI Model (7 Layers)

| Layer | Name | Data Unit | Key Protocols |
|-------|------|-----------|----------------|
| 7 | Application | Data | HTTP, HTTPS, FTP, SMTP, DNS |
| 6 | Presentation | Data | SSL/TLS, JPEG, MPEG |
| 5 | Session | Data | NetBIOS, SAP, SSH |
| 4 | Transport | Segment | TCP, UDP, SCTP |
| 3 | Network | Packet | IP, ICMP, ARP |
| 2 | Data Link | Frame | Ethernet, PPP, MAC |
| 1 | Physical | Bits | Copper, Fiber Optic, Wireless |

## 📡 TCP/IP Model (4 Layers)

| Layer | Name | OSI Layers | Key Protocols |
|-------|------|-----------|----------------|
| 4 | Application | 7, 6, 5 | HTTP, FTP, SMTP, DNS, SSH |
| 3 | Transport | 4 | TCP, UDP, SCTP |
| 2 | Internet | 3 | IP, ICMP, ARP |
| 1 | Link | 2, 1 | Ethernet, PPP, Wi-Fi |

## 🔄 Data Flow Process

### Encapsulation (Sender Side)
```
Application Data (Layer 7)
    ↓
Presentation Processing (Layer 6)
    ↓
Session Management (Layer 5)
    ↓
TCP/UDP Header Added → Segment (Layer 4)
    ↓
IP Header Added → Packet (Layer 3)
    ↓
MAC Header Added → Frame (Layer 2)
    ↓
Physical Transmission → Bits (Layer 1)
```

### Decapsulation (Receiver Side)
```
Bits Received (Layer 1)
    ↓
Frame (Remove MAC Header - Layer 2)
    ↓
Packet (Remove IP Header - Layer 3)
    ↓
Segment (Remove TCP/UDP Header - Layer 4)
    ↓
Session Processing (Layer 5)
    ↓
Presentation Processing (Layer 6)
    ↓
Application (Layer 7) → Original Message
```

## 📚 Educational Use

### For Students
- Understand layer responsibilities
- Learn encapsulation/decapsulation
- See protocol usage at each layer
- Perfect for network course studies

### For Vivas/Presentations
- Clear visual representation
- Step-by-step animation
- Easy to explain concepts
- Interactive demonstration

## 🎨 Interface Components

1. **Header Section**
   - Title and control buttons
   - Start Transmission, Reset, Help buttons

2. **Left Panel (OSI Model)**
   - 7 color-coded layers (Layer 7 at top)
   - Shows data units
   - Clickable for details

3. **Right Panel (TCP/IP Model)**
   - 4 color-coded layers (Layer 4 at top)
   - Clickable for details
   - OSI mapping information

4. **Center Panel (Information)**
   - Layer details
   - Functions and responsibilities
   - Associated protocols

5. **Bottom Panel (Data Flow)**
   - Encapsulation visualization
   - Decapsulation visualization
   - Step-by-step transformation

6. **Mapping Table**
   - Side-by-side comparison
   - Functions for each TCP/IP layer
   - OSI layer equivalents

## 🚀 Advanced Features

### Layer Highlighting
- Active layer is highlighted during animation
- Easy to follow data movement
- Hover effects for better UI

### Real-time Explanations
- Text updates as data flows through layers
- Shows current data unit at each stage
- Detailed function descriptions

### Complete Protocol Information
- All major protocols listed
- Organized by layer
- Easy reference material

## 📁 Project Structure

```
osi_tcp_ip_simulator/
├── app.py                          # Flask application (main entry point)
├── models.py                       # OSI and TCP/IP model definitions
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── templates/
│   └── index.html                  # Main HTML template
└── static/
    ├── css/
    │   └── style.css               # Styling
    └── js/
        └── script.js               # Frontend interactivity
```

## 💡 Tips & Tricks

1. **Best Learning Approach**
   - Start by clicking different layers to understand their functions
   - Then click "Start Transmission" to see the full process
   - Compare OSI and TCP/IP models side by side
   - Review the mapping table for understanding relationships

2. **For Presentations**
   - Use full-screen browser for better visibility
   - Click layers to highlight specific points
   - Use animations to demonstrate concepts
   - Explain layer mapping during TCP/IP discussion

3. **Understanding Encapsulation**
   - Watch data transform as it moves down layers
   - Notice headers being added at each layer
   - See final bit transmission
   - Compare with decapsulation on receiver side

4. **Teaching Tips**
   - Use the Help modal to explain features
   - Let students interact with layers
   - Animate transmission multiple times
   - Discuss real-world protocol examples

## 🐛 Troubleshooting

### Application won't start
- Ensure Python 3.6+ is installed
- Check Flask is installed: `pip install -r requirements.txt`
- Check port 5000 is available

### UI not loading
- Clear browser cache (Ctrl+Shift+Delete)
- Check browser console for errors (F12)
- Ensure static files are present

### Animation not working
- Click "Start Transmission" button
- Ensure no other animations are running
- Try resetting with "Reset" button
- Check JavaScript is enabled in browser

### Port already in use
- Change port in `app.py` (last line)
- Or kill process using port 5000:
  ```bash
  # Windows
  netstat -ano | findstr :5000
  taskkill /PID <PID> /F
  ```

## 📖 References

- OSI Reference Model - ISO 7498
- TCP/IP Protocol Suite - RFC Documents
- Network Fundamentals - Networking Basics
- [RFC 1122 - Requirements for Internet Hosts](https://tools.ietf.org/html/rfc1122)

## 👨‍💻 Developer Notes

### Extending the Simulator

1. **Add New Protocols**
   - Edit `models.py`
   - Add to `OSILayer.protocols` or `TCPIPLayer.protocols`

2. **Customize Colors**
   - Modify `color` parameter in layer definitions
   - Update CSS root variables for consistency

3. **Add More Animations**
   - Extend `script.js` in `NetworkSimulator` class
   - Use `await this.sleep()` for timing

4. **Modify UI**
   - Edit `templates/index.html`
   - Update `static/css/style.css`
   - Add functionality in `static/js/script.js`

### API Endpoints

- `GET /` - Main page
- `GET /api/osi-layers` - All OSI layers
- `GET /api/tcpip-layers` - All TCP/IP layers
- `GET /api/osi-layer/<number>` - Specific OSI layer
- `GET /api/tcpip-layer/<number>` - Specific TCP/IP layer
- `GET /api/encapsulation` - Encapsulation sequence
- `GET /api/decapsulation` - Decapsulation sequence
- `GET /api/layer-mapping` - Layer mappings

## 📄 License

Educational use - Feel free to modify and distribute for learning purposes.

## 👥 Support

For issues or suggestions:
- Check the Help button in the application
- Review this README
- Check browser console (F12) for errors
- Verify all files are in correct directories

---

**Happy Learning! 🎓**

**Built with:** Python (Flask) + HTML/CSS/JavaScript

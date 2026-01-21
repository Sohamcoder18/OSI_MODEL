## 🚀 QUICK START GUIDE

This guide will help you get the OSI vs TCP/IP Model Visual Simulator up and running in minutes!

### Prerequisites
- Python 3.6 or higher
- Modern web browser (Chrome, Firefox, Safari, or Edge)

---

## ⚡ Fastest Way (Recommended)

### Windows Users
Double-click the `run.bat` file in the simulator folder. It will:
- Check for Python installation
- Install Flask automatically if needed
- Start the server
- Open the application in your browser

### macOS/Linux Users
Run this in terminal:
```bash
bash run.sh
```

---

## 📋 Manual Installation (If above doesn't work)

### Step 1: Navigate to the Project Directory
```bash
cd d:\DCN\osi_tcp_ip_simulator
```

### Step 2: Install Dependencies
```bash
python -m pip install -r requirements.txt
```

Or on macOS/Linux:
```bash
python3 -m pip install -r requirements.txt
```

### Step 3: Start the Server
```bash
python app.py
```

Or on macOS/Linux:
```bash
python3 app.py
```

### Step 4: Open in Browser
Open your web browser and go to:
```
http://localhost:5000
```

---

## 🎮 Using the Simulator

### Explore Individual Layers
1. Click on any OSI layer (1-7) in the left panel
2. View layer details in the center panel:
   - Functions
   - Associated protocols
   - Data units

### View Data Flow
1. Click "Start Transmission" button
2. Watch the animation showing:
   - Encapsulation (data moves down layers)
   - Decapsulation (data moves up layers)
   - Active layers are highlighted in red

### Compare Models
- **Left Panel**: OSI 7-layer model
- **Right Panel**: TCP/IP 4-layer model
- **Center Panel**: Detailed information
- **Bottom Table**: Layer mapping comparison

### View Encapsulation/Decapsulation
- Click tabs at the bottom to switch views
- See step-by-step data transformation
- Understand header addition and removal

### Get Help
- Click "Help" button for detailed information
- Hover over layers for quick visual feedback
- Read tooltips for layer information

---

## 🎯 Learning Objectives

After using this simulator, you'll understand:

✓ OSI Model layers and their responsibilities
✓ TCP/IP Model layers and their roles
✓ How data encapsulation works
✓ How data decapsulation works
✓ Network protocols at each layer
✓ Differences between OSI and TCP/IP models
✓ Data flow from application to physical layer

---

## 🔧 Troubleshooting

### Problem: "Python not found" or "Python not recognized"
**Solution**: Python is not in your system PATH
- [Install Python](https://www.python.org/) with "Add Python to PATH" option checked
- Or use the full path: `C:\Program Files\Python39\python.exe app.py`

### Problem: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Flask is not installed
```bash
python -m pip install Flask==2.3.2
```

### Problem: "Address already in use" or "Port 5000 in use"
**Solution**: Another application is using port 5000
- Wait a moment and try again, or
- Edit the last line in `app.py` to use a different port:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Use port 8000
```

### Problem: Browser won't open automatically
**Solution**: Open manually
- Go to `http://localhost:5000` in your browser address bar
- Make sure the server is running

### Problem: CSS/JS not loading or styling looks broken
**Solution**: Clear browser cache
- Press `Ctrl+Shift+Delete` (Windows) or `Cmd+Shift+Delete` (Mac)
- Select "All time" and click "Clear"
- Refresh the page

### Problem: Animation/Interactivity not working
**Solution**: Check JavaScript is enabled
- Open browser DevTools (F12)
- Check Console tab for errors
- Refresh the page
- Try a different browser

---

## 📁 Project Files

```
osi_tcp_ip_simulator/
├── app.py                   # Main Flask application
├── models.py                # OSI & TCP/IP model definitions
├── requirements.txt         # Python dependencies
├── run.py                   # Python launcher script
├── run.bat                  # Windows launcher script
├── run.sh                   # Linux/macOS launcher script
├── README.md                # Full documentation
├── SETUP.md                 # This file
├── templates/
│   └── index.html           # Main web page
└── static/
    ├── css/
    │   └── style.css        # Styling
    └── js/
        └── script.js        # Interactivity
```

---

## 🌐 Accessing the Application

### Local (Your Computer)
- **Address**: `http://localhost:5000`
- **From Same Network**: `http://192.168.X.X:5000` (check output when server starts)

### What to Do Next
1. Start the server
2. Open the application
3. Click on different layers to explore
4. Click "Start Transmission" to see animation
5. Use tabs to view encapsulation/decapsulation
6. Check the mapping table for comparisons

---

## 💡 Tips for Best Experience

1. **Use Full Screen**
   - Press F11 in browser for better visibility

2. **Take Your Time**
   - Click layers slowly to absorb information
   - Watch animation multiple times
   - Pause and discuss each step

3. **Read the Help**
   - Click "Help" button for detailed explanations
   - Reference the table for protocol information

4. **Practice**
   - Try to explain each layer's function
   - Identify where each protocol operates
   - Compare with real-world applications

5. **Study Resources**
   - Use this with textbooks
   - Reference standards (RFC, ISO)
   - Combine with networking courses

---

## 🎓 Educational Features

This simulator is perfect for:

- **Individual Learning**: Self-paced study of network models
- **Classroom Use**: Demonstrate concepts to students
- **Presentations**: Impress examiners with visual explanations
- **Viva Preparation**: Understand layers deeply for interviews
- **Projects**: Learn by implementing network concepts

---

## 📞 Support

If you encounter issues:

1. **Check Console** (Press F12)
   - Look for error messages
   - Note any red text

2. **Verify Installation**
   - Run: `python -m pip list | findstr Flask`
   - Should show Flask version

3. **Try Restart**
   - Stop server (Ctrl+C)
   - Wait 5 seconds
   - Start again

4. **Review Files**
   - Ensure all files are present
   - Check file names are exact matches
   - Verify folder structure matches above

---

## 🎉 You're Ready!

Now you have everything set up to explore networking concepts visually!

**Start by:**
1. Launching the application
2. Clicking on OSI Layer 7 (Application)
3. Reviewing its functions and protocols
4. Then clicking "Start Transmission"
5. Watching how data flows through all layers

Happy learning! 🚀

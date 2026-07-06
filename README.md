# OSINT Tool - Open-Source Intelligence Suite

A comprehensive, modern Python-based OSINT (Open-Source Intelligence) tool with a sleek CustomTkinter GUI. Perform reconnaissance on usernames, emails, domains, IPs, phone numbers, and more.

## 🌟 Features

### 🔍 Username Search
- Search across multiple social media platforms
- Display account existence status
- Show profile URLs
- Copy results to clipboard

### 📧 Email Intelligence
- Validate email format
- Check MX records
- Detect disposable email providers
- Extract domain information

### 🌐 Domain Lookup
- WHOIS lookup
- DNS records (A, MX, TXT, NS, CNAME)
- SSL certificate information
- IP address resolution

### 🌍 IP Lookup
- Geolocation data
- ASN information
- ISP details
- Reverse DNS lookup

### 📱 Phone Number Lookup
- Country identification
- Carrier information
- Number type detection
- Time zone information

### 🖼️ Metadata Viewer
- EXIF metadata extraction
- GPS coordinates
- Camera information
- Image details

### 🔐 Hash Tools
- Generate MD5, SHA1, SHA256
- Identify common hash types
- Batch hash generation

### 🔑 Password Utilities
- Password strength checker
- Password generator with custom options
- Real-time strength feedback

### 🔎 DNS Tools
- Reverse DNS lookup
- DNS propagation checker
- Subdomain enumeration

### 📊 Reports
- Export results as JSON
- Export results as CSV
- Generate PDF reports
- Search history

## 🎨 Design Features

- **Dark Theme**: Modern, eye-friendly interface
- **Sidebar Navigation**: Easy tool access
- **Icons**: Visual indicators for all tools
- **Progress Bars**: Real-time search feedback
- **Search History**: Track previous searches
- **Copy-to-Clipboard**: Quick result copying
- **Responsive UI**: Never freezes during operations

## 📋 System Requirements

- Python 3.12+
- Windows, macOS, or Linux
- 100MB free disk space

## 🚀 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/bando11223/OSINT-Tool.git
cd OSINT-Tool
```

### 2. Create Virtual Environment (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Settings (Optional)
Edit `config.json` to customize:
- API keys for various services
- Theme preferences
- Default settings
- Rate limits

## 💻 Usage

### Run the Application
```bash
python main.py
```

### First Launch
1. The application creates a `config.json` file automatically
2. Configure API keys if needed (some features work without keys)
3. Select a tool from the sidebar
4. Enter your search query
5. Click "Search" and wait for results
6. Export results if needed

## 🛠️ Project Structure

```
OSINT-Tool/
├── main.py                  # Application entry point
├── config.json              # Configuration file (auto-generated)
├── requirements.txt         # Python dependencies
├── README.md                # This file
├── src/
│   ├── __init__.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── main_window.py   # Main GUI window
│   │   ├── sidebar.py       # Navigation sidebar
│   │   ├── themes.py        # Color schemes & styling
│   │   └── widgets.py       # Custom UI components
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── username_search.py    # Social media lookup
│   │   ├── email_intel.py        # Email validation & verification
│   │   ├── domain_lookup.py      # Domain WHOIS & DNS
│   │   ├── ip_lookup.py          # IP geolocation & ASN
│   │   ├── phone_lookup.py       # Phone number analysis
│   │   ├── metadata_viewer.py    # EXIF & image metadata
│   │   ├── hash_tools.py         # Hash generation & identification
│   │   ├── password_utils.py     # Password checker & generator
│   │   ├── dns_tools.py          # DNS utilities
│   │   └── report_generator.py   # Export & reports
│   ├── api/
│   │   ├── __init__.py
│   │   ├── requests_handler.py   # HTTP request wrapper
│   │   └── validators.py         # Input validation
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── config.py             # Config management
│   │   ├── logger.py             # Logging setup
│   │   └── helpers.py            # Utility functions
│   └── models/
│       ├── __init__.py
│       └── data_models.py        # Data classes
└── assets/
    └── icons/                    # Application icons
```

## ⚙️ Configuration

The `config.json` file contains:

```json
{
  "app": {
    "theme": "dark",
    "window_width": 1400,
    "window_height": 900,
    "update_check": true
  },
  "api_keys": {
    "ipinfo": "",
    "abuseipdb": "",
    "emailrep": ""
  },
  "settings": {
    "timeout": 10,
    "max_retries": 3,
    "log_searches": true
  }
}
```

## 🔑 API Keys (Optional)

Some features work better with API keys:

- **IPInfo**: https://ipinfo.io/ (Free tier available)
- **AbuseIPDB**: https://www.abuseipdb.com/ (Free tier available)
- **EmailRep**: https://emailrep.io/ (Free tier available)

Add your keys to `config.json` to unlock premium features.

## 🧵 Threading & Async

All network requests run on separate threads to keep the UI responsive:
- GUI never freezes during searches
- Real-time progress updates
- Cancellable operations
- Smooth animations

## 📝 Logging

Application logs are saved to:
- **Windows**: `%APPDATA%/OSINT-Tool/logs/`
- **macOS**: `~/Library/Application Support/OSINT-Tool/logs/`
- **Linux**: `~/.local/share/OSINT-Tool/logs/`

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Submit a pull request

## ⚖️ Legal Disclaimer

This tool is intended for authorized security testing and educational purposes only. Users are responsible for ensuring they have proper authorization before gathering intelligence on any individuals, organizations, or systems. Misuse of this tool may violate laws and regulations in your jurisdiction.

## 📄 License

MIT License - See LICENSE file for details

## 🐛 Bug Reports

Found a bug? Please open an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Screenshots (if applicable)

## 📞 Support

For support, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review documentation in code comments

## 🔄 Updates

The application checks for updates on startup (if enabled in config). To manually check:
- Look for update notifications in the UI
- Download the latest release from GitHub

---

**Made with ❤️ for the cybersecurity community**

### Disclaimer
This tool is provided as-is for educational and authorized security testing purposes only. Users assume all responsibility for proper use in compliance with applicable laws and regulations.

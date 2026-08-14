# CF-Scanner
A Python tool for scanning Cloudflare IP ranges, built for educational and authorized testing

Features

- Scan up to 1,000,000 Cloudflare IP addresses
- High scanning speed — approximately 100,000 IPs per minute depending on system and network conditions
- Custom Port — choose any port you want to scan
- Geo IPs — identify the country associated with scanned IP addresses
- Telegram Bot Support — send scanned IPs directly to your Telegram bot
- Very low data consumption
- Lightweight and easy to use
- No additional Python packages required

Telegram Integration

After the scan is completed, you can enter:

- Telegram Bot Token
- Telegram User/Chat ID

The scanner can then send the successfully scanned IP addresses directly to your Telegram bot.

Custom Port Scanning

The Custom Port section allows you to specify your desired port.
The scanner will test Cloudflare IP addresses based on the selected port.

Geo IP

The Geo IPs feature shows the country associated with each scanned IP address.

Performance

The scanner is designed to handle large IP ranges efficiently while keeping CPU, memory, and network usage relatively low.

«Performance may vary depending on your internet connection, system specifications, and network conditions.»

Requirements

- Python 3.x
- No additional libraries required


## 📥 Installation

### Quick Start (Recommended)

#### 📱 Termux (Android)

```bash
# Update Termux
pkg update && pkg upgrade -y

# Install Python and curl
pkg install python curl -y

# Download the scanner
curl -fsSL https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py -o Scanner.py

# Run the scanner
python3 Scanner.py
```

#### 🐧 Linux (Ubuntu, Debian, Kali, etc.)

```bash
# Download the scanner
curl -fsSL https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py -o Scanner.py

# Run the scanner
python3 Scanner.py
```

If `curl` is not installed:

```bash
# Ubuntu/Debian/Kali
sudo apt update && sudo apt install curl -y

# Fedora/Red Hat
sudo dnf install curl -y

# Arch Linux
sudo pacman -S curl
```

#### 🪟 Windows (PowerShell)

```powershell
# Download the scanner
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py" -OutFile "Scanner.py"

# Run the scannerpython Scanner.py
```

#### 🪟 Windows (CMD with curl)

```cmd
curl -fsSL https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py -o Scanner.py
python Scanner.py
```

---

### Alternative: Git Clone

```bash
git clone https://github.com/antteiku/CF-Scanner.git
cd CF-Scanner
python3 Scanner.py
```

---

## 🔧 Usage

### Basic Usage

```bash
python3 Scanner.py
```

### View Help

```bash
python3 Scanner.py --help
```

### Custom Port Scanning

```bash
python3 Scanner.py --port 8080
```

### Telegram Bot Integration

```bash
python3 Scanner.py --bot-token YOUR_BOT_TOKEN --chat-id YOUR_CHAT_ID
```

### Geo-IP Detection
```bash
python3 Scanner.py --geo
```

---

## 🔧 Troubleshooting

### Error: could not resolve host

This is usually a DNS issue. Change your DNS:

**Termux:**
```bash
echo "nameserver 8.8.8.8" > $PREFIX/etc/resolv.conf
echo "nameserver 1.1.1.1" >> $PREFIX/etc/resolv.conf
```

**Linux:**
```bash
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
echo "nameserver 1.1.1.1" | sudo tee -a /etc/resolv.conf
```

### Error: python not found

Python is not installed. Install it:

**Termux:**
```bash
pkg install python
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt install python3
```

**Windows:**
Download Python from [python.org](https://www.python.org/downloads/) and make sure to check "Add Python to PATH" during installation.

### Error: permission denied

You don't have execute permissions:

```bash
chmod +x Scanner.py
```

### Error: curl not found
Install curl:

**Termux:**
```bash
pkg install curl
```

**Linux:**
```bash
sudo apt install curl
```

**Windows:**
Use PowerShell method instead, or install curl from [curl.se](https://curl.se/windows/).


© 2026 Antteiku. All rights reserved.

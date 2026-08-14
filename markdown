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

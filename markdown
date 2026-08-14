 📥 Installation

 Quick Start (Recommended)

📱 Termux (Android)

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

 🐧 Linux (Ubuntu, Debian, Kali, etc.)

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

 🪟 Windows (PowerShell)

```powershell
# Download the scanner
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py" -OutFile "Scanner.py"

# Run the scannerpython Scanner.py
```

 🪟 Windows (CMD with curl)

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

<div align="center">

<img src="https://raw.githubusercontent.com/antteiku/CF-Scanner/main/banner.png" alt="CF-Scanner Banner" width="100%">

# CF-Scanner

### High-Performance Cloudflare IP Scanner

**A blazing-fast, zero-dependency Python tool for scanning up to 1,000,000 Cloudflare IPs — with Geo-IP lookup and native Telegram delivery.**

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Python](https://img.shields.io/badge/Python-3.6%2B-green.svg)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS%20%7C%20Termux-orange.svg)](#supported-platforms)
[![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen.svg)](#requirements)
[![Speed](https://img.shields.io/badge/Speed-~100k%20IPs%2Fmin-red.svg)](#performance)

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Telegram](#telegram-integration) • [FAQ](#faq)

</div>

---

## Overview

CF-Scanner is a lightweight command-line tool that rapidly scans Cloudflare IP ranges to find responsive, low-latency addresses. It is written in pure Python with no external dependencies, making it trivial to run anywhere — from a full Linux server to an Android phone via Termux.

It is built strictly for educational purposes and authorized network testing on infrastructure you own or have explicit permission to test.

---

## Table of Contents

- [Features](#features)
- [Supported Platforms](#supported-platforms)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Telegram Integration](#telegram-integration)
- [Configuration Options](#configuration-options)
- [Performance](#performance)
- [FAQ](#faq)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Features

| Feature | Description |
|---|---|
| **Massive Scale** | Scan up to 1,000,000 Cloudflare IP addresses in a single run |
| **High Speed** | Approximately 100,000 IPs per minute, depending on hardware and network |
| **Custom Port** | Target any port you choose for the connectivity test |
| **Geo-IP Lookup** | Identify the country associated with each responsive IP |
| **Telegram Delivery** | Automatically push results straight to your Telegram bot |
| **Low Data Usage** | Minimal bandwidth consumption during scans |
| **Zero Dependencies** | Runs on a stock Python install — no `pip install` required |
| **Cross-Platform** | Works on Linux, Windows, macOS, and Termux (Android) |

---

## Supported Platforms

<div align="center">

| Platform | Status | Notes |
|---|:---:|---|
| **Linux** (Ubuntu, Debian, Kali…) | Yes | Recommended |
| **Windows** (PowerShell / CMD) | Yes | Python 3 required |
| **macOS** | Yes | Use `python3` |
| **Termux** (Android) | Yes | Great for on-the-go scanning |

</div>

---

## Requirements

- Python 3.6+
- No additional libraries — the scanner relies only on the Python standard library.
- An active internet connection.

> Verify your Python version with `python3 --version` (or `python --version` on Windows).

---

## Installation

### Quick Start (Recommended)

Pick the block for your platform, paste it into a terminal, and you're running.

<details open>
<summary><b>Termux (Android)</b></summary>

```bash
# Update Termux and install prerequisites
pkg update && pkg upgrade -y
pkg install python curl -y

# Download and run the scanner
curl -fsSL https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py -o Scanner.py
python3 Scanner.py
```
</details>

<details>
<summary><b>Linux (Ubuntu · Debian · Kali)</b></summary>

```bash
# Download and run
curl -fsSL https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py -o Scanner.py
python3 Scanner.py
```

If `curl` is missing, install it first:

```bash
# Ubuntu / Debian / Kali
sudo apt update && sudo apt install curl -y

# Fedora / Red Hat
sudo dnf install curl -y

# Arch Linux
sudo pacman -S curl
```
</details>

<details>
<summary><b>Windows (PowerShell)</b></summary>

```powershell
# Download the scanner
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py" -OutFile "Scanner.py"

# Run it
python Scanner.py
```
</details>

<details>
<summary><b>Windows (CMD with curl)</b></summary>

```cmd
curl -fsSL https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py -o Scanner.py
python Scanner.py
```
</details>

<details>
<summary><b>macOS</b></summary>

```bash
curl -fsSL https://raw.githubusercontent.com/antteiku/CF-Scanner/main/Scanner.py -o Scanner.py
python3 Scanner.py
```
</details>

### Alternative: Git Clone

```bash
git clone https://github.com/antteiku/CF-Scanner.git
cd CF-Scanner
python3 Scanner.py
```

---

## Usage

1. Launch the scanner:
   ```bash
   python3 Scanner.py
   ```
2. Follow the interactive prompts to set:
   - Number of IPs to scan
   - Custom port (optional)
   - Geo-IP lookup (on/off)
   - Telegram bot token & chat ID (optional)
3. Wait for the scan to finish — responsive IPs are displayed live and saved to the output file.
4. If Telegram is configured, results are pushed to your bot automatically.

---

## Telegram Integration

Have your scan results delivered straight to Telegram.

### Step 1 — Create a bot
1. Open [@BotFather](https://t.me/BotFather) in Telegram.
2. Send `/newbot` and follow the steps.
3. Copy the Bot Token it gives you (looks like `123456789:ABC-Def...`).

### Step 2 — Get your Chat ID
1. Open [@userinfobot](https://t.me/userinfobot) and press Start.
2. Copy the numeric Chat ID it returns.

### Step 3 — Enter them in the scanner
When prompted, paste your:
- Telegram Bot Token
- Telegram User / Chat ID

The scanner will then forward every successfully scanned IP directly to your bot.

---

## Configuration Options

| Option | Description | Default |
|---|---|---|
| **IP Count** | How many Cloudflare IPs to scan (up to 1,000,000) | Prompted |
| **Custom Port** | The port to test connectivity against | `443` |
| **Geo-IP** | Resolve the country for each responsive IP | Optional |
| **Telegram Token** | Bot token for result delivery | Optional |
| **Chat ID** | Destination chat for results | Optional |

---

## Performance

The scanner is engineered to process large IP ranges efficiently while keeping CPU, memory, and bandwidth usage low.

| Metric | Value |
|---|---|
| Max IPs per run | 1,000,000 |
| Typical throughput | ~100,000 IPs / min |
| Memory footprint | Low |
| Data consumption | Very low |

> Actual results vary with your internet connection, hardware, and network conditions.

---

## FAQ

<details>
<summary><b>Do I need to install any Python packages?</b></summary>

No. CF-Scanner uses only the Python standard library. A stock Python 3.6+ install is all you need.
</details>

<details>
<summary><b>Why would I scan Cloudflare IPs?</b></summary>

For educational purposes and authorized network diagnostics — e.g. measuring latency and reachability of endpoints you own or are permitted to test.
</details>

<details>
<summary><b>Can I run it on my phone?</b></summary>

Yes — via Termux on Android. See the installation section above.
</details>

<details>
<summary><b>The Telegram bot isn't receiving results. Why?</b></summary>

Make sure you pressed Start on your bot, and that both the Bot Token and Chat ID are correct. See [Troubleshooting](#troubleshooting).
</details>

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `python3: command not found` | Install Python 3, or try `python` instead of `python3` |
| `curl: command not found` | Install curl (see the Linux install block) |
| Slow scan speed | Check your internet connection; reduce the IP count |
| No Telegram messages | Press Start on your bot; re-verify the token and chat ID |
| Permission denied | Run in a directory you have write access to |

---

## License

This project is licensed under the GNU General Public License v3.0 — see the [LICENSE](https://www.gnu.org/licenses/gpl-3.0) file for details.

---

<div align="center">

**If you find CF-Scanner useful, consider starring the repo!⭐**

© 2026 Antteiku. All rights reserved.

</div>

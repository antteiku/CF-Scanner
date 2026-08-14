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

Disclaimer

This tool is intended for educational purposes and authorized network testing. Only scan IP addresses and ports that you have permission to test.

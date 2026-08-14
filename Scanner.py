import socket
import time
import json
import os
import random
import ipaddress
import subprocess
import urllib.request
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor, as_completed


R = "\033[0m"
B = "\033[1m"
DIM = "\033[2m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAG = "\033[95m"
WHITE = "\033[97m"
BG_BLUE = "\033[44m"
BG_CYAN = "\033[46m"

CF_RANGES = [
    "173.245.48.0/20", "103.21.244.0/22", "103.22.200.0/22",
    "103.31.4.0/22", "141.101.64.0/18", "108.162.192.0/18",
    "190.93.240.0/20", "188.114.96.0/20", "197.234.240.0/22",
    "198.41.128.0/17", "162.158.0.0/15", "104.16.0.0/13",
    "104.24.0.0/14", "172.64.0.0/13", "131.0.72.0/22",
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def expand(cidr):
    return [str(ip) for ip in ipaddress.ip_network(cidr, strict=False).hosts()]

def gen_ips(count):
    all_ips = []
    for c in CF_RANGES: all_ips.extend(expand(c))
    return random.sample(all_ips, min(count, len(all_ips)))

def tcp_test(ip, port=80, timeout=2.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((ip, port))
        s.close()
        return (ip, True)
    except:
        s.close()
        return (ip, False)

def scan(ips, ports=[80], threads=3000, timeout=0.08):
    t0 = time.time()
    done = [0]
    results = []
    total = len(ips) * len(ports)
    batch = min(1000, len(ips))

    print(f"\n{CYAN}{B}  Scanning {len(ips)} IPs x {len(ports)} port(s) ({threads} threads)...{R}\n")
    with ThreadPoolExecutor(max_workers=threads) as ex:
        for i in range(0, len(ips), batch):
            chunk = ips[i:i+batch]
            futures = [ex.submit(tcp_test, ip, p, timeout) for ip in chunk for p in ports]
            for f in as_completed(futures):
                done[0] += 1
                ip, ok = f.result()
                if ok: results.append({"ip": ip, "ms": 0, "ok": True})
                if done[0] % 50 == 0:
                    pct = int(done[0]*100/total) if total > 0 else 100
                    bar = f"{BLUE}{'█'*(pct//2)}{DIM}{'░'*(50-pct//2)}{R}"
                    print(f"\r  [{bar}] {CYAN}{pct}%{R} ({done[0]}/{total})", end="", flush=True)
    print(f"\r  {BLUE}{'█'*50}{R} {CYAN}100%{R} ({done[0]}/{total})")
    elapsed = time.time() - t0
    # Deduplicate
    seen = set()
    unique = []
    for r in results:
        if r["ip"] not in seen:
            seen.add(r["ip"])
            unique.append(r)
    speed = total/elapsed if elapsed > 0 else 0
    print(f"\n  {GREEN}{B}Done: {len(unique)}/{len(ips)} alive | {elapsed:.2f}s | {speed:.0f} scans/sec{R}\n")
    return unique

def show(results, count=25):
    if not results:
        print(f"  {RED}No results!{R}")
        return
    print(f"  {B}{BLUE}{'#':>3}  {'IP':<20} {'Status'}{R}")
    print(f"  {DIM}{'─'*40}{R}")
    for i, r in enumerate(results[:count], 1):
        print(f"  {B}{BLUE}{i:>3}{R}  {GREEN}{r['ip']:<20}{R} {GREEN}{B}✅ ALIVE{R}")
    print(f"\n  {GREEN}{B}🏆 First: {results[0]['ip']}{R}")

def save(results):
    if not results:
        print(f"\n  {YELLOW}No alive IPs to save!{R}")
        return
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cloudflare")
    os.makedirs(d, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fn = os.path.join(d, f"cloudflare_ip_{ts}.txt")
    with open(fn, "w") as f:
        for r in results: f.write(r["ip"] + "\n")
    print(f"\n  {GREEN}💾 Saved: {CYAN}{fn}{R}")

def copy_ips(results):
    if not results:
        print(f"\n  {YELLOW}No IPs to copy!{R}")
        return
    text = "\n".join(r["ip"] for r in results)
    try:
        if os.name == 'nt':
            subprocess.run('clip', input=text.encode('utf-16le'), check=True)
        else:
            subprocess.run('xclip', '-selection', 'clipboard', input=text.encode(), check=True)
        print(f"\n  {GREEN}✅ {len(results)} IPs copied to clipboard!{R}")
    except:
        print(f"\n  {YELLOW}Clipboard not available. IPs:{R}")
        for r in results[:10]:
            print(f"    {CYAN}{r['ip']}{R}")

def geoip(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode())
            if data.get("bogon"):
                return None
            return {
                "ip": ip,
                "country": data.get("country", "?"),
                "city": data.get("city", "?"),
                "region": data.get("region", "?"),
                "org": data.get("org", "?"),
                "hostname": data.get("hostname", "cloudflare"),
            }
    except:
        pass
    return None

def geoip_scan(results):
    if not results:
        print(f"\n  {YELLOW}No IPs to check!{R}")
        return
    print(f"\n{CYAN}{B}  Checking GeoIP for {len(results)} IPs...{R}")
    print(f"  {YELLOW}(These are Cloudflare CDN edge IPs, location = nearest datacenter){R}\n")
    for i, r in enumerate(results[:20], 1):
        info = geoip(r["ip"])
        if info:
            loc = f"{info['country']}, {info['city']}"
            org = info.get('org', '').replace('AS13335 ', '')
            print(f"  {GREEN}{i:>3}. {info['ip']:<18}{R} {YELLOW}{loc:<25}{R} {DIM}{org}{R}")
        else:
            print(f"  {RED}{i:>3}. {r['ip']:<18} ???{R}")

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scanner_config.json")

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}

def save_config(key, value):
    cfg = load_config()
    cfg[key] = value
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=2)

def telegram_send(results):
    if not results:
        print(f"\n  {YELLOW}No IPs to send!{R}")
        return
    cfg = load_config()
    token = cfg.get("tg_token", "")
    chat_id = cfg.get("tg_chat", "")
    if token and chat_id:
        masked = token[:8] + "..." + token[-4:] if len(token) > 12 else token
        print(f"\n  {GREEN}Saved settings:{R}")
        print(f"    Token: {CYAN}{masked}{R}")
        print(f"    Chat:  {CYAN}{chat_id}{R}")
        use = input(f"\n  {B}Use saved? (y/n): {R}").strip().lower()
        if use == "n":
            token = input(f"  {B}Bot token: {R}").strip()
            chat_id = input(f"  {B}Chat ID: {R}").strip()
            save_config("tg_token", token)
            save_config("tg_chat", chat_id)
    else:
        print(f"\n  {YELLOW}No saved settings found{R}")
        token = input(f"  {B}Bot token: {R}").strip()
        chat_id = input(f"  {B}Chat ID: {R}").strip()
        save_config("tg_token", token)
        save_config("tg_chat", chat_id)
    text = f"🔍 Amir Scanner Results\n"
    text += f"📊 Found: {len(results)} alive IPs\n\n"
    for i, r in enumerate(results[:30], 1):
        text += f"{i}. {r['ip']}\n"
    if len(results) > 30:
        text += f"\n... and {len(results)-30} more"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = json.dumps({"chat_id": chat_id, "text": text}).encode()
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
    try:
        urllib.request.urlopen(req, timeout=10)
        print(f"\n  {GREEN}✅ Sent to Telegram!{R}")
    except Exception as e:
        print(f"\n  {RED}Error: {e}{R}")

def banner():
    clear()
    print(f"""
{GREEN}{B}  ========================================
         Anteiku SCANNER
    Cloudflare IP Scanner
  ========================================{R}
""")

def menu():
    print(f"""{BLUE}{B}  ┌──────────────────────────────────────┐
  │{R}{GREEN}  >{R} {WHITE}1. Quick Scan{R}     500 CF IPs        {BLUE}{B}│
  │{R}{YELLOW}  >{R} {WHITE}2. Turbo Scan{R}     2000 CF IPs       {BLUE}{B}│
  │{R}{CYAN}  >{R} {WHITE}3. Custom{R}          N IPs, any port   {BLUE}{B}│
  │{R}{MAG}  >{R} {WHITE}4. IP Range{R}       scan CIDR range   {BLUE}{B}│
  │{R}{GREEN}  >{R} {WHITE}5. Copy IPs{R}       copy to clipboard {BLUE}{B}│
  │{R}{YELLOW}  >{R} {WHITE}6. GeoIP{R}          check IP location {BLUE}{B}│
  │{R}{CYAN}  >{R} {WHITE}7. Telegram{R}       send results      {BLUE}{B}│
  │{R}{RED}  >{R} {WHITE}8. Exit{R}                              {BLUE}{B}│
  └──────────────────────────────────────┘{R}
""")

def main():
    last_results = []
    while True:
        banner()
        menu()
        c = input(f"  {BLUE}{B}Select (1-8): {R}").strip()
        if c == "1":
            banner()
            last_results = scan(gen_ips(500), [80], 3000, 0.08)
            show(last_results)
            save(last_results)
        elif c == "2":
            banner()
            last_results = scan(gen_ips(2000), [80, 443], 3000, 0.08)
            show(last_results)
            save(last_results)
        elif c == "3":
            banner()
            n = input(f"  {B}How many IPs? (default 1000): {R}").strip()
            count = int(n) if n.isdigit() else 1000
            print(f"\n  {YELLOW}Port options:{R}")
            print(f"  {GREEN}1.{R} Port 80 (fast)")
            print(f"  {GREEN}2.{R} Port 443 (HTTPS)")
            print(f"  {GREEN}3.{R} All common ports (80,443,8080,8443,2053,2083,2087,2096,8880)")
            print(f"  {GREEN}4.{R} Custom port number")
            pc = input(f"  {B}Select (1-4): {R}").strip()
            if pc == "1": ports = [80]
            elif pc == "2": ports = [443]
            elif pc == "3": ports = [80, 443, 8080, 8443, 2053, 2083, 2087, 2096, 8880]
            elif pc == "4":
                cp = input(f"  {B}Enter port number: {R}").strip()
                ports = [int(cp)] if cp.isdigit() and int(cp) > 0 else [80]
            else: ports = [80]
            last_results = scan(gen_ips(count), ports, 3000, 0.08)
            show(last_results)
            save(last_results)
        elif c == "4":
            banner()
            cidr = input(f"  {B}Enter IP range (e.g. 104.16.0.0/16): {R}").strip()
            try:
                all_ips = expand(cidr)
                print(f"\n  {CYAN}Total IPs in range: {len(all_ips)}{R}")
                n = input(f"  {B}How many to scan? (default 1000): {R}").strip()
                count = int(n) if n.isdigit() else 1000
                ips = random.sample(all_ips, min(count, len(all_ips)))
                print(f"\n  {YELLOW}Port options:{R}")
                print(f"  {GREEN}1.{R} Port 80 (fast)")
                print(f"  {GREEN}2.{R} Port 443 (HTTPS)")
                print(f"  {GREEN}3.{R} All common ports")
                print(f"  {GREEN}4.{R} Custom port number")
                pc = input(f"  {B}Select (1-4): {R}").strip()
                if pc == "1": ports = [80]
                elif pc == "2": ports = [443]
                elif pc == "3": ports = [80, 443, 8080, 8443, 2053, 2083, 2087, 2096, 8880]
                elif pc == "4":
                    cp = input(f"  {B}Enter port number: {R}").strip()
                    ports = [int(cp)] if cp.isdigit() and int(cp) > 0 else [80]
                else: ports = [80]
                last_results = scan(ips, ports, 3000, 0.08)
                show(last_results)
                save(last_results)
            except Exception as e:
                print(f"  {RED}Invalid CIDR! Error: {e}{R}")
        elif c == "5":
            copy_ips(last_results)
        elif c == "6":
            banner()
            geoip_scan(last_results)
        elif c == "7":
            banner()
            telegram_send(last_results)
        elif c in ("8", "q"):
            print(f"\n  {CYAN}{B}Goodbye!{R}\n")
            break
        else:
            print(f"  {RED}Invalid!{R}")
        input(f"\n  {DIM}Press Enter...{R}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
# ============================================================
#   HACKPATH PASSWORD GENERATOR v2
#   Created by: Sachin Ser | HackPath
#   Works on: Termux | Linux | Kali
#   Run: python3 passgen.py
#   No extra install needed — Pure Python!
#   GitHub: github.com/sachin-null/hackpath-passgen
# ============================================================

import os, sys, random, string, hashlib, math, re, json

class C:
    R='\033[91m'; G='\033[92m'; Y='\033[93m'
    B='\033[94m'; M='\033[95m'; CY='\033[96m'
    W='\033[97m'; DIM='\033[2m'; X='\033[0m'; BOLD='\033[1m'

def clear(): os.system('clear' if os.name!='nt' else 'cls')

def banner():
    clear()
    print(f"""{C.M}{C.BOLD}
  _____                                      
 |  __ \                                     
 | |__) |_ _ ___ ___ ______ __ _  ___ _ __   
 |  ___/ _` / __/ __|______/ _` |/ _ \ '_ \  
 | |  | (_| \__ \__ \     | (_| |  __/ | | | 
 |_|   \__,_|___/___/      \__, |\___|_| |_| 
                            __/ |            
                           |___/                                          {C.X}
{C.CY} 

 │  {C.M}PASSWORD GENERATOR v2{C.CY}  ·  {C.Y}Sachin Ser{C.CY}      
 │  {C.DIM}HackPath | Termux · Linux · Kali{C.CY}          
 │  {C.G}Strong · Custom · Passphrase · PIN · Bulk{C.CY}  
 {C.X}
""")

def sep(t=""):
    if t: print(f"\n{C.CY}{'═'*14} {C.Y}{t}{C.CY} {'═'*14}{C.X}")
    else: print(f"{C.DIM}{'─'*52}{C.X}")

def ok(m):    print(f"{C.G}[+] {m}{C.X}")
def err(m):   print(f"{C.R}[-] {m}{C.X}")
def inf(m):   print(f"{C.CY}[*] {m}{C.X}")
def res(k,v): print(f"  {C.Y}{k:<22}{C.X}: {C.W}{v}{C.X}")
def pause():  input(f"\n{C.DIM}Press Enter...{C.X}")
def inp(p):   return input(f"{C.M}  {p} > {C.X}").strip()

# ══════════════════════════════════════════
#   STRENGTH CHECKER
# ══════════════════════════════════════════
def check_strength(pwd):
    score = 0
    issues = []
    tips = []

    # Length
    if len(pwd) >= 16:   score += 3
    elif len(pwd) >= 12: score += 2
    elif len(pwd) >= 8:  score += 1
    else: issues.append("Too short (min 8)")

    # Uppercase
    if re.search(r'[A-Z]', pwd): score += 1
    else: tips.append("Add uppercase letters")

    # Lowercase
    if re.search(r'[a-z]', pwd): score += 1
    else: tips.append("Add lowercase letters")

    # Digits
    if re.search(r'\d', pwd): score += 1
    else: tips.append("Add numbers")

    # Special chars
    if re.search(r'[!@#$%^&*()_+\-=\[\]{}|;:,.<>?]', pwd):
        score += 2
    else: tips.append("Add special characters (!@#$%)")

    # No common patterns
    common = ['123','abc','qwe','password','pass','admin','letme']
    if any(c in pwd.lower() for c in common):
        score -= 2
        issues.append("Contains common pattern")

    # No repeated chars
    if re.search(r'(.)\1{2,}', pwd):
        score -= 1
        issues.append("Repeated characters detected")

    # Entropy
    charset = 0
    if re.search(r'[a-z]', pwd): charset += 26
    if re.search(r'[A-Z]', pwd): charset += 26
    if re.search(r'\d', pwd): charset += 10
    if re.search(r'[^a-zA-Z0-9]', pwd): charset += 32
    entropy = len(pwd) * math.log2(charset) if charset > 0 else 0

    # Crack time estimate
    guesses_per_sec = 1_000_000_000  # 1 billion/sec (GPU)
    combinations = charset ** len(pwd) if charset > 0 else 1
    seconds = combinations / guesses_per_sec

    if seconds < 60: crack_time = f"{seconds:.1f} seconds"
    elif seconds < 3600: crack_time = f"{seconds/60:.1f} minutes"
    elif seconds < 86400: crack_time = f"{seconds/3600:.1f} hours"
    elif seconds < 31536000: crack_time = f"{seconds/86400:.1f} days"
    elif seconds < 3153600000: crack_time = f"{seconds/31536000:.1f} years"
    else: crack_time = "Centuries+ 🛡️"

    # Rating
    if score >= 8:   rating,color = "VERY STRONG 🔒", C.G
    elif score >= 6: rating,color = "STRONG 💪", C.G
    elif score >= 4: rating,color = "MEDIUM ⚠️", C.Y
    elif score >= 2: rating,color = "WEAK 😟", C.Y
    else:            rating,color = "VERY WEAK 💀", C.R

    return {
        'score':score,'rating':rating,'color':color,
        'entropy':entropy,'crack_time':crack_time,
        'issues':issues,'tips':tips
    }

def show_strength(pwd):
    s = check_strength(pwd)
    sep("STRENGTH ANALYSIS")
    res("Password",     pwd)
    res("Length",       str(len(pwd)))
    res("Score",        f"{s['score']}/10")
    print(f"  {C.Y}{'Rating':<22}{C.X}: {s['color']}{s['rating']}{C.X}")
    res("Entropy",      f"{s['entropy']:.1f} bits")
    res("Crack time",   s['crack_time'])

    # Strength bar
    bar_len = min(s['score'], 10)
    bar = '█' * bar_len + '░' * (10-bar_len)
    color = C.G if s['score']>=7 else C.Y if s['score']>=4 else C.R
    print(f"\n  {color}[{bar}]{C.X} {s['score']}/10")

    if s['issues']:
        print(f"\n  {C.R}Issues:{C.X}")
        for i in s['issues']: print(f"    {C.R}✗ {i}{C.X}")
    if s['tips']:
        print(f"\n  {C.Y}Tips:{C.X}")
        for t in s['tips']: print(f"    {C.Y}→ {t}{C.X}")

# ══════════════════════════════════════════
#   1. STRONG PASSWORD GENERATOR
# ══════════════════════════════════════════
def strong_password():
    sep("STRONG PASSWORD GENERATOR")

    try:
        length = int(inp("Length [16]") or "16")
    except: length = 16

    print(f"\n  Include:")
    upper   = inp("Uppercase A-Z? [Y/n]").lower() != 'n'
    lower   = inp("Lowercase a-z? [Y/n]").lower() != 'n'
    digits  = inp("Numbers 0-9? [Y/n]").lower() != 'n'
    special = inp("Special !@#$%? [Y/n]").lower() != 'n'
    exclude = inp("Exclude chars (leave blank for none)") or ""

    charset = ''
    if upper:   charset += string.ascii_uppercase
    if lower:   charset += string.ascii_lowercase
    if digits:  charset += string.digits
    if special: charset += '!@#$%^&*()_+-=[]{}|;:,.<>?'

    # Remove excluded chars
    charset = ''.join(c for c in charset if c not in exclude)

    if not charset:
        err("No character set selected!"); pause(); return

    sep("GENERATED PASSWORDS")
    passwords = []
    for i in range(5):
        while True:
            pwd = ''.join(random.choice(charset) for _ in range(length))
            # Ensure at least one from each selected type
            valid = True
            if upper and not re.search(r'[A-Z]', pwd): valid = False
            if lower and not re.search(r'[a-z]', pwd): valid = False
            if digits and not re.search(r'\d', pwd): valid = False
            if special and not re.search(r'[^a-zA-Z0-9]', pwd): valid = False
            if valid: break

        s = check_strength(pwd)
        color = C.G if s['score']>=7 else C.Y
        print(f"  {color}{i+1}.{C.X} {C.W}{pwd}{C.X}  {color}[{s['rating'].split()[0]}]{C.X}")
        passwords.append(pwd)

    # Save option
    if inp("\nSave to file? [y/N]").lower() == 'y':
        fname = inp("Filename [passwords.txt]") or "passwords.txt"
        with open(fname,'w') as f:
            for p in passwords: f.write(p+'\n')
        ok(f"Saved to {fname}")

    # Show strength of first
    show_strength(passwords[0])
    pause()

# ══════════════════════════════════════════
#   2. CUSTOM PATTERN PASSWORD
# ══════════════════════════════════════════
def custom_pattern():
    sep("CUSTOM PATTERN PASSWORD")
    print(f"""
  {C.CY}Pattern symbols:{C.X}
  {C.Y}U{C.X} = Uppercase  {C.Y}L{C.X} = Lowercase
  {C.Y}D{C.X} = Digit      {C.Y}S{C.X} = Special
  {C.Y}A{C.X} = Any letter {C.Y}*{C.X} = Any char
  {C.Y}X{C.X} = Hex char   {C.Y}P{C.X} = Printable

  {C.DIM}Example: UUUDDDSSS → 3 upper + 3 digit + 3 special{C.X}
""")
    pattern = inp("Pattern")
    if not pattern: err("Empty!"); pause(); return

    count = int(inp("How many? [5]") or "5")

    sep("GENERATED")
    char_map = {
        'U': string.ascii_uppercase,
        'L': string.ascii_lowercase,
        'D': string.digits,
        'S': '!@#$%^&*()-_+=[]{}|;:,.<>?',
        'A': string.ascii_letters,
        '*': string.ascii_letters + string.digits + '!@#$%^&*()',
        'X': '0123456789abcdef',
        'P': string.printable.strip(),
    }

    for i in range(count):
        pwd = ''
        for ch in pattern:
            if ch.upper() in char_map:
                pwd += random.choice(char_map[ch.upper()])
            else:
                pwd += ch  # literal character
        print(f"  {C.G}{i+1}.{C.X} {C.W}{pwd}{C.X}")
    pause()

# ══════════════════════════════════════════
#   3. PASSPHRASE GENERATOR
# ══════════════════════════════════════════
def passphrase():
    sep("PASSPHRASE GENERATOR")

    # Word list
    words = [
        "apple","brave","cloud","dance","eagle","flame","grace","honor",
        "ivory","jade","karma","lunar","magic","noble","ocean","piano",
        "quest","radar","solar","tiger","ultra","vivid","winter","xenon",
        "yacht","zebra","alpha","blade","cyber","delta","echo","frost",
        "ghost","hero","iron","jewel","knight","laser","matrix","nova",
        "omega","pixel","quantum","realm","storm","thunder","unity","vault",
        "wave","xray","yellow","zero","attack","breach","cipher","defend",
        "exploit","firewall","guard","hash","inject","kernel","linux","malware",
        "network","packet","recon","secure","terminal","unix","vector","wireless",
        "kali","ninja","shadow","falcon","raven","wolf","phoenix","dragon",
        "cobra","viper","python","script","binary","crypto","hacker","stealth",
    ]

    try:
        word_count = int(inp("Number of words [4]") or "4")
        separator  = inp("Separator [-]") or "-"
        capitalize = inp("Capitalize words? [Y/n]").lower() != 'n'
        add_number = inp("Add number at end? [Y/n]").lower() != 'n'
        add_symbol = inp("Add symbol? [Y/n]").lower() != 'n'
    except: word_count=4; separator='-'; capitalize=True; add_number=True; add_symbol=True

    sep("GENERATED PASSPHRASES")
    for i in range(5):
        chosen = random.sample(words, min(word_count, len(words)))
        if capitalize:
            chosen = [w.capitalize() for w in chosen]
        phrase = separator.join(chosen)
        if add_number: phrase += separator + str(random.randint(10,999))
        if add_symbol: phrase += random.choice('!@#$%^&*')
        s = check_strength(phrase)
        print(f"  {C.G}{i+1}.{C.X} {C.W}{phrase}{C.X}  {C.DIM}[{s['crack_time']}]{C.X}")
    pause()

# ══════════════════════════════════════════
#   4. PIN / OTP GENERATOR
# ══════════════════════════════════════════
def pin_otp():
    sep("PIN / OTP GENERATOR")
    print(f"  {C.G}[1]{C.X} PIN (numeric)")
    print(f"  {C.G}[2]{C.X} OTP (alphanumeric)")
    print(f"  {C.G}[3]{C.X} Secure token (hex)")
    print(f"  {C.G}[4]{C.X} TOTP-style code")
    ch = inp("Choice")

    try: count = int(inp("How many? [5]") or "5")
    except: count = 5

    sep("GENERATED")
    if ch == '1':
        try: length = int(inp("PIN length [6]") or "6")
        except: length = 6
        for i in range(count):
            pin = ''.join(random.choice(string.digits) for _ in range(length))
            print(f"  {C.G}{i+1}.{C.X} {C.W}{pin}{C.X}")

    elif ch == '2':
        try: length = int(inp("OTP length [8]") or "8")
        except: length = 8
        charset = string.ascii_uppercase + string.digits
        for i in range(count):
            otp = ''.join(random.choice(charset) for _ in range(length))
            print(f"  {C.G}{i+1}.{C.X} {C.W}{otp}{C.X}")

    elif ch == '3':
        try: length = int(inp("Token length in bytes [16]") or "16")
        except: length = 16
        import os as _os
        for i in range(count):
            token = _os.urandom(length).hex()
            print(f"  {C.G}{i+1}.{C.X} {C.W}{token}{C.X}")

    elif ch == '4':
        import time
        # Simple TOTP-like (not real TOTP, just time-based)
        for i in range(count):
            seed = str(int(time.time()) + i * 30)
            code = hashlib.md5(seed.encode()).hexdigest()[:6].upper()
            print(f"  {C.G}{i+1}.{C.X} {C.W}{code}{C.X}  {C.DIM}(30s window){C.X}")
    pause()

# ══════════════════════════════════════════
#   5. BULK PASSWORD GENERATOR
# ══════════════════════════════════════════
def bulk_generate():
    sep("BULK PASSWORD GENERATOR")

    try:
        count  = int(inp("How many passwords? [100]") or "100")
        length = int(inp("Password length [12]") or "12")
    except: count=100; length=12

    print(f"\n  Type:")
    print(f"  {C.G}[1]{C.X} Strong (letters+digits+special)")
    print(f"  {C.G}[2]{C.X} Alphanumeric (letters+digits)")
    print(f"  {C.G}[3]{C.X} Numeric only")
    ptype = inp("Choice") or "1"

    fname = inp("Output file [bulk_passwords.txt]") or "bulk_passwords.txt"

    charsets = {
        '1': string.ascii_letters + string.digits + '!@#$%^&*()-_+=',
        '2': string.ascii_letters + string.digits,
        '3': string.digits,
    }
    charset = charsets.get(ptype, charsets['1'])

    inf(f"Generating {count:,} passwords...")

    passwords = []
    for _ in range(count):
        pwd = ''.join(random.choice(charset) for _ in range(length))
        passwords.append(pwd)

    with open(fname,'w') as f:
        for p in passwords: f.write(p+'\n')

    ok(f"Generated {count:,} passwords → {fname}")
    inf(f"Preview (first 5):")
    for p in passwords[:5]:
        print(f"  {C.W}{p}{C.X}")
    pause()

# ══════════════════════════════════════════
#   6. PASSWORD STRENGTH CHECKER
# ══════════════════════════════════════════
def strength_checker():
    sep("PASSWORD STRENGTH CHECKER")
    pwd = inp("Enter password to check")
    if not pwd: err("Empty!"); pause(); return
    show_strength(pwd)

    # Hash of password
    sep("PASSWORD HASHES")
    res("MD5",    hashlib.md5(pwd.encode()).hexdigest())
    res("SHA1",   hashlib.sha1(pwd.encode()).hexdigest())
    res("SHA256", hashlib.sha256(pwd.encode()).hexdigest())
    pause()

# ══════════════════════════════════════════
#   7. PASSWORD HISTORY / COMPARE
# ══════════════════════════════════════════
def compare_passwords():
    sep("COMPARE PASSWORDS")
    print(f"  Enter passwords to compare (empty line to stop):\n")
    passwords = []
    i = 1
    while True:
        p = inp(f"Password {i}")
        if not p: break
        passwords.append(p)
        i += 1

    if len(passwords) < 2:
        err("Need at least 2 passwords!"); pause(); return

    sep("COMPARISON")
    print(f"  {'#':<4} {'Password':<30} {'Score':<8} {'Rating':<20} {'Crack Time'}")
    print(f"  {C.DIM}{'─'*80}{C.X}")

    for i, pwd in enumerate(passwords):
        s = check_strength(pwd)
        color = s['color']
        display = pwd[:28]+'...' if len(pwd)>28 else pwd
        print(f"  {C.Y}{i+1:<4}{C.X} {C.W}{display:<30}{C.X} {color}{s['score']:<8}{C.X} {color}{s['rating']:<20}{C.X} {C.DIM}{s['crack_time']}{C.X}")

    # Winner
    best = max(passwords, key=lambda p: check_strength(p)['score'])
    sep()
    ok(f"Strongest: {C.W}{best}")
    pause()

# ══════════════════════════════════════════
#   8. PASSWORD TIPS
# ══════════════════════════════════════════
def password_tips():
    sep("PASSWORD SECURITY TIPS")
    tips = [
        (f"{C.G}DO ✅{C.X}", [
            "Use 16+ characters for strong passwords",
            "Mix uppercase, lowercase, numbers, symbols",
            "Use a unique password for each account",
            "Use passphrases (4+ random words)",
            "Enable 2FA/MFA on all accounts",
            "Use a password manager",
            "Change passwords if breach detected",
        ]),
        (f"{C.R}DON'T ❌{C.X}", [
            "Never use personal info (name, birthday)",
            "Don't reuse passwords across sites",
            "Never use common passwords (123456, password)",
            "Don't write passwords on paper",
            "Never share passwords over email/chat",
            "Don't use dictionary words alone",
            "Never use keyboard patterns (qwerty, asdf)",
        ]),
        (f"{C.Y}TOOLS 🔧{C.X}", [
            "Bitwarden — Free password manager",
            "KeePass — Offline password manager",
            "Have I Been Pwned — Check breaches",
            "2FAS — 2FA authenticator app",
        ]),
    ]
    for title, items in tips:
        print(f"\n  {title}")
        for item in items:
            print(f"    {C.DIM}•{C.X} {C.W}{item}{C.X}")
    print(f"\n  {C.DIM}by Sachin Ser | HackPath{C.X}")
    pause()

# ══════════════════════════════════════════
#   MAIN MENU
# ══════════════════════════════════════════
def main():
    while True:
        banner()
        print(f"""  {C.BOLD}MENU{C.X}

  {C.M}[1]{C.X}  Strong Password Generator
  {C.M}[2]{C.X}  Custom Pattern Password
  {C.M}[3]{C.X}  Passphrase Generator
  {C.M}[4]{C.X}  PIN / OTP Generator
  {C.M}[5]{C.X}  Bulk Password Generator
  {C.M}[6]{C.X}  Password Strength Checker
  {C.M}[7]{C.X}  Compare Passwords
  {C.M}[8]{C.X}  Password Security Tips 💡
  {C.R}[0]{C.X}  Exit

{C.DIM}  python3 passgen.py | HackPath v2{C.X}
""")
        ch = input(f"{C.M}HackPath PassGen > {C.X}").strip()

        menu = {
            '1':strong_password,'2':custom_pattern,
            '3':passphrase,'4':pin_otp,'5':bulk_generate,
            '6':strength_checker,'7':compare_passwords,'8':password_tips,
        }

        if ch in menu:
            menu[ch]()
        elif ch == '0':
            print(f"\n{C.M}HackPath PassGen v2 — Bye! 👋{C.X}\n")
            sys.exit(0)
        else:
            print(f"{C.R}Invalid!{C.X}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.M}Bye! 👋{C.X}\n")
        sys.exit(0)

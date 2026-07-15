# 🔐 HackPath Password Generator v2

> **8-in-1 Password toolkit for security professionals & everyday users**
> Created by **Sachin Ser** | HackPath

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)](https://python.org)
[![Version](https://img.shields.io/badge/Version-2.0-purple?style=flat-square)](https://github.com/sachin-null/hackpath-passgen)
[![Platform](https://img.shields.io/badge/Platform-Termux%20|%20Linux%20|%20Kali-orange?style=flat-square)](https://github.com/sachin-null)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![HackPath](https://img.shields.io/badge/HackPath-CEH%20v12-red?style=flat-square)](https://github.com/sachin-null/hackpath)

---

## ⚡ All 8 Tools

| # | Tool | Features |
|---|------|---------|
| 1 | 💪 **Strong Password** | Custom length · Charset control · 5 passwords · Save to file |
| 2 | 🎯 **Custom Pattern** | U/L/D/S/X/P symbols · Literal chars |
| 3 | 📝 **Passphrase** | 80+ words · Custom separator · Capitalize · Number/Symbol |
| 4 | 🔢 **PIN / OTP** | Numeric PIN · Alphanumeric OTP · Secure token · TOTP-style |
| 5 | 📦 **Bulk Generate** | 1-10,000+ passwords · 3 types · Save to file |
| 6 | 🔍 **Strength Checker** | Score/10 · Entropy · Crack time · Hash output · Visual bar |
| 7 | ⚖️ **Compare Passwords** | Side by side · Best password finder |
| 8 | 💡 **Security Tips** | Do's and Don'ts · Recommended tools |

---

## 📌 What's New in v2?

- Compare Passwords tool (NEW)
- Password Security Tips (NEW)
- Entropy calculation in strength checker
- GPU crack time estimate
- Visual strength bar `[████████░░] 8/10`
- Secure token + TOTP-style PIN
- 80+ word passphrase list
- Custom pattern with 8 symbols (U/L/D/S/A/X/P/*)
- Hash output (MD5/SHA1/SHA256)

---

## 📲 Install & Run

### Termux (Android)
```bash
pkg install python git -y
git clone https://github.com/sachin-null/hackpath-passgen
cd hackpath-passgen
python3 passgen.py
```

### Kali Linux / Linux
```bash
git clone https://github.com/sachin-null/hackpath-passgen
cd hackpath-passgen
python3 passgen.py
```

### One Line (Termux)
```bash
pkg install python git -y && git clone https://github.com/sachin-null/hackpath-passgen && cd hackpath-passgen && python3 passgen.py
```

---

## 🎯 Custom Pattern Guide

```
Pattern symbols:
  U = Uppercase (A-Z)
  L = Lowercase (a-z)
  D = Digit (0-9)
  S = Special (!@#$%...)
  A = Any letter (a-zA-Z)
  * = Any character
  X = Hex character (0-9a-f)
  P = Printable ASCII

Examples:
  UUUDDDSSS   -> 3 upper + 3 digit + 3 special
  ULLLDDSS    -> Mixed format
  XXXXXXXXXX  -> 10 hex chars (like a token)
```

---

## 🔍 Strength Checker Output

```
  STRENGTH ANALYSIS

  Password     : MyP@ssw0rd#2024
  Length       : 15
  Score        : 9/10
  Rating       : VERY STRONG
  Entropy      : 98.5 bits
  Crack time   : Centuries+

  [█████████░] 9/10
```

---

## 📦 Requirements

```
Python 3.x only
Zero extra packages needed
Works offline
Termux / Kali / Ubuntu / Windows
```

---

## 🔄 Changelog

### v2.0
- 8 tools (was 7)
- Compare Passwords
- Security Tips
- Entropy + crack time
- Visual strength bar
- 80+ passphrase words
- Hash output

### v1.0
- Initial release

---

## ⚠️ Disclaimer

> For educational and personal use only.
> Never use to crack others passwords.
> Use ethically and responsibly.

---

## 👤 Created by

**Sachin Ser** | [HackPath](https://github.com/sachin-null)

- GitHub: [@sachin-null](https://github.com/sachin-null)
- Instagram: [@sachin_ser](https://instagram.com/sachin_ser)

---

## 🔗 More HackPath Tools

| Tool | Repo |
|------|------|
| 🔓 CTF Helper | [hackpath-ctf-helper](https://github.com/sachin-null/hackpath-ctf-helper) |
| 📋 Wordlist Maker | [hackpath-wordlist-maker](https://github.com/sachin-null/hackpath-wordlist-maker) |
| 🌐 OSINT Tool | [hackpath-osint](https://github.com/sachin-null/hackpath-osint) |
| 📱 Phone Analyzer | [hackpath-phone-analyzer](https://github.com/sachin-null/hackpath-phone-analyzer) |

---

<div align="center">

**Star this repo if it helped you!**

`Made with love by Sachin Ser | HackPath`

</div>

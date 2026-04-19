# PDF Password Cracker

A Python-based tool to recover passwords from password-protected PDF files. This tool is designed for legitimate use cases such as recovering access to PDFs you own but have forgotten the password to.

## ⚠️ Legal Disclaimer

**IMPORTANT:** This tool is intended for legal and ethical use only. Use this tool only on PDF files that you own or have explicit permission to access. Unauthorized access to password-protected documents may be illegal in your jurisdiction.

**Legitimate use cases:**
- Recovering passwords for PDFs you purchased but lost the password
- Accessing your own encrypted documents where you've forgotten the password
- Security testing on your own files with permission

**DO NOT use this tool for:**
- Accessing documents you don't have permission to view
- Breaking into others' password-protected files
- Any illegal or unethical activities

By using this tool, you agree to use it responsibly and legally.

## 🚀 Features

- **Multiple Attack Methods:**
  - Common patterns attack (fast, tries typical passwords)
  - Dictionary attack (uses wordlist files)
  - Brute force attack (tries all combinations for specified length)

- **Progress Tracking:** Real-time feedback on attempts and speed
- **Automatic PDF Unlocking:** Save decrypted PDF without password protection
- **Flexible Configuration:** Customize character sets and password length for brute force

## 📋 Requirements

- Python 3.7+
- `pikepdf` library

## 🔧 Installation

### Option 1: Using Virtual Environment (Recommended)

```bash
# Clone the repository
git clone https://github.com/alphingj/pdf-password-cracker.git
cd pdf-password-cracker

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/Mac:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# Install dependencies
pip install pikepdf
```

### Option 2: System-wide Installation

```bash
# Clone the repository
git clone https://github.com/alphingj/pdf-password-cracker.git
cd pdf-password-cracker

# Install using pip
pip install pikepdf

# Or on Debian/Ubuntu/Kali Linux:
sudo apt install python3-pikepdf
```

## 💻 Usage

### Basic Usage

```bash
python crack.py
```

The tool will prompt you for:
1. Path to the password-protected PDF file
2. Attack method to use
3. Additional configuration based on the chosen method

### Attack Methods

#### 1. Common Patterns (Fastest)
Tries common passwords like "password", "123456", years (1900-2025), and simple sequences.

```
Select attack method: 1
```

**Best for:** Weak passwords, quick initial attempt

#### 2. Dictionary Attack
Uses a wordlist file containing potential passwords.

```
Select attack method: 2
Enter wordlist file path: /path/to/wordlist.txt
```

**Best for:** Passwords based on common words or phrases

**Popular wordlists:**
- [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) - 14 million passwords
- [SecLists](https://github.com/danielmiessler/SecLists/tree/master/Passwords) - Various password lists
- [10-million-password-list](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt)

#### 3. Brute Force (Slowest)
Tries all possible combinations for specified length and character set.

```
Select attack method: 3
Minimum password length: 1
Maximum password length: 4
Character set: 1 (lowercase + numbers)
```

**Best for:** Short, simple passwords (4-6 characters max)

**⚠️ Warning:** Brute force is extremely slow for longer passwords. An 8-character password with mixed case can take years to crack.

### Example Session

```bash
$ python crack.py
============================================================
PDF Password Cracker
============================================================

Enter PDF file path: /home/user/documents/locked.pdf

Select attack method:
1. Common patterns (fast)
2. Dictionary attack (requires wordlist)
3. Brute force (slow, limited length)

Enter choice (1-3): 1

[*] Trying common password patterns...
[*] Tried 100 patterns...
[*] Tried 200 patterns...

============================================================
[+] SUCCESS! Password found!
[+] Password: 12345678
[+] Attempts: 243
[+] Time elapsed: 0.87 seconds
============================================================

Save unlocked PDF? (y/n): y
Enter output file path: /home/user/documents/unlocked.pdf
[+] Unlocked PDF saved to: /home/user/documents/unlocked.pdf
```

## 📊 Performance Expectations

| Attack Method | Speed | Best For |
|--------------|-------|----------|
| Common Patterns | ~1000-5000/sec | Weak passwords |
| Dictionary | ~500-2000/sec | Word-based passwords |
| Brute Force (4 chars) | ~500-1000/sec | Very short passwords |
| Brute Force (6 chars) | ~500-1000/sec | May take hours |
| Brute Force (8+ chars) | ~500-1000/sec | Impractical (days/years) |

*Speed varies based on CPU performance and PDF encryption strength*

## 🛠️ Creating a Custom Wordlist

If you don't have a wordlist, create one:

```bash
# Simple wordlist
cat > wordlist.txt << EOF
password
123456
admin
welcome
letmein
qwerty
EOF

# Or generate based on patterns
echo "myname"{1900..2025} > custom_wordlist.txt
```

## 📁 Project Structure

```
pdf-password-cracker/
├── crack.py           # Main cracker script
├── README.md          # This file
├── LICENSE            # License file
└── requirements.txt   # Python dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 TODO

- [ ] Add GPU acceleration support
- [ ] Implement hybrid attack (dictionary + rules)
- [ ] Add resume capability for interrupted attacks
- [ ] Support for batch processing multiple PDFs
- [ ] GUI interface option
- [ ] More intelligent password generation patterns

## 🐛 Known Issues

- Very slow on PDFs with AES-256 encryption
- Memory usage can be high with large wordlists
- No multi-threading support (yet)

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with [pikepdf](https://github.com/pikepdf/pikepdf)
- Inspired by various password recovery tools
- Thanks to the open-source community

## 📧 Contact

Your Name - [@alphingj](https://github.com/alphingj)

Project Link: [https://github.com/alphingj/pdf-password-cracker](https://github.com/alphingj/pdf-password-cracker)

## ⚡ Quick Tips

1. **Always try common patterns first** - it's fast and often works
2. **Use good wordlists** - quality matters more than quantity
3. **Be patient with brute force** - it's exponentially slower as length increases
4. **Check your email** - the password might be in the purchase confirmation
5. **Contact the seller** - always easier than cracking

---

**Remember:** This tool is for recovering access to your own files. Always use responsibly and legally! 🔐

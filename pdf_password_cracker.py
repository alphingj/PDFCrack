import pikepdf
import itertools
import string
from pathlib import Path
import time

class PDFPasswordCracker:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.attempts = 0
        self.start_time = None
        
    def try_password(self, password):
        """Attempt to open PDF with given password"""
        self.attempts += 1
        try:
            with pikepdf.open(self.pdf_path, password=password):
                return True
        except pikepdf.PasswordError:
            return False
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def dictionary_attack(self, wordlist_path):
        """Try passwords from a wordlist file"""
        print(f"[*] Starting dictionary attack with {wordlist_path}")
        self.start_time = time.time()
        
        try:
            with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
                for line in f:
                    password = line.strip()
                    if not password:
                        continue
                    
                    if self.attempts % 1000 == 0:
                        elapsed = time.time() - self.start_time
                        rate = self.attempts / elapsed if elapsed > 0 else 0
                        print(f"[*] Tried {self.attempts} passwords ({rate:.0f} passwords/sec)")
                    
                    if self.try_password(password):
                        self._success(password)
                        return password
                        
            print("[!] Dictionary attack completed. Password not found.")
            return None
        except FileNotFoundError:
            print(f"[!] Wordlist file not found: {wordlist_path}")
            return None
    
    def brute_force(self, charset=None, min_length=1, max_length=4):
        """Brute force attack with given character set"""
        if charset is None:
            charset = string.ascii_lowercase + string.digits
        
        print(f"[*] Starting brute force attack")
        print(f"[*] Character set: {charset}")
        print(f"[*] Length range: {min_length}-{max_length}")
        self.start_time = time.time()
        
        for length in range(min_length, max_length + 1):
            print(f"[*] Trying passwords of length {length}...")
            total = len(charset) ** length
            print(f"[*] Total combinations for length {length}: {total:,}")
            
            for combo in itertools.product(charset, repeat=length):
                password = ''.join(combo)
                
                if self.attempts % 1000 == 0:
                    elapsed = time.time() - self.start_time
                    rate = self.attempts / elapsed if elapsed > 0 else 0
                    print(f"[*] Tried {self.attempts:,} passwords ({rate:.0f}/sec) - Current: {password}")
                
                if self.try_password(password):
                    self._success(password)
                    return password
        
        print("[!] Brute force attack completed. Password not found.")
        return None
    
    def common_patterns(self):
        """Try common password patterns"""
        print("[*] Trying common password patterns...")
        self.start_time = time.time()
        
        patterns = [
            # Empty password
            "",
            # Common passwords
            "password", "123456", "12345678", "password123", "admin",
            "letmein", "welcome", "monkey", "dragon", "master",
            "qwerty", "abc123", "111111", "123123",
            # Years
            *[str(year) for year in range(1900, 2026)],
            # Simple number sequences
            *[str(i) * 4 for i in range(10)],
            *[str(i).zfill(4) for i in range(10000)],
        ]
        
        for password in patterns:
            if self.attempts % 100 == 0:
                print(f"[*] Tried {self.attempts} patterns...")
            
            if self.try_password(password):
                self._success(password)
                return password
        
        print("[!] Common patterns exhausted. Password not found.")
        return None
    
    def _success(self, password):
        """Print success message and stats"""
        elapsed = time.time() - self.start_time
        print("\n" + "="*60)
        print("[+] SUCCESS! Password found!")
        print(f"[+] Password: {password}")
        print(f"[+] Attempts: {self.attempts:,}")
        print(f"[+] Time elapsed: {elapsed:.2f} seconds")
        print("="*60)
    
    def unlock_and_save(self, password, output_path):
        """Unlock PDF and save without password"""
        try:
            with pikepdf.open(self.pdf_path, password=password) as pdf:
                pdf.save(output_path)
                print(f"[+] Unlocked PDF saved to: {output_path}")
                return True
        except Exception as e:
            print(f"[!] Error saving unlocked PDF: {e}")
            return False


def main():
    print("="*60)
    print("PDF Password Cracker")
    print("="*60)
    print()
    
    # Configuration
    pdf_path = input("Enter PDF file path: ").strip()
    
    if not Path(pdf_path).exists():
        print("[!] PDF file not found!")
        return
    
    cracker = PDFPasswordCracker(pdf_path)
    
    print("\nSelect attack method:")
    print("1. Common patterns (fast)")
    print("2. Dictionary attack (requires wordlist)")
    print("3. Brute force (slow, limited length)")
    
    choice = input("\nEnter choice (1-3): ").strip()
    
    password = None
    
    if choice == "1":
        password = cracker.common_patterns()
    
    elif choice == "2":
        wordlist = input("Enter wordlist file path: ").strip()
        password = cracker.dictionary_attack(wordlist)
    
    elif choice == "3":
        print("\nBrute force configuration:")
        min_len = int(input("Minimum password length (1): ") or "1")
        max_len = int(input("Maximum password length (4): ") or "4")
        
        print("\nCharacter set:")
        print("1. Lowercase letters + numbers (a-z, 0-9)")
        print("2. All lowercase + uppercase + numbers")
        print("3. All printable characters")
        
        charset_choice = input("Enter choice (1-3): ").strip()
        
        if charset_choice == "2":
            charset = string.ascii_letters + string.digits
        elif charset_choice == "3":
            charset = string.printable.strip()
        else:
            charset = string.ascii_lowercase + string.digits
        
        password = cracker.brute_force(charset, min_len, max_len)
    
    else:
        print("[!] Invalid choice")
        return
    
    # If password found, offer to save unlocked PDF
    if password is not None:
        save = input("\nSave unlocked PDF? (y/n): ").strip().lower()
        if save == 'y':
            output_path = input("Enter output file path: ").strip()
            cracker.unlock_and_save(password, output_path)
    else:
        print("\n[!] Password not found. Consider:")
        print("    - Using a better wordlist")
        print("    - Trying longer brute force length (WARNING: very slow)")
        print("    - Contacting the PDF seller for the password")


if __name__ == "__main__":
    main()

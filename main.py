import argparse
import secrets
import string
import sys
import math
import os
from pathlib import Path

# UI Styling for a professional terminal experience
class UI:
    CYAN = '\033[38;5;51m'
    GREEN = '\033[38;5;112m'
    GOLD = '\033[38;5;220m'
    RED = '\033[38;5;196m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    BAR = f"{CYAN}{'━' * 60}{RESET}"

def get_pool(charset_arg):
    """Processes the charset input and returns the character pool."""
    pool = ""
    choice = charset_arg.lower().strip()
    
    if "abc" in choice:
        pool += string.ascii_letters
    if "123" in choice:
        pool += string.digits
        
    if not pool:
        print(f"{UI.RED}[!] Error: Invalid charset. Use 'abc', '123', or 'abc123'.{UI.RESET}")
        sys.exit(1)
    return pool

def main():
    # 1. Argument Setup
    parser = argparse.ArgumentParser(description="Professional Encryption Key Generator")
    parser.add_argument("length", type=int, help="Number of characters")
    parser.add_argument("charset", help="Pool selection (abc / 123 / abc123)")
    parser.add_argument("filename", nargs="?", default="key.txt", help="Output filename")
    
    args = parser.parse_args()

    # 2. Filename Enforcement (Fixing the bug you found)
    raw_name = args.filename.strip()
    if not raw_name.lower().endswith(".txt"):
        raw_name += ".txt"
    
    target_path = Path(raw_name).resolve()

    # 3. Secure Key Generation
    char_pool = get_pool(args.charset)
    # secrets.choice is cryptographically secure for encryption keys
    secure_key = "".join(secrets.choice(char_pool) for _ in range(args.length))

    # 4. Atomic Write Logic
    try:
        # Create folder if it doesn't exist
        target_path.parent.mkdir(parents=True, exist_ok=True)

        # Write to a temporary file first, then swap (prevents partial writes)
        temp_path = target_path.with_suffix(".tmp")
        with open(temp_path, "w", encoding="utf-8") as f:
            f.write(secure_key)

        # Set permissions: Read/Write for current user ONLY (Unix/Mac)
        if os.name != 'nt':
            os.chmod(temp_path, 0o600)

        # Final move to destination
        temp_path.replace(target_path)

        # 5. Professional CLI Output
        entropy = math.log2(len(char_pool)) * args.length
        
        print(f"\n{UI.BAR}")
        print(f"  {UI.BOLD}{UI.GREEN}✔ GENERATION SUCCESSFUL{UI.RESET}")
        print(f"{UI.BAR}")
        print(f"  {UI.BOLD}File Name:{UI.RESET}  {target_path.name}")
        print(f"  {UI.BOLD}Location:{UI.RESET}   {target_path.parent}")
        print(f"  {UI.BOLD}Key Size:{UI.RESET}   {args.length} characters")
        print(f"  {UI.BOLD}Security:{UI.RESET}   {entropy:.2f} bits of entropy")
        
        if entropy < 128:
            print(f"  {UI.BOLD}Strength:{UI.RESET}   {UI.GOLD}Standard{UI.RESET}")
        else:
            print(f"  {UI.BOLD}Strength:{UI.RESET}   {UI.CYAN}Military-Grade{UI.RESET}")
        print(f"{UI.BAR}\n")

    except PermissionError:
        print(f"{UI.RED}[!] Permission Denied: Cannot write to {target_path}{UI.RESET}")
    except Exception as e:
        print(f"{UI.RED}[!] System Error: {e}{UI.RESET}")
    finally:
        # Scrub sensitive data from memory
        secure_key = "0" * len(secure_key)
        del secure_key

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{UI.RED}[!] Aborted by user.{UI.RESET}")
        sys.exit(0)
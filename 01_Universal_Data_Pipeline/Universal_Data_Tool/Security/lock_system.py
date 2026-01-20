"""
SECURITY SYSTEM: LOCK & KEY
"""
import os
import sys

# TARGET: The file we want to protect (up one level, then into Core_Original)
TARGET_FILE = "../Core_Original/universal_loader.py" 
KEY_FILE = "vault.key"

def install_and_import():
    try:
        from cryptography.fernet import Fernet
        return Fernet
    except ImportError:
        print("Installing security pack...")
        os.system(f"{sys.executable} -m pip install cryptography")
        from cryptography.fernet import Fernet
        return Fernet

def toggle_lock():
    Fernet = install_and_import()
    
    # Locate the target file relative to this script
    current_folder = os.path.dirname(os.path.abspath(__file__))
    target_path = os.path.join(current_folder, TARGET_FILE)
    
    # Key Management
    key_path = os.path.join(current_folder, KEY_FILE)
    
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as kf: kf.write(key)
        print("NEW KEY GENERATED.")
    else:
        with open(key_path, "rb") as kf: key = kf.read()
    
    fernet = Fernet(key)

    if not os.path.exists(target_path):
        print(f"ERROR: Could not find target file at:\n{target_path}")
        return

    with open(target_path, "rb") as f: data = f.read()
    
    try:
        # Try to Decrypt
        newdata = fernet.decrypt(data)
        print("SUCCESS: UNLOCKED (Readable)")
    except:
        # If that fails, Encrypt
        newdata = fernet.encrypt(data)
        print("SUCCESS: LOCKED (Encrypted)")
        
    with open(target_path, "wb") as f: f.write(newdata)

if __name__ == "__main__":
    toggle_lock()

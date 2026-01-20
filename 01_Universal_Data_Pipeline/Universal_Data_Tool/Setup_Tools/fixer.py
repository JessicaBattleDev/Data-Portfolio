import os

# 1. Define the exact path to your Desktop
# This finds your specific user folder automatically
desktop = os.path.join(os.path.expanduser("~"), "Desktop")
project_path = os.path.join(desktop, "Universal_Data_Tool")
security_path = os.path.join(project_path, "Security")
file_path = os.path.join(security_path, "lock_system.py")

# 2. Force Create the Folders (If they are missing, make them)
if not os.path.exists(security_path):
    os.makedirs(security_path)
    print(f"FIXED: Created missing folder -> {security_path}")

# 3. Write the Security Code directly to the file
code_content = r'''"""
SECURITY SYSTEM: LOCK & KEY
"""
import os
import sys

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
    # Key Logic
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as kf: kf.write(key)
    else:
        with open(KEY_FILE, "rb") as kf: key = kf.read()
    
    fernet = Fernet(key)
    target = os.path.join(os.path.dirname(__file__), TARGET_FILE)
    
    if not os.path.exists(target):
        print(f"Error: Cannot find {target}")
        return

    with open(target, "rb") as f: data = f.read()
    
    try:
        # Decrypt
        newdata = fernet.decrypt(data)
        print("SUCCESS: UNLOCKED (Readable)")
    except:
        # Encrypt
        newdata = fernet.encrypt(data)
        print("SUCCESS: LOCKED (Encrypted)")
        
    with open(target, "wb") as f: f.write(newdata)

if __name__ == "__main__":
    toggle_lock()
'''

with open(file_path, "w") as f:
    f.write(code_content)

print(f"\nSUCCESS! The file 'lock_system.py' has been created here:\n{file_path}")
print("You can now go to that folder and run it.")

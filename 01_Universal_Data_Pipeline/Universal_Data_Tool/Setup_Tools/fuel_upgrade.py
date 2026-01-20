import sys
import subprocess

def upgrade_fuel():
    print("--- UPGRADING ENGINE ---")
    # pyarrow is the driver needed for Parquet files
    packages = ["pyarrow"]
    
    for package in packages:
        print(f"Installing {package}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            print(f"  [+] {package} installed!")
        except:
            print(f"  [-] Failed to install {package}")
            
    print("\n--- UPGRADE COMPLETE ---")

if __name__ == "__main__":
    upgrade_fuel()

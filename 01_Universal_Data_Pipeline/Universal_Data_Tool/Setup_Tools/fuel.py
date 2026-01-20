import sys
import subprocess

def fill_gas_tank():
    print("--- INSTALLING ENGINE FUEL (LIBRARIES) ---")
    # These are the tools your Gold Code needs to run
    required_tools = ["pandas", "openpyxl"]
    
    for tool in required_tools:
        print(f"Installing {tool}...")
        try:
            # Force install the package
            subprocess.check_call([sys.executable, "-m", "pip", "install", tool])
            print(f"  [+] {tool} is READY.")
        except:
            print(f"  [-] Error installing {tool}.")
            
    print("\n--- SYSTEM FULLY OPERATIONAL ---")
    print("You can now unlock and run your code anytime.")

if __name__ == "__main__":
    fill_gas_tank()

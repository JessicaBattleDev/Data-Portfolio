import sys
import subprocess

def install_viz_tools():
    print("--- INSTALLING ARTIST TOOLS ---")
    tools = ["matplotlib", "seaborn"] # The standard plotting libraries
    
    for tool in tools:
        print(f"Installing {tool}...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", tool])
            print(f"  [+] {tool} installed.")
        except:
            print(f"  [-] Failed to install {tool}")
            
    print("\n--- READY TO PAINT ---")

if __name__ == "__main__":
    install_viz_tools()

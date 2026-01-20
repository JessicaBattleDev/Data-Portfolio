"""
PROJECT: BELLABEAT REFURBISHED
TASK: Step 1 - Data Inspection
"""
import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FOLDER = "Input"
# We try to load the file you copied over
FILE_NAME = "BBdaily_activity_03-05.16.xlsx" 

def inspect_data():
    # 1. Construct the path to the file
    # (Goes from 'Scripts' folder -> Up one level -> 'Input' folder)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", INPUT_FOLDER, FILE_NAME)
    
    print(f"--- INSPECTING: {FILE_NAME} ---")
    
    try:
        # 2. Load Data
        df = pd.read_excel(file_path)
        
        # 3. Print Vitals
        print(f"\n[+] SUCCESS: File Loaded!")
        print(f"    Total Rows:    {df.shape[0]}")
        print(f"    Total Columns: {df.shape[1]}")
        
        print("\n[+] COLUMN NAMES:")
        print(list(df.columns))
        
        print("\n[+] FIRST 3 ROWS:")
        print(df.head(3))
        
    except FileNotFoundError:
        print(f"\n[-] ERROR: Could not find the file.")
        print(f"    I looked here: {file_path}")
        print("    CHECK: Did you name the file exactly 'BBdaily_activity_03-05.16'?")
    except Exception as e:
        print(f"\n[-] ERROR: Something else went wrong.\n    {e}")

if __name__ == "__main__":
    inspect_data()

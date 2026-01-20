"""
PROJECT: BELLABEAT REFURBISHED
TASK: Step 2 - Data Cleaning & Transformation
"""
import pandas as pd
import os

# --- CONFIGURATION ---
INPUT_FOLDER = "Input"
OUTPUT_FOLDER = "Output"
FILE_NAME = "BBdaily_activity_03-05.16.xlsx" 

def clean_data():
    # 1. Setup Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, "..", INPUT_FOLDER, FILE_NAME)
    output_path = os.path.join(base_dir, "..", OUTPUT_FOLDER, "Clean_Bellabeat_Data.csv")
    
    print("--- STARTING CLEANING PROCESS ---")
    
    # 2. Load Data
    try:
        df = pd.read_excel(input_path)
        print(f"[1] Data Loaded. Raw Shape: {df.shape}")
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")
        return

    # 3. Standardize Column Names (Lowercase & Snake_case)
    # This fixes "ActivityDate" becoming "activity_date"
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    print("[2] Columns normalized (lowercase).")

    # 4. Fix Date Formats
    # We look for a column that has 'date' in the name
    date_col = None
    for col in df.columns:
        if 'date' in col:
            date_col = col
            break
            
    if date_col:
        print(f"[3] Found Date Column: '{date_col}'")
        df[date_col] = pd.to_datetime(df[date_col])
        
        # FEATURE ENGINEERING: Add 'day_of_week'
        df['day_of_week'] = df[date_col].dt.day_name()
        print(f"    -> Added new column: 'day_of_week'")
    else:
        print("[!] WARNING: No date column found. Skipping date steps.")

    # 5. Remove Duplicates
    before_dedup = len(df)
    df = df.drop_duplicates()
    after_dedup = len(df)
    print(f"[4] Removed {before_dedup - after_dedup} duplicate rows.")

    # 6. Save to Output
    # Ensure Output folder exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    df.to_csv(output_path, index=False)
    print(f"\n[+] SUCCESS: Clean data saved to:")
    print(f"    {output_path}")

if __name__ == "__main__":
    clean_data()

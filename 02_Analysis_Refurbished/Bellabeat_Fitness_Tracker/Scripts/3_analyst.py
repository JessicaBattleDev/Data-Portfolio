"""
PROJECT: BELLABEAT REFURBISHED
TASK: Step 3 - Analysis & Visualization (FIXED)
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CONFIGURATION ---
OUTPUT_FOLDER = "Output"
CLEAN_FILE = "Clean_Bellabeat_Data.csv"

def run_analysis():
    # 1. Setup Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", OUTPUT_FOLDER, CLEAN_FILE)
    chart_path = os.path.join(base_dir, "..", OUTPUT_FOLDER, "Activity_Correlation_Chart.png")
    
    print("--- STARTING ANALYSIS ---")
    
    # 2. Load the Clean Data
    try:
        df = pd.read_csv(data_path)
        print(f"[1] Loaded Clean Data: {len(df)} rows")
    except FileNotFoundError:
        print("ERROR: Run Step 2 (Cleaner) first!")
        return

    # 3. Generate Summary Stats
    # FIX: We changed 'totalsteps' to 'total_steps' to match your data
    avg_steps = df['total_steps'].mean()
    avg_cals = df['calories'].mean()
    
    print(f"\n[2] QUICK INSIGHTS:")
    print(f"    Average Daily Steps:    {int(avg_steps):,}")
    print(f"    Average Calories Burned: {int(avg_cals):,}")
    
    # 4. Create Visualization (Scatter Plot)
    print("\n[3] Generating Chart...")
    
    plt.figure(figsize=(10, 6))
    # FIX: Updated column name here too
    sns.scatterplot(data=df, x='total_steps', y='calories', alpha=0.6, color='teal')
    
    # Add titles and labels
    plt.title('Impact of Daily Steps on Calories Burned', fontsize=14)
    plt.xlabel('Total Steps', fontsize=12)
    plt.ylabel('Calories Burned', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # 5. Save the Chart
    plt.savefig(chart_path)
    print(f"[+] Chart saved to: {chart_path}")
    print("    (Go check the Output folder!)")

if __name__ == "__main__":
    run_analysis()

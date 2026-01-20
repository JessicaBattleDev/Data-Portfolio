import os

# CONFIGURATION
PROJECT_NAME = "Universal_Data_Tool"
FOLDERS = ["Core_Original", "Rebuild_Zone", "Output", "Quarantine", "Logs"]

# BUILD LOGIC
def create_structure():
    print(f"--- BUILDING PROJECT: {PROJECT_NAME} ---")
    
    # 1. Create Main Folder
    if not os.path.exists(PROJECT_NAME):
        os.makedirs(PROJECT_NAME)
        print(f"CREATED Main Folder: {PROJECT_NAME}/")
    else:
        print(f"Main Folder '{PROJECT_NAME}' already exists.")
    
    # 2. Create Sub-Folders
    for folder in FOLDERS:
        path = os.path.join(PROJECT_NAME, folder)
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"  + Sub-folder Created: {folder}/")
        else:
            print(f"  (i) Sub-folder Exists: {folder}/")

    # 3. Create requirements.txt
    req_path = os.path.join(PROJECT_NAME, "requirements.txt")
    if not os.path.exists(req_path):
        with open(req_path, "w") as f:
            f.write("pandas\nopenpyxl\ncryptography\n")
        print("  + File Created: requirements.txt")

    print("\nSUCCESS! Look for the folder 'Universal_Data_Tool' on your Desktop.")

if __name__ == "__main__":
    create_structure()

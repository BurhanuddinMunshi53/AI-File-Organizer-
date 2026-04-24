import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".bmp", ".svg", ".raw", ".cr2", ".nef", ".arw", ".dng", ".tiff", ".psd", ".ai", ".eps", ".avif", ".jif", ".jfif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".epub", ".md", ".rtf", ".odt", ".pages", ".numbers", ".key", ".tex", ".wpd"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv", ".wmv", ".m4v", ".3gp", ".mpg", ".mpeg", ".vob", ".ogv", ".ts", ".m2ts", ".rmvb"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".opus", ".amr", ".mid", ".midi", ".wma", ".aiff", ".m4b", ".m4p", ".mka"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso", ".dmg", ".pkg", ".deb", ".rpm", ".xz", ".bz2", ".cbz", ".cbr", ".wim"],
    "Apps_Code": [".apk", ".exe", ".msi", ".py", ".js", ".html", ".json", ".css", ".cpp", ".c", ".h", ".java", ".sh", ".bat", ".php", ".rb", ".go", ".rs", ".swift", ".ts", ".kt", ".dart", ".lua", ".pl"],
    "Data_Scientific": [".sql", ".db", ".sqlite", ".xml", ".jsonl", ".parquet", ".avro", ".dat", ".sav", ".hdf5", ".mat", ".cdf", ".nc"],
    "Design_3D": [".dwg", ".dxf", ".obj", ".stl", ".blend", ".3ds", ".c4d", ".ma", ".mb", ".fig", ".xd", ".skp", ".step", ".iges"],
    "Game_Assets": [".unitypackage", ".uasset", ".umap", ".tga", ".dds", ".pck", ".pak", ".assets"],
    "Virtual_Machines": [".vmdk", ".vdi", ".ova", ".ovf", ".vhd", ".vhdx", ".qcow2"],
    "Fonts": [".ttf", ".otf", ".woff", ".woff2", ".eot"],
    "System_Config": [".log", ".bak", ".tmp", ".ini", ".conf", ".yaml", ".yml", ".env", ".toml", ".prop", ".properties", ".plist", ".reg"]
}

C_MAIN = "\033[96m"  # Cyan
C_SUCC = "\033[92m"  # Green
C_WARN = "\033[93m"  # Yellow
C_DANG = "\033[91m"  # Red
BOLD, RESET = "\033[1m", "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_base():
    return "/sdcard" if os.path.exists("/sdcard") else os.path.expanduser("~")

def targeted_delete(path):
    """Specific file browser and deletion logic."""
    while True:
        clear()
        try:
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
        except Exception as e:
            print(f"{C_DANG}Access Error: {e}{RESET}")
            input("Press Enter...")
            break

        print(f"{C_DANG}{BOLD}--- TARGETED DELETION ---{RESET}")
        print(f"Path: {path}\n")
        
        if not files:
            print(f"{C_WARN}Directory is empty.{RESET}")
            input("\nPress Enter to return...")
            break

       
        for i, f in enumerate(files, 1):
            print(f" {i:03d} | {f}")
        
        print(f"\n{BOLD}[#] Delete File | [A] Delete ALL | [0] Back{RESET}")
        choice = input(f"{C_MAIN}Selection: {RESET}").strip().upper()

        if choice == '0': break
        elif choice == 'A':
            confirm = input(f"{C_DANG}Wipe all {len(files)} files? (y/n): {RESET}").lower()
            if confirm == 'y':
                for f in files: 
                    try: os.remove(os.path.join(path, f))
                    except: pass
                print(f"{C_SUCC}Purge complete.{RESET}")
                input("...")
                break
        elif choice.isdigit() and 0 < int(choice) <= len(files):
            target = files[int(choice)-1]
            try:
                os.remove(os.path.join(path, target))
                print(f"{C_SUCC}Deleted: {target}{RESET}")
            except Exception as e:
                print(f"{C_DANG}Error: {e}{RESET}")
                input("...")
        else:
            print(f"{C_DANG}Invalid entry.{RESET}")

def folder_operations(target_path):
    """Sub-menu for a specific folder."""
    while True:
        clear()
        name = os.path.basename(target_path)
        print(f"{C_MAIN}{BOLD}╔" + "═"*44 + "╗")
        print(f"║ {name[:42]:^42} ║")
        print(f"╚" + "═"*44 + "╝{RESET}")
        print(f"[{C_SUCC}1{RESET}] ORGANIZE (Sort by {len(FILE_TYPES)} categories)")
        print(f"[{C_DANG}2{RESET}] DELETE (Specific Selection)")
        print(f"[0] BACK")
        
        cmd = input(f"\n{BOLD}Action: {RESET}")
        if cmd == '1':
            moved = 0
            for filename in os.listdir(target_path):
                file_path = os.path.join(target_path, filename)
                if os.path.isfile(file_path):
                    ext = os.path.splitext(filename)[1].lower()
                    for folder, extensions in FILE_TYPES.items():
                        if ext in extensions:
                            dest = os.path.join(target_path, folder)
                            os.makedirs(dest, exist_ok=True)
                            shutil.move(file_path, os.path.join(dest, filename))
                            moved += 1
            print(f"\n{C_SUCC}Complete: {moved} files sorted into system-optimized categories.{RESET}")
            input("Press Enter...")
        elif cmd == '2': targeted_delete(target_path)
        elif cmd == '0': break

def main():
    root = get_base()
    while True:
        clear()
        print(f"{C_MAIN}{BOLD}Aether Engine v6.0 {RESET}")
        print(f"Directory: {root}")
        print("─" * 46)
        print("1. Scan Entire System")
        print("2. Search Via Name ")
        print("Q. Quit")
        
        choice = input(f"\n{BOLD}Command: {RESET}").lower()
        if choice == 'q':
            print("Shutting Down...Have a clean digital desk") 
            break

        if choice == '1':
            print(f"{C_WARN}Indexing storage...{RESET}")
            found = {}
            for r, d, _ in os.walk(root):
                for folder in d:
                    if not folder.startswith('.'):
                        found[folder.lower()] = os.path.join(r, folder)
            
            clear()
            print(f"{C_MAIN}{BOLD}--- STORAGE FOLDER MAP ---{RESET}")
            # Sorted Vertical List
            for name in sorted(found.keys()):
                print(f"  • {name}")
            
            print(f"\n{BOLD}Indexed: {len(found)} Folders{RESET}")
            name_input = input(f"\n{BOLD}Select Folder Name: {RESET}").lower().strip()
            if name_input in found: folder_operations(found[name_input])
            else: input(f"{C_DANG}Target not found. Enter to return...{RESET}")

        elif choice == '2':
            query = input(f"{BOLD}Search Target: {RESET}").lower().strip()
            matches = []
            print(f"{C_WARN}Searching for '{query}'...{RESET}")
            for r, d, _ in os.walk(root):
                if query in [f.lower() for f in d]:
                    matches.append(os.path.join(r, query))
            
            if not matches:
                input(f"{C_DANG}No match found for '{query}'.{RESET}")
            elif len(matches) == 1:
                folder_operations(matches[0])
            else:
                clear()
                print(f"{C_MAIN}Multiple paths detected for '{query}':{RESET}")
                for i, p in enumerate(matches, 1): print(f"{i}. {p}")
                idx = input("\nSelect Index: ")
                if idx.isdigit() and 0 < int(idx) <= len(matches):
                    folder_operations(matches[int(idx)-1])

if __name__ == "__main__":
    main()

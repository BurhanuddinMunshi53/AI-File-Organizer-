import os
import shutil
import time
import sys
import random
import zipfile
import hashlib
import platform
from datetime import datetime

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".heic", ".bmp", ".svg", ".raw", ".cr2", ".nef", ".arw", ".dng", ".tiff", ".psd", ".ai", ".eps", ".avif", ".jif", ".jfif", ".ico"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".xls", ".pptx", ".ppt", ".csv", ".epub", ".md", ".rtf", ".odt", ".pages", ".numbers", ".key", ".tex", ".wpd"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".webm", ".flv", ".wmv", ".m4v", ".3gp", ".mpg", ".mpeg", ".vob", ".ogv", ".ts", ".m2ts", ".rmvb"],
    "Audio": [".mp3", ".wav", ".flac", ".m4a", ".aac", ".ogg", ".opus", ".amr", ".mid", ".midi", ".wma", ".aiff", ".m4b", ".m4p", ".mka"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso", ".dmg", ".pkg", ".deb", ".rpm", ".xz", ".bz2", ".cbz", ".cbr", ".wim"],
    "Dev Stack": [".apk", ".exe", ".msi", ".py", ".js", ".html", ".json", ".css", ".cpp", ".c", ".h", ".java", ".sh", ".bat", ".php", ".rb", ".go", ".rs", ".swift", ".ts", ".kt", ".dart", ".lua", ".pl"],
    "AI Neural": [".onnx", ".tflite", ".pb", ".h5", ".pth", ".weights", ".gguf", ".ckpt", ".safetensors", ".bin", ".model"],
    "Data Sci": [".sql", ".db", ".sqlite", ".xml", ".jsonl", ".parquet", ".avro", ".dat", ".sav", ".hdf5", ".mat", ".cdf", ".nc"],
    "Design CAD": [".dwg", ".dxf", ".obj", ".stl", ".blend", ".3ds", ".c4d", ".ma", ".mb", ".fig", ".xd", ".skp", ".step", ".iges"],
    "Game Dev": [".unitypackage", ".uasset", ".umap", ".tga", ".dds", ".pck", ".pak", ".assets", ".bundle"],
    "VM Cloud": [".vmdk", ".vdi", ".ova", ".ovf", ".vhd", ".vhdx", ".qcow2"],
    "Sys Config": [".log", ".bak", ".tmp", ".ini", ".conf", ".env", ".toml", ".prop", ".properties", ".plist", ".reg"]
}

C_CYAN = "\033[38;5;51m"
C_GREY = "\033[38;5;244m"
C_BOLD = "\033[1m"
C_RESET = "\033[0m"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def neural_anim(label="SYSTEM LOADING"):
    for _ in range(3):
        for opac in [C_GREY, C_CYAN, C_BOLD + C_CYAN]:
            sys.stdout.write(f"\r {opac}◈ {label}...{C_RESET}")
            sys.stdout.flush()
            time.sleep(0.06)
    print()

def jarvis_type(text, color=C_CYAN, speed=0.005):
    for char in text:
        sys.stdout.write(f"{color}{char}{C_RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def progress_tactical(label, total=100, speed=0.006):
    for i in range(total + 1):
        bar = "█" * (i // 4) + "░" * (25 - (i // 4))
        sys.stdout.write(f"\r {C_CYAN}{label:<20} {C_GREY}▕{C_CYAN}{bar}{C_GREY}▏ {i}%{C_RESET}")
        sys.stdout.flush()
        time.sleep(speed)
    print()

def draw_prime_hud():
    clear()
    t = datetime.now().strftime("%H:%M:%S")
    print(f"{C_CYAN}┏" + "━"*72 + "┓")
    print(f"┃ {C_BOLD}AETHER OS v19.0{C_RESET}{C_CYAN}               {t} ┃")
    print(f"┣" + "━"*72 + "┫")
    print(f"┃ {C_GREY}UI: {C_CYAN}SENTINEL {C_GREY}| CORE: {C_CYAN}JARVIS HYPERION {C_GREY}| SECURITY: {C_CYAN}ULTRA-PURE{C_CYAN}    ┃")
    print(f"┗" + "━"*72 + f"┛{C_RESET}")

def sector_select(root):
    draw_prime_hud()
    nodes = {item.lower(): os.path.join(root, item) for item in os.listdir(root) if os.path.isdir(os.path.join(root, item))}
    print(f" {C_CYAN}DETECTED DATA SECTORS:{C_RESET}")
    keys = sorted(nodes.keys())
    for i in range(0, len(keys), 2):
        row = keys[i:i+2]
        display = "".join([f" {C_CYAN}◆ {C_GREY}{k[:30].replace('_', ' '):<32}{C_RESET}" for k in row])
        print(display)
    target = input(f"\n {C_CYAN}ENGAGE SECTOR NAME>> {C_RESET}").lower().strip().replace(" ", "_")
    return nodes.get(target)

def op_scan_entire_system(root):
    draw_prime_hud()
    progress_tactical("MAPPING MAIN SECTORS", 100, 0.01)
    print(f"\n {C_CYAN}MAIN SYSTEM FOLDERS DETECTED:{C_RESET}")
    main_folders = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
    for i in range(0, len(main_folders), 2):
        row = main_folders[i:i+2]
        display = "".join([f" {C_GREY}▚ {C_CYAN}{f[:30].replace('_', ' '):<34}{C_RESET}" for f in row])
        print(display)
    input()

def main():
    clear()
    progress_tactical("MAPPING MAIN SECTORS", 100, 0.015)
    time.sleep(0.5)
    
    root = "/sdcard" if os.path.exists("/sdcard") else os.path.expanduser("~")
    
    while True:
        draw_prime_hud()
        print(f" {C_CYAN}01. SCAN ENTIRE SYSTEM       07. MASS IDENTITY REWRITE{C_RESET}")
        print(f" {C_CYAN}02. NEURAL CATEGORY SORT     08. METADATA RECONNAISSANCE{C_RESET}")
        print(f" {C_CYAN}03. SECURE NODE VAPORIZER    09. DATA INTEGRITY CHECK{C_RESET}")
        print(f" {C_CYAN}04. DEEP SEARCH FREQUENCY    10. SECTOR CLONE REDUNDANCY{C_RESET}")
        print(f" {C_CYAN}05. ENCRYPT DATA SECTOR      11. SECTOR FLATTEN & PURGE{C_RESET}")
        print(f" {C_CYAN}06. DECRYPT DATA SECTOR      12. SYSTEM VOLUME DIAGNOSTICS{C_RESET}")
        print(f" {C_CYAN}━" * 72 + f"{C_RESET}")
        print(f" {C_GREY}ACTIVE ROOT: {root.replace('_', ' ')}           {C_CYAN}[XX] TERMINATE{C_RESET}")
        
        cmd = input(f"\n {C_CYAN}STARK@AETHER:~$ {C_RESET}").strip().upper()
        
        if cmd == 'XX':
            clear()
            neural_anim("DE-INITIALIZING NEURAL LINK")
            print(f"\n{C_CYAN}┏" + "━"*40 + "┓")
            print(f"┃ {C_BOLD}SESSION TERMINATED. GOODBYE, SIR.      {C_RESET}{C_CYAN}┃")
            print(f"┗" + "━"*40 + f"┛{C_RESET}\n")
            time.sleep(1)
            break
        elif cmd in ['01', '1']: op_scan_entire_system(root)
        elif cmd in ['02', '2']:
            p = sector_select(root)
            if p:
                progress_tactical("SORTING DATA")
                for f in os.listdir(p):
                    f_p = os.path.join(p, f)
                    if os.path.isfile(f_p):
                        ext = os.path.splitext(f)[1].lower()
                        for cat, exts in FILE_TYPES.items():
                            if ext in exts:
                                d = os.path.join(p, cat); os.makedirs(d, exist_ok=True)
                                shutil.move(f_p, os.path.join(d, f))
                input()
        elif cmd in ['03', '3']:
            p = sector_select(root)
            if p:
                fs = [f for f in os.listdir(p) if os.path.isfile(os.path.join(p, f))]
                for i, f in enumerate(fs): print(f" {C_CYAN}0{i:02d} {C_GREY}{f}{C_RESET}")
                idx = input(f" {C_CYAN}VAPORIZE INDEX: {C_RESET}")
                if idx.isdigit() and int(idx) < len(fs):
                    progress_tactical("VAPORIZING NODE")
                    os.remove(os.path.join(p, fs[int(idx)]))
                input()
        elif cmd in ['04', '4']:
            q = input(f" {C_CYAN}TARGET KEYWORD: {C_RESET}").lower()
            neural_anim("SEARCHING MATRIX")
            for r, _, fs in os.walk(root):
                for f in fs:
                    if q in f.lower(): print(f" {C_CYAN}FOUND: {C_GREY}{f}{C_RESET}")
            input()
        elif cmd in ['05', '5']:
            p = sector_select(root)
            if p:
                progress_tactical("ENCRYPTING")
                for f in os.listdir(p):
                    f_p = os.path.join(p, f)
                    if not f.endswith(".stark"): os.rename(f_p, f_p + ".stark")
                input()
        elif cmd in ['06', '6']:
            p = sector_select(root)
            if p:
                progress_tactical("DECRYPTING")
                for f in os.listdir(p):
                    f_p = os.path.join(p, f)
                    if f.endswith(".stark"): os.rename(f_p, f_p.replace(".stark", ""))
                input()
        elif cmd in ['07', '7']:
            p = sector_select(root)
            if p:
                px = input(f" {C_CYAN}NEW IDENTITY: {C_RESET}")
                for i, f in enumerate(os.listdir(p)):
                    ext = os.path.splitext(f)[1]
                    os.rename(os.path.join(p, f), os.path.join(p, f"{px} {i:03d}{ext}"))
                input()
        elif cmd in ['08', '8']:
            p = sector_select(root)
            if p:
                for f in os.listdir(p):
                    if os.path.isfile(os.path.join(p, f)):
                        s = os.path.getsize(os.path.join(p, f)) // 1024
                        print(f" {C_CYAN}▚ {C_GREY}{f[:25]:<27} {C_CYAN}{s} KB{C_RESET}")
                input()
        elif cmd in ['09', '9']:
            p = sector_select(root)
            if p:
                for f in os.listdir(p):
                    h = hashlib.md5(f.encode()).hexdigest()[:8]
                    print(f" {C_CYAN}[{h.upper()}] {C_GREY}{f}{C_RESET}")
                input()
        elif cmd == '10':
            p = sector_select(root)
            if p:
                progress_tactical("CLONING")
                shutil.copytree(p, p + " CLONE")
                input()
        elif cmd == '11':
            jarvis_type("INITIATING SECTOR FLATTEN PROTOCOL...", C_CYAN)
            source_p = sector_select(root)
            if source_p:
                draw_prime_hud()
                jarvis_type("SELECT DESTINATION SECTOR...", C_CYAN)
                print(f" {C_CYAN}01. {C_GREY}FLATTEN TO SOURCE ROOT")
                print(f" {C_CYAN}02. {C_GREY}FLATTEN TO EXTERNAL SECTOR")
                dest_choice = input(f"\n {C_CYAN}TARGET MODE>> {C_RESET}")
                
                dest_p = source_p if dest_choice == '01' else sector_select(root)
                
                if dest_p:
                    progress_tactical("COLLATING SUB-NODES", 100, 0.01)
                    for r_dir, _, files in os.walk(source_p):
                        if r_dir == dest_p and source_p != dest_p: continue
                        for file in files:
                            s_file = os.path.join(r_dir, file)
                            d_file = os.path.join(dest_p, file)
                            if os.path.exists(d_file):
                                b, e = os.path.splitext(file)
                                d_file = os.path.join(dest_p, f"{b}_{random.randint(100,999)}{e}")
                            try:
                                shutil.move(s_file, d_file)
                            except: pass
                    
                    neural_anim("PURGING EMPTY HIERARCHIES")
                    for r, ds, _ in os.walk(source_p, topdown=False):
                        for d in ds:
                            path = os.path.join(r, d)
                            if not os.listdir(path): os.rmdir(path)
                    jarvis_type("SECTOR STABILIZED. ALL NODES FLATTENED.", C_CYAN)
                input()
        elif cmd == '12':
            total, used, free = shutil.disk_usage(root)
            jarvis_type(f"TOTAL: {total // (2**30)} GB | USED: {used // (2**30)} GB | FREE: {free // (2**30)} GB", C_CYAN)
            input()

if __name__ == "__main__":
    main()

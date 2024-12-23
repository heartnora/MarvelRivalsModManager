# Made my Lumemrian !! (2024 Dec)

import customtkinter
from tkinter import filedialog
import os
import json
import ctypes
import shutil


customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk()
app.geometry("750x550")
app.title("Marvel Rivals Mod Manager (MRMM)")
app.wm_attributes("-topmost", 1)
app.resizable(False, False)

# =========================================== Frame Var ==============================================

frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=5, padx=40, fill="both", expand=False)

frame_3 = customtkinter.CTkScrollableFrame(master=app)
frame_3.pack(pady=10, padx=60, fill="both", expand=True)

# ============================================ Def (Depreciated)===============================================
"""def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )
    sys.exit() # Enable this when the app is complete"""

# Your normal script logic here
"""print("Running as admin")"""
# ============================================ Main ===============================================

label_1 = customtkinter.CTkLabel(master=frame_1, text="Mod Directories ",
                                 font=customtkinter.CTkFont(weight="bold", slant="italic"),
                                  justify=customtkinter.LEFT)
label_1.pack(pady=5, padx=10)

def browse_mod_location():
    filetypes = [("Executable Files", "*.exe"), ("All Files", "*.*")]
    file = filedialog.askopenfilename(filetypes=filetypes, title="Select Game Executable")
    if file:
        mod_location_entry.delete(0, customtkinter.END)
        mod_location_entry.insert(0, file)

def browse_mod_folder():
    folder = filedialog.askdirectory()
    if folder:
        mod_folder_entry.delete(0, customtkinter.END)
        mod_folder_entry.insert(0, folder)

# Frame for Mod Manager options
mod_frame = customtkinter.CTkFrame(frame_1)
mod_frame.pack(pady=10, padx=10)

# Mod Location Row
mod_location_row = customtkinter.CTkFrame(mod_frame)
mod_location_row.pack(fill="x", pady=5)

mod_location_label = customtkinter.CTkLabel(mod_location_row, text="Game Location:")
mod_location_label.pack(side="left", padx=10)

mod_location_entry = customtkinter.CTkEntry(mod_location_row, width=400)
mod_location_entry.pack(side="left", padx=10)

browse_mod_button = customtkinter.CTkButton(mod_location_row, text="Browse", command=browse_mod_location)
browse_mod_button.pack(side="left", padx=10)

# Mod Folder Row
mod_folder_row = customtkinter.CTkFrame(mod_frame)
mod_folder_row.pack(fill="x", pady=5)

mod_folder_label = customtkinter.CTkLabel(mod_folder_row, text="Mod Folder:")
mod_folder_label.pack(side="left", padx=10)

mod_folder_entry = customtkinter.CTkEntry(mod_folder_row, width=400)
mod_folder_entry.pack(side="left", padx=10)

browse_folder_button = customtkinter.CTkButton(mod_folder_row, text="Browse", command=browse_mod_folder)
browse_folder_button.pack(side="left", padx=10)

# Mod Folder Row
tooltiptext_area = customtkinter.CTkFrame(mod_frame)
tooltiptext_area.pack(fill="x", pady=5)

tooltiptext_area = customtkinter.CTkLabel(tooltiptext_area, text="It's recommended that you create a folder called 'Mods' in your Marvel Rivals directory.")
tooltiptext_area.pack(side="left", padx=11)

# ============================================= Mod Picker ==================================================

label_2 = customtkinter.CTkLabel(master=frame_3, text="Mods ",
                                 font=customtkinter.CTkFont(weight="bold", slant="italic"),
                                  justify=customtkinter.LEFT)
label_2.pack(pady=5, padx=10)

# ===== Extra Stuffs =====

config_file = "config.json"
mod_files = {}
check_vars = {}

# === Save & Load === 
def update_mod_list(folder_path):
    for widget in frame_3.winfo_children():
        widget.destroy()

    global mod_files, check_vars
    mod_files.clear()
    check_vars.clear()

    try:
        files = [f for f in os.listdir(folder_path) if f.endswith('.pak')]
        if not files:
            label = app.CTkLabel(frame_3, text="No .pak files found.")
            label.pack(pady=10)
            return

        for file in files:
            check_vars[file] = app.StringVar(value="on")
            checkbox = app.CTkCheckBox(
                frame_3,
                text=file,
                variable=check_vars[file],
                onvalue="on",
                offvalue="off",
                command=lambda f=file: toggle_mod(f, check_vars[f].get())
            )
            checkbox.pack(anchor="w", padx=10, pady=5)
            mod_files[file] = checkbox
    except Exception as e:
        label = app.CTkLabel(frame_3, text=f"Error: {str(e)}")
        label.pack(pady=10)

def toggle_mod(file, state):
    folder = mod_folder_entry.get()
    file_path = os.path.join(folder, file)
    disabled_path = os.path.join(folder, f"{file}.disabled")

    if state == "on" and os.path.exists(disabled_path):
        os.rename(disabled_path, file_path)
    elif state == "off" and os.path.exists(file_path):
        os.rename(file_path, disabled_path)



def save_directory(folder_path):
    """Save directory path to config.json."""
    try:
        with open(config_file, 'w') as config:
            json.dump({"mod_folder": folder_path}, config)
    except Exception as e:
        print("Error saving directory:", e)

def load_directory():
    """Load directory path from config.json."""
    try:
        if os.path.exists(config_file):
            with open(config_file, 'r') as config:
                data = json.load(config)
                return data.get("mod_folder", "")
    except Exception as e:
        print("Error loading directory:", e)
    return ""

def save_config(mod_folder, mod_location):
    config = {
        "mod_folder": mod_folder,
        "mod_location": mod_location
    }
    with open(config_file, "w") as f:
        json.dump(config, f)

def load_config():
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = json.load(f)
            return config.get("mod_folder", ""), config.get("mod_location", "")
    return "", ""

def browse_mod_location():
    filetypes = [("Executable Files", "*.exe"), ("All Files", "*.*")]
    file = filedialog.askopenfilename(filetypes=filetypes, title="Select Game Executable")
    if file:
        mod_location_entry.delete(0, app.END)
        mod_location_entry.insert(0, file)
        save_config(mod_folder_entry.get(), file)  # Save both directories when updated

def apply_mods():
    mod_folder = mod_folder_entry.get().strip()
    game_dir = os.path.dirname(mod_location_entry.get().strip())
    mods_dir = os.path.join(game_dir, "Mods")  # Adjust based on the game

    # Ensure the mods directory exists
    os.makedirs(mods_dir, exist_ok=True)

    # Copy enabled mods to the game Mods directory
    for mod in get_enabled_mods():
        source = os.path.join(mod_folder, mod)
        destination = os.path.join(mods_dir, mod)
        if os.path.exists(source):
            shutil.copy(source, destination)

# Function to load .pak files from the directory and populate the checkbox list
def load_mod_files():
    mod_folder = mod_folder_entry.get()  # Get the folder path from the entry field
    if not os.path.isdir(mod_folder):
        return

    # Clear any existing checkboxes in the mods frame
    for widget in mods_frame.winfo_children():
        widget.destroy()

    # List all .pak files in the directory
    pak_files = [f for f in os.listdir(mod_folder) if f.endswith(".pak")]

    # Create a checkbox for each .pak file
    for pak_file in pak_files:
        var = customtkinter.StringVar(value="off")  # Variable to store checkbox state
        checkbox = customtkinter.CTkCheckBox(mods_frame, text=pak_file, variable=var, onvalue="on", offvalue="off")
        checkbox.var = var  # Attach the variable to the checkbox for later access
        checkbox.pack(anchor="w", padx=10, pady=2)

# Function to get enabled mods
def get_enabled_mods():
    enabled_mods = []
    for widget in mods_frame.winfo_children():
        if isinstance(widget, customtkinter.CTkCheckBox) and widget.var.get() == "on":
            enabled_mods.append(widget.cget("text"))  # Get the text of the enabled checkbox
    return enabled_mods

# Function to simulate running the game with selected mods
def run_game():
    mod_location = mod_location_entry.get().strip()  # Get the path from the "Mod Location" entry
    enabled_mods = get_enabled_mods()  # Get the list of enabled mods

    # Validate the game executable path
    if not os.path.isfile(mod_location) or not mod_location.endswith(".exe"):
        print("Error: Invalid game executable. Please select a valid .exe file.")
        return

    # Apply mods (if needed)
    if enabled_mods:
        print(f"Enabled mods: {enabled_mods}")

    # Run the game executable
    try:
        # Run the game with administrative privileges
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", mod_location, None, None, 1
        )
    except Exception as e:
        print(f"Failed to launch the game: {e}")

# Adding Mod Files List Frame
mods_frame = customtkinter.CTkFrame(frame_3)
mods_frame.pack(padx=10, pady=10, fill="both", expand=True)



# Add a button to refresh the mod file list
refresh_button = customtkinter.CTkButton(frame_1, text="Refresh Mods", command=load_mod_files)
refresh_button.pack(pady=5)

# Add a button to simulate running the game
run_button = customtkinter.CTkButton(frame_1, text="Run Game", command=run_game)
run_button.pack(pady=5)

saved_dir = load_directory()
if saved_dir:
    mod_folder_entry.delete(0, app.END)
    mod_folder_entry.insert(0, saved_dir)
    update_mod_list(saved_dir)
# ============================================= Radio Check (DEPRECIATED) ==================================================

""" label_r = customtkinter.CTkLabel(master=frame_2, text="* cosmetic as of now (23/09/24)",
                                 font=customtkinter.CTkFont(weight="bold", slant="italic"),
                                  justify=customtkinter.LEFT)
   label_r.pack(pady=10, padx=10)

    radiobutton_var = customtkinter.IntVar(value=1)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_2, text="Open as Administrator.",
                                              variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = customtkinter.CTkRadioButton(master=frame_2, text="Open as Guest.",
                                             variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=10, padx=10)

radiobutton_3 = customtkinter.CTkRadioButton(master=frame_2, text="Always open as Administrator.",
                                              variable=radiobutton_var, value=3)
radiobutton_3.pack(pady=10, padx=10)

radiobutton_4 = customtkinter.CTkRadioButton(master=frame_2, text="Always open as Guest.",
                                             variable=radiobutton_var, value=4)
radiobutton_4.pack(pady=10, padx=10)
""" 
# ========================================== Launch Options =========================================================

"""optionmenu_1 = customtkinter.CTkOptionMenu(frame_4, values=["Currently Unavailable",])

optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Launch Options.")"""

app.mainloop()
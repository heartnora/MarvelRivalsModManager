# Marvel Rivals Mod Manager (WIP)

Marvel Rivals Mod Manager (MRMM) is a Python-based tool designed to simplify the management of mods for the game Marvel Rivals. With a sleek GUI powered by customtkinter, it allows users to browse, enable, or disable .pak mod files easily.

***

# Features
## Mod Management:
- Automatically lists all .pak files in the selected folder.
- Enables or disables mods with simple checkboxes.
- Saves mod folder preferences for future sessions.

Directory Handling:
- Browse or auto-detect the mod folder.
- Persistent directory storage using a config.json file.

Game Executable Support:
- Allows selection of the game executable for easy integration.

# Installation

### Prerequisites
Python 3.6 or later

Required Libraries:

```pip install customtkinter```

# Setup

### Clone the repository:

git clone https://github.com/username/marvel-rivals-mod-manager.git

Navigate to the project folder:

cd marvel-rivals-mod-manager

Run the application:

python mod_manager.py

Usage

Select Game Executable:

Click Browse under "Mod Location" to select the game executable (e.g., .exe file).

Set Mod Folder:

Use Browse or Auto to define the mod folder location.

Automatically lists all .pak files present in the folder.

Enable/Disable Mods:

Use checkboxes to enable or disable specific mods.

Disabled mods are renamed with a .disabled extension.

Save Preferences:

The selected mod folder is saved and loaded automatically when reopening the app.

Contributing

Contributions are welcome! Feel free to submit pull requests for new features, bug fixes, or enhancements.

License

This project has no liscence.

Acknowledgements

- customtkinter for the modern GUI framework.

Open-source contributors for inspiration and libraries.

Issues

For any issues or feature requests, please open an issue on the GitHub repository.


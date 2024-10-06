# 🖥️ Set Custom Screen Resolution on Linux

**A tool by IceLabs Inc.**  
Easily configure custom screen resolutions using Python on your Linux system. This script leverages `xrandr` and `cvt` to simplify the process.

## 🚀 Quick Start

### Prerequisites

Make sure the following utilities are installed:

- `xrandr`
- `cvt`

### Install them via:

```sh
sudo apt-get install x11-xserver-utils
```

## 📝 Usage

1. Save the script as `set_resolution.py`.

2. Make the script executable:
   ```sh
   chmod +x set_resolution.py
   ```
3. Run the script:
    ```
    python3 set_resolution.py
    ```
    This will set your screen resolution to 1280x1024.

## 🛠️ How It Works
1. Generate Resolution Mode
    - Uses `cvt 1280 1024` to get the modeline for the desired resolution.

2. Extract and Prepare Mode Data
    - Extracts the configuration needed to create a new display mode.

3. Get Display Name
    - Runs `xrandr` to find the connected display (e.g., `eDP-1`).

4. Apply New Resolution
    - Adds and sets the new resolution mode using `xrandr`.

## ⚠️ Important Notes
- Ensure your hardware supports the resolution you're setting.
- Use `xrandr` to list available displays and modes if needed.

## 📋 Example Scenario
Running the script changes your screen resolution to 1280x1024 if supported by your display.

## 📝 License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/IcelabsInc/Resolution-Fix-Python-Linux/blob/main/LICENSE.txt) file for more details.

#
© 2024 IceLabs Inc.

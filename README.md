# LIFX Light Control Application (BETA)

## Intended Application Use

The LIFX Light Control Application is a sophisticated utility designed to provide seamless, real-time control of LIFX smart lighting systems over a local network. Tailored for both casual users and professionals in smart home automation, this application leverages the LIFX LAN Protocol to enable dynamic lighting adjustments. It is ideal for enhancing ambiance in residential or commercial spaces, creating immersive lighting effects for events, or integrating into broader IoT ecosystems for automated environmental control.

The application empowers users to manipulate LIFX light states and colors through an intuitive graphical user interface (GUI), making it accessible without requiring deep technical knowledge of network protocols or embedded systems. Its primary use case is to offer a standalone, portable solution for controlling LIFX lights without dependency on cloud services or mobile apps, ensuring low-latency performance critical for real-time applications.

## Features

- **Light Discovery and Management**: Automatically detects all LIFX lights on the local network using the LIFX LAN Protocol (UDP port 56700), providing a robust foundation for device interaction.
- **Static Color Control**: Instantly sets all connected LIFX lights to predefined colors (Red or White) with full brightness and customizable color temperature.
- **Power Control**: Allows users to turn all lights off with a single command, ensuring efficient power management.
- **Dynamic Rainbow Gradient**: Features a high-speed, smooth color gradient cycle that transitions through the full hue spectrum (0-65535 in HSBK format), optimized for visual impact and performance.
- **Toggleable Rainbow Mode**: Activates or deactivates the rainbow cycle with a single button, offering flexibility for static or dynamic lighting preferences.
- **Responsive GUI**: Built with `tkinter`, the interface provides immediate feedback via a status label and supports asynchronous operations to prevent UI freezing.
- **Error Handling and Logging**: Incorporates comprehensive logging (`logging` module) to diagnose network or device issues, enhancing reliability and debuggability.
- **Cross-Platform Compatibility**: Designed to run on Windows, macOS, and Linux, with executable generation support via PyInstaller for standalone deployment.

## Options of the Application

The LIFX Light Control Application offers four primary control options accessible through its GUI:

1. **Turn On Red**:
   - Sets all LIFX lights to a vibrant red hue (HSBK: `[0, 65535, 65535, 3500]`).
   - Ideal for creating a bold, warm atmosphere.

2. **Turn On White**:
   - Configures all lights to a bright white (HSBK: `[0, 0, 65535, 6500]`).
   - Suited for task lighting or neutral ambiance.

3. **Turn Off**:
   - Powers down all connected LIFX lights.
   - Useful for energy conservation or resetting the lighting state.

4. **Start/Stop Rainbow Cycle**:
   - Initiates a rapid, continuous gradient cycle through the color spectrum (hue step: 1024, update interval: 0.01s).
   - Toggles off with a second press, halting the cycle instantly.
   - Perfect for dynamic lighting effects in entertainment or creative settings.

## Application Environment

### Hardware Requirements
- **LIFX Lights**: Compatible with any LIFX smart lights supporting the LAN Protocol (Wi-Fi enabled, firmware updated).
- **Host Device**: A computer or embedded system (e.g., Raspberry Pi) with network connectivity to the same LAN as the LIFX lights.
- **Network**: A local Wi-Fi network with UDP multicast support (port 56700 open). No internet access required, though firewalls must permit local traffic.

### Software Requirements
- **Operating System**: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+ recommended).
- **Python Environment** (for development):
  - Python 3.8 or higher.
  - Required libraries:
    - `lifxlan`: LIFX LAN Protocol implementation (`pip install lifxlan`).
    - `tkinter`: GUI framework (typically bundled with Python; on Linux, install via `sudo apt-get install python3-tk`).
- **Executable Deployment**:
  - PyInstaller 5.0+ (`pip install pyinstaller`) for creating standalone binaries.
  - No Python installation needed on end-user systems when distributed as an executable.

### Development and Deployment
- **Source Execution**: Run directly with `python lifx_gui.py` in a Python environment with dependencies installed.
- **Executable Generation**:
  - Command: `python -m PyInstaller --onefile --windowed lifx_gui.py`
  - Produces a single executable (e.g., `lifx_gui_debug.exe` on Windows) in the `dist/` directory.
  - Size: Approximately 15-25 MB, depending on OS and Python version.
- **Logging**: Outputs debug information to the console (or terminal when not using `--windowed`), aiding in troubleshooting network or device connectivity issues.

### Network Considerations
- The application operates over the LIFX LAN Protocol, requiring a stable local network. Performance may degrade if network latency exceeds 50ms or if UDP packets are blocked.
- For optimal rainbow cycle speed, ensure the host device has sufficient processing power and network bandwidth (tested with updates at 100 Hz).

## Installation and Usage

1. **Clone or Download**: Obtain the source code (`lifx_gui.py`) or download the lifx.exe binary
3. **Install Dependencies** (if running from source):
   ```bash
   pip install lifxlan
4. A debug CMD window will be opened. Note that the application is in BETA state

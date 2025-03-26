import tkinter as tk
from tkinter import messagebox
from lifxlan import LifxLAN
import threading
import time
import logging

# Set up basic logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

class LifxControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("LIFX Light Control")
        self.root.geometry("300x250")
        
        # Initialize LifxLAN
        logging.debug("Initializing LifxLAN")
        self.lifx = LifxLAN(None)
        self.lights = []
        
        # State variables
        self.cycling = False
        self.rainbow_thread = None
        
        # GUI elements
        self.label = tk.Label(root, text="LIFX Light Controller", font=("Arial", 14))
        self.label.pack(pady=10)
        
        self.red_button = tk.Button(root, text="Turn On Red", command=self.turn_on_red, width=20)
        self.red_button.pack(pady=5)
        
        self.white_button = tk.Button(root, text="Turn On White", command=self.turn_on_white, width=20)
        self.white_button.pack(pady=5)
        
        self.off_button = tk.Button(root, text="Turn Off", command=self.turn_off, width=20)
        self.off_button.pack(pady=5)
        
        self.rainbow_button = tk.Button(root, text="Start Rainbow Cycle", command=self.toggle_rainbow, width=20)
        self.rainbow_button.pack(pady=5)
        
        self.status_label = tk.Label(root, text="Discovering lights...", font=("Arial", 10))
        self.status_label.pack(pady=10)
        
        # Start discovery
        threading.Thread(target=self.discover_lights, daemon=True).start()

    def discover_lights(self):
        """Discover LIFX lights on the network."""
        logging.debug("Starting light discovery")
        try:
            self.lights = self.lifx.get_lights()
            if not self.lights:
                logging.warning("No LIFX lights found on the network")
                self.status_label.config(text="No LIFX lights found!")
            else:
                logging.info(f"Found {len(self.lights)} lights: {[light.get_label() for light in self.lights]}")
                self.status_label.config(text=f"Found {len(self.lights)} light(s)")
        except Exception as e:
            logging.error(f"Discovery error: {str(e)}")
            self.status_label.config(text=f"Error: {str(e)}")

    def control_lights(self, power, color=None):
        """Control all lights with given power state and optional color."""
        if not self.lights:
            logging.warning("No lights available to control")
            return
        
        logging.debug(f"Controlling lights: power={power}, color={color}")
        for light in self.lights:
            try:
                light.set_power(power, rapid=True)
                if power and color:
                    light.set_color(color, rapid=True)
                logging.info(f"Successfully controlled {light.get_label()}")
            except Exception as e:
                logging.error(f"Error controlling {light.get_label()}: {str(e)}")
                messagebox.showerror("Error", f"Failed to control {light.get_label()}: {str(e)}")

    def turn_on_red(self):
        """Turn all lights on and set to red."""
        self.stop_rainbow()
        logging.debug("Turning lights red")
        threading.Thread(target=self.control_lights, args=(True, [0, 65535, 65535, 3500])).start()
        self.status_label.config(text="Lights set to Red")

    def turn_on_white(self):
        """Turn all lights on and set to white."""
        self.stop_rainbow()
        logging.debug("Turning lights white")
        threading.Thread(target=self.control_lights, args=(True, [0, 0, 65535, 6500])).start()
        self.status_label.config(text="Lights set to White")

    def turn_off(self):
        """Turn all lights off."""
        self.stop_rainbow()
        logging.debug("Turning lights off")
        threading.Thread(target=self.control_lights, args=(False,)).start()
        self.status_label.config(text="Lights turned off")

    def rainbow_cycle(self):
        """Fast rainbow cycle with smooth gradient transitions."""
        hue = 0
        step = 1024  # Fast hue change
        max_hue = 65535
        delay = 0.01  # Rapid updates
        
        logging.debug("Starting rainbow cycle")
        while self.cycling and self.lights:
            color = [hue, 65535, 65535, 3500]
            self.control_lights(True, color)
            hue = (hue + step) % (max_hue + 1)
            time.sleep(delay)
        logging.debug("Rainbow cycle stopped")

    def toggle_rainbow(self):
        """Toggle the rainbow cycle on or off."""
        if not self.lights:
            logging.warning("No lights found for rainbow cycle")
            messagebox.showwarning("Warning", "No lights found on the network!")
            return
        
        if not self.cycling:
            self.cycling = True
            self.rainbow_button.config(text="Stop Rainbow Cycle")
            self.rainbow_thread = threading.Thread(target=self.rainbow_cycle, daemon=True)
            self.rainbow_thread.start()
            logging.info("Rainbow cycle started")
        else:
            self.stop_rainbow()

    def stop_rainbow(self):
        """Stop the rainbow cycle."""
        if self.cycling:
            self.cycling = False
            self.rainbow_button.config(text="Start Rainbow Cycle")
            if self.rainbow_thread:
                self.rainbow_thread.join(timeout=1)
            logging.info("Rainbow cycle stopped")

if __name__ == "__main__":
    root = tk.Tk()
    app = LifxControlApp(root)
    root.mainloop()

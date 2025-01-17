import os
from skidl import *

# Set KiCad environment variables
os.environ['KICAD_SYMBOL_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/symbols'
os.environ['KICAD_FOOTPRINT_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/footprints'

print("KICAD_SYMBOL_DIR:", os.environ.get('KICAD_SYMBOL_DIR'))

# Load the symbol library explicitly
# device_lib_path = 'C:/Program Files/KiCad/8.0/share/kicad/symbols/Device.kicad_sym'
# device_lib_path = './Device.kicad_sym'
# device_lib_path = r"C:\\Users\\matth\\Documents\\KiCad\\8.0\\symbols"
device_lib_path = "C:\\Program Files\\KiCad\\8.0\\share\\kicad\\symbols\\/Device.kicad_sym"

try:
    lib = SchLib(device_lib_path, tool=KICAD)
    print(f"Parts in {device_lib_path}:")
    for part in lib:
        print(part.name)
except Exception as e:
    print(f"Failed to load library: {e}")

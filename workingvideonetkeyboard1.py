import os

# Set KiCad environment variables (use forward slashes)
os.environ['KICAD_SYMBOL_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/symbols'
os.environ['KICAD_FOOTPRINT_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/footprints'

os.environ['KICAD6_SYMBOL_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/symbols'
os.environ['KICAD6_FOOTPRINT_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/footprints'
os.environ['KICAD7_SYMBOL_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/symbols'
os.environ['KICAD7_FOOTPRINT_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/footprints'
os.environ['KICAD8_SYMBOL_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/symbols'
os.environ['KICAD8_FOOTPRINT_DIR'] = r'C:/Program Files/KiCad/8.0/share/kicad/footprints'

os.environ['KICAD_CONFIG_HOME'] = r'C:/Users/matth/AppData/Roaming/kicad/8.0'

print("KICAD_SYMBOL_DIR:", os.environ.get('KICAD_SYMBOL_DIR'))
print("KICAD8_FOOTPRINT_DIR:", os.environ.get('KICAD8_FOOTPRINT_DIR'))

from skidl import *

# Load the symbol library
lib = SchLib(r'C:/Program Files/KiCad/8.0/share/kicad/symbols/Device.kicad_sym', tool=KICAD8)

# Create a resistor part (use only the library name and part name, no full path for footprint)
r1 = Part('Device', 'R', footprint='Resistor_SMD:R_0805_2012Metric')
r2 = Part('Device', 'R', footprint='Resistor_SMD:R_0805_2012Metric')

r1.value = '100'
r2.value = '220'

gnd = Net('GND')
vin = Net('VIN')

gnd += r1[1]
gnd += r2[1]

vin += r1[2], r2[2]

# Generate the netlist (output file named video.net)
generate_netlist(file_='video.net')


# instead of os.environ, try: set KICAD_SYMBOL_DIR=C:\Program Files\KiCad\share\kicad\kicad-symbols in Windows terminal
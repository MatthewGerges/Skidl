# from skidl import *
# import os

# os.environ['KICAD8_SYMBOL_DIR'] = '/mnt/c/Program Files/KiCad/8.0/share/kicad/symbols/'
# os.environ['KICAD8_FOOTPRINT_DIR'] = '/mnt/c/Program Files/KiCad/8.0/share/kicad/footprints/'

# # Create input & output voltages and ground reference.
# vin, vout, gnd = Net('VI'), Net('VO'), Net('GND')

# # Create two resistors.
# r1, r2 = 2 * Part("Device", 'R', TEMPLATE, footprint='Resistor_SMD.pretty:R_0805_2012Metric')
# r1.value = '1K'   # Set upper resistor value.
# r2.value = '500'  # Set lower resistor value.

# # Connect the nets and resistors.
# vin += r1[1]      # Connect the input to the upper resistor.
# gnd += r2[2]      # Connect the lower resistor to ground.
# vout += r1[2], r2[1] # Output comes from the connection of the two resistors.

# # Or you could do it with a single line of code:
# # vin && r1 && vout && r2 && gnd

# # Output the netlist to a file.
# generate_netlist(tool=KICAD8)

from skidl import *

lib = SchLib('/mnt/c/Program Files/KiCad/8.0/share/kicad/symbols/Device.kicad_sym', tool=KICAD)

# Create input & output voltages and ground reference.
vin, vout, gnd = Net('VI'), Net('VO'), Net('GND')

# Create two resistors.
# r1, r2 = 2 * Part(lib, 'R', TEMPLATE, footprint='Resistor_SMD.pretty:R_0805_2012Metric')
r1, r2 = 2 * Part("/mnt/c/Program Files/KiCad/8.0/share/kicad/symbols/Device.kicad_sym", 'R', TEMPLATE, footprint='Resistor_SMD.pretty:R_0805_2012Metric')
r1.value = '1K'   # Set upper resistor value.
r2.value = '500'  # Set lower resistor value.

# Connect the nets and resistors.
vin += r1[1]      # Connect the input to the upper resistor.
gnd += r2[2]      # Connect the lower resistor to ground.
vout += r1[2], r2[1] # Output comes from the connection of the two resistors.

# Output the netlist to a file.
generate_netlist(tool=KICAD)

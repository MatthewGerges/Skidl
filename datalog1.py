import os

os.environ['KICAD_SYMBOL_DIR'] = r'C:\Program Files\KiCad\8.0\share\kicad\symbols'
os.environ['KICAD6_SYMBOL_DIR'] = r'C:\Program Files\KiCad\8.0\share\kicad\symbols'
os.environ['KICAD7_SYMBOL_DIR'] = r'C:\Program Files\KiCad\8.0\share\kicad\symbols'
os.environ['KICAD8_SYMBOL_DIR'] = r'C:\Program Files\KiCad\8.0\share\kicad\symbols'
os.environ['KICAD_FOOTPRINT_DIR'] = r'C:\Program Files\KiCad\8.0\share\kicad\footprints'
os.environ['KICAD8_FOOTPRINT_DIR'] = r'C:\Program Files\KiCad\8.0\share\kicad\footprints'
os.environ['KICAD_CONFIG_HOME'] = r'C:\Users\matth\AppData\Roaming\kicad\8.0'

print("KICAD_SYMBOL_DIR:", os.environ.get('KICAD_SYMBOL_DIR'))
print("KICAD8_FOOTPRINT_DIR:", os.environ.get('KICAD8_FOOTPRINT_DIR'))

from skidl import *
search('opamp')
search('^lm386$')

# # from skidl import set_debug_level
# # set_debug_level(4)  # Set debug level to maximum verbosity

# # Manually add the footprint library path
# # add_lib_path('Resistor_SMD.pretty', r'C:\Program Files\KiCad\8.0\share\kicad\footprints')

lib = SchLib(r'C:\Program Files\KiCad\8.0\share\kicad\symbols\Device.kicad_sym', tool=KICAD8)

# resistor = Part('Device','R', footprint='Resistor_SMD.pretty:R_0805_2012Metric')

# Create input & output voltages and ground reference.
vin, vout, gnd = Net('VI'), Net('VO'), Net('GND')

# Create two resistors.
# r1, r2 = 2 * Part(lib, 'R', TEMPLATE, footprint='Resistor_SMD.pretty:R_0805_2012Metric')
# r1, r2 = 2 * Part(lib, 'R', TEMPLATE, footprint=r'C:\Program Files\KiCad\8.0\share\kicad\footprints\Resistor_SMD.pretty\R_08090_2012Metric.kicad_mod')
r1 = Part(r'C:\Program Files\KiCad\8.0\share\kicad\symbols\Device.kicad_sym', 'R', footprint=r'C:\Program Files\KiCad\8.0\share\kicad\footprints\Resistor_SMD.pretty\R_0805_2012Metric.kicad_mod')
r2 = Part(r'C:\Program Files\KiCad\8.0\share\kicad\symbols\Device.kicad_sym', 'R', footprint=r'C:\Program Files\KiCad\8.0\share\kicad\footprints\Resistor_SMD.pretty\R_0805_2012Metric.kicad_mod')
r1.value = '1K'   # Set upper resistor value.
r2.value = '500'  # Set lower resistor value.

# Connect the nets and resistors.
vin += r1[1]      # Connect the input to the upper resistor.
gnd += r2[2]      # Connect the lower resistor to ground.
vout += r1[2], r2[1] # Output comes from the connection of the two resistors.

# Output the netlist to a file.
generate_netlist(tool=KICAD8)
generate_pcb(fp_libs=[r'C:\Program Files\KiCad\8.0\share\kicad\footprints'])
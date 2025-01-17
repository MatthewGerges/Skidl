import os

from skidl import *

vin, vout, gnd = Net('VI'), Net('VO'), Net('GND')

r1 = Part('Device', 'R', footprint='Resistor_SMD:R_0805_2012Metric')
r2 = Part('Device', 'R', footprint='Resistor_SMD:R_0805_2012Metric')

r1.value = '1000'   # Set upper resistor value.
r2.value = '50'  # Set lower resistor value.

# Connect the nets and resistors.
vin += r1[1]      # Connect the input to the upper resistor.
gnd += r2[2]      # Connect the lower resistor to ground.
vout += r1[2], r2[1] # Output comes from the connection of the two resistors.

# Output the netlist to a file.
generate_netlist(tool=KICAD8)
generate_pcb(fp_libs=[r'C:\Program Files\KiCad\8.0\share\kicad\footprints'])
# import os

# # Set KiCad environment variables (use forward slashes)

# from skidl import *

# # lib = SchLib('Device')
# # print(lib.list_parts())

# # Create part templates.
# # q = Part(lib="Device.lib", name="Q_PNP_CBE", dest=TEMPLATE, symtx="V")
# # q = Part(lib="Device", name="Q_PNP_CBE", dest=TEMPLATE, symtx="V")
# # r = Part("Device", "R", dest=TEMPLATE)
# r1 = Part('Device', 'R', footprint='Resistor_SMD:R_0805_2012Metric')

# r = Part('Device', 'R', footprint='Resistor_SMD:R_0805_2012Metric')
# # q = Part('Device', name="Q_PNP_CBE", dest=TEMPLATE, symtx="V", footprint='Transistor_Power_Module:ST_SDIP-25L')
# # q = Part('Device', 'Q', footprint='Transistor_Power_Module:ST_SDIP-25L')

# q = Part('Device', 'R', value="10K", footprint='Resistor_SMD:R_0603_1608Metric')

# # Create nets.
# gnd, vcc = Net("GND"), Net("VCC")
# a, b, a_and_b = Net("A"), Net("B"), Net("A_AND_B")

# # Instantiate parts.
# gndt = Part("power", "GND")  # Ground terminal.
# vcct = Part("power", "VCC")  # Power terminal.
# q1, q2 = q(2)
# r1, r2, r3, r4, r5 = r(5, value="10K")

# # Make connections between parts.
# a & r1 & q1["B", "C"] & r4 & q2["B", "C"] & a_and_b & r5 & gnd
# b & r2 & q1["B"]
# q1["C"] & r3 & gnd
# vcc += q1["E"], q2["E"], vcct
# gnd += gndt



# generate_svg()


from skidl import *

# Create two resistors
r1 = Part('Device', 'R', value="10K", footprint='Resistor_SMD:R_0805_2012Metric')
r2 = Part('Device', 'R', value="10K", footprint='Resistor_SMD:R_0805_2012Metric')

# Create nets for the connections
net_vcc = Net("VCC")  # Power net
net_gnd = Net("GND")  # Ground net
net_intermediate = Net("Intermediate")  # Connection between r1 and r2

# Connect the resistors
net_vcc += r1[1]  # Connect VCC to one terminal of r1
net_intermediate += r1[2], r2[1]  # Connect r1's second terminal to r2's first terminal
net_gnd += r2[2]  # Connect r2's second terminal to GND

# Generate an SVG of the schematic
generate_svg()

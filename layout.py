# import sys
# from pcbnew import *

# filename=sys.argv[1]

# pcb = LoadBoard(filename)

# # nets = board.GetNetsByName()

# # for netname, net in nets.items():
# #     print("netcode: {}, name: {}".format(net.GetNetcode(), netname))

# # for module in board.GetModules():
# #     print("Module: ", module.GetReference())

# for module in pcb.GetModules():
#     print ("* Module: %s"%module.GetReference())
#     module.Value().SetVisible(False)      # set Value as Hidden
#     module.Reference().SetVisible(True)   # set Reference as Visible

import sys
print(sys.executable)

from pcbnew import *

# Provide the absolute path to your .kicad_pcb file
filename = r'C:/Users/matth\Documents/AI-Skidl-PCB/datalogger-tutorial/datalog1.kicad_pcb'

# Load the board file
board = LoadBoard(filename)

# Now, you can inspect the nets or components
nets = board.GetNetsByName()

# Example of printing nets and modules
for netname, net in nets.items():
    print(f"netname: {netname}")

for module in board.GetFootprints():
    print(f"Module: {module.GetReference()}")

# Find the footprint with reference 'R1'
r1 = None
for footprint in board.GetFootprints():
    if footprint.GetReference() == 'R1':
        r1 = footprint
        break

# If R1 was found, reposition and rotate it
if r1:
    r1.SetPosition(wxPoint(0,0))
    r1.Rotate(wxPoint(0,0), 90 * 10)

# Refresh the PCB view to reflect the changes
Refresh()
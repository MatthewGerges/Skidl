import pcbnew
from pcbnew import GetBoard

# Get the currently loaded board.
board = GetBoard()

# Get the nets on the board.
nets = board.GetNetsByName()

# Print net details.
for netname, net in nets.items():
    print(f"netname: {netname}, netcode: {net.GetNetClassName()}")

# Print module details.
for module in board.GetFootprints():
    print(f"Module: {module.GetReference()}")

# Find the module by reference
def find_module_by_reference(board, ref):
    for module in board.GetFootprints():
        if module.GetReference() == ref:
            return module
    return None

# Example: Modify R1
resistor_1 = find_module_by_reference(board, 'R1')
if resistor_1:
    resistor_1.SetPosition(pcbnew.VECTOR2I(0, 0))  # Correct usage with VECTOR2I
    # Rotate around origin, using EDA_ANGLE for the angle
    resistor_1.Rotate(pcbnew.VECTOR2I(0, 0), pcbnew.EDA_ANGLE(90 * 10))
else:
    print("Resistor R1 not found!")

# Example: Modify R1 and R2 dynamically
for i in range(2):
    modref = f'R{i + 1}'
    resistor = find_module_by_reference(board, modref)
    if resistor:
        # Position the resistors dynamically using pcbnew.VECTOR2I
        resistor.SetPosition(pcbnew.VECTOR2I(int(10e6 * i), int(5e6 * i)))
    else:
        print(f"Resistor {modref} not found!")

# Refresh the board
pcbnew.Refresh()



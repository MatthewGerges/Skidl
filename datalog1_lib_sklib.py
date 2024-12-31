from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

SKIDL_lib_version = '0.0.1'

datalog1_lib = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'R', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'R'}), 'ref_prefix':'R', 'fplist':[''], 'footprint':'C:\\Program Files\\KiCad\\8.0\\share\\kicad\\footprints\\Resistor_SMD.pretty\\R_0805_2012Metric.kicad_mod', 'keywords':'R res resistor', 'description':'', 'datasheet':'~', 'pins':[
            Pin(num='1',name='~',func=Pin.types.PASSIVE,unit=1),
            Pin(num='2',name='~',func=Pin.types.PASSIVE,unit=1)], 'unit_defs':[] })])
from magma import *

__all__  = ['A0', 'A1', 'A2', 'A3']
__all__ += ['I0', 'I1', 'I2', 'I3']
__all__ += ['ALL', 'ANY', 'PARITY']
__all__ += ['ZERO', 'ONE']
__all__ += ['LUTS_PER_LOGICBLOCK', 'BITS_PER_LUT', 'LOG_BITS_PER_LUT']

__all__ += ['_LUT1', '_LUT2', '_LUT3', '_LUT4']
__all__ += ['MUXF5', 'MUXF6', 'MUXF7', 'MUXF8']
__all__ += ['MUXCY', 'MUXCY_L', 'MUXCY_D', 'ANDCY', 'XORCY']
__all__ += ['FDRSE', 'FDCPE', 'FDCE']

LUTS_PER_LOGICBLOCK = 2
LOG_BITS_PER_LUT = 4
BITS_PER_LUT = 1 << LOG_BITS_PER_LUT

ZERO = 0
ONE = (1<<BITS_PER_LUT)-1

A0 = 0xAAAA
A1 = 0xCCCC
A2 = 0xF0F0
A3 = 0xFF00

I0 = A0
I1 = A1
I2 = A2
I3 = A3

ALL = A0 & A1 & A2 & A3
ANY = A0 | A1 | A2 | A3 
PARITY = A0 ^ A1 ^ A2 ^ A3 

_LUT1 = DeclareCircuit('LUT1',
               "I0", In(Bit),
               "O",  Out(Bit))

_LUT2 = DeclareCircuit('LUT2',
               "I0", In(Bit),
               "I1", In(Bit),
               "O",  Out(Bit))

_LUT3 = DeclareCircuit('LUT3',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "O",  Out(Bit))

_LUT4 = DeclareCircuit('LUT4',
               "I0", In(Bit),
               "I1", In(Bit),
               "I2", In(Bit),
               "I3", In(Bit),
               "O",  Out(Bit)) 

# D-FF with Clock Enable and Aynchronous Clear
FDCE = DeclareCircuit('FDCE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "CLR", In(Bit),
               "D",   In(Bit),
               "Q",   Out(Bit))
    
# D-FF with Clock Enable and Aynchronous Preset and Clear
FDCPE = DeclareCircuit('FDCPE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "CLR", In(Bit),
               "PRE", In(Bit),
               "D",   In(Bit),
               "Q",   Out(Bit)) 

# D-FF with Synchronous Reset and Set and Clock Enable
FDRSE = DeclareCircuit('FDRSE',
               "C",   In(Clock),
               "CE",  In(Enable),
               "R",   In(Bit),
               "S",   In(Bit),
               "D",   In(Bit),
               "Q",   Out(Bit)) 

MUXF5 = DeclareCircuit('MUXF5',
               "I0", In(Bit),
               "I1", In(Bit),
               "S",  In(Bit),
               "O",  Out(Bit))

MUXF6 = DeclareCircuit('MUXF6',
               "I0", In(Bit),
               "I1", In(Bit),
               "S",  In(Bit),
               "O",  Out(Bit))

MUXF7 = DeclareCircuit('MUXF7',
               "I0", In(Bit),
               "I1", In(Bit),
               "S",  In(Bit),
               "O",  Out(Bit))

MUXF8 = DeclareCircuit('MUXF8',
               "I0", In(Bit),
               "I1", In(Bit),
               "S", In(Bit),
               "O", Out(Bit))


MUXCY = DeclareCircuit('MUXCY',
               "DI", In(Bit),
               "CI", In(Bit),
               "S", In(Bit),
               "O", Out(Bit))

MUXCY_L = DeclareCircuit('MUXCY_L',
               "DI", In(Bit),
               "CI", In(Bit),
               "S", In(Bit),
               "LO", Out(Bit))

MUXCY_D = DeclareCircuit('MUXCY_D',
               "DI", In(Bit),
               "CI", In(Bit),
               "S", In(Bit),
               "O", Out(Bit),
               "LO", Out(Bit))

XORCY = DeclareCircuit('XORCY',
               "LI", In(Bit),
               "CI", In(Bit),
               "O", Out(Bit))

ANDCY = DeclareCircuit('MULT_AND',
               "I0", In(Bit),
               "I1", In(Bit),
               "LO", Out(Bit))

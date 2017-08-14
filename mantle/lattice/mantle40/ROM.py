from collections import Sequence
from magma import *
from .LUT import LUT1, LUT2, LUT3, LUT4, LUT5, LUT6, LUT7, LUT8, A0, A1, A2, A3
from .MUX import Mux2

__all__  = ['ROM1', 'ROM2', 'ROM3', 'ROM4']
__all__ += ['ROM5', 'ROM6', 'ROM7', 'ROM8']
__all__ += ['ROMN', 'ROM']

__all__ += ['ROM16xN']

# Move the lutinit function to Circuit init
def ROM1(rom, **kwargs):
    return uncurry(LUT1(rom, **kwargs))

def ROM2(rom, **kwargs):
    return uncurry(LUT2(rom, **kwargs))

def ROM3(rom, **kwargs):
    return uncurry(LUT3(rom, **kwargs))

def ROM4(rom, **kwargs):
    return uncurry(LUT4(rom, **kwargs))

def ROM5(rom, **kwargs):
    return uncurry(LUT5(rom, **kwargs))

def ROM6(rom, **kwargs):
    return uncurry(LUT6(rom, **kwargs))

def ROM7(rom, **kwargs):
    return uncurry(LUT7(rom, **kwargs))

def ROM8(rom, **kwargs):
    return uncurry(LUT8(rom, **kwargs))


#
# create a ROM with n entries and initialize if to the comtents of rom
#
# if n is None: n = lem(rom)
#
def ROMN(rom, n=None, **kwargs):
    """
    n-bit LUT

    I[n] -> n
    """

    # rom must be a sequence
    if isinstance(rom, Sequence):
        assert n is None
        n = len(rom)
    else:
        assert n is not None
        n = 1 << n

    if n == 2:
        return ROM1(rom, **kwargs)
    if n == 4:
        return ROM2(rom, **kwargs)
    if n == 8:
        return ROM3(rom, **kwargs)
    if n == 16:
        return ROM4(rom, **kwargs)
    if n == 32:
        return ROM5(rom, **kwargs)
    if n == 64:
        return ROM6(rom, **kwargs)
    if n == 128:
        return ROM7(rom, **kwargs)
    if n == 256:
        return ROM8(rom, **kwargs)

    return None

def ROM(rom, **kwargs):
    return ROMN(rom, **kwargs)

ROMCache = {}

# Rom Module name
def _ROMName(name, n, data):
    return '%s%d_%d' % (name, n, abs(hash(__builtin__.tuple(data))))

def DefineROM16xN(rom):
    """
    Construct a 16 entry ROM of arbitrary width.

    rom[16][w]
    """
    assert(len(rom) == 16)
    # transpose - rom must be a sequence of sequences
    rom = zip(*rom)
    n = len(rom)

    # could be different memory contents ...
    name = _ROMName('ROM16x', n, rom)
    if name in ROMCache:
        return ROMCache[name]

    args = ['I', In(Bits(4)), 'O', Out(Bits(n))]

    define = DefineCircuit(name, *args)

    def ROM(y):
        return ROM4(rom[y])

    rom = fork(col(ROM, n))

    rom(define.I)
    wire(rom.O, define.O)

    EndCircuit()

    ROMCache[name] = define
    return define

#
# Create a 16xN ROM
#
def ROM16xN(rom):
    return DefineROM16xN(rom)()

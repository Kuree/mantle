from magma import *
from mantle import *
from loam.boards.icestick import IceStick


def test_bit():
    @circuit(clock=False)
    def circ(a : In(Bit), b : In(Bit), c : Out(Bit)):
        c = a + b

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", In(Bit), "c", Out(Bit))
inst0 = Add(1)(circ.a, circ.b)
wire(inst0, circ.c)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_array():
    @circuit(clock=False)
    def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
        c = a + b

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))
inst0 = Add(5)(circ.a, circ.b)
wire(inst0, circ.c)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_sub():
    @circuit(clock=False)
    def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
        c = -(a - b)

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))
inst0 = Sub(5)(circ.a, circ.b)
inst1 = Negate(5)(inst0)
wire(inst1, circ.c)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_logic_ops():
    @circuit(clock=False)
    def circ(a : In(Array(5, Bit)), b : In(Array(5, Bit)), c : Out(Array(5, Bit))):
        c = ~((a | b ^ a) & b) >> 2
    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(5, Bit)), "b", In(Array(5, Bit)), "c", Out(Array(5, Bit)))
inst0 = Xor(2, width=5)(circ.b, circ.a)
inst1 = Or(2, width=5)(circ.a, inst0)
inst2 = And(2, width=5)(inst1, circ.b)
inst3 = Invert(5)(inst2)
inst4 = RightShift(5, 2)(inst3)
wire(inst4, circ.c)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_clock():
    @circuit
    def circ(a : In(Bit), b : Out(Bit)):
        b = a

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))
wire(circ.a, circ.b)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_wire():
    @circuit
    def circ(a : In(Bit), b : Out(Bit)):
        wire(a, b)

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))
wire(circ.a, circ.b)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_register():
    @circuit
    def circ(a : In(Bit), b : Out(Bit)):
        c = Register(1)
        wire(a, c.I[0])
        wire(c.O[0], b)

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Bit), "b", Out(Bit), "CLK", In(Bit))
c = Register(1)
wire(circ.a, c.I[0])
wire(c.O[0], circ.b)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_assign_constant():
    @circuit
    def circ(b : Out(Array(3, Bit))):
        b = 6

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "b", Out(Array(3, Bit)), "CLK", In(Bit))
wire(int2seq(6, 3), circ.b)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_width_promotion():
    @circuit
    def circ(b : Out(Array(3, Bit))):
        a = Register(4)
        a(1)
        c = Register(4)
        c.I = 1

    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "b", Out(Array(3, Bit)), "CLK", In(Bit))
a = Register(4)
wire(a.I, int2seq(1, 4))
c = Register(4)
wire(int2seq(1, 4), c.I)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_width_promotion_binop():
    @circuit
    def circ(a : In(Array(3, Bit)), b : Out(Array(3, Bit))):
        b = a + 1


    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(3, Bit)), "b", Out(Array(3, Bit)), "CLK", In(Bit))
inst0 = Add(3)(circ.a, int2seq(1, 3))
wire(inst0, circ.b)
EndCircuit()
"""
    assert circ.__magma_source == expected

def test_subscript():
    @circuit
    def circ(a : In(Array(4, Bit)), b : Out(Bit), c : In(Array(2, Bit)), d : Out(Bit)):
        b = a[0]
        d = a[c]


    expected = \
"""from magma import *
from mantle import *
circ = DefineCircuit("circ", "a", In(Array(4, Bit)), "b", Out(Bit), "c", In(Array(2, Bit)), "d", Out(Bit), "CLK", In(Bit))
wire(circ.a[0], circ.b)
inst0 = MuxN(4)(circ.a, circ.c)
wire(inst0, circ.d)
EndCircuit()
"""
    assert circ.__magma_source == expected

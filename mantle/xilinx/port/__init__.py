import os

target = os.getenv('MANTLE_TARGET', None)
target = target.strip()

assert target == 'spartan3' or target == 'spartan6' or target == 'kintex7'

if   target == 'spartan3':
    from ..port3 import *
else:
    from ..port6 import *

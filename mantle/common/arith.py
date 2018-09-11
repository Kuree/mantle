import magma as m
from mantle import DefineAdd, DefineSub, DefineNegate

__all__ = [ "Add", "Sub", "Negate", "UDiv", "SDiv" ]


def Add(n, cin=False, cout=False, **kwargs):
    return DefineAdd(n, cin=cin, cout=cout)(**kwargs)


def Sub(n, cin=False, cout=False, **kwargs):
    return DefineSub(n, cin=cin, cout=cout)(**kwargs)


def Negate(width, **kwargs):
    return DefineNegate(width)(**kwargs)


def UDiv(width, **kwargs):
    if m.mantle_target != "coreir":
        raise NotImplementedError(
            "Division not implemented for mantle target {m.mantle_target}")
    # Workaround import error for other targets by delaying import until after
    # if guard
    from mantle import DefineUDiv
    return DefineUDiv(width)(**kwargs)


def SDiv(width, **kwargs):
    if m.mantle_target != "coreir":
        raise NotImplementedError(
            "Division not implemented for mantle target {m.mantle_target}")
    # Workaround import error for other targets by delaying import until after
    # if guard
    from mantle import DefineSDiv
    return DefineSDiv(width)(**kwargs)

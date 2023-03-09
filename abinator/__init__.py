from .abi_logic import Abi
from .events import Event, anonymous, indexed
from .inputs import Struct
from .state_mutability import payable, view, pure
from .types import *


def to_abi(abi_cls: Abi) -> list:
    return abi_cls.to_abi()

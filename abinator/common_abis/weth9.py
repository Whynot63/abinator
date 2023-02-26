from ..types import uint256, address
from ..state_mutability import payable
from ..events import Event, indexed
from .erc20 import ERC20


class WETH9(ERC20):
    @payable
    def deposit():
        ...

    def withdraw(wad: uint256):
        ...

    class Deposit(Event):
        dst: indexed(address)
        wad: uint256

    class Withdrawal(Event):
        src: indexed(address)
        wad: uint256

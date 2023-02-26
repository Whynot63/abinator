from ..abi_logic import Abi
from ..state_mutability import view
from ..types import string, uint8, uint256, address, bool
from ..events import Event, indexed


# https://eips.ethereum.org/EIPS/eip-20


class ERC20(Abi):
    # Methods
    name: string
    symbol: string
    decimals: uint8
    totalSupply: uint256

    @view
    def balanceOf(_owner: address) -> uint256:
        ...

    def transfer(_to: address, _value: uint256) -> bool:
        ...

    def transferFrom(_from: address, _to: address, _value: uint256) -> bool:
        ...

    def approve(_spender: address, _value: uint256) -> bool:
        ...

    @view
    def allowance(_owner: address, _spender: address) -> uint256:
        ...

    # Events

    class Transfer(Event):
        _from: indexed(address)
        _to: indexed(address)
        _value: uint256

    class Approval(Event):
        _owner: indexed(address)
        _spender: indexed(address)
        _value: uint256

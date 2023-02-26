from abinator import (
    Event,
    Abi,
    indexed,
    view,
    payable,
    address,
    uint256,
    string,
    uint8,
    uint,
    bool,
)


class ERC20(Abi):
    name: string
    symbol: string
    decimals: uint8
    totalSupply: uint256

    class Transfer(Event):
        from_: indexed(address)
        to: indexed(address)
        value: uint256

    @view
    def allowance(owner: address, spender: address) -> uint256:
        ...

    @view
    def balanceOf(account: address) -> uint256:
        ...

    def approve(spender: address, amount: uint256) -> bool:
        ...

    def transfer(to: address, amount: uint256) -> bool:
        ...

    def transferFrom(from_: address, to: address, amount: uint256) -> bool:
        ...


class WETH(ERC20):
    @payable
    def deposit():
        ...

    def withdraw(wad: uint):
        ...


print(ERC20().to_abi())

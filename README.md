# Abinator

Define ABI for your smart contract with dataclass-like style.

#### Quick example
Define your abi as `Abi` child. `Abi.to_abi()` returns abi as json, so you can use it with `web3py` and `web3-premium`.
```python
from abinator import Abi, uint256, uint8

class ERC20Fragment(Abi):
    decimals: uint8

    @view
    def balanceOf(account: address) -> uint256:
        ...

ERC20Fragment.to_abi() # returns json with abi
```

<hr/>

## Documentation

### State mutability
You can use `view`, `pure`, `payable` decoratos for state mutabilty.

```python
from abinator import Abi, uint256

class Contract(Abi):
    @view
    def balanceOf(account: address) -> uint256:
        ...
    
    @payable
    def deposit():
        ...

    @pure
    def safe_add(a: uint256, b: uint256) -> uint256:
        ...
```


### Events
Define events with child class of `Event` inside your abi class.

You can use `indexed` decorator for topics.

```python
from abinator import Abi, Event, address, uint256, indexed

class ERC20Fragment(Abi):
    class Transfer(Event):
        from_: indexed(address)
        to: indexed(address)
        value: uint256
```

Also there is `anonymous` for event class:
```python
from abinator import Abi, Event, anonymous, uint256

class Contract(Abi):
    @anonymous
    class AnonymousEvent(Event):
        value: uint256
```
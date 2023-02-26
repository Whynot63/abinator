from typing import TypeVar, get_type_hints

from .events import Event
from .inputs import parse_input


class Abi:
    # https://docs.soliditylang.org/en/v0.8.13/abi-spec.html#json
    @classmethod
    def to_abi(cls):
        abi = []

        for name, type_ in cls.__annotations__.items():
            abi.append(
                {
                    "type": "function",
                    "name": name,
                    "inputs": [],
                    "outputs": [{"name": "", **parse_input(type_)}],
                    "stateMutability": "view",
                }
            )

        for item_name in set(dir(cls)) - set(dir(Abi)):
            item = getattr(cls, item_name)
            if item_name == "__init__":
                # constructor
                ...
            elif item_name == "__annotations__":
                # constants, already parsed
                ...
            elif not callable(item):
                if issubclass(item, Event):
                    # events
                    abi.append(item.to_abi_item())
            else:
                inputs = []
                outputs = []
                for name, type_ in get_type_hints(item).items():
                    if name == "return":
                        outputs = [{"name": "", **parse_input(type_)}]
                    else:
                        inputs.append({"name": name, **parse_input(type_)})

                abi.append(
                    {
                        "type": "function",
                        "name": item_name,
                        "inputs": inputs,
                        "outputs": outputs,
                        "stateMutability": getattr(
                            item, "_state_mutability", "nonpayable"
                        ),
                    }
                )

        return abi

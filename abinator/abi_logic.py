import inspect
from typing import get_type_hints

from .events import Event
from .inputs import Struct, parse_input


class Abi:
    @classmethod
    @property
    def events(cls) -> list[Event]:
        events_list = []
        for item_name in set(dir(cls)) - set(dir(Abi)):
            item = getattr(cls, item_name)
            if inspect.isclass(item) and issubclass(item, Event):
                events_list.append(item)

        return events_list

    @classmethod
    @property
    def functions(cls) -> list[callable]:
        functions_list = []
        for item_name in set(dir(cls)) - set(dir(Abi)):
            item = getattr(cls, item_name)

            if (
                item_name != "__init__"  # constructor
                and item_name != "__annotations__"  # constants
                and not (
                    inspect.isclass(item) and issubclass(item, (Event, Struct))
                )  # events / structs
            ):
                functions_list.append(item)
        return functions_list

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

        for event in cls.events:
            abi.append(event.to_abi_item())

        for function in cls.functions:
            inputs = []
            outputs = []
            for name, type_ in get_type_hints(function).items():
                if name == "return":
                    outputs = [{"name": "", **parse_input(type_)}]
                else:
                    inputs.append({"name": name, **parse_input(type_)})

            abi.append(
                {
                    "type": "function",
                    "name": function.__name__,
                    "inputs": inputs,
                    "outputs": outputs,
                    "stateMutability": getattr(
                        function, "_state_mutability", "nonpayable"
                    ),
                }
            )

        return abi

from .inputs import parse_input


def anonymous(cls):
    cls._anonymous = True
    return cls


def indexed(typeVar):
    typeVar._indexed = True
    return typeVar


class Event:
    @classmethod
    def to_abi_item(cls):
        inputs = []
        for name, type_ in cls.__annotations__.items():
            inputs.append(
                {
                    "name": name,
                    "indexed": getattr(type_, "_indexed", False),
                    **parse_input(type_),
                }
            )

        return {
            "type": "event",
            "name": cls.__name__,
            "inputs": inputs,
            "anonymous": getattr(cls, "_anonymous", False),
        }

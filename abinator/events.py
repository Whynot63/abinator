from .inputs import parse_input


def anonymous(cls):
    cls._anonymous = True
    return cls


def indexed(typeVar):
    typeVar._indexed = True
    return typeVar


class Event:
    @classmethod
    @property
    def signature(cls):
        inputs = [parse_input(type_)["type"] for type_ in cls.__annotations__.values()]
        return f"{cls.__name__}({','.join(inputs)})"

    @classmethod
    @property
    def selector(cls):
        raise NotImplementedError
        # return keccak(cls.signature)

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

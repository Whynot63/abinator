from typing import TypeVar
from types import GenericAlias


class Struct:
    ...


def parse_input(type_):
    if type(type_) != TypeVar and issubclass(type_, Struct):
        raise NotImplementedError()
        # return {"type": tuple, "components": ...}
    elif type(type_) == GenericAlias:
        args = type_.__args__
        if len(args) > 1:
            raise NotImplementedError(f"Couldn't parse {type_}")
        if type_.__origin__ != list:
            raise RuntimeWarning(f"Use list[...] instead of {type_}")

        return {"type": str(args[0]).lstrip("~") + "[]", "components": []}

    return {"type": str(type_).lstrip("~"), "components": []}

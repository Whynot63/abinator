from typing import TypeVar
from types import GenericAlias


class Struct:
    @classmethod
    def to_components(cls):
        return [
            {"name": name, **parse_input(type_)}
            for name, type_ in cls.__annotations__.items()
        ]


def _parse_struct(type_):
    return {"type": "tuple", "components": type_.to_components()}


def _parse_tuple(type_):
    return {
        "type": "tuple",
        "components": [{"name": "", **parse_input(a)} for a in type_.__args__],
    }


def _parse_list(type_):
    return {"type": str(type_.__args__[0]).lstrip("~") + "[]", "components": []}


def _parse_type(type_):
    return {"type": str(type_).lstrip("~"), "components": []}


def _parse_python_type(type_):
    type_name = None

    if type_ == bool:
        type_name = "bool"
    elif type_ == str:
        type_name = "string"

    if type_name:
        return {"type": type_name, "components": []}
    raise NotImplementedError(f"Couldn't parse {type_}")


def parse_input(type_):
    if type(type_) == GenericAlias:
        if type_.__origin__ == list and len(type_.__args__) == 1:
            return _parse_list(type_)
        elif type_.__origin__ == tuple:
            return _parse_tuple(type_)
    elif type(type_) == TypeVar:
        return _parse_type(type_)
    elif issubclass(type_, Struct):
        return _parse_struct(type_)
    else:
        return _parse_python_type(type_)

def state_mutability_decorator(state_mutability):
    def wrapper(fn):
        _state_mutability = getattr(fn, "_state_mutability", None)
        if _state_mutability is not None:
            raise RuntimeWarning(
                f"Couldn't add @{state_mutability} for @{_state_mutability} function"
            )
        fn._state_mutability = state_mutability
        return fn

    return wrapper


pure = state_mutability_decorator("pure")
view = state_mutability_decorator("view")
payable = state_mutability_decorator("payable")

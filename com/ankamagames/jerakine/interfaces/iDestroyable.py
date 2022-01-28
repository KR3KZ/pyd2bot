from abc import ABC


class IDestroyable(ABC):
    def destroy() -> None:
        pass
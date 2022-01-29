from abc import ABC


class Prioritizable(ABC):

    @property
    def priority() -> int:
        pass
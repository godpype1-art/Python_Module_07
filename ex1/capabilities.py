from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def heal(self, target: Creature) -> str:
        ...


class TransformCapability(ABC):

    def __init__(self) -> None:
        super().__init__()
        self.transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...

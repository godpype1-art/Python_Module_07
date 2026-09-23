from abc import ABC, abstractmethod
from ex1.capabilities import HealCapability, TransformCapability
from typing import Any


class InvalidCombination(Exception):
    ...


class BattleStrategy(ABC):

    @abstractmethod
    def act(self, creature: Any) -> None:
        ...

    @abstractmethod
    def is_valid(self, creature: Any) -> bool:
        ...


class NormalStrategy(BattleStrategy):

    def act(self, creature: Any) -> None:
        print(creature.attack())

    def is_valid(self, creature: Any) -> bool:
        return True


class AgressiveStrategy(BattleStrategy):

    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.transform())
            print(creature.attack())
            print(creature.revert())
        else:
            raise InvalidCombination(
                f"Invalid Creature '{creature.name}' "
                "for this agressive strategy"
                )

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):

    def act(self, creature: Any) -> None:
        if self.is_valid(creature):
            print(creature.attack())
            print(creature.heal(creature.name))
        else:
            raise InvalidCombination(
                f"Invalid Creature '{creature.name}' "
                "for this defensive strategy"
                )

    def is_valid(self, creature: Any) -> bool:
        return isinstance(creature, HealCapability)

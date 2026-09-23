from abc import ABC, abstractmethod
from ex0.creature import Creature, Charmander, Charizard, Squirtle, Blastoise


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> Creature:
        ...


class FlameFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Charmander()

    def create_evolved(self) -> Creature:
        return Charizard()


class AquaFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Squirtle()

    def create_evolved(self) -> Creature:
        return Blastoise()

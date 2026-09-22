from abc import ABC, abstractmethod
import ex0.creature


class CreatureFactory(ABC):

    @abstractmethod
    def create_base(self) -> ex0.creature.Creature:
        ...

    @abstractmethod
    def create_evolved(self) -> ex0.creature.Creature:
        ...


class FlameFactory(CreatureFactory):

    def create_base(self) -> ex0.creature.Creature:
        return ex0.creature.Charmander()

    def create_evolved(self) -> ex0.creature.Creature:
        return ex0.creature.Charizard()


class AquaFactory(CreatureFactory):

    def create_base(self) -> ex0.creature.Creature:
        return ex0.creature.Squirtle()

    def create_evolved(self) -> ex0.creature.Creature:
        return ex0.creature.Blastoise()

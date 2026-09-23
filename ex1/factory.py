from ex1.creature import Bulbasaur, Venusaur, Riolu, Lucario
from ex0.factory import CreatureFactory, Creature


class HealingCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Bulbasaur()

    def create_evolved(self) -> Creature:
        return Venusaur()


class TransformCreatureFactory(CreatureFactory):

    def create_base(self) -> Creature:
        return Riolu()

    def create_evolved(self) -> Creature:
        return Lucario()

from .capabilities import HealCapability, TransformCapability
from ex0.creature import Creature


class Bulbasaur(HealCapability, Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Bulbasaur"
        self._type = "Grass"

    def attack(self) -> str:
        return f"{self.name} used Vine Whip!"

    def heal(self, target: Creature) -> str:
        return f"{self.name} heals {target} for a small amount"


class Venusaur(HealCapability, Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Venusaur"
        self._type = "Grass/Poison"

    def attack(self):
        return f"{self.name} used Petal Dance!"

    def heal(self, target: Creature) -> str:
        return f"{self.name} heals {target.name} "
    "and its allies for a large amount"


class Riolu(TransformCapability, Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Riolu"
        self._type = "Fighting"

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} used Metal Claw!"
        else:
            return f"{self.name} used Tackle."

    def transform(self) -> str:
        self.transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.transformed = False
        return f"{self.name} return to its normal form!"


class Lucario(TransformCapability, Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Lucario"
        self._type = "Fighting/Steel"

    def attack(self) -> str:
        if self.transformed:
            return f"{self.name} used Meteor Mash!"
        else:
            return f"{self.name} used Sucker Punch."

    def transform(self) -> str:
        self.transformed = True
        self.name = "Mega Lucario"
        return f"{self.name} shifts into its MEGA form!"

    def revert(self) -> str:
        self.transformed = False
        self.name = "Lucario"
        return f"{self.name} stabilizes in its base form!"

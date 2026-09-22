from abc import ABC, abstractmethod


class Creature(ABC):

    def __init__(self) -> None:
        self.name: str = ""
        self._type: str = ""

    @abstractmethod
    def attack(self) -> str:
        ...

    def describe(self) -> str:
        return f"{self.name} is a {self._type} Creature"


class Charmander(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Charmander"
        self._type = "Fire"

    def attack(self) -> str:
        return f"{self.name} used Ember!"


class Charizard(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Charizard"
        self._type = "Fire/Flying"

    def attack(self):
        return f"{self.name} used Flamethrower!"


class Squirtle(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Squirtle"
        self._type = "Water"

    def attack(self) -> str:
        return f"{self.name} used Water Gun!"


class Blastoise(Creature):

    def __init__(self) -> None:
        super().__init__()
        self.name = "Blastoise"
        self._type = "Water"

    def attack(self):
        return f"{self.name} used Hydro Pump!"


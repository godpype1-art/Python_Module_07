import ex0
from typing import Any


def verify_factory(factory: ex0.CreatureFactory) -> None:
    print("Testing factory")
    base: Any = factory.create_base()
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    evolved: Any = factory.create_evolved()
    print(f"{evolved.describe()}")
    print(f"{evolved.attack()}")


def battle(fact_1: ex0.CreatureFactory, fact_2: ex0.CreatureFactory) -> None:
    print("Testing battle")
    creat_1: Any = fact_1.create_base()
    creat_2: Any = fact_2.create_base()
    print(creat_1.describe())
    print(" vs.")
    print(creat_2.describe())
    print(" fight!")
    print(creat_1.attack())
    print(creat_2.attack())


def main() -> None:
    flame_factory: ex0.CreatureFactory = ex0.FlameFactory()
    aqua_factory: ex0.CreatureFactory = ex0.AquaFactory()
    verify_factory(flame_factory)
    print()
    verify_factory(aqua_factory)
    print()
    battle(flame_factory, aqua_factory)


if __name__ == "__main__":
    main()

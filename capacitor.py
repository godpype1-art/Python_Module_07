import ex1
from typing import Any


def verify_heal(factory: ex1.CreatureFactory) -> None:
    base: Any = factory.create_base()
    print(" base:")
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    print(f"{base.heal(base.name)}")
    evolved: Any = factory.create_evolved()
    print(" evolved:")
    print(f"{evolved.describe()}")
    print(f"{evolved.attack()}")
    print(f"{evolved.heal(evolved.name)}")


def verify_transform(factory: ex1.CreatureFactory) -> None:
    base: Any = factory.create_base()
    print(" base:")
    print(f"{base.describe()}")
    print(f"{base.attack()}")
    print(f"{base.transform()}")
    print(f"{base.attack()}")
    print(f"{base.revert()}")
    evolved: Any = factory.create_evolved()
    print(" evolved:")
    print(f"{evolved.describe()}")
    print(f"{evolved.attack()}")
    print(f"{evolved.transform()}")
    print(f"{evolved.attack()}")
    print(f"{evolved.revert()}")


def main() -> None:
    healing_factory: ex1.CreatureFactory = ex1.HealingCreatureFactory()
    transform_factory: ex1.CreatureFactory = ex1.TransformCreatureFactory()
    print("Testing Creature with healing capability")
    verify_heal(healing_factory)
    print()
    print("Testing Creature with transform capability")
    verify_transform(transform_factory)


if __name__ == "__main__":
    main()

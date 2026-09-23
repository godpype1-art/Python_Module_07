from ex0 import CreatureFactory, FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import BattleStrategy, NormalStrategy, \
    AgressiveStrategy, DefensiveStrategy, InvalidCombination
from typing import Any


def battle(opponents: list[tuple[CreatureFactory, BattleStrategy]]) -> None:
    print(
        [(c.create_base().name + "+" + type(s).__name__) for c, s in opponents]
        )
    print("=== Tournament ===")
    print(f"{len(opponents)} oponents envolved")
    print()

    fighters: list[tuple[Any, BattleStrategy]] = []
    for factory, strategy in opponents:
        creature: Any = factory.create_base()
        fighters.append((creature, strategy))
    for i, (creature_a, strategy_a) in enumerate(fighters):
        for j, (creature_b, strategy_b) in enumerate(fighters):
            if i >= j:
                continue
            print("== Battle ==")
            print(creature_a.describe())
            print(" vs.")
            print(creature_b.describe())
            print(" now fight!")
            try:
                strategy_a.act(creature_a)
                strategy_b.act(creature_b)
            except InvalidCombination as error:
                print(f"Battle error, aborting the tournament: {error}")
            finally:
                print()


def main() -> None:
    flame_factory: CreatureFactory = FlameFactory()
    aqua_factory: CreatureFactory = AquaFactory()
    heal_factory: CreatureFactory = HealingCreatureFactory()
    transform_factory: CreatureFactory = TransformCreatureFactory()

    normal: BattleStrategy = NormalStrategy()
    agressive: BattleStrategy = AgressiveStrategy()
    defensive: BattleStrategy = DefensiveStrategy()

    testing_data: list[tuple[CreatureFactory, BattleStrategy]] = [
        (flame_factory, normal),
        (heal_factory, defensive)
        ]
    print("Tournament 0 (basic)")
    battle(testing_data)
    testing_data = [
        (flame_factory, agressive),
        (heal_factory, defensive)
        ]
    print("Tournament 1 (error)")
    battle(testing_data)
    testing_data = [
            (aqua_factory, normal),
            (heal_factory, defensive),
            (transform_factory, agressive)
            ]
    print("Tournament 2 (multiple)")
    battle(testing_data)


if __name__ == "__main__":
    main()

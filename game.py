"""Текстовое РПГ. Герой либо побеждает, убив 10 монстров, либо погибает."""

from random import randint
from time import sleep

hero_health = 10
hero_strength = 10
dead_monsters = 0


def finding_apple() -> None:
    """Увеличивает количество жизни героя на случайное число от 5 до 15."""
    global hero_health
    adding_health = randint(5, 15)
    print(f'Вы обнаружили волшебное яблоко,'
          f'которое увеличивает ваши жизни на {adding_health}!')
    hero_health += adding_health
    print(f'Теперь у вас {hero_health} жизней')
    sleep(1)


def finding_sword() -> None:
    """Позволяет игроку изменить силу атаки героя."""
    global hero_strength
    sword_strength = randint(10, 25)
    print(f'Вы обнаружили новый меч с силой атаки {sword_strength}')
    answer = 0
    while answer != '1' and answer != '2':
        answer = input('Хотите взять новый меч или пройти мимо?\n'
                       '1 - взять\n2 - пройти мимо\n')
        if answer == '1':
            hero_strength = sword_strength
            print(f'Вы взяли новый меч,'
                  f'теперь сила вашей атаки {hero_strength}')
        elif answer == '2':
            print('Вы прошли мимо, сила вашей атаки осталась прежней')
        else:
            print('Вы ввели некорректный ответ, попробуйте ещё раз')
    sleep(1)


def meeting_monster() -> None:
    """Инициирует встречу героя с монстром.

    Игроку предлагается вступить в бой с монстром.
    Если игрок соглашается - вызывается функция поединка - battle.
    """
    monster_strength = randint(10, 30)
    monster_health = randint(10, 30)
    answer = 0
    while answer != '1' and answer != '2':
        answer = input(f"Вы встретили монстра с атакой {monster_strength}"
                       f" и количеством жизней {monster_health}\n"
                       f"Хотите вступить с ним в бой?\n"
                       f"1 - сражаться\n"
                       f"2 - убежать, чтобы набраться сил\n")
        if answer == '1':
            print('Вы вступаете в сражение с монстром')
            battle(monster_strength, monster_health)
        elif answer == '2':
            print('Вы убежали, чтобы набраться сил перед следующей встречей')
        else:
            print('Вы ввели некорректный ответ, попробуйте ещё раз')
    sleep(1)


def battle(monster_strength: int, monster_health: int) -> None:
    """Функция поединка с монстром.

    Герой и монстр сражаются до тех пор, пока один из них не умрёт.

    :monster_strength (int): сила атаки монстра. Принимает случайным образом
    сгенерированную переменную из функции meeting_monster

    :monster_health (int): количество жизней монстра. Принимает случайным
    образом сгенерированную переменную из функции meeting_monster
    """
    global hero_health
    global hero_strength
    global dead_monsters
    while hero_health > 0 and monster_health > 0:
        hero_health -= monster_strength
        monster_health -= hero_strength
        if hero_health <= 0:
            print('Вы были убиты, конец игры...')
        elif monster_health <= 0:
            dead_monsters += 1
            print(f'Вы победили ещё одного монстра!'
                  f'Общее количество побед: {dead_monsters}\n'
                  f'У вас осталось {hero_health} жизней.')
            if dead_monsters >= 10:
                print('Вы сразили 10 монстров, победоносный конец игры!')
    sleep(1)


actions = {1: finding_apple, 2: finding_sword, 3: meeting_monster}

if __name__ == '__main__':
    while hero_health > 0 and dead_monsters != 10:
        actions[randint(1, 3)]()

from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):
    quips = ["You died, you suck", "Your mom would be proud of this, if she's smarter", "Such a miser", "You are worse than your dad's jokes."]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

class CentralCorridor(Scene):
    def enter(self):
        print(dedent("""
        Aliens have invaded your planet. You are the last survivor. You are running down the central corridor to the weapon armory when an alien jumps out. He's blocking the door and is ready to attack you.
        """))

        action = input("> ")

        if action == "shoot!":
            print(dedent("""
            You missed. He eats you
            """))
            return 'death'

        elif action == "dodge!":
            print(dedent("""
            You bang on the head while dodging. He eats you.
            """))
            return 'death'
    
        elif action == "tell a joke":
            print(dedent("""
            You paralyzed him with your joke. Yea. You passed the room.
            """))
            return 'laser_weapon_armory'

        else:
            print("Huh?")
            return 'central_corridor'

class LaserWeaponArmory(Scene):
    def enter(self):
        print(dedent("""
        There's a bomb. There's a lock. If you can't get it 10 times ur dead. The code is 3 digits.
        """))

        code = f"{randint(1,9)}"
        guess = input("[Keypad]> ")
        guesses = 1

        while guess != code and guesses < 10:
            print("BAAAAAAAA")
            guesses += 1
            guess = input("[Keypad]> ")

        if guess == code:
            print(dedent("""
            The container clicks open but there are gases. You run as fast as you can to the bridge where you must place it in the right spot.
            """))
            return 'the_bridge'
        else:
            print(dedent("""huh?"""))
            return 'death'

class TheBridge(Scene):
    def enter(self):
        print(dedent("""
        You see all those ugly goblins. What are you gonna do?
        """))

        action = input("> ")
        if action == "throw the bomb":
            print(dedent("""You and the goblins die together"""))
            return 'death'
        elif action == "Slowly place the bomb":
            print(dedent("""
            You are awesome sauce. You got this. You successfully arrived at the escape pod.
            """))
            return 'escape_pod'
        else:
            print("huh?")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print(dedent("""
        There are no more aliens. But you have to choose between 5 pods. Which one do you choose?
        """))

        good_pod = randint(1, 5)
        guess = input("[pod #]  > ")

        if int(guess) != good_pod:
            print(dedent("""
            You jumped into pod {guess} and you got crushed mercilessly.
            """))
            return 'death'
        else:
            print(dedent("""
            You jumped into pod {guess} and you looked back to see the space ship exploded. You won!
            """))
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Good Job!")
        return 'finished'

class Map(object):
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
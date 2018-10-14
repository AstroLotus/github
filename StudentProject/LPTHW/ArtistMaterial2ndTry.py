from sys import exit
from random import randint


class Scene(object):
    Gamble = True
    def enter(self):
        print("\nThis scene has not yet configured.")
        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        current_scene.enter()


class StorageA(object):
    safe = randint(1, 2)

    gamble = randint(1, 4)
    if gamble >= 3:
        gamble -= 2

    m = randint(0, 1)
    n = randint(0, 2)
        
class Intro(Scene):
    x = 0
    talents = {
            "musict": randint(0, 3),  # stands for music talent
            "writingt": randint(0, 3),
            "artt": randint(0, 3),
            "dancet": randint(0, 3),
        }
        
    def enter(self):
        print(
            "\nYou have come to the wonderland! --- The Paradise for Prospective Artists!" 
        )
        

        print(
            "\n Quite talented for a day one student! Your talent scores are: Music: {musict}, Writing: {writingt}, Art: {artt}, Dance: {dancet}".format(
                **Intro.talents
            )
        )
        print("\nNow what do you choose for your new career?")
        print("\n1 = music")
        print("\n2 = writing")
        print("\n3 = art")
        print("\n4 = dance")

        action = input("\n1, 2, 3, or 4? > ")

        if action == "1":
            Music.enter(Music)
        elif action == "2":
            Writing.enter(Writing)
        elif action == "3":
            Art.enter(Art)
        elif action == "4":
            Dance.enter(Dance)
        else:
            Loss.enter(Loss)

    num = [talents.get("musict"), 
        talents.get("writingt"),
        talents.get("artt"),
        talents.get("dancet")]


class Score(object):
    def choice(self, x, seq):
        self.score = x
        if x > 0:
            if Music.change == False:
                y = randint(1, 5)
                x += y
                print(f"\nYour score increase by {y}")
                return x
            else:
                z = randint(0, 7)
                x += z
                print(f"\nYour score increase by {y}")
                return x
        elif x == 0:
            if Music.change == False:
                y = randint(1, 5)
                x = Intro.num[seq] + y
                print(f"\nYour score increase by {y}")
                return x
            else:
                z = randint(0, 7)
                x = Intro.num[seq] + y
                print(f"\nYour score increase by {y}")
                return x 
        else:
            Loss.enter(Loss)

class Music(Scene):
    change = Scene.Gamble
    musicscore = [Intro.num[0], 0]
    music_score = int(Intro.num[0] + musicscore[-1])

    def enter(self):
        print("\nWelcome to your music class. It is a nice choice. Now, what would you like to learn?")
        music_instruments = input("\nviolin, piano, guitar, voice? >  ")
        if music_instruments == "guitar" or "voice":
            Music.change = False
            Music.musicscore = Music.musicscore + [Score.choice(Score, Music.musicscore[-1], 0)]
            Music.music_score = Music.musicscore[-1]
            print(f"\nYour music score now is {Music.music_score}")
            if Music.music_score <= 11:
                return Everyday.enter(Everyday)
            else:
                print("\nYou are a master musician now!")
                return Awards.enter(Awards)
        elif music_instruments == "violin" or "piano":
            music.change = True
            Music.musicscore = Music.musicscore + [Score.choice(Score, Music.musicscore[-1], 0)]
            Music.music_score = Music.musicscore[-1]
            print(f"\nYour music score now is {Music.music_score})")
            if Music.music_score <= 11:
                return Everyday.enter(Everyday)
            else:
                print("\nYou are a master musician now!")
                return Awards.enter(Awards)
        else:
            return Music.enter(Music)
        return Music.music_score
        

class Writing(Scene):
    change = Scene.Gamble
    writingscore = [Intro.num[1], 0]
    writing_score = int(Intro.num[1] + writingscore[-1])

    def enter(self):
        print("\nWelcome to your writing class. It is a nice choice. Now, what would you like to learn?")
        writing_p = input("\nreading, vocabulary, creative writing, journaling? >  ")
        if writing_p == "reading" or "vocabulary":
            Music.change = False
            Writing.writingscore = Writing.writingscore + [Score.choice(Score, Writing.writingscore[-1], 1)]
            Writing.writing_score = Writing.writingscore[-1]
            print(f"\nYour writing score now is {Writing.writing_score}")
            if Writing.writing_score <= 11:
                return Everyday.enter(Everyday)
            else:
                print("\nYou are a master writer now!")
                return Awards.enter(Awards)
        elif writing_p == "creative writing" or "journaling":
            Music.change = True
            Writing.writingscore = Writing.writingscore + [Score.choice(Score, Writing.writingscore[-1], 1)]
            Writing.writing_score = Writing.writingscore[-1]
            print(f"\nYour writing score now is {Writing.writing_score}")
            if Writing.writing_score <= 11:
                return Everyday.enter(Everyday)
            else:
                print("\nYou are a master writer now!")
                return Awards.enter(Awards)
        else:
            return Writing.enter(Writing)
        return Writing.writing_score


class Art(Scene):
    artscore = [Intro.num[2], 0]
    art_score = int(Intro.num[2] + artscore[-1])

    def enter(self):
        print("\nWelcome to your art class. It is a nice choice. Now, what would you like to learn?")
        art_p = input("\nsketching, inking, acrylic, photography? >  ")
        if art_p == "sketching" or "inking":
            Music.change = False
            Art.artscore = Art.artscore + [Score.choice(Score, Art.artscore[-1], 2)]
            Art.art_score = Art.artscore[-1]
            print(f"\nYour Art score now is {Art.art_score}")
            if Art.art_score <= 11:
                return Everyday.enter(Everyday)
            else:
                print("\nYou are a master painter now!")
                return Awards.enter(Awards)
        elif art_p == "acrylic" or "photography":
            Music.change = True
            Art.artscore = Art.artscore + [Score.choice(Score, Art.artscore[-1], 2)]
            Art.art_score = Art.artscore[-1]
            print(f"\nYour Art score now is {Art.art_score}")
            if Art.art_score <= 11:
                return Everyday.enter(Everyday)
            else:
                print("\nYou are a master Painter now!")
                return Awards.enter(Awards)
        else:
            return Art.enter(Art)
        return Art.art_score


class Dance(Scene):
    dancescore = [Intro.num[3], 0]
    dance_score = int(Intro.num[3] + dancescore[-1])

    def enter(self):
        print("\nWelcome to your dance class. It is a nice choice. Now, what would you like to learn?")
        dance_p = input("\njazz, modern, ballet, traditional Chinese? >  ")
        if dance_p == "jazz" or "modern":
            Music.change = False
            Dance.dancescore = Dance.dancescore + [Score.choice(Score, Dance.dancescore[-1], 3)]
            Dance.dance_score = Dance.dancescore[-1]
            print(f"\nYour Dance score now is {Dance.dance_score}")
            if Dance.dance_score <= 11:
                return Everyday.enter(Everyday)
            else:
                print("\nYou are a master dancer now!")
                return Awards.enter(Awards)
        elif dance_p == "ballet" or "traditional Chinese":
            Music.change = True
            Dance.dancescore = Dance.dancescore + [Score.choice(Score, Dance.dancescore[-1], 3)]
            Dance.dance_score = Dance.dancescore[-1]
            print(f"\nYour Dance score now is {Dance.dance_score}")
            if Dance.dance_score <= 11:
                return Everyday.enter(Everyday)
            else:
                print("\nYou are a master dancer now!")
                return Awards.enter(Awards)
        else:
            return Dance.enter(Dance)
        return Dance.dance_score


class Awards(Scene):
    def enter(self):
        print("\nYou did it!")
        print(f"\nYour music score review is {Music.music_score}")
        print(f"\nYour writing score review is {Writing.writing_score}")
        print(f"\nYour art score review is {Art.art_score}")
        print(f"\nYour dance score review is {Dance.dance_score}")
        total = int(Music.music_score
                + Writing.writing_score
                + Art.art_score
                + Dance.dance_score)
        if total >= 20 and total < 30:
            print("\nYour total talent score exceeds 20 points")
            print("\nYou are a regional artist now. Not only you excel at your profession. You are well-rounded. A hundred people come to your art show.\n")
        elif total >= 30 and total < 40:
            print("\nYour total talent score exceeds 30 points")
            print("\nYou are a national artist now. Not only you excel at your profession. You are extremely well-rounded. A thousand people come to your art show.\n")
        
        elif total >= 40:
            print("\nYour total talent score exceeds 40 points")
            print("\nYou are an international artist now. Not only you did a stunning job at your profession. You are extremely verstile. A million people come to your art show.\n")
        else:
            print("\nYou are not quite well-arounded but you do great on your profession. Keep at it! It is just the end of the game but that doesn't mean you should stop trying!\n")
        exit(1)




class Loss(Scene):
    quips = [
        "Maybe you are better off as a scientist",
        "Who knows, maybe one day pigs can fly",
        "Hmm, maybe you have 2 left brains?",
    ]

    def enter(self):
        print(Loss.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class Map(object):
    scenes = {
        'intro': Intro(),
        'music': Music(),
        'writing': Writing(),
        'art': Art(),
        'dance': Dance(),
        'loss': Loss(),
        'awards': Awards(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


class Everyday(Scene):
    counter = 1

    def day(self):
        Everyday.counter += 1
        return Everyday.counter

    def enter(self):
        print(f"\nA new day has started! It is day {Everyday.day(Everyday)}!Welcome back, fellow artists!")
        print(f"\nYour music score review is {Music.music_score}")
        print(f"\nYour writing score review is {Writing.writing_score}")
        print(f"\nYour art score review is {Art.art_score}")
        print(f"\nYour dance score review is {Dance.dance_score}")
        total = Music.music_score + Writing.writing_score + Art.art_score + Dance.dance_score
        print(f"\nYour total score is {total}")
        print("\nNow what do you choose for your new career?")
        print("\n1 = music")
        print("\n2 = writing")
        print("\n3 = art")
        print("\n4 = dance")

        action = input("\n1, 2, 3, or 4? > ")

        if action == "1":
            Music.enter(Music)
        elif action == "2":
            Writing.enter(Writing)
        elif action == "3":
            Art.enter(Art)
        elif action == "4":
            Dance.enter(Dance)
        else:
            Loss.enter(Loss)



a_map = Map('intro')
a_game = Engine(a_map)
a_game.play()

"""
One starts with a random selection or talents, ranging from 0-3 for musician, writer, artist and dancer. Everyday, one can take a course of their choice adding 1-2 score, and a random generated activity adding 0-1 score. When one's talent score reaches 7, one will win a regional award, then their course of choice will only add 0-1 score and activity add 0-2 score; when one's talent score reaches 12, one wins
"""

from sys import exit
from random import randint
from textwrap import dedent

talent_score = {
    "musician": [randint(0, 3), "Music"],
    "writer": [randint(0, 3), "Writing"],
    "artist": [randint(0, 3), "Artist"],
    "dancer": [randint(0, 3), "Dancer"],
}

print(
    dedent(
        """You are quite talented:'{musician} {writer} {artist} {dancer}'""".format(
            **talent_score
        )
    )
)

resource = 20

class Loss(object):
    quips = [
        "Maybe you are better off as a scientist",
        "Who knows, maybe one day pig can fly",
        "Hmm, maybe you have 2 left brains?",
    ]

    def enter(self):
        print(Loss.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class Finished(object):
    def enter(self):
        print(dedent("""You have won! You are a true artist!"""))
        Finished.enter(Finished)


class Activites(object):
    def __init__(self, activity):
        self.activity = activity
    a = {
        "Performing an Opera piece": "music",
        "Meeting with the editor": "writing",
        "Sketeches real life models": "art",
        "Dance for ABS": "dance",
    }
    def enter(self):
        activity = Activites.a[randint(0, len(self.a) - 1)]
        print(dedent(f"""You have been selected for: {acti}"""))
        next_resource(resource)
        Acs(fs, acti)

class Courses(object):
    def __init__(self, cou):
        self.cou = cou
    def enter(self):
        print(dedent("""You have bathed in the delight of art more and more!"""))
        Activites()

class Game(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene
    def play(self):
        print(
        dedent("""A new day has started. Is one ready to embrace the art career? :D"""))
        current_course = "musician"
        if "music" or "art" or "writing" or "dance" in current_course:
            Courses(current_course)
        else:
            game()

    def next_resource(current_resource):
        if current_resource != resource + 1:
            resource -= 2
            print(dedent(f"""You have {resource} resources left."""))
            return resource


class Score(object):
    def __init__(self, start_score):
        self.start_score = start_score

    def c_score(self, course_name):
        val = Score.talent_score.get(current_course)
        return val


class Ts(Score):
    def enter(self, s, cc):
        if s < 7:
            s += random.randint(1, 2)
        else:
            s += random.randint(0, 1)
        talent_score[cc] = s
        fs = ts(val, current_course)
        print(
            dedent(
                """You have such talent course scores: Music {}, Writing {}, Art {}, Dance {}"""
            ).format(*fs)
        )


class Acs(Score):
    def enter(self, acs, act):
        if acs + fs < 7:
            acs += random.randint(0, 1)
        elif acs + random.fs == 7 or 12:
            "award"
        else:
            acs += random.randint(0, 2)
        talent_score[a[act]] = acs + fs
        print(
            dedent(
                """You have such talent total scores: Music {}, Writing {}, Art {}, Dance {}"""
            ).format(*talent_score[a[act]])
        )



class Award(object):
    def enter(self):
        if acs == 7:
            print(
                dedent(
                    """
            Congrats!You have won a regionally award.You are a semi - artist now! """
                )
            )
            game()
        else:
            print(
                dedent(
                    """
            Congrats!You have won a national award.Getting there.You are a professional now! """
                )
            )
            return Finish()


Game(Courses("musician")).play()


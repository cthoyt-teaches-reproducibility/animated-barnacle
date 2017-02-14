class Reanimator:
    def __init__(self, corps, alive=False):
        self.corps = corps
        self.alive = alive

    def reanimate(self):
        if self.alive:
            raise ValueError("Can't reanimate something that's alive")

        self.alive = True

    def __str__(self):
        if self.alive:
            return "{}... it's alive!!!".format(self.corps)

        return "The lifeless body of {}".format(self.corps)


def build_bodies(list_of_str):
    return [Reanimator(s) for s in list_of_str]

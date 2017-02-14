class Reanimator:
    """This class represents lifeless bodies that can be reanimated"""

    def __init__(self, corpse, alive=False):
        """

        :param corpse: The name of the corpse
        :type corpse: str
        :param alive: Is the corpse alive? Defaults to False.
        :type alive: bool
        """
        self.corps = corpse
        self.alive = alive

    def reanimate(self):
        """Reanimates a corpse, or raises a ValueError if it's already alive"""
        if self.alive:
            raise ValueError("Can't reanimate something that's alive")

        self.alive = True

    def __str__(self):
        if self.alive:
            return "{}... it's alive!!!".format(self.corps)

        return "The lifeless body of {}".format(self.corps)

    def __repr__(self):
        return str(self)


def build_bodies(list_of_str):
    """Makes a corpse object for each name in the list

    :param list_of_str: list of strings of names for corpses
    :type list_of_str: list of str
    :return:
    :rtype: list of Reanimator
    """
    return [Reanimator(s) for s in list_of_str]

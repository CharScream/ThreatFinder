from enum import Enum, auto


class EV(Enum):  # usage is EV.HP.value
    HP = auto()
    ATK = auto()
    SPA = auto()
    DEF = auto()
    SPD = auto()
    SPE = auto()


class Pokemon:
    def __init__(self, name, set_name, item, ability, nature, move_tuple, ev_li = []):
        self.name = name
        self.set_name = set_name
        self.item = item
        self.ability = ability
        self.nature = nature
        self.move_tuple = move_tuple
        self.ev_li = ev_li

    def print_all(self):
        """
        prints everything in the mon
        :return: None
        """
        print(self.name)
        print("Set:", self.set_name)

        for i in range(4):
            print('{:27}'.format("Move" + " " + str(i + 1) + ":" + " " + self.move_tuple[i]), end="")

            if i == 0:
                print("Item:", self.item)

            elif i == 1:
                print("Ability:", self.ability)

            elif i == 2:
                print("Nature:", self.nature)

            else:
                print("")

    def get_name(self):
        return self.name

    def get_set(self):
        return self.set_name

    def get_item(self):
        return self.item

    def get_ability(self):
        return self.ability

    def get_nature(self):
        return

    def get_evs(self):
        """
        :return: ev list
        """
        return self.ev_li


def make_moveset(m1, m2, m3, m4):
    """
    Creates and returns a tuple containing the moves
    :param m1: first move
    :param m2: second move
    :param m3: third move
    :param m4: fourth move
    :return: move tuple
    """

    moves = (m1, m2, m3, m4)
    return moves


def make_evs(hp=0, atk=0, de=0, spa=0, spd=0, spe=0):
    """ -> not sure how to make the function call clean but doing it this way
           will make it so we will see a zeroed ev as zero
    creates and returns a list of evs
    :param hp: hp ev
    :param atk: attack ev
    :param de: defence ev
    :param spa: special attack ev
    :param spd: specival defence ev
    :param spe: speed ev
    :return: list with ev values
    """

    evs = [hp, atk, de, spa, spd, spe]
    return evs


def main():
    # moves = make_moveset("Swords Dance", "Extreme Speed", "Shadow Claw", "Recover")
    arceus = Pokemon("Arceus", "Extreme Killer", "Leftovers", "Multitype", "Adamant",
                     make_moveset("Swords Dance", "Extreme Speed", "Shadow Claw", "Recover"))
    arceus.print_all()

    evs = (123, 456, 789, 11)
    evn = ["HP", "ATK", "DEF", "SPE"]
    ev_list = ["EV." + item for item in evn]

    dicta = dict(zip(ev_list, evs))
    print(dicta)
    for item in EV:
        print(item)
        if item.value in dicta:
            print("yes")


"""
use dict(zip(x,y)) to turn lists or tuples into a dictionary 
note: zip will stop at the max of the shortest iterable 
"""

if __name__ == "__main__":
    main()

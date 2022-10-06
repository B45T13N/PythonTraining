import random


class justePrix:

    def justePrix(self):
        return self


def jeuJustePrix():
    random_int = random.randrange(0, 10000, 1)
    user_choice = int(input("Pour jouer entrez un nombre entre 0 et 10 000"))
    while user_choice != random_int:
        if user_choice > random_int:
            print("C'est moins !")
            user_choice = int(input("Entrez un autre nombre"))
        else:
            print("C'est plus !")
            user_choice = int(input("Entrez un autre nombre"))
    print("Bravo ! Le nombre était : {}".format(random_int))

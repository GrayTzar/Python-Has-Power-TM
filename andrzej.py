import random

print("Welcome to 'Where is Andrzej?!'")
print("Let's find out who's with us tonight")
Andrzej_list = []

name = input("Ok, who's attending?" )
Andrzej_list.append(name)


def get_names():
    answer = input("Anyone else? Type 'n' if that's all. ")
    if answer == 'n':
        print("Ok, I guess that's all.")
    else:
        Andrzej_list.append(answer)
        get_names()


get_names()

print("Here's who's with us:" + str(Andrzej_list))
print("\nBut where's Andrzej?!")
chosen = random.choice(Andrzej_list)
print("Let's take a closer look at " + chosen + " ...\n\n" + chosen + " is in fact Andrzej!")

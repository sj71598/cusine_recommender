import random

cusines = ['American', 'Indian', 'Chinese', 'Thai', 'Italian', 'Mexican', 'Cook']

while len(cusines) > 0:

    user_input = input('press any key to get cuisine')
    choosen_cuisine = random.choice(cusines)

    cusines.remove(choosen_cuisine)
    print(cusines)

    print(choosen_cuisine)

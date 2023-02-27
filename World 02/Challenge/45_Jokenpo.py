from random import randint
from time import sleep
print("""rock -> 1
paper -> 2
scisso -> 3""")
player_01 = int(input('(Player 01) Choice this options for game of jokempô:'))
pc = randint(0, 2)
if player_01 != pc:
    if (player_01 == 1 and pc == 3) or (player_01 == 2 and pc == 1) or (player_01 == 3 and pc == 2):
        sleep(1)
        print("Player 01 WIN!")
    else:
        sleep(1)
        print("Compiuter WIN!")
else:
    print('EMPATED')

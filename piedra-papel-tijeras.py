import random

def run():
  user = input("elije 't' tijeras 'p' papel 'r' piedra: ")
  computadora = random.choice(['r', 'p', 't'])

  if user == computadora:
    print('empate')


def is_win(player, opponent):
    if player == 'r' and opponent == 't' or player == 'p' and opponent == 'r' or player == 't' and opponent == 'p':
        print('player wins')
    else:
        print('opponent wins')

    

if __name__ == '__main__':
    run()
    
import random

def play():
  user = input("elije 't' tijeras 'p' papel 'r' piedra: ")
  computadora = random.choice(['r', 'p', 't'])

  if user == computadora:
    print('empate')

  if is_win(user, computadora):
    return 'You won'
  else:
    return 'you lost'

def is_win(player, opponent):
    if player == 'r' and opponent == 't' or player == 'p' and opponent == 'r' or player == 't' and opponent == 'p':
        return True

print(play())
    
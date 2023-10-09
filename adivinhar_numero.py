guess = 0
tries = 0

while guess != 6 and tries < 5:
  guess = int(input('Adivinhe o numero : '))
  tries = tries + 1
  print(tries)
  if tries >= 5:
    print('Voce superou o numero de tentativas')
  elif guess == 6:
    print('Voce adivinhou !!!')

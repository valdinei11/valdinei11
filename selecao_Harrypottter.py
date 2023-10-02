
grifinoria = 0
sonserina = 0
lufalufa = 0
corvinal = 0

#primeira pergunta
print('Q1) Voce gosta de Dawn ou Dusk ? ')
print('1) Dawn')
print('2) Dusk')
pontos = int(input(''))
if pontos == 1:
  grifinoria = grifinoria + 1
  print('Ponto para grifinoria ',grifinoria)
elif pontos == 2:
  sonserina = sonserina + 1
  print('Ponto para sonserina ',sonserina)
else:
  print('Entrada errada!!!')

#segunda pergunta
print('Q2) Quando eu estiver morto, quero que as pessoas se lembrem de mim como: ')
print('1) O Bem ')
print('2) O Grande')
print('3) O Sabio')
print('4) O Ousado')
pontos = int(input(''))

if pontos == 1:
  grifinoria = grifinoria + 2
  print('Ponto para grifinoria!!!')
elif pontos == 2:
  sonserina = sonserina + 2
  print('Ponto para sonserina ')
elif pontos == 3:
  lufalufa = lufalufa + 2
elif pontos == 4:
  corvinal = corvinal +2
else:
  print('Entrada errada!!!')

#terceira pergunta
print('Q3) Qual tipo de instrumento mais agrada o seu ouvido ?')
print('1) O violino ')
print('2) O trompete')
print('3) O piano')
print('4) O tambor')
pontos = int(input(''))

if pontos == 1:
  grifinoria = grifinoria + 4
  print('Ponto para grifinoria!!!')
elif pontos == 2:
  sonserina = sonserina + 4
  print('Ponto para sonserina ')
elif pontos == 3:
  lufalufa = lufalufa + 4
elif pontos == 4:
  corvinal = corvinal + 4
else:
  print('Entrada errada!!!')

print('Grifinoria: ',grifinoria)
print('Sonserina: ',sonserina)
print('Lufa lufa: ',lufalufa)
print('Corvinal: ',corvinal)

if grifinoria > sonserina and grifinoria > lufalufa and grifinoria > corvinal:
  print('Voce pertence a grifinoria !!!')
elif sonserina > grifinoria and sonserina > lufalufa and sonserina > corvinal:
  print('Voce pertence a sonserina !!!')
elif lufalufa > grifinoria and lufalufa > sonserina and lufalufa > corvinal:
  print('Voce pertence a lufa lufa !!!')
elif corvinal > sonserina and corvinal > lufalufa and corvinal > grifinoria:
  print('Voce pertence a corvinal !!!')

altura = float(input('Digite a sua altura(cm): '))
creditos =  int(input('Digite a quantidade de creditos: '))

if altura > 1.35 and creditos > 10:
  print('Aproveite o passeio ☺')
elif altura < 1.35 and creditos > 10:
  print('Sinto muito mas voce nao tem a altura recomendada.')
elif altura > 1.35 and creditos < 10:
  print('Sinto muito mas voce não possui creditos suficiente.')
else:
  print('disculpe mas voce não possue nenhum dos requisitos.')

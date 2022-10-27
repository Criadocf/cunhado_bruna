#ATIVIDADE DO CUNHADO DA BRUNA
def media():
  totals = 0
  qtd_numero = 0
  y = int(input('digite um número: '))
  while (y != 0):
    totals += y
    y = int(input('digite um número: '))
    qtd_numero += 1
  if qtd_numero != 0:
    print(f'{totals/qtd_numero}')
  
def main():
  media()

if __name__=='__main__':
  main()
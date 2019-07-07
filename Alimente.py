def criar():
    print('====X====X====X Seja Bem-vindo ====X====X====X')
    print('\n'+'\n'+'\n'+'\n')
    a=str(input(' 1-) Diga-me, qual é o comando ou aplicativo que deseja executar(COLOQUE  O NOME DO PROGRAMA OU COMANDO ENTRE ASPAS SIMPLES)'+'\n'))
    print('\n'+'====X====X====X----====X====X====X'+'\n')
    b=str(input('2-) Diga-me, como quer que seja chamado esse programa quando for executar-lo(Nota:palavras simples e pequenas são mais faceis de serem entendidas)'+'\n'))
    print('\n'+'====X====X====X----====X====X====X'+'\n')
    c=('Certo, então você quer que a nina execute o',a,'quando chamado por',b)
    print(c)

    d=('import os'+'\n')
    e=('a=os.system'+'('+a+')')

    arquivo=open('comandos/'+b,'w')
    arquivo.write(d)
    arquivo.write(e)
    arquivo.close()
criar()
x=input('Deseja adiconar mais alguma coisa ? Se sim (1) Se não(2)')
if x == '1':
    criar()
    criar()
else:
    print('====X====X====X ADEUS ====X====X====X')
    exit()

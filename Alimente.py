import time
def criar():
    try:
        print('====X====X====X Seja Bem-vindo ====X====X====X')
        print('\n'+'\n'+'\n'+'\n')
        a=str(input(' 1-) Diga-me, qual é o comando ou aplicativo que deseja executar(COLOQUE  O NOME DO PROGRAMA OU COMANDO ENTRE ASPAS EX:"sudo apt install arduino" ou "gparted"  '+'\n'))
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
        print('press crtl+c for exit')
        criar()

    except KeyboardInterrupt:

        print('====X====X====X Programa feito por ====X====X====X')

        print('''
        ========x========x========x========x========x========x========x========x========x========x========x========x=======x=======    
        |  ::::::::  :::        :::      ::::::::::::  :::::::::  :::::::::::          ::::::     ::::::::::::::::      ::    ::   |
        |  ::::::::  :::        :::      :::       ::         ::  :::      ::         ::    ::    ::                    ::   ::    |
        |    :::     :::        :::      :::       ::         ::  :::      ::        ::      ::    ::                   ::  ::     |
        |    :::     :::        :::      :::       ::         ::  :::      ::       ::        ::    ::                  :: ::      |
        |    :::     :::        :::      ::::::::::::  :::::::::  :::::::::::      ::::::::::::::    ::                 ::::       | 
        |    :::     :::        :::      :::       ::         ::  :::      ::     ::            ::    ::                :: ::      | 
        |    :::     :::        :::      :::       ::         ::  :::      ::    ::              ::    ::               ::  ::     | 
        |  ::::::::  :::::::::  :::::::: :::       ::         ::  :::      ::   ::                ::    ::              ::   ::    | 
        |  ::::::::  :::::::::  :::::::: ::::::::::::  :::::::::  :::::::::::  ::                  ::    ::::::::::::   ::    ::   |        
        ========x========x========x========x========x========x========x========x========x========x========x========x=======x=======
           ''' )
        
criar()

    



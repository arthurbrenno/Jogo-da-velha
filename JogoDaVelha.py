import os
os.system("cls")
class Quadro:
    #definir as posições do quadro em uma lista
    def __init__(self):
        self.pos = ['*']*10

    #mostrar o quadro nas posições da lista que criei
    def display(self):
        print(f'{self.pos[7]}|{self.pos[8]}|{self.pos[9]}')
        print(f'{self.pos[4]}|{self.pos[5]}|{self.pos[6]}')
        print(f'{self.pos[1]}|{self.pos[2]}|{self.pos[3]}')

    #dar update no quadro com as cordenadas passadas
    def update(self, coordenada, jogador):
        try:
            self.pos[coordenada] = jogador
        except:
            print('Número acima da tabela!')

    #definir o vencedor
    def vencedor(self,jogador):
        wins = [(1,2,3),(4,5,6),(7,8,9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
        return any(self.pos[a] + self.pos[b] + self.pos[c] == jogador*3 for a, b, c in wins)

    #resetar caso queira jogar novamente
    def resetar(self):
        self.pos = ['*']*10

    #verificar se deu velha
    def checa_espaco(self,posicao):
        return self.pos[posicao] == '*'

    def velha(self):
        for i in range(1, 10):
            if self.checa_espaco(i):
                return False
        return True

def cabecalho():
    print('[Jogo da velha]\n'
          'Dev by Arthur Brenno\n'
          '---------------------------------------')
#resetar e mostrar o quadro
def limpar():
    os.system('cls')
    cabecalho()
    quadro.display()

def jogar_de_novo():
    jogar_dnv = input('Digite "S" para jogar novamente ou qualquer tecla para sair -> ').lower()
    if jogar_dnv != 's':
        exit()
    else:
        quadro.resetar()


#Definir objeto da classe Quadro
quadro = Quadro()

###Jogo
while True:
    #Exibir o cabecalho e dar o display
    cabecalho()
    quadro.display()
    limpar()

    #Pedir input do int(x) e fazer o update
    try:
        x = int(input('\nX - Digite a posição desejada (1-9) ---> '))
    except ValueError:
        print('ERRO-------------------------------------^\n'
              'O valor digitado não é um numero inteiro!\n\n')
        continue

    quadro.update(x,'X')
    limpar()

    #verificar se X ganhou
    if quadro.vencedor('X'):
        print('X GANHOU!')
        jogar_de_novo()

    #verificar se deu velha
    if quadro.velha():
        print('DEU VELHA!')
        jogar_de_novo()

    # Pedir input do O e fazer o update
    try:
        o = int(input('\nO - Digite a posição desejada (1-9) ---> '))
    except ValueError:
        print('ERRO-------------------------------------^\n'
              'O valor digitado não é um numero inteiro!\n\n')
        continue
    quadro.update(o, 'O')
    limpar()

    #verificar se O ganhou
    if quadro.vencedor('O'):
        print('O GANHOU!')
        jogar_de_novo()
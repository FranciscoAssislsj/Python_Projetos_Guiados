import random

board = ['''

****Jogo da Forca****

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========''']


class Hangman:
    lista_palavras = ['Cachorro','Elefante','Macaco','Canguru'] 
    def __init__(self):
        self.palavra_secreta = random.choice(self.lista_palavras).lower() 
        self.letras_adivinhadas = [] 
        self.letras_erradas = [] 
        self.chances = 6 
        
    def adivinha_letra(self, letra):
        if letra in self.palavra_secreta: 
            if letra not in self.letras_adivinhadas:  
                self.letras_adivinhadas.append(letra) 
        else:
            if letra not in self.letras_erradas: 
                self.letras_erradas.append(letra) 
        
    def jogo_terminou(self):
        return set(self.palavra_secreta) == set(self.letras_adivinhadas)
	

    def mostrar_progresso(self):
        progresso = ''
        for letra in self.palavra_secreta: 
            if letra in self.letras_adivinhadas: 
                progresso += letra + '' 
            else:
                progresso += '_ ' 
                
        return progresso.strip() 

    def iniciar_jogo(self):
        print('Bem-vindo ao jogo da forca!')
        
        while not self.jogo_terminou() and len(self.letras_erradas) < self.chances:
            print(board[len(self.letras_erradas)])
            print("\nPalavra: ",self.mostrar_progresso()) 
            print("Letras erradas: ", ' '.join(self.letras_erradas))
            print("Chances restantes: ", (self.chances - len(self.letras_erradas)))

            letra = input('Digite uma letra: ').lower()
            if letra in self.letras_adivinhadas or letra in self.letras_erradas:
                print('Você ja tentou essa letra')
            else:
                self.adivinha_letra(letra)

        if self.jogo_terminou():
            print("\nParabéns! Você adivinhou a palavra:",self.palavra_secreta)
        else:
            print(board[len(self.letras_erradas)])
            print("\nVocê perdeu! A palavra era:",self.palavra_secreta)

jogo = Hangman()
jogo.iniciar_jogo()


from os import system, name

def limpa_tela():


	if name == "nt":
		_ = system('cls')
	

	else:
		_ = system('clear')

def game():

	print("\nBem-vindo(a) ao jogo de forca!")
	print("Adivinhe a palavra abaixo \n")

	lista_de_palavras = ["azul","amarelo","cinza","vermelho","verde"]

	import random
	palavra_aleatoria = random.choice(lista_de_palavras)

	letras_palavra = ["_" for cadaletra in palavra_aleatoria]

	chances = 6

	letras_erradas = []

	while chances > 0:

		print(" ".join(letras_palavra))
		print("Chances restantes: ",chances)
		print("Letras erradas: ",letras_erradas)

		tentativa = input("Digite uma letra: ").lower()


		if tentativa in palavra_aleatoria:
			index = 0
			for letra in palavra_aleatoria:
				if tentativa == letra:
					letras_palavra[index] = letra
				index += 1

		else:
			chances -= 1
			letras_erradas.append(tentativa)

		if "_" not in letras_palavra:
			print("\nVocê venceu, a palavra era:",palavra_aleatoria)

	if "_" in letras_palavra:
		print('\nVocê perdeu, a palavra era:',palavra_aleatoria)



if __name__ == "__main__":
	game()
	print("\nParabéns. Você está aprendendo programaçã em Python com a DSA. :)\n")

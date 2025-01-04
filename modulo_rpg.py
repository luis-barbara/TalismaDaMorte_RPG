''' Jogo de RPG Textual: Contexto - Criar um jogo de RPG textual onde o utilizador pode
criar uma personagem, explorar um mundo fictício e tomar decisões que afetam o
enredo. Nota: O aluno deve criar estruturas para representar o personagem e o
mundo do jogo. '''


# Desenvolvimento

import main

#Modelo Jogador
class Jogador:
    def __init__(self, nome = "", skill = 8, stamina = 10, luck = 5):
        self.nome = nome
	    self.skill = skill
	    self.stamina = stamina
        self.luck = luck
        self.vida = True
        self.equipCombate = {"Espada": 1, "Sinalizadores de fogo": 4}
        self.refeicoes = 10
        self.porcoes = []
        self.ouro = []
        self.joias = []

    def criarJogador(self)
        nome = input("Insere um nome para a personagem do jogo: ")
        if type(nome) != str or len(nome) == 0  # Verifica se o nome não é string ou se o tamanho é 0
            print("Insere um nome com pelo menos 1 caractere")
            return 0  # Retorna 0 para indicar falha
        self.nome = nome
        print("Personagem criado com sucesso!")
        return 1

    def mostrarEquipamento(self)
        # Aceder ao dicionário de equipamentos
        equip_info = ""
        for chave, valor in self.equipCombate.items():
            equip_info += f"Equipamento: {chave} - {valor}\n"
        
        # Verificar se as listas têm valores antes de aceder
        refeicoes = self.refeicoes[0] if self.refeicoes else "Nenhuma refeição"
        porcoes = self.porcoes[0] if self.porcoes else "Nenhuma porção"
        ouro = self.ouro[0] if self.ouro else "Nenhum ouro"
        joias = self.joias[0] if self.joias else "Nenhuma jóia"
        
        return f"{equip_info}Refeições: {refeicoes}\nPorções: {porcoes}\nOuro: {ouro}\nJóias: {joias}"


    def mostrarScores(self)
        return f"Skill: {self.skill}, Stamina: {self.stamina}, Luck: {self.luck}"



#exercicio 64
#Crie uma classe chamada mamífero com propriedades de mamíferos
#Herde os detalhes desta classe e crie novas para cachorro, gato e outros animais que você quiser
#crie objetos desta classe que herdam de mamífero
#exiba as propriedades e métodos na tela

#Classe mamífero

class Mamifero:
    def __init__(self,glandulasmamarias,pelo,termorregulacao,cerebrodesenvolvido,dentesincisivos,dentescaninos,dentesmolares,coracaocomdoisatriosedoisventriculos,respiracaopulmonar,sistemanervosocomplexo,comportamentosocial,cuidadoparental):
        self.glandulasmamarias = True
        self.pelo = True
        self.termoregulacao = True
        self.cerebrodesenvolvido = True
        self.dentesincisivos = True
        self.dentescaninos = True
        self.destesmolares = True
        self.coracaocomdoisatrisedoisventriculos = True
        self.respiracaopulmonar = True
        self.sistemanervosocomplexo = True
        self.comportamentosocial = True
        self.cuidadoparental = True

    def apresentar(self)
        return f"Olá eu sou um mamífero e possuo {self.glandulasmamarias}, {self.cerebrodesenvolvido}, {self.comportamentosocial}, {self.coracaocomdoisatrisedoisventriculos}, {self.cuidadoparental},{self.dentescaninos},{self.dentesincisivos} {self.destesmolares, {self.pelo}}"
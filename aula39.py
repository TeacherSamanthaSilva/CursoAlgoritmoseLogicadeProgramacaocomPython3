#Exercicio 53
#criar uma classe pessoa com nome e idade crie uma classe chamada superheroi que herda as características de pessoa crie poderes para a classe superheroi e teste as duas classes criando novos objetos


# Classe Pessoa
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."

# Classe SuperHeroi que herda de Pessoa
class SuperHeroi(Pessoa):
    def __init__(self, nome, idade, poderes):
        super().__init__(nome, idade)  # chama o construtor da classe Pessoa
        self.poderes = poderes  # lista ou string com poderes
    
    def mostrar_poderes(self):
        return f"{self.nome} possui os seguintes poderes: {', '.join(self.poderes)}"
    
    def usar_poder(self, poder):
        if poder in self.poderes:
            return f"{self.nome} está usando o poder: {poder}!"
        else:
            return f"{self.nome} não possui o poder {poder}."

# Testando as classes
p1 = Pessoa("Ana", 30)
print(p1.apresentar())

heroi1 = SuperHeroi("Carlos", 25, ["voar", "super força", "visão de raio-x"])
print(heroi1.apresentar())           # herdado da classe Pessoa
print(heroi1.mostrar_poderes())      # método da classe SuperHeroi
print(heroi1.usar_poder("voar"))
print(heroi1.usar_poder("invisibilidade"))

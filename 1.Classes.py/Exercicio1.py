import os

os.system("cls||clear")
class Endereco:
    def __init__(self,logradouro:str,numero:int) -> None:
        self.logradouro=logradouro
        self.numero=numero

    def exibir_endereco(self):
        return f"Logradouro:{self.logradouro} \nNumero:{self.numero}"



class Aluno:
    #nome,idade
    #Construtor
    def __init__(self,nome:str,idade:int,endereco:Endereco) -> None:
        #Atributos
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
    def exibir_dados(self)-> str:
        return f"Nome: {self.nome} \nIdade:{self.idade} \nEndereço {self.endereco.exibir_endereco()}"
       
#Instanciar a classe 

aluno=Aluno("Julio Cesar",19,Endereco("Rua A",22))

#print(f"Nome:{aluno.nome}")
#print(f"Idade:{aluno.idade}")

print(aluno.exibir_dados())
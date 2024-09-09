from abc import ABC, abstractmethod
import os


os.system("cls||clear")

def

class Endereco:
    def __init__(self,logradouro:str,numero:str,cidade:str) -> None:
        self.logradouro=logradouro
        self.numero=numero
        self.cidade=cidade


class Funcionario(ABC):

    def __init__(self,nome:str,email:str,salario:float,endereco:Endereco) -> None:
        super().__init__()

        self.nome=nome 
        self.email=email
        self.salario=salario
        self.endereco=Endereco

    def salario(self):
        
        

class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco,cnh:str) -> None:
        super().__init__(nome, email, salario, endereco)
        self.cnh=cnh

class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, salario: float, endereco: Endereco,cnh:str) -> None:
        super().__init__(nome, email, salario, endereco)
    
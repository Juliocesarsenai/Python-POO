from enum import Enum

class Sexo(Enum):
    MASCULINO="Masculino";
    FEMININO="Feminino";

class Pessoa:
    def __init__(self,nome:str,idade:int,sexo:Sexo) -> None:
        self.nome=nome
        self.idade=idade
        self.sexo=sexo

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}")
    
pessoa_1=Pessoa("Julio Cesar",19,Sexo.MASCULINO)

print(pessoa_1)
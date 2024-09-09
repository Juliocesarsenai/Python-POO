from enum import Enum
import os

class Setor(Enum):
    FINANCEIRO="Financeiro"
    RECURSOS_HUMANOS="Recursos Humanos"
    VENDAS="Vendas"
    MARKETING="Marketing"

class Sexo(Enum):
    MASCULINO="Masculino"
    FEMININO="Feminino"

class Funcionario:
    def __init__(self,id:int,nome:str,idade:int,salario:float,setor:Setor,sexo:Sexo) -> None:
     self.id=id   
     self.nome=nome   
     self.idade=idade   
     self.salario=salario   
     self.setor=setor  
     self.sexo=sexo

    def __str__(self) -> str:
        return (f"\nID:{self.id}"
                f"\nNome:{self.nome}"
                f"\nIdade:{self.idade}"
                f"\nSalário:{self.salario}"  
                f"\nSetor:{self.setor.value}"
                f"\nSexo:{self.sexo.value}")

os.system("cls||clear")

primeiro_funcionario=Funcionario("12345","Julio César",19,30000,Setor.VENDAS,Sexo.MASCULINO)

print(primeiro_funcionario)